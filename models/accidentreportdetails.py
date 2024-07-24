# accidentreportdetails.py
from pydantic import BaseModel
from typing import Optional, List

class AccidentReport(BaseModel):
    client_name: str
    contact_number: str
    accident_description: str
    street_name: str
    surburb_name: str
    city_name: str
    time:str
    images: Optional[List[str]] = []
    police_station_address: Optional[str] = None
    ar_number: Optional[str] = None

class AccidentReportUpdate(BaseModel):
    client_name: Optional[str] = None
    contact_number: Optional[str] = None
    accident_description: Optional[str] = None
    street_name: Optional[str] = None
    surburb_name: Optional[str] = None
    city_name: Optional[str] = None
    time: Optional[str] = None
    images: Optional[List[str]] = None
    police_station_address: Optional[str] = None
    ar_number: Optional[str] = None