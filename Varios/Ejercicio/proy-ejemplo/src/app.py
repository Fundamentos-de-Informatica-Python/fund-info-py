from flask import Flask, jsonify, request
from db.db_manager import save_client_statistics
from db.db_manager import load_client_statistics
import statistics

app = Flask(__name__)
client_stats = load_client_statistics()

@app.route('/hello', methods=['GET'])
def hello():
    return "hello"


@app.route("/api/prometheus/statistics", methods=['GET'])
def get_client_statistics():
    stat_cl = load_client_statistics()
    for c in stat_cl:
        return jsonify(c.serialize())

@app.route('/api/prometheus/statistics', methods=['POST'])
def create_client_statistics():
    client_req_json = request.json
    save_client_statistics(client_req_json)
    return jsonify(client_req_json)


@app.route("/api/prometheus/statistics/reports/<date>", methods=['GET'])
def get_stat_by_date(date):
    date = request.args.get('date')
    if date == None:
        return jsonify({"error": "no date info given"})
    else:
        average_blood = statistics.mean([int(date.blood_sugar_level) for date in client_stats])
        average_emotion = statistics.mean([int(date.emotion_level) for date in client_stats])
        return jsonify({"average_blood_level": average_blood, "average_emotion_level": average_emotion})




if __name__ == '__main__':
    app.run(debug=True, port=5000)
