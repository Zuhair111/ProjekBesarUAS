from flask import Flask
from flask_mysqldb import MySQL



app = Flask(__name__)
app.config["MYSQL_HOST"] = "localhost"
app.config['MYSQL_PORT'] = 3306
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "db_pekerjaan"
mysql = MySQL(app)
app.secret_key = 'secret'


from AplikasiKu.controllers.jobs import login as log,register as reg, akun as ak,require_login,explore as exp,form_cari as fc, cari_kerja as ck,form_tambah as ft,form_pelamar as fp,daftar_pelamar as dafp,logout as lo,index as ix

@app.route('/',methods=['GET','POST'])
def index():
    return ix()

@app.route('/register', methods=['GET', 'POST'])
def register():
    return reg()

@app.route('/login', methods=['GET', 'POST'])
def login():
    return log()

@app.route('/logout')
def logout():
    return lo()

@app.route('/akun')
def akun():
    return ak()

@app.before_request
def before_request():
    return require_login()

@app.route('/explore')
def explore():
    return exp()

@app.route('/form_cari')
def form_cari():
    return fc()

@app.route('/cari_kerja', methods=['POST'])
def cari_kerja():
    return ck()
    
@app.route('/form_tambah', methods=['GET','POST'])
def form_tambah():
    return ft()

@app.route('/form_pelamar/<int:pekerjaan_id>', methods=['GET','POST'])
def form_pelamar(pekerjaan_id):
    return fp(pekerjaan_id) 

@app.route('/daftar_pelamar/<int:pekerjaan_id>')
def daftar_pelamar(pekerjaan_id):
    return dafp(pekerjaan_id)


