from flask import Flask, request, jsonify
import util2

app = Flask(__name__)
@app.route('http://localhost:5000/classify_image', methods=['GET', 'POST'])
def classify_image():
    image_data = request.form['image_data']

    response = jsonify(util2.classify_image(image_data))

    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Technology's Scientist Image Classification")
    util2.load_saved_artifacts()
    app.run(port=5000)