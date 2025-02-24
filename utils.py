from typing import Any

from schmeas.userwithmetadata import user_w_metadata


def return_user(result) -> list[dict[str, Any]]:
    user_list = []
    for row in result:
        user = user_w_metadata(row["user_id"], row["name"], row["email"], row["email"].split("@")[0],
                               row["email"].split("@")[1])
        user_list.append(vars(user))
    return user_list