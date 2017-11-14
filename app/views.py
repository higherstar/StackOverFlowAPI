from flask import render_template, redirect, url_for, request
import requests, json
from app import app

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/basic', methods = ['POST'])
def success_basic():
    if request.method == 'POST':
        result = requests.get("http://api.stackexchange.com/2.2/users/"+request.form.get('id')+"/posts?order=desc&sort=activity&site=stackoverflow")

        data = json.loads(result.text)

        return render_template('basic.html', data = data['items'])

@app.route('/oauth', methods=['GET'])
def success_oauth():
    if request.method == 'GET':
        l_code = request.args.get('code')

        post = requests.post("https://stackexchange.com/oauth/access_token/json", {'client_id': 11232, 'code': l_code, 'redirect_uri': 'https://evening-bastion-23546.herokuapp.com/oauth', 'client_secret': 'RMbXU*ZWMEmksJa9Jr9mlw(('})

        token = json.loads(post.text)['access_token']

        result = requests.get("https://api.stackexchange.com/2.2/me?key=wgCesEt7UiUBalOQX*4E9A((&site=stackoverflow&order=desc&sort=reputation&access_token="+token+"&filter=default")

        id = json.loads(result.text)['items'][0]['user_id']

        res = requests.get("http://api.stackexchange.com/2.2/users/"+str(id)+"/posts?order=desc&sort=activity&site=stackoverflow")

        data = json.loads(res.text)

        return render_template('oauth.html', data=data['items'])