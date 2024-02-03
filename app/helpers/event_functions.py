from config.firebase_config import db 
from helpers.email_sender import send_email
from helpers.zoom_client import create_meeting

def create_event(date, time, attendees, timeZone, summary, userId, duration, type, isGroup=False, isOnline=True, direction=None, meetLink=None):
    try:
        doc_ref = db.collection('events').document()
        if isOnline:
            meet_date = date.split("T")[0]
            zoomLink = create_meeting(summary, duration, meet_date, time)

        doc_ref.set({
            'date': date,
            'time': time,
            'attendees': attendees,
            'timeZone': timeZone,
            'summary': summary,
            'userId': userId,
            'duration': duration,
            'type': type,
            'isGroup': isGroup,
            'isOnline': isOnline,
            'direction': direction,
            'meetLink': zoomLink['meeting_url'],
            'meetPassword': zoomLink['password']
        })


        emailResponse = []

        body = "Tienes una invitación a un evento el {} a las {} con {}. Por favor confirma tu asistencia.".format(date, time, summary)
        # if zoomLink: 
        #     body += "El evento será en línea, puedes acceder a la reunión en el siguiente enlace: {} and use the following password: {}".format(zoomLink.meeting_url, zoomLink.password)

        for attendee in attendees:
            emailResponse.append(send_email(attendee, "Invitation to {}".format(summary), body))
        return {
            "event": doc_ref.id,
            "emails": emailResponse,
            'zoomLink': doc_ref.get().to_dict()['meetLink']
        }
    except Exception as e:
        return "Error creating event: {}".format(str(e))

    

def add_multiple_events(events):
    try:
        for event in events:
            doc_ref = db.collection(u'events').document()
            doc_ref.set({
                u'date': event.date,
                u'time': event.time,
                u'attendees': event.attendees,
                u'timeZone': event.timeZone,
                u'summary': event.summary,
                u'userId': event.userId,
                u'duration': event.duration,
                u'type': event.type,
                u'isGroup': event.isGroup,
                u'isOnline': event.isOnline,
                u'direction': event.direction,
                u'meetLink': event.meetLink,
            })
        return "Events created successfully"
    except Exception as e:
        return "Error creating events: {}".format(str(e))

def get_events(userId):
    #Get all events for a user
    try:
        events = db.collection(u'events').where(u'userId', u'==', userId).stream()
        results = []
        for event in events:
            if event.to_dict()['userId'] == userId:
                results.append(event.to_dict())
        if results:
            return results
        else:
            return "No events found for user: {}".format(userId)
    except Exception as e:
        return "Error getting events: {}".format(str(e))
    