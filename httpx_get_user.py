import time

import httpx

payload = {
    "email": f"{time.time()}@example.com",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string",
    "phoneNumber": "string"
}

create_user_response = httpx.post("http://localhost:8003/api/v1/users", json=payload)
create_user_response_data = create_user_response.json()

user_id = create_user_response_data["user"]["id"]
get_user_response = httpx.get(f"http://localhost:8003/api/v1/users/{user_id}")
get_user_response_data = get_user_response.json()

print("Get user response:", get_user_response_data)
print("Status Code:", get_user_response.status_code)