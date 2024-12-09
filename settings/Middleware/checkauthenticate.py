import requests
def check_auth_usermicroserivices(token):
    try:
        Apiurl='http://localhost:3003/api/users/check_user'
        headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"  # Optional, depending on the API
        }

        # Make a GET request
        response = requests.get(Apiurl, headers=headers)
        if response.status_code==200:
            data= response.json()
            if data.get('role') in ['Owner','Admin']:
                return {"status":200,"data":data}
            else:
                return {"status":404, "mesaage":"User does not have the required permissions"}
        else:
            return response.json()
    except requests.exceptions.RequestException as e:
        return {"status":500,"message":"internal Error Occurs"}