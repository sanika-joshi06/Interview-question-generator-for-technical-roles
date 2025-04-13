from flask import Flask, render_template, request, jsonify
import openai
import os
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
app.config['DEBUG']=True
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_questions():
    data = request.get_json()
    role = data['role']
    level = data['level']

    prompt = f"""
    Generate a list of 10 technical interview questions for the role of "{role}".
    The questions should be suitable for a candidate with {level} level of experience.
    Cover a mix of theory, practical problem-solving, and conceptual questions.
    Format as a numbered list.
    """

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{ "role": "user", "content": prompt }],
        temperature=0.7,
        max_tokens=600
    )

    questions = response.choices[0].message.content.strip()
    return jsonify({ 'questions': questions })

if __name__ == '__main__':
    app.run(debug=True)