from flask import Flask, jsonify

app = Flask(__name__)

# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

# Route to check prime number
@app.route("/prime_number/<int:number>", methods=["GET"])
def check_prime(number):
    result = {
        "Number": number,
        "isPrime": is_prime(number)
    }
    return jsonify(result)

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)