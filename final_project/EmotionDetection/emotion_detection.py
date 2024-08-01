import requests
import json

def emotion_detector(text_to_analyze):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = {"raw_document": {"text": text_to_analyze}}
    
    response = requests.post(URL, json=input_json, headers=headers)
    
    if response.status_code == 200:
        response_dict = response.json()
        
        # Check if 'emotionPredictions' is in the response
        if 'emotionPredictions' in response_dict and response_dict['emotionPredictions']:
            emotions = response_dict['emotionPredictions'][0]['emotion']
            anger = emotions.get('anger', 0)
            disgust = emotions.get('disgust', 0)
            fear = emotions.get('fear', 0)
            joy = emotions.get('joy', 0)
            sadness = emotions.get('sadness', 0)
            dominant_emotion = max(emotions, key=emotions.get)
            
            formatted_response = {
                'anger': anger,
                'disgust': disgust,
                'fear': fear,
                'joy': joy,
                'sadness': sadness,
                'dominant_emotion': dominant_emotion
            }
            return formatted_response
        
        else:
            return {
                'anger': None,
                'disgust': None, 
                'fear': None, 
                'joy': None, 
                'sadness': None, 
                'dominant_emotion': None
            }
        
    elif response.status_code == 400:
        return {
            'anger': None,
            'disgust': None, 
            'fear': None, 
            'joy': None, 
            'sadness': None, 
            'dominant_emotion': None
        }

def emotion_predictor(text_to_analyze):
    detected_text = emotion_detector(text_to_analyze)
    return detected_text

#...........................
# import requests
# import json

# def emotion_detector(text_to_analyze):
#     URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
#     headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
#     input_json = {"raw_document": {"text": text_to_analyze}}
    
#     response = requests.post(URL, json=input_json, headers=headers)
    
#     if response.status_code == 200:
#         response_dict = response.json()
        
#         # Check if 'emotionPredictions' is in the response
#         if 'emotionPredictions' in response_dict and response_dict['emotionPredictions']:
#             emotions = response_dict['emotionPredictions'][0]['emotion']
#             dominant_emotion = max(emotions, key=emotions.get)
#             return dominant_emotion
#         else:
#             return None
#     elif response.status_code == 400:
#         return None

# # Example usage:
# text_to_analyze = "I love this new technology"
# dominant_emotion = emotion_detector(text_to_analyze)
# print(dominant_emotion)
