from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy data
pendaftar = []

@app.route('/')
def home():
    programs = [
        {"name": "Pelatihan Web Developer", "desc": "membangun dan mengelola aplikasi berbasis web interaktif", "img": "https://picsum.photos/200/300"},
        {"name": "Data Scientist", "desc": "Analisis data besar", "img": "https://picsum.photos/200/300"},
        {"name": "Android Developer", "desc": " merancang dan membangun aplikasi berbasis mobile menggunakan sistem operasi Android.", "img": "https://picsum.photos/200/300"},
        {"name": "Video Editor", "desc": "Mengedit video profesional", "img": "https://picsum.photos/200/300"},
        {"name": "Animator", "desc": "Membuat animasi", "img": "https://picsum.photos/200/300"},
        {"name": "Content Creator", "desc": "Membuat konten kreatif untuk disebarkan melalui social media", "img": "https://picsum.photos/200/300"},
        {"name": "Enterprise Resource Planning", "desc": "Mengelola sumber daya perusahaan", "img": "https://picsum.photos/200/300"},
        {"name": "Desainer Grafis", "desc": "Desain grafis profesional", "img": "https://picsum.photos/200/300"},
        {"name": "Teknisi Jaringan", "desc": "Mengelola jaringan komputer", "img": "https://picsum.photos/200/300"}
    ]
    return render_template('home.html', programs=programs)

@app.route('/pendaftaran', methods=['GET', 'POST'])
def pendaftaran():
    if request.method == 'POST':
        nama = request.form['nama']
        nik = request.form['nik']
        whatsapp = request.form['whatsapp']
        email = request.form['email']
        program = request.form['program']

        pendaftar.append({"nama": nama, "nik": nik, "whatsapp": whatsapp, "email": email, "program": program})

        return redirect(url_for('pendaftar'))
    return render_template('pendaftaran.html')

@app.route('/pendaftar')
def pendaftar():
    return render_template('pendaftar.html', pendaftar=pendaftar)

@app.route('/edit/<int:index>', methods=['GET', 'POST'])
def edit(index):
    if request.method == 'POST':
        pendaftar[index]['nama'] = request.form['nama']
        pendaftar[index]['nik'] = request.form['nik']
        pendaftar[index]['whatsapp'] = request.form['whatsapp']
        pendaftar[index]['email'] = request.form['email']
        pendaftar[index]['program'] = request.form['program']

        return redirect(url_for('pendaftar'))
    return render_template('edit.html', index=index, data=pendaftar[index])

@app.route('/delete/<int:index>')
def delete(index):
    pendaftar.pop(index)
    return redirect(url_for('pendaftar'))

if __name__ == '__main__':
    app.run(debug=True)
