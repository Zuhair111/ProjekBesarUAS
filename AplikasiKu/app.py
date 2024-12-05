from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_mysqldb import MySQL


app = Flask(__name__)
app.config["MYSQL_HOST"] = "localhost"
app.config['MYSQL_PORT'] = 3306
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "db_pekerjaan"
mysql = MySQL(app)
app.secret_key = 'secret'

from AplikasiKu.models.jobs import get_jobs, add_jobs,explore as ex, add_pelamar, daftar_pelamar_by_job as dp,get_jobs_by_id as gj

@app.route('/',methods=['GET','POST'])
def index():
    return render_template('index.html')

@app.route('/explore')
def explore():
    pekerjaan=ex()
    return render_template('explore.html', pekerjaan=pekerjaan)

@app.route('/form_cari')
def form_cari():
    return render_template('form_cari.html')

@app.route('/cari_kerja', methods=['POST'])
def cari_kerja():
    experience = request.form['experience']
    jobs = get_jobs(experience)
    return render_template('cari_kerja.html',jobs=jobs  )
    
@app.route('/form_tambah', methods=['GET','POST'])
def form_tambah():
    if request.method == 'POST':
        perusahaan=request.form['perusahaan']
        deskripsi=request.form['description']
        requirement=request.form['requirement']
        add_jobs(perusahaan,deskripsi,requirement)
        return redirect(url_for('explore'))
    return render_template('form_tambah.html')

@app.route('/form_pelamar/<int:pekerjaan_id>', methods=['GET','POST'])
def form_pelamar(pekerjaan_id):
    if request.method == 'POST':
        nama=request.form['nama']
        email=request.form['email']
        pendidikan=request.form['pendidikan']
        add_pelamar(nama,email,pendidikan,pekerjaan_id)
        return redirect(url_for('explore'))
    pekerjaan=gj(pekerjaan_id)
    return render_template('form_pelamar.html',pekerjaan_id=pekerjaan_id ,pekerjaan=pekerjaan) 

@app.route('/daftar_pelamar/<int:pekerjaan_id>')
def daftar_pelamar(pekerjaan_id):
    pelamar=dp(pekerjaan_id)
    pekerjaan=gj(pekerjaan_id)
    return render_template('daftar_pelamar.html', pelamar=pelamar, pekerjaan=pekerjaan)


