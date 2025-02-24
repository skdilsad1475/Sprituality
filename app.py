from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit_quiz():
    data = request.json
    score = data['score']
    
    # Custom response based on score
    if score >= 50:
        message = "You have a high level of spirituality and security awareness!"
    elif score >= 30:
        message = "You're doing well, but there's room for improvement."
    else:
        message = "You need to improve your spirituality and security habits."

    return jsonify({"message": message, "score": score})

if __name__ == '__main__':
    app.run(debug=True)
