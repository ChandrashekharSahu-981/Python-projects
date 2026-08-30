import requests
from dotenv import load_dotenv
import os
from datetime import datetime as dt

load_dotenv()

user_name = os.getenv("USER_NAME")
pixela_token = os.getenv("PIXELA")
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token" : pixela_token,
    "username" : user_name,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes"
}

""" Pixela user account have already been created.The following code is only required for initial setup."""
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{user_name}/graphs"
graph_config = {
    "id" : GRAPH_ID,
    "name" : "Coding",
    "unit" : "commit",
    "type" : "int",
    "color" : "sora"
}
headers = {
    "X-USER-TOKEN" : pixela_token
}

""" Pixela graph have already been created.The following code is only required for initial setup."""
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

while True:

    print("\n===== PIXELA CODING TRACKER =====")
    print("1. Add commits")
    print("2. Update commits")
    print("3. Delete commits")
    print("4. Exit")

    choice = input("Choose an option: ")

    # ADD
    if choice == "1":

        commit_count = int(input("How many commits did you make today? "))
        pixel_creation_endpoint = f"{pixela_endpoint}/{user_name}/graphs/{GRAPH_ID}"
        today = dt.now()
        pixel_data = {
            "date" : today.strftime("%Y%m%d"),
            "quantity" : str(commit_count)
        }
        response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
        print(response.text)

    # UPDATE
    elif choice == "2":

        date_input = input("Enter date (DD-MM-YYYY): ")
        date = dt.strptime(date_input, "%d-%m-%Y").strftime("%Y%m%d")
        commit_count = int(input("Enter new number of commits: "))
        pixel_data = {
            "quantity": str(commit_count)
        }
        update_endpoint = f"{graph_endpoint}/{GRAPH_ID}/{date}"
        response = requests.put(url=update_endpoint, json=pixel_data, headers=headers)
        print(response.text)

    # DELETE
    elif choice == "3":

        date_input = input("Enter date (DD-MM-YYYY): ")
        date = dt.strptime(date_input, "%d-%m-%Y").strftime("%Y%m%d")
        delete_endpoint = f"{graph_endpoint}/{GRAPH_ID}/{date}"
        response = requests.delete(url=delete_endpoint, headers=headers)
        print(response.text)

    # EXIT
    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid option.")








