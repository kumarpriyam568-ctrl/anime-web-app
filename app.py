from flask import Flask, render_template, request

app = Flask(__name__)

anime_db = {
    "action": ["Attack on Titan", "Jujutsu Kaisen", "Demon Slayer"],
    "romance": ["Your Name", "Toradora", "Horimiya"],
    "comedy": ["Gintama", "Konosuba", "One Punch Man"],
    "dark": ["Death Note", "Tokyo Ghoul", "Parasyte"],
    "adventure": ["Naruto", "One Piece", "Hunter x Hunter"]
}

@app.route("/", methods=["GET", "POST"])
def home():
    recommendations = []
    
    if request.method == "POST":
        mood = request.form.get("mood").lower()
        recommendations = anime_db.get(mood, ["No results found"])

    return render_template("index.html", recommendations=recommendations)

if __name__ == "__main__":
    app.run(debug=True)
