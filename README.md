# dumbways Test Batch 19 Kloter 4
Soal yang dikerjakan adalah soal no 1-4A
untuk soal 4b telah mencoba menggunakan flask dan mysqlalchemy namun masih baru 1 proses CRUD pada Tabel Genre saja. 

# OS yang digunakan:
Windows 10 

# Software yang digunakan: 
- VS code Studio
- MYSQL Workbench 8.0
- anaconda environtment Download the Anaconda installer di https://www.anaconda.com/products/individual#windows



# set path anaconda sehingga bisa digunakan di terminal windows(command prompt)
1. buka anaconda prompt
2. ketik where conda.exe enter lalu copy direktori tersebut // untuk mengetahui direktori conda.exe
3. ketik SETX PATH "%PATH%(direktori yang dicopy)" enter //tanpa tanda kurung

# library package yang digunakan:
1. Flask

cara install di anaconda prompt/cmd jika sudah di set path:
pip install Flask

2. Flask-SQL Alchemy

cara install di anaconda prompt/cmd jika sudah di set path:
pip install Flask-SQLAlchemy

3.mysql client

cara install di anaconda prompt/cmd jika sudah di set path:
pip install mysqlclient


# NOTE
- Untuk menjalankan soal no 4B diperlukan pembuatan database dan tabel terlebih dahulu dengan nama database webmusic dan tabel genre
- Untuk bagian app.py no 4B kode dibawah ini diperlukan penggantian password sql, password einstein bisa diganti dengan password pada mysql yang anda gunakan

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:einstein@localhost/webmusic'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False









