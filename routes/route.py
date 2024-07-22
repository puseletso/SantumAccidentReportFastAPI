from fastapi import APIRouter
from models.accidentreportdetails import AccidentReport, AccidentReportUpdate
from config.database import collection_name
from bson import ObjectId
from schema.schemas import list_serial  # Adjust the path if necessary

router = APIRouter()

@router.get("/")
async def get_accidentreports():
    accidentreports = list_serial(collection_name.find())
    return accidentreports


#Post request method
@router.post("/")
async def post_accidentreport(accidentreport : AccidentReport):
    collection_name.insert_one(accidentreport.dict())
    return {"message": "Accident report added successfully"}




# Put request method
@router.put("/{id}")
async def put_accidentreport(id: str, accidentreport: AccidentReportUpdate):
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