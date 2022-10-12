## Tugas 6
Hasil Tugas 6 saya dapat dilihat [di sini](https://jonathan-tugas2.herokuapp.com/todolist/).

## 1. Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.
Synchronous programming merupakan suatu model programming yang hanya dapat mengeksekusi perintah satu demi satu mengikuti alur dari program, sedangkan asynchronous programming merupakan suatu model programming yang dapat mengeksekusi lebih dari satu perintah secara bersamaan sehingga tidak perlu menunggu suatu perintah selesai tereksekusi untuk menjalankan perintah berikutnya.

## 2. Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.
Event driven programming merupakan suatu paradigma programming dimana alur dari program ditentukan oleh aksi dari user, seperti menekan button menggunakan mouse, menekan suatu key pada keyboard, dan lain-lain. Pada tugas 6 ini, salah satu penerapannya adalah ketika user menekan tombol "Add a new task" pada halaman todolist, program akan menampilkan suatu modal atau popup window yang merupakan form untuk menambahkan task baru.

## 3. Jelaskan penerapan asynchronous programming pada AJAX.
Penerapan asynchronous programming pada AJAX memungkinkan perubahan yang dilakukan pada suatu halaman website, seperti penambahan suatu task baru, langsung ditampilkan tanpa harus melakukan refresh pada halaman website tersebut terlebih dahulu.

## 4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
1. Menghilangkan kode yang mengambil data user dengan cara `Task.objects.filter(user=request.user)` pada fungsi `show_todolist` dalam `views.py`
2. Membuat fungsi `show_json` pada `views.py` yang mengembalikan data dari user dalam format JSON
3. Melakukan routing terhadap fungsi `show_json` pada `views.py` dengan menambahkan `path('json/', show_json, name='show_json')` pada `urls.py`
4. Membuat `$(document).ready(() => {..` untuk menjalankan beberapa hal terlebih dahulu ketika dokumen selesai diload
5. Membuat fungsi GET pada `todolist.html`
6. Membuat modal atau popup window pada `todolist.html` dengan isinya yang merupakan form untuk menambahkan suatu task baru
7. Membuat fungsi POST pada `todolist.html`
8. Membuat fungsi `add` pada `views.py` untuk POST input dari user menggunakan AJAX
8. Melakukan routing terhadap fungsi `add` pada `views.py` dengan menambahkan `path("add/", add, name="add")` pada `urls.py`