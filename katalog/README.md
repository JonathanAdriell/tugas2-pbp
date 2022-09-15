
# Tugas 2 PBP

Hasil Tugas 2 saya dapat dilihat [di sini](https://jonathan-tugas2.herokuapp.com/katalog/).

## Bagan
<img src="https://user-images.githubusercontent.com/112321270/190301970-4161f4ed-ce77-4ce5-a6be-78e58b090d8c.png" alt="" height="500" width="700" />

**Penjelasan:**
Ketika user melakukan request, URL yang di-request tersebut akan diproses di urls.py dengan cara menyesuaikan antara URL yang di-request dengan URL yang ada di urls.py. Kemudian, request tersebut akan diteruskan ke views.py yang bersesuaian dengan request tersebut untuk diproses. Fungsi yang telah didefinisikan di views.py memungkinkan untuk melakukan pemanggilan query ke models.py dan database untuk memperoleh suatu data dari database. Kemudian, data yang telah diperoleh dari database dipetakan ke templates, dalam hal ini katalog.html, yang kemudian akan dirender dan dikembalikan kepada user sebagai response.

## Mengapa kita menggunakan virtual environment?
Virtual environment merupakan suatu lingkungan virtual dapat digunakan untuk memisahkan antara suatu proyek Django dengan proyek Django lainnya. Dengan menggunakan virtual environment yang berbeda untuk setiap proyek Django, kita dapat memisahkan pengaturan dan package yang telah kita install untuk mengerjakan suatu proyek tertentu. Dengan ini, perubahan yang dilakukan untuk suatu proyek tidak berpengaruh terhadap proyek lainnya dikarenakan saling berada pada lingkungan virtual yang berbeda.

## Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
Tentu kita masih bisa membuat suatu proyek Django tanpa menggunakan virtual environment. Namun, sangat tidak disarankan jika proyek Django yang ingin kita buat tidak sementara atau akan digunakan oleh banyak orang. Alasan pertama adalah terdapat kemungkinan bahwa akan terjadinya error atau konflik dengan proyek Django lainnya dikarenakan semua proyek Django berada pada satu lingkungan yang sama. Selain itu, tidak semua lingkungan dapat menjalankan suatu proyek Django tertentu. Oleh karena itu, kita perlu menggunakan virtual environment yang telah ditetapkan dengan spesifikasi tertentu untuk dapat memastikan bahwa proyek Django tersebut dapat dijalankan oleh semua orang, terutama para developer ketika sedang mengembangkan suatu proyek Django bersama, dengan menjalankannya pada virtual environment yang sama.

## Langkah Implementasi pada Proyek Django
**1. Membuat sebuah fungsi pada views.py yang dapat melakukan pengambilan data dari model dan dikembalikan ke dalam sebuah HTML.**<br>
Dibuat suatu fungsi yang menerima suatu request dari user sebagai parameternya di views.py. Dalam hal ini, fungsi tersebut bernama show_catalog. Dalam fungsi tersebut, terdapat pemanggilan query ke database dengan menggunakan kelas dari model. Hasil dari pemanggilan query ke database tersebut akan disimpan ke dalam suatu variabel. Dalam hal ini, variabel tersebut bernama catalog_list. Fungsi tersebut akan mengembalikan hasil render template, dalam hal ini katalog.html, yang telah ditambahkan dengan data-data yang terdapat pada catalog_list dengan tambahan nama dan NPM mahasiswa.

Pada katalog > views.py<br>
<img src="https://user-images.githubusercontent.com/112321270/190307545-ca69bb71-1674-40b5-9c44-eb829c9dbab1.png" alt="" height="200" width="400" />

Pada katalog > models.py<br>
<img src="https://user-images.githubusercontent.com/112321270/190307864-86aa2ed1-43e9-4496-a0c6-29bc1b571d29.png" alt="" height="200" width="400" />
    
**2. Membuat sebuah routing untuk memetakan fungsi yang telah kamu buat pada views.py.**<br>
Untuk melakukan routing terhadap fungsi yang terdapat di views.py, tambahkan path(‘’, show_catalog, name=’show_catalog’) pada urls.py di katalog agar halaman HTML dapat ditampilkan di browser. Kemudian, tambahkan ('katalog/', include('katalog.urls')) pada urls.py di project_django untuk mendaftarkan aplikasi katalog. 

**3. Memetakan data yang didapatkan ke dalam HTML dengan sintaks dari Django untuk pemetaan data template.**<br>
Setelah data diperoleh dari database, data tersebut akan dipetakan ke template, dalam hal ini katalog.html, dengan mengisi {{data}} dengan data yang bersesuaian. Untuk mengambil data yang diperoleh dari database sendiri, digunakan for loop seperti berikut:<br>
<img src="https://user-images.githubusercontent.com/112321270/190308015-b333a7d6-f48c-41ab-a611-3aa5b183f8f1.png" alt="" height="200" width="300" />

**4. Melakukan deployment ke Heroku terhadap aplikasi yang sudah kamu buat.**<br>
Untuk melakukan deployment ke Heroku, pastikan seluruh perubahan pada repository untuk Tugas 2 sudah di-push. Dalam hal ini, repository Tugas 2 saya bernama tugas2-pbp. Kemudian, pergi ke account settings pada Heroku dan salin API key. Lalu, pergi ke repository Tugas 2 > settings > secrets > actions untuk membuat dua buah repository secret.

Untuk repository secret yang pertama, namanya adalah HEROKU_API_KEY dengan secret nya adalah API key yang telah diperoleh sebelumnya dari account settings pada Heroku. Untuk repository secret yang kedua, namanya adalah HEROKU_APP_NAME dengan secret nya adalah nama aplikasi Tugas 2 di Heroku. Kemudian, pergi ke actions pada repository Tugas 2 dan klik Re-run all jobs. Deployment telah selesai. 
