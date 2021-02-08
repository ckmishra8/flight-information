[![Build Status](https://travis-ci.com/thisischandanmishra/flight-information.svg?branch=master)](https://travis-ci.com/thisischandanmishra/flight-information)

# Flight Information
This project provides few APIs to manipulate flight information. For fetching any flight related data user needs to have valid API token.

## Setup
It runs on the local server. User needs to execute `run.sh` file in-order to install all the prerequisite and start the application. Please install [sqlite](https://www.sqlite.org/download.html) as per you operating system before starting the application.
The project is developed on [Python3.x](https://www.python.org/downloads/), user must install Python3 before executing `run.sh`
It creates a virtual environment `flight_info_venv` and installs all the required packages.

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

## Sample APIs calls
**Index**
```
    {
      "name": "Index",
      "request": {
        "method": "GET",
        "header": [],
        "url": {
          "raw": "http://localhost:5000",
          "protocol": "http",
          "host": [
            "localhost"
          ],
          "port": "5000"
        }
      },
      "response": <Make Actual API call to get response>
    }
```
**User Register**
```
    {
      "name": "Register",
      "request": {
        "method": "POST",
        "header": [],
        "body": {
          "mode": "raw",
          "raw": "{\n    \"username\": \"admin\",\n    \"password\": \"1234567890\",\n    \"email\": \"admin@test.comm\"\n}",
          "options": {
            "raw": {
              "language": "json"
            }
          }
        },
        "url": {
          "raw": "http://localhost:5000/v1/auth/register",
          "protocol": "http",
          "host": [
            "localhost"
          ],
          "port": "5000",
          "path": [
            "v1",
            "auth",
            "register"
          ]
        }
      },
      "response": <Make Actual API call to get response>
    }
```
**User Login**
```
    {
      "name": "Login",
      "request": {
        "method": "POST",
        "header": [],
        "body": {
          "mode": "raw",
          "raw": "{\n    \"password\": \"1234567890\",\n    \"email\": \"admin@test.com\"\n}",
          "options": {
            "raw": {
              "language": "json"
            }
          }
        },
        "url": {
          "raw": "http://localhost:5000/v1/auth/login",
          "protocol": "http",
          "host": [
            "localhost"
          ],
          "port": "5000",
          "path": [
            "v1",
            "auth",
            "login"
          ]
        }
      },
      "response": <Make Actual API call to get response>
    }
```
**Add Flight Details**
```
{
      "name": "Add Flight",
      "request": {
        "auth": {
          "type": "bearer",
          "bearer": [
            {
              "key": "token",
              "value": "eyJhbGciOiJIUzUxMiIsImlhdCI6MTYxMjY5OTcwMCwiZXhwIjoxNjEyNzA2OTAwfQ.eyJlbWFpbCI6ImFkbWluQHRlc3QuY29tbSIsImFkbWluIjowfQ.xs1Wk3tQVkqVagEz_XQyXBYBVeudpAAHcUP1e6RGeSt5_tApvSXwLYFpo5hukG8H2x1f-YugU4C6qwbT3NRHmA",
              "type": "string"
            }
          ]
        },
        "method": "POST",
        "header": [],
        "body": {
          "mode": "raw",
          "raw": "{\n    \"flight_number\": 6,\n    \"flight_name\": \"Air Asia\",\n    \"departure\": \"BLR\",\n    \"destination\": \"XLR\",\n    \"fare_in_usd\": 200\n}",
          "options": {
            "raw": {
              "language": "json"
            }
          }
        },
        "url": {
          "raw": "http://localhost:5000/v1/flight/add",
          "protocol": "http",
          "host": [
            "localhost"
          ],
          "port": "5000",
          "path": [
            "v1",
            "flight",
            "add"
          ]
        }
      },
      "response": <Make Actual API call to get response>
    }
```
**Remove flight Details**
```
{
      "name": "Remove flight",
      "request": {
        "auth": {
          "type": "bearer",
          "bearer": [
            {
              "key": "token",
              "value": "eyJhbGciOiJIUzUxMiIsImlhdCI6MTYxMjY5OTcwMCwiZXhwIjoxNjEyNzA2OTAwfQ.eyJlbWFpbCI6ImFkbWluQHRlc3QuY29tbSIsImFkbWluIjowfQ.xs1Wk3tQVkqVagEz_XQyXBYBVeudpAAHcUP1e6RGeSt5_tApvSXwLYFpo5hukG8H2x1f-YugU4C6qwbT3NRHmA",
              "type": "string"
            }
          ]
        },
        "method": "POST",
        "header": [],
        "body": {
          "mode": "raw",
          "raw": "{\n    \"flight_number\": 202\n}",
          "options": {
            "raw": {
              "language": "json"
            }
          }
        },
        "url": {
          "raw": "http://localhost:5000/v1/flight/remove",
          "protocol": "http",
          "host": [
            "localhost"
          ],
          "port": "5000",
          "path": [
            "v1",
            "flight",
            "remove"
          ]
        }
      },
      "response": <Make Actual API call to get response>
    }
```
**Update flight Details**
```
{
      "name": "Update flight",
      "request": {
        "auth": {
          "type": "bearer",
          "bearer": [
            {
              "key": "token",
              "value": "eyJhbGciOiJIUzUxMiIsImlhdCI6MTYxMjYxMjA3NCwiZXhwIjoxNjEyNjE1Njc0fQ.eyJlbWFpbCI6InZrbWNmdEBnbWFpbC5jb20iLCJhZG1pbiI6MH0.5DGUliuqXeNySubJr_GDasELRZnXJAnFUF0N3cU88hMYvmj2Qfzgril5DXermw-sEXrim6Ilsmz4zHlLoT-TYQ",
              "type": "string"
            }
          ]
        },
        "method": "POST",
        "header": [],
        "body": {
          "mode": "raw",
          "raw": "{\n    \"flight_name\": \"Air XYZ\",\n    \"departure\": \"PTL\",\n    \"destination\": \"ADV\",\n    \"fare_in_usd\": 420\n}",
          "options": {
            "raw": {
              "language": "json"
            }
          }
        },
        "url": {
          "raw": "http://localhost:5000/v1/flight/update",
          "protocol": "http",
          "host": [
            "localhost"
          ],
          "port": "5000",
          "path": [
            "v1",
            "flight",
            "update"
          ]
        }
      },
      "response": <Make Actual API call to get response>
    }
```
**Search flight details**
```
{
      "name": "Search flight",
      "protocolProfileBehavior": {
        "disableBodyPruning": true
      },
      "request": {
        "auth": {
          "type": "bearer",
          "bearer": [
            {
              "key": "token",
              "value": "eyJhbGciOiJIUzUxMiIsImlhdCI6MTYxMjY5OTcwMCwiZXhwIjoxNjEyNzA2OTAwfQ.eyJlbWFpbCI6ImFkbWluQHRlc3QuY29tbSIsImFkbWluIjowfQ.xs1Wk3tQVkqVagEz_XQyXBYBVeudpAAHcUP1e6RGeSt5_tApvSXwLYFpo5hukG8H2x1f-YugU4C6qwbT3NRHmA",
              "type": "string"
            }
          ]
        },
        "method": "GET",
        "header": [],
        "body": {
          "mode": "raw",
          "raw": "{\n}",
          "options": {
            "raw": {
              "language": "json"
            }
          }
        },
        "url": {
          "raw": "http://localhost:5000/v1/flight/search",
          "protocol": "http",
          "host": [
            "localhost"
          ],
          "port": "5000",
          "path": [
            "v1",
            "flight",
            "search"
          ]
        }
      },
      "response": <Make Actual API call to get response>
    }
```
**User Logout**
```
{
      "name": "Logout flight",
      "request": {
        "auth": {
          "type": "bearer",
          "bearer": [
            {
              "key": "token",
              "value": "eyJhbGciOiJIUzUxMiIsImlhdCI6MTYxMjY5OTcwMCwiZXhwIjoxNjEyNzA2OTAwfQ.eyJlbWFpbCI6ImFkbWluQHRlc3QuY29tbSIsImFkbWluIjowfQ.xs1Wk3tQVkqVagEz_XQyXBYBVeudpAAHcUP1e6RGeSt5_tApvSXwLYFpo5hukG8H2x1f-YugU4C6qwbT3NRHmA",
              "type": "string"
            }
          ]
        },
        "method": "POST",
        "header": [],
        "url": {
          "raw": "http://localhost:5000/v1/auth/logout",
          "protocol": "http",
          "host": [
            "localhost"
          ],
          "port": "5000",
          "path": [
            "v1",
            "auth",
            "logout"
          ]
        }
      },
      "response": <Make Actual API call to get response>
    }
```
