from flask import Flask, render_template, request
import openai

app = Flask(__name__)

openai.api_key = ''  # замените на ваш собственный ключ API OpenAI

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get')
def get_bot_response():
    userText = request.args.get('msg')
    response = openai.ChatCompletion.create(
        #model='gpt-3.5-turbo-0301',      # Используйте модель GPT-3.5-turbo-0301
        model='gpt-4-0314',      # Используйте модель GPT-3.5-turbo-0301
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": userText}
        ],
        max_tokens=1000
    )
    return str(response.choices[0].message['content'].strip())

if __name__ == "__main__":
    #app.run(debug=True, host='0.0.0.0', port=8000)
    app.run(host='0.0.0.0', port=80, debug=True)
