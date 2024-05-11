import mongoengine as db_engine
# from settings import MONGO_DB, MONGO_DB_PORT, MONGO_DB_HOST, MONGO_DB_USER, MONGO_DB_PASS

# try:
#     db_engine.connect(
#         MONGO_DB, host=MONGO_DB_HOST, port=MONGO_DB_PORT,
#         username=MONGO_DB_USER, password=MONGO_DB_PASS,
#         alias="default")
# except Exception:
#     pass

class TechLoreTest(db_engine.Document):
    test_user_name = db_engine.StringField()
    test_user_id = db_engine.IntField()