---
layout: help
permalink: /help
title: AI help
---
import wolframalpha

app_id = 'YOUR_WOLFRAM_ALPHA_APP_ID'
client = wolframalpha.Client(app_id)

def handle_math_question(question):
    res = client.query(question)
    return next(res.results).text

def handle_chemistry_question(question):
    # Add your chemistry-specific logic here
    return "Answer from chemistry module"

def handle_biology_question(question):
    # Add your biology-specific logic here
    return "Answer from biology module"

def handle_computer_science_question(question):
    # Add your computer science-specific logic here
    return "Answer from computer science module"

def handle_user_query(question, domain):
    if domain == 'math':
        return handle_math_question(question)
    elif domain == 'chemistry':
        return handle_chemistry_question(question)
    elif domain == 'biology':
        return handle_biology_question(question)
    elif domain == 'computer science':
        return handle_computer_science_question(question)
    else:
        return "Domain not supported"

user_question = "What is the integral of x^2?"
user_domain = "math"
result = handle_user_query(user_question, user_domain)
print(result)
