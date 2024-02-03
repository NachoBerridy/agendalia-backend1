from typing import List, Union
from pydantic import BaseModel

class TimeInterval(BaseModel):
    start: str
    end: str

class AvailabilityModel(BaseModel):
    userId: str
    name: str
    availability: dict[str, List[dict[str, str]]]
    overrideDates: List[dict[str, Union[List[dict[str, str]], str, None]]]
    timeZone: str

    class Config:
        schema_extra = {
            "example": {
                "userId": "string",
                "name": "string",
                "availability": {
                    "monday": [
                        {
                            "start": '8:00am',
                            "end": '12:00pm'
                        },
                        {
                            "start": '2:00pm',
                            "end": '6:00pm'
                        }
                    ],
                    "tuesday": []  # NOT AVAILABLE
                },
                "overrideDates": [
                    {
                        "date": '2021-10-10',
                        "hours": [
                            {
                                "start": '8:00am',
                                "end": '12:00pm'
                            },
                            {
                                "start": '2:00pm',
                                "end": '6:00pm'
                            }
                        ]
                    },
                    {
                        "date": '2021-10-11',
                        "hours": []  # full day
                    }
                ],
                "timeZone": "America/New_York"
            }
        }
