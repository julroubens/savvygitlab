# Create a Python script that performs the following:

# Prompt the user to type a string input as the variable for your destination URL.

# Prompt the user to select a HTTP Method of the following options:
# GET
# POST
# PUT
# DELETE
# HEAD
# PATCH
# OPTIONS
# Print to the screen the entire request your script is about to send. Ask the user to confirm before proceeding.
# Add some comments of what these request are doing to your script
# Using the requests library, perform a GET request to your github.

# For the given header, translate the codes into plain terms that print to the screen; for example, a 404 error should print Site not found to the terminal instead of 404.
#response = requests.get()
# For the given URL, print response header information to the screen.
from urllib import response
import requests

b = input("Get, Post, Put, Delete , Head, Patch, Options:")
# Get URL from user
url = input("Enter the destination URL: ")

# Print request details and get confirmation
print(f"\nAbout to send {b.upper()} request to: {url}")
confirm = input("Do you want to proceed? (y/n): ")

if confirm.lower() == 'y':
    try:
        # Send request based on selected method
        if b.lower() == 'get':
            response = requests.get(url)
        elif b.lower() == 'post':
            response = requests.post(url)
        elif b.lower() == 'put':
            response = requests.put(url)
        elif b.lower() == 'delete':
            response = requests.delete(url)
        elif b.lower() == 'head':
            response = requests.head(url)
        elif b.lower() == 'patch':
            response = requests.patch(url)
        elif b.lower() == 'options':
            response = requests.options(url)
        else:
            print("Invalid HTTP method selected")
            exit()

        # Translate status codes to plain language
        if response.status_code == 200:
            status = "Success"
        elif response.status_code == 201:
            status = "Created"
        elif response.status_code == 204:
            status = "No Content"
        elif response.status_code == 400:
            status = "Bad Request"
        elif response.status_code == 401:
            status = "Unauthorized"
        elif response.status_code == 403:
            status = "Forbidden"
        elif response.status_code == 404:
            status = "Site Not Found"
        elif response.status_code == 500:
            status = "Internal Server Error"
        else:
            status = f"Status Code: {response.status_code}"

        # Print response information
        print(f"\nResponse Status: {status}")
        print("\nResponse Headers:")
        for header, value in response.headers.items():
            print(f"{header}: {value}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
else:
    print("Request cancelled")
