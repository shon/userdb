import uuid
import pickle
import settings
import redis

rconn = redis.Redis(
    host=settings.SESSIONS_DB_HOST,
    port=settings.SESSIONS_DB_PORT,
    password=settings.SESSIONS_DB_PASSWORD,
    db=settings.SESSIONS_DB_NO
    )


def skey(sid):
    return settings.SESSION_KEY_SEP.join((settings.SESSION_KEY_PREFIX, sid))


def gen_sid():
    return str(uuid.uuid4())


def create():
    sid = gen_sid()
    return sid


def exists(sid):
    return rconn.exists(skey(sid))


def get(sid, keys=[]):
    if keys:
        s_values = rconn.hmget(skey(sid), keys)
        data = {k: pickle.loads(v) if v else v for k, v in zip(keys, s_values)}
    else:
        s_values = rconn.hgetall(skey(sid))
        if s_values is None:
            s_values = {}
        data = {k.decode('ascii'): pickle.loads(v) for k, v in s_values.items()}
    return data


def get_attribute(sid, attribute):
    value = rconn.hget(skey(sid), attribute)
    return pickle.loads(value) if value else None


def destroy(sid):
    rconn.delete(skey(sid))
    return True


def update(sid, mod_data):
    key = skey(sid)
    mod_data = {k: pickle.dumps(v) for k, v in mod_data.items()
                if k in settings.SESSION_KEYS}
    rconn.hmset(key, mod_data)
    rconn.expire(key, settings.SESSION_TTL)
    return True


def update_attribute(sid, attribute, value):

    key = skey(sid)
    rconn.hset(key, attribute, pickle.dumps(value))
    rconn.expire(key, settings.SESSION_TTL)
    return True
