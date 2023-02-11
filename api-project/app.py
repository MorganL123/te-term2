from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/genre', methods=['POST'])
def genre_fn():
    genre = request.form['dropdown']
    response = requests.get(f"https://openlibrary.org/subjects/{genre}.json") 
    data = response.json()  
    #return data['works'][0]['title']
    return render_template('genre.html',data=data)

if __name__== '__main__':
    app.run(debug=True, host ='0.0.0.0', port = 9000)