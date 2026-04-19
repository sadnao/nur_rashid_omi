from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)
connection = mysql.connector.connect(
    host='localhost',
    port=3306,
    database='demogame',
    user='root',
    password='passisset',
    autocommit=True
)

@app.route('/airport/<icao>')
def get_airport(icao):
    cursor = connection.cursor(dictionary=True)

    query = "SELECT name, municipality FROM airport WHERE ident = %s"
    cursor.execute(query, (icao,))
    result = cursor.fetchone()

    if result:
        return jsonify({
            "ICAO": icao,
            "Name": result["name"],
            "Location": result["municipality"]
        })
    else:
        return jsonify({"error": "Airport not found"})

if __name__ == '__main__':
    app.run(debug=True, port=5001)