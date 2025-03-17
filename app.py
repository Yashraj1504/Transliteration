from flask import Flask, render_template, request

from langchain_groq import ChatGroq

app = Flask(__name__)

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.1,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    api_key="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" 
)

@app.route("/", methods=["GET", "POST"])
def index():
    transliterated_text = None  

    if request.method == "POST":
        user_input = request.form["text_input"]

        # Define system message and input message
        messages = [
            ("system", "You are an AI that performs transliteration, converting English words into Marathi script without translating them. Preserve the original pronunciation as much as possible."),
            ("human", user_input),
        ]

        # Invoke the model
        response = llm.invoke(messages)
        transliterated_text = response.content

    return render_template("index.html", transliterated_text=transliterated_text)

if __name__ == "__main__":
    app.run(debug=True)
