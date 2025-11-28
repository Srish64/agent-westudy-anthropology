import uuid
def gen_session_id():
    return uuid.uuid4().hex[:8]