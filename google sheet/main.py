import requests
from datetime import datetime
import os

gender = "male"
weight_kg = 90
height_cm = 176
age = 20

nutritionix_api_id = os.environ["NT_APP_ID"]
nutritionix_api_key = os.environ["NT_API_KEY"]

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = os.environ["SHEET_ENDPOINT"]

exercise_params = {
    "query": input("Tell me which exercises you did: "),
    "gender": gender,
    "weight_kg": weight_kg,
    "height_cm": height_cm,
    "age": age
}

headers = {
    "x-app-id": nutritionix_api_id,
    "x-app-key": nutritionix_api_key
}

response = requests.post(url=exercise_endpoint, json=exercise_params, headers=headers)
result = response.json()
print(result)

# today_date = datetime.now().strftime("%d/%m/%Y")
# now_time = datetime.now().strftime("%X")
#
# for exercise in result["exercises"]:
#     sheet_input = {
#         "workout": {
#             "date": today_date,
#             "time": now_time,
#             "exercise": exercise["name"].title(),
#             "duration": exercise["duration_min"],
#             "calories": exercise["nf_calories"]
#         }
#     }
#     sheet_response = requests.post(sheet_endpoint, json=sheet_input)
#
#     sheet_response = requests.post(
#         sheet_endpoint,
#         json=sheet_input,
#         auth=(
#             os.environ["USERNAME"],
#             os.environ["PASSWORD"],
#         )
#     )
#
#     bearer_headers = {
#         "Authorization": f"Bearer {os.environ['TOKEN']}"
#     }
#     sheet_response = requests.post(
#         sheet_endpoint,
#         json=sheet_input,
#         headers=bearer_headers
#     )
#     print(sheet_response.text)