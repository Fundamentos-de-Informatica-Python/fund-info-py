import csv
import statistics
from models.product import Report

def save_client_statistics(info):
    with open('db/statistics.csv', 'a') as client_statistics_file:
        header = ['date', 'dna', 'blood_sugar_level', 'emotion_level']

        writer = csv.DictWriter(client_statistics_file, fieldnames=header)

        if client_statistics_file.tell() == 0:
            writer.writeheader()

        writer.writerow(info)


def load_client_statistics():
    client_statistics = []
    with open('db/statistics.csv', 'r') as statistics_file:
        rows = csv.DictReader(statistics_file)

        for row in rows:
            client_statistics.append(
                Report(
                    row['date'],
                    row['dna'],
                    row['blood_sugar_level'],
                    row['emotion_level']
                )
            )
        return client_statistics

def statistics_average():
    client_statistics = load_client_statistics()
    average_blood = statistics.mean([report.blood_sugar_level for report in client_statistics])
    average_emotion = statistics.mean([report.emotion_level for report in client_statistics])
    return average_blood, average_emotion