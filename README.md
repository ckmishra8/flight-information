# Flight Information
This project provides few APIs to manipulate flight information. For fetching any flight related data user needs to have valid API token.

## Setup
It runs on the local server. User needs to execute `deploy.sh` file in-order to install all the prerequisite and start the application. Please install [sqlite](https://www.sqlite.org/download.html) as per you operating system before starting the application.
The project is developed on [Python3.x](https://www.python.org/downloads/), user must install Python3 before executing `deploy.sh`

## API details

| API Name | API Path  | Method  | API Details |
| :-----: | :-: | :-: | :-: |
| Index | / | GET | Details about Flight APIs |
| Register | /v1/auth/register | POST | API to register an user |
| Login | /v1/auth/login | POST | API to login and get API token |
| Logout | /v1/auth/logout | POST | API to logout API token |
| AddFlightInformation | /v1/flight/add | POST | API to add flight details |
| RemoveFlightInformation | /v1/flight/remove | POST | API to remove flight details |
| UpdateFlightInformation | /v1/flight/update | POST | API to update flight details |
| SearchFlightInformation | /v1/flight/search | GET | API to search flight details |

## Architecture
Below is the architecture of the project:

![architecture](architecture.png)
