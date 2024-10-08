from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    wisatas = [
        {"name": "Keraton Ngayogyakarta Hadiningrat", "image": url_for('static', filename='images/kraton.png'), "description": "Sejarah dan budaya Yogyakarta."},
        {"name": "Gunung Merapi", "image": url_for('static', filename='images/merapi.png'), "description": "Pantai indah dengan pemandangan sunset."},
        {"name": "Candi Prambanan", "image": url_for('static', filename='images/prambanan.png'), "description": "Candi Hindu terbesar di Indonesia."},
        {"name": "Candi Prambanan", "image": url_for('static', filename='images/prambanan.png'), "description": "Candi Hindu terbesar di Indonesia."},
        {"name": "Candi Prambanan", "image": url_for('static', filename='images/prambanan.png'), "description": "Candi Hindu terbesar di Indonesia."},
        {"name": "Candi Prambanan", "image": url_for('static', filename='images/prambanan.png'), "description": "Candi Hindu terbesar di Indonesia."},
        {"name": "Candi Prambanan", "image": url_for('static', filename='images/prambanan.png'), "description": "Candi Hindu terbesar di Indonesia."},
        {"name": "Candi Prambanan", "image": url_for('static', filename='images/prambanan.png'), "description": "Candi Hindu terbesar di Indonesia."},

    ]
    return render_template('index.html', wisatas=wisatas)

if __name__ == '__main__':
    app.run(debug=True)
