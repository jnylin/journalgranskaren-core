from flask import Flask, render_template_string, request
import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('wordnet')
nltk.download('omw-1.4')
from nltk.tokenize import sent_tokenize

app = Flask(__name__)

# Enkel regelbaserad analys
def analyse(text):
    meningar = sent_tokenize(text, language='swedish')
    flaggningar = []
    for i in range(len(meningar) - 1):
        m1 = meningar[i].lower()
        m2 = meningar[i + 1].lower()
        if "bättre" in m1 and "sjukskriv" in m2 and "inte" not in m1 and "ej" not in m1:
            flaggningar.append((meningar[i], meningar[i+1]))
    return flaggningar

HTML = """<!doctype html>
<title>Journalgranskaren</title>
<h2>Granska journaltext</h2>
<form method=post>
  <textarea name=text rows=10 cols=100>{{ request.form.text or '' }}</textarea><br>
  <input type=submit value="Granska">
</form>
{% if resultat %}
  <h3>Flaggade avsnitt</h3>
  {% for m1, m2 in resultat %}
    <b>Mening 1:</b> {{ m1 }}<br>
    <b>Mening 2:</b> {{ m2 }}<br><br>
  {% endfor %}
{% endif %}
"""

@app.route("/", methods=["GET", "POST"])
def index():
    resultat = []
    if request.method == "POST":
        text = request.form["text"]
        resultat = analyse(text)
    return render_template_string(HTML, resultat=resultat)

if __name__ == "__main__":
    app.run(debug=True)
