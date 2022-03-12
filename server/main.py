from flask import Flask , request , json
from flask_cors import CORS
from hashlib import blake2b

app = Flask(__name__)
CORS(app)

@app.route('/')
def main():
    return {'status': 'success'}

@app.route("/signup", methods=['POST'])
def signup():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        data = request.json
        mail = data['mail']
        with open('./storage/creds.json', 'r') as f : 
            ex_cred = json.load(f)
        if mail in ex_cred :
            return "User already exists!"
        else :
            ex_cred[mail] = {}
            ex_cred[mail] = data
            with open('./storage/creds.json','w') as f :
                json.dump(ex_cred,f)
        return data
    else:
        return 'Content-Type not supported!'

@app.route("/login",methods=['POST'])
def login():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        data = request.json
        handle = data['handle']
        password = data['password']
        if handle.endswith('.com') : 
            with open('./storage/creds.json', 'r') as f : 
                ex_cred = json.load(f)
                if handle in ex_cred and ex_cred[handle]['password'] == password :
                    return "Login successful"
                else:
                    return "Invalid credentials"
        else :
            with open('./storage/creds.json', 'r') as f : 
                ex_cred = json.load(f)
                for item in ex_cred:
                    if ex_cred[item]['username'] == handle and ex_cred[item]['password'] == password:
                        return "Login successful"
                    else:
                        print(ex_cred[item])
                        print(handle, password)
                        return "Invalid credentials"
                
                return "User doesn't exist"
    else:
        return 'Content-Type not supported!'

@app.route("/<data1>-<data2>",methods=['POST'])
def messages(data1,data2):
    print(data1,data2)


if __name__ == '__main__':
    app.run()
