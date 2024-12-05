from flask import  render_template, request, redirect, url_for, session, flash
from AplikasiKu.models.jobs import get_user_by_username, verify_password,create_user,get_user_pekerjaan,get_all_jobs,get_jobs_by_experience,add_jobs,add_pelamar,get_jobs_by_id,daftar_pelamar_by_job,explore as ex

def index():
    return render_template('index.html')

def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = get_user_by_username(username)
        if user and verify_password(user[2], password):  # Password hash di kolom ke-3
            session['user_id'] = user[0]  # Simpan `user_id` ke session
            session['username'] = user[1]  # Simpan `username` ke session
            flash('Login berhasil!', 'success')
            return redirect(url_for('akun'))
        else:
            flash('Login gagal. Periksa username dan password.', 'danger')
    return render_template('login.html')

def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        
        # Memanggil fungsi create_user untuk menambahkan pengguna ke database
        create_user(username, email, password)
        
        flash('Registrasi berhasil! Silakan login.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html')

def akun():
    if 'user_id' not in session:
        flash('Silakan login terlebih dahulu.', 'warning')
        return redirect(url_for('login'))
    
    user_id = session['user_id']
    
    # Memanggil fungsi get_user_pekerjaan untuk mendapatkan data pekerjaan yang didaftar
    pekerjaan = get_user_pekerjaan(user_id)
    
    return render_template('akun.html', username=session['username'], pekerjaan=pekerjaan)

def require_login():
    restricted_paths = ['/akun', '/logout']
    if request.path in restricted_paths and 'user_id' not in session:
        flash('Silakan login untuk mengakses halaman ini.', 'warning')
        return redirect(url_for('login'))
    return None

def explore():
    pekerjaan = ex()
    return render_template('explore.html', pekerjaan=pekerjaan)

def form_cari():
    return render_template('form_cari.html')

def cari_kerja():
    experience = request.form['experience']
    jobs = get_jobs_by_experience(experience)
    return render_template('cari_kerja.html', jobs=jobs)

def form_tambah():
    if request.method == 'POST':
        perusahaan = request.form['perusahaan']
        deskripsi = request.form['description']
        requirement = request.form['requirement']
        add_jobs(perusahaan, deskripsi, requirement)
        return redirect(url_for('explore'))
    return render_template('form_tambah.html')

def form_pelamar(pekerjaan_id):
    if 'user_id' not in session:
        flash('Silakan login terlebih dahulu.', 'warning')
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        nama = request.form['nama']
        email = request.form['email']
        pendidikan = request.form['pendidikan']
        user_id = session['user_id']
        add_pelamar(nama, email, pendidikan, pekerjaan_id, user_id)
        return redirect(url_for('explore'))
    
    pekerjaan = get_jobs_by_id(pekerjaan_id)
    return render_template('form_pelamar.html', pekerjaan_id=pekerjaan_id, pekerjaan=pekerjaan)

def daftar_pelamar(pekerjaan_id):
    pelamar = daftar_pelamar_by_job(pekerjaan_id)
    pekerjaan = get_jobs_by_id(pekerjaan_id)
    return render_template('daftar_pelamar.html', pelamar=pelamar, pekerjaan=pekerjaan)

def logout():
    session.pop('user_id', None)
    session.pop('username', None)
    flash('Anda telah logout.', 'info')
    return redirect(url_for('login'))