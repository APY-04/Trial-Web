from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Untuk notifikasi flash

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        flash("Pesan berhasil dikirim! Terima kasih, " + name + " 😊", "success")
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)

posts = [
    {"title": "Belajar Flask", "content": "Flask adalah framework Python yang ringan..."},
    {"title": "Tailwind CSS", "content": "Tailwind membuat desain lebih mudah dengan utility class..."},
]

@app.route('/blog')
def blog():
    return render_template('blog.html', posts=posts)

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

