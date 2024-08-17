from flask import Flask, jsonify

app = Flask(__name__)

feeding_stats = []
petting_stats = []

@app.route('/stats', methods=['GET'])
def stats():
    return jsonify({
        'feeding': feeding_stats,
        'petting': petting_stats
    })


if __name__ == "__main__":
    app.run(debug=False)