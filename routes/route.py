from fastapi import APIRouter, File, UploadFile, HTTPException, Form
from typing import List
from models.accidentreportdetails import AccidentReport, AccidentReportUpdate
from config.database import collection_name
from bson import ObjectId
from schema.schemas import list_serial

router = APIRouter()

def serialize_object(obj):
    """Convert MongoDB ObjectId and other non-serializable fields to serializable formats."""
    if isinstance(obj, ObjectId):
        return str(obj)
    if isinstance(obj, dict):
        return {k: serialize_object(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [serialize_object(i) for i in obj]
    return obj

@router.get("/")
async def get_accidentreports():
    accidentreports = list_serial(collection_name.find())
    return [serialize_object(report) for report in accidentreports]

# Post request method with image upload
@router.post("/")
async def post_accidentreport(
    client_name: str = Form(...),
    contact_number: str = Form(...),
    accident_description: str = Form(...),
    street_name: str = Form(...),
    surburb_name: str = Form(...),
    city_name: str = Form(...),
    time: str = Form(...),
    police_station_address: str = Form(...),
    ar_number: str = Form(...),
    files: List[UploadFile] = File(...)
):
    images = []
    for file in files:
        contents = await file.read()
        # Handle saving the file as needed (e.g., to disk or cloud storage)
        images.append(file.filename)
    
    accident_report = {
        "client_name": client_name,
        "contact_number": contact_number,
        "accident_description": accident_description,
        "street_name": street_name,
        "surburb_name": surburb_name,
        "city_name": city_name,
        "time": time,
        "police_station_address": police_station_address,
        "ar_number": ar_number,
        "images": images
    }
    
    collection_name.insert_one(accident_report)
    return {"message": "Accident report added successfully", "data": serialize_object(accident_report)}

# Put request method
@router.put("/{id}")
async def put_accidentreport(
    id: str,
    accidentreport: AccidentReportUpdate,
    files: List[UploadFile] = File(None)
):
    obj_id = ObjectId(id)
    existing_report = collection_name.find_one({"_id": obj_id})
    
    if existing_report is None:
        raise HTTPException(status_code=404, detail="Accident report not found")
    
    update_data = {k: v for k, v in accidentreport.dict().items() if v is not None}

    if files:
        images = []
        for file in files:
            contents = await file.read()
            images.append(file.filename)
        update_data["images"] = images
    
    if not update_data:
        raise HTTPException(status_code=400, detail="No valid fields to update")
    
    result = collection_name.find_one_and_update(
        {"_id": obj_id},
        {"$set": update_data},
        return_document=True
    )
    
    if result:
        result['_id'] = str(result['_id'])
    
    return {"message": "Accident report updated successfully", "data": serialize_object(result)}

@router.delete("/{id}")
async def delete_accidentreport(id: str):
    delete_result = collection_name.delete_one({"_id": ObjectId(id)})
    
    if delete_result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Accident report not found")

    return {"message": "Accident report deleted successfully"}
