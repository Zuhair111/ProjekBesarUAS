from AplikasiKu.app import mysql

def explore():
        cursor=mysql.connection.cursor()
        cursor.execute("SELECT * FROM pekerjaan")
        result=cursor.fetchall()
        return result

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

def add_pelamar(nama,email,pendidikan,pekerjaan_id):
        cursor=mysql.connection.cursor()
        cursor.execute("INSERT INTO daftar_pelamar (nama,email,pendidikan,pekerjaan_id) VALUES (%s,%s,%s,%s)",(nama,email,pendidikan,pekerjaan_id))
        mysql.connection.commit()
        cursor.close()

def daftar_pelamar_by_job(pekerjaan_id):
        cursor=mysql.connection.cursor()
        cursor.execute("SELECT nama,email,pendidikan FROM daftar_pelamar WHERE pekerjaan_id=%s",(pekerjaan_id,))
        return cursor.fetchall()
        

# class Pekerjaan:
#     @staticmethod
#     def get_all():
#         cursor = mysql.connection.cursor()
#         cursor.execute("SELECT * FROM pekerjaan")
#         return cursor.fetchall()

#     @staticmethod
#     def get_by_id(pekerjaan_id):
#         cursor =mysql.connection.cursor()
#         cursor.execute("SELECT * FROM pekerjaan WHERE id = %s", (pekerjaan_id,))
#         return cursor.fetchone()

# class Pelamar:
#     @staticmethod
#     def get_by_pekerjaan(pekerjaan_id):
#         cursor = mysql.connection.cursor()
#         cursor.execute("""
#             SELECT nama, email, telepon 
#             FROM pelamar 
#             WHERE pekerjaan_id = %s
#         """, (pekerjaan_id,))
#         return cursor.fetchall()

#     @staticmethod
#     def add(nama, email, telepon, pekerjaan_id):
#         cursor = mysql.connection.cursor()
#         cursor.execute("""
#             INSERT INTO pelamar (nama, email, telepon, pekerjaan_id) 
#             VALUES (%s, %s, %s, %s)
#         """, (nama, email, telepon, pekerjaan_id))
#         mysql.connection.commit()