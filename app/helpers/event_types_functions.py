from config.firebase_config import db 
from helpers.firebase_auth import get_user_by_userName

class EventTypeCreationError(Exception):
    pass


def save_event_type(name, description, duration, price, isGroup, isOnline, direction, meetService, link, isActive, userId):
    try:
        price = price.dict()
        doc_ref = db.collection(u'event_types').document()
        #Verify this user has not created an event type with this name
        event_types = db.collection(u'event_types').where(u'userId', u'==', userId).stream()
        for event_type in event_types:
            if event_type.to_dict()['name'] == name:
                raise Exception("Ya existe un evento con este nombre")
        doc_ref.set({
            u'name': name,
            u'description': description,
            u'duration': duration,
            u'price': price,
            u'isGroup': isGroup,
            u'isOnline': isOnline,
            u'directions': direction,
            u'meetService': meetService,
            u'link': link,
            u'isActive': isActive,
            u'userId': userId,
        })
        return "Event type saved successfully: {}".format(doc_ref.id)
    except Exception as e:
        raise EventTypeCreationError(str(e))
    
def get_event_types(userId):
    try:
        event_types = db.collection(u'event_types').where(u'userId', u'==', userId).stream()
        results = []
        for event_type in event_types:
            if event_type.to_dict()['userId'] == userId:
                results.append(event_type.to_dict())
        if results:
            return results
        else:
            return "No event types found for user: {}".format(userId)
    except Exception as e:
        return "Error getting event types: {}".format(str(e))
    
def get_event_types_by_username(userName):
    try:
        # Convertir userName a minúsculas
        userName_lower = userName.lower()

        response = get_user_by_userName(userName_lower)
        uid = response['id']

        if uid:
            # Obtener event types
            return {
                "event_types": get_event_types(uid),
                'user': response['user']['firstName'] + " " + response['user']['lastName']
            }
        else:
            return "No user found with username: {}".format(userName)
    except Exception as e:
        return "Error getting event types: {}".format(str(e))


def get_event_type_by_link(userName, link):
    try:    
        # Convertir userName a minúsculas
        userName_lower = userName.lower()

        response = get_user_by_userName(userName_lower)
        uid = response['id']

        if uid:
            event_types = db.collection(u'event_types').where(u'userId', u'==', uid).stream()
            for event_type in event_types:
                if event_type.to_dict()['link'] == link:
                    return {
                        'event_type': event_type.to_dict(),
                        'user': response['user']['firstName'] + " " + response['user']['lastName'],
                        'userEmail': response['user']['email']
                    }
            return "No event type found with link: {}".format(link)
        else:
            return "No user found with username: {}".format(userName)
    except Exception as e:
        return "Error getting event type: {}".format(str(e))