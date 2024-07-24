from fastapi import APIRouter, File, UploadFile, HTTPException, Form, Query
from typing import List, Optional
from app.models.accidentreportdetails import AccidentReport, AccidentReportUpdate
from app.config.database import collection_name
from bson import ObjectId
from app.schema.schemas import list_serial


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
async def show_all_accidentreports():
    accidentreports = list_serial(collection_name.find())
    return accidentreports


#Post request method
@router.post("/")
async def create_accidentreport(accidentreport : AccidentReportUpdate):
    collection_name.insert_one(accidentreport.dict())
    return {"message": "Accident report added successfully"}




# Put request method
@router.put("/{id}")
async def update_accidentreport(id: str, accidentreport: AccidentReportUpdate):
    # Convert id to ObjectId
    obj_id = ObjectId(id)
    
    # Fetch the existing document
    existing_report = collection_name.find_one({"_id": obj_id})
    
    if existing_report is None:
        raise HTTPException(status_code=404, detail="Accident report not found")
    
    # Prepare the update data
    update_data = {k: v for k, v in accidentreport.dict().items() if v is not None}
    
    if not update_data:
        raise HTTPException(status_code=400, detail="No valid fields to update")
    
    # Merge existing data with the new update data
    updated_report = {**existing_report, **update_data}
    
    # Perform the update
    result = collection_name.find_one_and_update(
        {"_id": obj_id},
        {"$set": updated_report},
        return_document=True
    )
    
    # Convert ObjectId to string in result for serialization
    result['_id'] = str(result['_id'])
    
    return {"message": "Accident report updated successfully", "data": result}



@router.delete("/{id}")
async def delete_accidentreport(id: str):
    delete_result = collection_name.delete_one({"_id": ObjectId(id)})
    
    if delete_result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Accident report not found")

    return {"message": "Accident report deleted successfully"}



@router.get("/search")
async def search_accidentreports(
    client_name: Optional[str] = None,
    contact_number: Optional[str] = None,
    accident_description: Optional[str] = None,
    street_name: Optional[str] = None,
    surburb_name: Optional[str] = None,
    city_name: Optional[str] = None,
    time: Optional[str] = None,
    police_station_address: Optional[str] = None,
    ar_number: Optional[str] = None
):
    query = {}
    if client_name:
        query["client_name"] = client_name
    if contact_number:
        query["contact_number"] = contact_number
    if accident_description:
        query["accident_description"] = accident_description
    if street_name:
        query["street_name"] = street_name
    if surburb_name:
        query["surburb_name"] = surburb_name
    if city_name:
        query["city_name"] = city_name
    if time:
        query["time"] = time
    if police_station_address:
        query["police_station_address"] = police_station_address
    if ar_number:
        query["ar_number"] = ar_number

    accidentreports = list_serial(collection_name.find(query))
    return {"reports": [serialize_object(report) for report in accidentreports]}
