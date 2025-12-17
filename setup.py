# pip install setuptools
from setuptools import find_packages, setup

setup(
    name="multilingual AI virtual assistant",
    version="0.0.0",
    author="Shivangi Tripathi",
    author_email="shivangi7273@gmail.com",
    packages=find_packages(),
    install_requires=["SpeechRecognition","pipwin","pyaudio","gTTS","google-generativeai","python-dotenv","streamlit"]
)