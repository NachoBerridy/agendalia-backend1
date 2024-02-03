from config.firebase_config import db 
from helpers.event_functions import get_events
from datetime import datetime, timedelta, timezone
from dateutil import parser

def save_availability(userId, availability, overrideDates, timeZone, name):
    try:
        # Use collection without specifying document ID to generate a unique ID
        doc_ref = db.collection(u'availability').add({
            u'userId': userId,
            u'availability': availability,
            u'overrideDates': overrideDates,
            u'timeZone': timeZone,
            u'name': name,
        })
        return "Availability saved successfully: {}".format(doc_ref.id)
    except Exception as e:
        # Handle exceptions
        return "Error saving availability: {}".format(str(e))

def get_availability(userId):
    try:
        availability = db.collection(u'availability').where(u'userId', u'==', userId).stream()
        results = []
        for avail in availability:
            if avail.to_dict()['userId'] == userId:
                results.append(avail.to_dict())
        if results:
            return results
        else:
            return "No availability found for user: {}".format(userId)
    except Exception as e:
        return "Error getting availability: {}".format(str(e))
    
    
def convert_12h_to_24h(time_12h):
    return parser.parse(time_12h).strftime("%H:%M")

def generate_time_slots(start_time, end_time):
    current_datetime = start_time
    time_slots = []
    while current_datetime <= end_time:
        time_slots.append(current_datetime.strftime("%H:%M"))
        current_datetime += timedelta(minutes=15)
    return time_slots

def filter_events(response, events, year, month, day):
    for event in events:
        event_datetime = parser.parse(event['date']).replace(tzinfo=timezone.utc)
        if event_datetime.year == year and event_datetime.month == month and event_datetime.day == day:
            event_start_time = event_datetime.strftime("%H:%M")
            event_end_time = (event_datetime + timedelta(minutes=event['duration'])).strftime("%H:%M")
            response = [time for time in response if not (event_start_time <= time < event_end_time)]
    return response

def get_availability_with_events(userId, month, year, day):
    try:
        availability = get_availability(userId)
        events = get_events(userId)
        
        base_availability = availability[0]

        month_start = datetime(year, month, 1)
        month_end = datetime(year, month + 1, 1) - timedelta(days=1)
        day_of_week = datetime(year, month, day).strftime("%A").lower()
        
        availability_day = base_availability['availability'][day_of_week]

        response = []

        for availability in availability_day:
            start_time_24h = convert_12h_to_24h(availability['start'])
            end_time_24h = convert_12h_to_24h(availability['end'])

            time_slots = generate_time_slots(parser.parse(start_time_24h), parser.parse(end_time_24h))
            response.extend(time_slots)

        response = filter_events(response, events, year, month, day)

        return response
    except Exception as e:
        return {"error": "Error getting availability: {}".format(str(e))}
    


