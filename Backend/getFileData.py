from flask import Flask, jsonify
import requests
import hashlib

# insert your api key from virus total;
api_key = "Insert you virusTotalApi"

app=Flask(__name__)

@app.route('/api/filedata', methods=['GET'])

def get_File_Data():

    #converting file path to hash
    def identifier_sha256(file_path):
        sha256_hash = hashlib.sha256()
        with open(file_path, "rb") as file:
            while True:
                data = file.read(65536)  # Read the file in 64KB chunks
                if not data:
                    break
                sha256_hash.update(data)
        return sha256_hash.hexdigest()

    #file path
    file_path = input("Enter File Path :- ")
    file_identifier = identifier_sha256(file_path)
    # print(file_identifier)

    headers = {
    "accept": "application/json",
    'x-apikey': api_key
    }

    try:
        response = requests.get(f'https://www.virustotal.com/api/v3/files/{file_identifier}', headers=headers)
        response_data=response.json()
        return jsonify(response_data)

    except exception as e:
        return jsonify({'error':str(e)})


if __name__ == '__main__':
    app.run(debug=True)


