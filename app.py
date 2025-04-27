from flask import Flask, render_template
import pymysql

app = Flask(__name__)

# Koneksi ke MySQL lokal XAMPP
db = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    database='profiledb',
    port=3307
)

@app.route('/')
def index():
    cursor = db.cursor()
    cursor.execute("SELECT name, email, kampus, gambar_url FROM profile LIMIT 1")
    profile = cursor.fetchone()
    return render_template('index.html', profile=profile)

if __name__ == '__main__':
    app.run(debug=True)
