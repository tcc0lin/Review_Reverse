def _get_signature(timestamp: int): str:
    ha = hmac.new(
        b"d1b964811afb40118a12068ff74a12f4",
        digestmod=hashlib.sha1
    )
    grant_type = login_data["grant_type"]
    client_id = login_data["client_id"]
    source = login_data["source"]
    ha.update(
        bytes(
            (grant_type + client_id + source + str(timestamp)),
            "utf-8"
        )
    )
    return ha.hexdigest()