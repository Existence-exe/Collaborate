from flask import Flask , request , json , hashlib
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
        ihash = blake2b(digest_size=20)
        ihash.update(mail)
        with open('./storage/creds.json', 'r') as f : 
            ex_cred = json.load(f)
        if ihash in ex_cred :
            return "User already exists!"
        else :
            ex_cred[ihash] = {}
            ex_cred[ihash] = data
            with open('./storage/creds.json','w') as f :
                json.dump(data,f)
        return data
    else:
        return 'Content-Type not supported!'

@app.route("/login",methods=['POST'])
def login():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        data = request.json
        handle = data['handle']
        if '.' in [a for a in handle] :
            if handle.endswith('.com') : 
                with open('./storage/creds.json', 'r') as f : 
                    ex_cred = json.load(f)
                    if handle in ex_cred : 
                        print('a')
                        pass
                    else : 
                        print('b')
                        return "User doesn't exist!"  
            else : 
                print('a')
                return "Invalid handle"
            return "420: BAD PLAYER"
        else : 
            with open('./storage/creds.json', 'r') as f : 
                    ex_cred = json.load(f)
                    if handle == ex_cred['mail'] or handle == ex_cred['username'] : 
                        print('d')
                        pass
                    else : 
                        print('e')
                        return "User doesn't exist!"
        return data
    else:
        return 'Content-Type not supported!'

@app.route("/<data1>-<data2>",methods=['POST'])
def messages(data1,data2):
    print(data1,data2)


if __name__ == '__main__':
    app.run()