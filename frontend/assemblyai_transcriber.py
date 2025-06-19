import requests
import time

import streamlit as st
API_KEY = st.secrets["ASSEMBLYAI_API_KEY"]


headers = {
    "authorization": API_KEY,
    "content-type": "application/json"
}

upload_headers = {
    "authorization": API_KEY
}


def upload_audio(file_path):
    with open(file_path, 'rb') as f:
        response = requests.post(
            'https://api.assemblyai.com/v2/upload',
            headers=upload_headers,
            data=f
        )
    return response.json()['upload_url']


def transcribe_audio(audio_url):
    json = {
        "audio_url": audio_url
    }
    response = requests.post(
        'https://api.assemblyai.com/v2/transcript',
        json=json,
        headers=headers
    )
    transcript_id = response.json()['id']
    polling_endpoint = f"https://api.assemblyai.com/v2/transcript/{transcript_id}"

    while True:
        transcription_result = requests.get(polling_endpoint, headers=headers).json()
        if transcription_result['status'] == 'completed':
            return transcription_result['text']
        elif transcription_result['status'] == 'error':
            raise Exception("Transcription failed:", transcription_result['error'])
        time.sleep(3)