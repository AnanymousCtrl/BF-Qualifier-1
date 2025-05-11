import requests
import json
# imported the required library for API working

url = "https://bfhldevapigw.healthrx.co.in/hiring/generateWebhook/PYTHON"
# this is url for posting the data to API

payload = json.dumps({
  "name": "RISHABH TIWARI",
  "regNo": "0827CD221059",
  "email": "rishabhtiwari220932@acropolis.in"
})

headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

webhook_data = response.json()
# this gives back the auth token and webhook for sql solution
access_token = webhook_data.get('accessToken')
submission_webhook = webhook_data.get('webhook')

headers = {
    "Authorization": access_token,
    "Content-Type": "application/json"
}

final_query = 'select pay.amount SALARY, concat(emp.FIRST_NAME, ' ', emp.LAST_NAME) NAME, year(current_date()) - year(emp.DOB) AGE, dep.DEPARTMENT_NAME from payments pay join employee emp on pay.EMP_ID = emp.EMP_ID join department dep ON emp.DEPARTMENT = dep.DEPARTMENT_ID where day(pay.payment_time) != 1 order by pay.AMOUNT desc limit 1;'
solution_payload = {
    "finalQuery": final_query
}

submission_response = requests.post(
    submission_webhook, 
    headers=headers,
    json=solution_payload
)

print("Solution submitted successfully!")