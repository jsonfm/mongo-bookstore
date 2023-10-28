import datetime


def add_create_timestamp(data: dict):
    data["created_at"] = datetime.datetime.now(tz=datetime.timezone.utc)
    data["updated_at"] = datetime.datetime.now(tz=datetime.timezone.utc)
    return data


def add_update_timestamp(data: dict):
    data["updated_at"] = datetime.datetime.now(tz=datetime.timezone.utc)
    return data
