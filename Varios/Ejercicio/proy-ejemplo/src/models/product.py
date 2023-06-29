class Report:
    def __init__(self, date, dna, blood_sugar_level, emotion_level) -> None:
        self.date = date
        self.dna = dna
        self.blood_sugar_level = blood_sugar_level
        self.emotion_level = emotion_level

    def serialize(self):
        return{
            'Date': self.date,
            'dna': self.dna,
            'Blood Sugar Levels': self.blood_sugar_level,
            'Emotion Levels': self.emotion_level
        }

class Report_Average(Report):
    def __init__(self, date, dna, blood_sugar_level, emotion_level, average_blood, average_emotion) -> None:
        super().__init__(date, dna, blood_sugar_level, emotion_level)
        self.average_blood = average_blood
        self.average_emotion = average_emotion


    def serialize_average(self):
        return {
            'Average Blood Sugar Levels': self.blood_sugar_level,
            'Average Emotion Levels': self.emotion_level
        }