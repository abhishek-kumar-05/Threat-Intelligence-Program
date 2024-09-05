from flask import Flask, jsonify
import requests,base64


# insert your api key from virus total;
api_key = "Insert you virusTotalApi"

app=Flask(__name__)

@app.route('/api/virustotal', methods=['GET'])

def get_URL_Data():
    #converting the the url to url_identifier 
    url_input = input("Enter the url :- ")
    url_id = base64.urlsafe_b64encode(url_input.encode()).decode().strip("=")
    #print(url_id)

    headers = {
    "accept": "application/json",
    "x-apikey": api_key
    }

    try:
        response = requests.get(f'https://www.virustotal.com/api/v3/urls/{url_id}', headers=headers)
        response_data=response.json()
        return jsonify(response_data)

    except exception as e:
        return jsonify({'error':str(e)})


if __name__ == '__main__':
    app.run(debug=True)

