from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def emotionDetector():
    if request.method == 'POST':
        text_to_analyze = request.form.get('text')
        if text_to_analyze:
            result = emotion_detector(text_to_analyze)
            return render_template('index.html', text=text_to_analyze, result=result)
    return render_template('index.html', text=None, result=None)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
