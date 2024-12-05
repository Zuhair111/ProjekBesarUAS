from AplikasiKu.app import mysql
from werkzeug.security import check_password_hash,generate_password_hash

def get_user_by_username(username):
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        user = cursor.fetchone()
        cursor.close()
        return user

def verify_password(hashed_password, password):
        return check_password_hash(hashed_password, password)

def create_user(username, email, password):
        hashed_password = generate_password_hash(password)
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO users (username, email, password) VALUES (%s, %s, %s)",
                   (username, email, hashed_password))
        mysql.connection.commit()
        cursor.close()
def get_user_pekerjaan(user_id):
        cursor = mysql.connection.cursor()
        cursor.execute("""
                SELECT d.nama, d.pendidikan, p.Perusahaan
                FROM daftar_pelamar d
                JOIN pekerjaan p ON d.pekerjaan_id = p.id
                WHERE d.user_id = %s
        """, (user_id,))
        pekerjaan = cursor.fetchall()
        cursor.close()
        return pekerjaan

def get_all_jobs():
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM jobs")
        jobs = cursor.fetchall()
        cursor.close()
        return jobs

def get_jobs_by_experience(experience):
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM jobs WHERE experience_required <= %s", (experience,))
        jobs = cursor.fetchall()
        cursor.close()
        return jobs


def explore():
        cursor=mysql.connection.cursor()
        cursor.execute("SELECT * FROM pekerjaan")
        pekerjaan=cursor.fetchall()
        return pekerjaan

def get_jobs(experience):
        cursor = mysql.connection.cursor()
        query = "SELECT * FROM pekerjaan WHERE requirement LIKE %s"
        cursor.execute(query, (f"%{experience}%",))
        result = cursor.fetchall()
        return result 

def get_jobs_by_id(pekerjaan_id):
        cursor=mysql.connection.cursor()
        cursor.execute("SELECT Perusahaan,description FROM pekerjaan where id=%s", (pekerjaan_id,))
        return cursor.fetchone()
 

def add_jobs(perusahaan,description,requirement): 
        cursor=mysql.connection.cursor()
        cursor.execute("INSERT INTO pekerjaan (Perusahaan,description,requirement) VALUES (%s,%s,%s)",(perusahaan,description,requirement))
        mysql.connection.commit()
        cursor.close()

def save_user_data(name, experience):
        cursor = mysql.connection.cursor()
        query = "INSERT INTO user_data (name, experience) VALUES (%s, %s)"
        cursor.execute(query, (name, experience))
        mysql.connection.commit()

def add_pelamar(nama,email,pendidikan,pekerjaan_id,user_id):
        cursor=mysql.connection.cursor()
        cursor.execute("INSERT INTO daftar_pelamar (nama,email,pendidikan,pekerjaan_id,user_id) VALUES (%s,%s,%s,%s,%s)",(nama,email,pendidikan,pekerjaan_id,user_id))
        mysql.connection.commit()
        cursor.close()

def daftar_pelamar_by_job(pekerjaan_id):
        cursor=mysql.connection.cursor()
        cursor.execute("SELECT nama,email,pendidikan FROM daftar_pelamar WHERE pekerjaan_id=%s",(pekerjaan_id,))
        return cursor.fetchall()
        
