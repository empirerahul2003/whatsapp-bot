from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/sms", methods=['POST'])
def reply():
    # Access the incoming message data
    incoming_msg = request.form.get('Body', '').strip()

    # Simple logic to determine response
    if 'hello' in incoming_msg.lower():
        response = "Hi there! How can I help you today?"
    else:
        response = "I'm not sure how to respond to that. Try saying 'hello'."

    # Create a response
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
