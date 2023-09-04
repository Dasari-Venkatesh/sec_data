
from celery import Celery
import datetime
import requests
from celery.schedules import crontab
from celery import shared_task





def fetch_13f_filings():
    # calculate today's date as end date

    # print("Hello 13f")
    # print("I am in second line")

    
    end_date = datetime.date.today()
    print(end_date)

    start_date=end_date - datetime.timedelta(days=4)

    # print(start_date)
    # end_date = "04-09-2023"
    # start_date = "02-09-2023"
    # start_date=end_date-datetime.timedelta(days=2)

    # API  endpoint``
    url = "https://api.sec-api.io"

    # payload for the post request
    data = {
        "query": {
            "query_string": {
                "query": f'formType: "13F-HR" AND NOT formType: "13F-HR/A" AND filedAt:[{start_date} TO {end_date}]',
                "time_zone": "UTC+0530" #f"UTC{current_timezone_offset}"
            }
        },
        "from": "0",
        "size": "0",
        "sort": [{ "filedAt": { "order": "desc" } }]
    }
    # data = {
    #     "query": {
    #         "query_string": {
    #             "query": "formType:\"13F-HR\" AND filedAt:[{} TO {}]".format(start_date, end_date)
    #         }
    #     },
    #     "from": "0",
    #     "size": "0",

    # }


    # # Defining the headers and  Provide the API key

    headers = {
        "Authorization": "api key",
        "Content-Type": "application/json"
    }

    # Send the post request
    response = requests.post(url, json = data ,headers = headers)

    if response.status_code == 200:
        filings = response.json()

    else:
        print("Error:",response.status_code, response.text)
        print("error in the website")
        return
    print("I got the filings.")
    print(filings)
    return filings 
    


