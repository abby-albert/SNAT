from flask import Flask, Blueprint, jsonify, request
from flask_restful import Api, Resource
from flask_cors import CORS
import requests


grammar_bot = Blueprint('grammar_bot', __name__,
                   url_prefix='/api/grammar')

# API generator https://grammarbot.p.rapidapi.com/check
api = Api(grammar_bot)


# URL and endpoint for GrammarBot API
url = 'https://grammarbot.p.rapidapi.com/check'

# Set your RapidAPI key
rapidapi_key = '9fb198c26fmsh98120fcb28c72fdp100517jsn7aa4c1e9a84c'

# Set headers for the request
headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'X-RapidAPI-Key': rapidapi_key,
    'X-RapidAPI-Host': 'grammarbot.p.rapidapi.com'
}

# Set data for the request
data = {
    'text': 'Susan go to the store everyday',
    'language': 'en-US'
}
