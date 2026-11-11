from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/api/submit", methods=["POST"])
def submit():
    data = request.get_json()

    name = data.get("name", "")
    email = data.get("email", "")
    message = data.get("message", "")

    if not name or not email or not message:
        return jsonify({"error": "All fields are required"}), 400

    print(f"Received submission from {name}: {email}")

    return jsonify({
        "message": f"Thank you, {name}! Your submission was received."
    })

@app.route("/health")
def health():
    return jsonify({"status": "Backend is running"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
