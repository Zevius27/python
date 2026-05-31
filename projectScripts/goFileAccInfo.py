import json
import requests
from dotenv import load_dotenv
import os


load_dotenv('z.env')
# Replace with your actual Gofile API Token
API_TOKEN = os.getenv('GOFILE')
# print(API_TOKEN)
# All API requests require the token in the headers for authentication
headers = {
    "Authorization": f"Bearer {API_TOKEN}"
}


def get_gofile_account_info():
    print("Fetching Account ID...")

    # Step 1: Retrieve the account ID associated with the provided API token
    get_id_url = "https://api.gofile.io/accounts/getid"
    response_id = requests.get(get_id_url, headers=headers)

    if response_id.status_code == 200:
        response_data = response_id.json()

        # Extract the account ID from the response
        account_id = response_data.get("data", {}).get("id")

        if account_id:
            print(f"Success! Account ID found: {account_id}\n")
            print("Fetching Account Details...")

            # Step 2: Retrieve detailed information about the specific account
            account_url = f"https://api.gofile.io/accounts/{account_id}"
            response_info = requests.get(account_url, headers=headers)

            if response_info.status_code == 200:
                account_details = response_info.json()
                print("---------------- Account Information -----------------")

                # Display the raw JSON data beautifullyz
                print(json.dumps(account_details, indent=4))
                print("success")
                return account_details['data']['statsCurrent']['folderCount']
            else:
                print(
                    f"Error fetching account details: {response_info.status_code} - {response_info.text}")
                return response_info.status_code, response_info.text
        else:
            print("Could not parse Account ID from the response.")
    else:

        print(
            f"Error fetching Account ID: {response_id.status_code} - {response_id.text}")
        print("Please double-check that your API token is correct.")


# Execute the function
get_gofile_account_info()
print('Helllooo   =-----------------', get_gofile_account_info())
