## Tugas 5
Hasil Tugas 5 saya dapat dilihat [di sini](https://jonathan-tugas2.herokuapp.com/todolist/).


## 1. Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?

Inline CSS adalah kode CSS yang diketik langsung dalam tag HTML. Setiap elemen HTML memiliki atribut style, yang akan
menjadi tempat dimana kode CSS tersebut diketik.

Kelebihan Inline css:
- Baik apabila ingin melihat perubahan yang terjadi atau menerapkan perubahan pada satu elemen HTML saja
- Proses permintaan HTTP lebih kecil dan proses load website akan lebih cepat

Kekurangan Inline CSS:
- Tidak efisien karena setiap elemen HTML yang ingin diberikan style harus dilakukan secara masing-masing.
- Kita tidak bisa langsung melakukan satu perubahan yang berpengaruh terhadap lebih dari satu elemen HTML.

Contoh dari Inline CSS adalah sebagai berikut:

```
<h2 style="color:blue>Hello</h2>
```

Internal CSS adalah kode CSS yang ditulis dalam tag `<style>`, yang diketik di bagian atas file HTML.

Contoh dari Internal CSS adalah sebagai berikut:

```
<head>
    <style>
        .card {
                background-color:lightgrey;
                margin: 20px;
                width: 200px;
                word-break: break-word;
        }
    </style>
</head>
```

Kelebihan dari Internal CSS:
- Perubahan yang dilakukan pada Internal CSS hanya berpengaruh terhadap satu halaman saja
- Tidak perlu mengupload beberapa file karena HTML dan CSS berada dalam satu file yang sama.

Kekurangan dari Internal CSS:
- Tidak efisien apabila ingin menggunakan CSS yang sama dalam beberapa file
- Performance dari suatu website dapat menurun karena CSS yang berbeda-beda mengakibatkan diperlukannya
loading ulang setiap kali ganti halaman.


External CSS
External CSS adalah kode CSS yang diketikkan secara terpisah dengan kode HTML. Tempat dimana Eksternal CSS tersebut diketik berada dalam suatu file yang berekstensi `.css`. File Eksternal CSS tersebut diletakkan setelah tag `<head>`.

Contoh dari External HTML adalah sebagai berikut:
Pertama, dibuat file bernama `style.css` yang isinya sebagai berikut:

```
i {
    font-family: sans-serif
    color: blue
}
```

Kemudian, tambahkan `<link href="style.css" rel="stylesheet" type="text/css">` ke dalam file HTML 
setelah tag `<head>` agar dapat menggunakan file style.css tersebut dalam HTML, seperti berikut:

```
<!DOCTYPE html>
<html lang="en">

<head>
    <link href="style.css" rel="stylesheet" type="text/css">
</head>
```

Kelebihan dari Eksternal CSS:
- File CSS dapat digunakan pada lebih dari satu halaman secara bersamaan
- Waktu loading website menjadi lebih cepat
- Struktur dari kode HTML akan terlihat lebih rapi dan ukuran file HTML akan menjadi lebih kecil

Kekurangan dari Eksternal CSS:
- Kegagalan dalam memanggil file CSS akan berpengaruh terhadap seluruh halaman yang menggunakan file CSS tersebut

 
## 2. Jelaskan tag HTML5 yang kamu ketahui.
- `<b>` untuk menampilkan teks dalam keadaan bold
- `<p>` untuk mendefinisikan suatu paragraf
- `<br>` untuk melakukan line break
- `<div>` untuk mendefinisikan suatu bagian atau mengelompokkan beberapa elemen HTML pada file
- `<title>` untuk memberikan judul pada suatu file
- `<table>` untuk mendefinisikan suatu table
- `<td>` untuk mendefinisikan suatu cell pada table
- `<th>` untuk mendefinisikan header cell pada table
- `<form>` untuk membuat suatu form untuk menerima input dari user
- `<button>` untuk membuat suatu button yang dapat diklik
- `<head>` untuk mendefinisikan bagian head dari suatu file
- `<body>` untuk mendefinisikan bagian body dari suatu file
- `<style>` untuk memberikan informasi styling pada suatu file

 
## 3. Jelaskan tipe-tipe CSS selector yang kamu ketahui.
- `CSS Element Selector` melakukan seleksi terhadap elemen HTML pada suatu halaman berdasarkan nama dari elemen tersebut
```
h1 {
    text-align: center;
    color:blue;
}
```

Nanti seluruh elemen HTML dengan tag`<h>` pada suatu halaman akan ditempatkan di tengah dengan warna textnya biru

- `CSS Class Selector` melakukan seleksi terhadap elemen HTML dengan attribut class tertentu. Untuk melakukan seleksi, digunakan tanda `.` diikuti dengan nama class attribut pada elemen HTML tersebut. Contohnya adalah sebagai berikut:

```
.card {
    background-color:lightgrey;
}
```

Nanti elemen HTML dengan attribute class bernama `card` akan terseleksi, dan nanti warnanya akan menjadi light grey.

- `CSS Universal Selector`melakukan seleksi terhadap seluruh elemen HTML pada suatu halaman. Untuk melakukan seleksi, digunakan tanda `*` seperti berikut:

* {
    background-color: grey;
}
Nanti seluruh elemen HTML pada suatu halaman akan berwarna grey

- `CSS Grouping Selector` melakukan seleksi terhadap seluruh elemen HTML pada suatu halaman dengan definisi style yang sama.
Contohnya adalah sebagai berikut:

```
h1 {
    text-align: center;
    color:blue;
}

h2 {
    text-align: center;
    color:blue
}
```

Kita dapat mengetiknya menjadi sebagai berikut:
```
h1, h2 {
    text-align: center;
    color: blue;
}
```
Nanti seluruh elemen HTML dengan tag`<h1>` dan `<h2>` pada suatu halaman akan ditempatkan di tengah dengan warna biru


## 4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
Pertama, saya dekorasi `login.html` terlebih dahulu. Saya menggunakan tailwind. Di sini, saya menggunakan flex agar dia responsive. Saya membuat formnya dengan background abu-abu, dan saya letakinnya di tengah halaman. Lalu, saya menggunakan font Rubik untuk text `To Do List` nya. Agar text `To Do List` nya bisa berubah sizenya ketika ukuran halaman berubah, saya menggunakan media query yang dari Tailwind, yaitu sm, md, dan lg. Untuk button submitnya, saya memberikan warna biru dengan textnya berwarna abu-abu. Saya membuat buttonnya dengan ujung yang tidak kotak juga dan ketika dihover, warnanya akan berubah.

Kedua, saya mendekorasi `todolist.html`. Saya menggunakan flex juga agar responsive dan saya menempatkan semuanya di tengah halaman. Untuk to do listnya saya menggunakan card. Saya beri warna juga untuk card tersebut dan isinya. Untuk deskirpsi, saya mengurungnya dalam `<div>` yang saya beri warna backgroundnya whitesmoke. Untuk buttonnya juga, saya beri warna dan memberikan shape dengan ujung yang tidak 90 derajat.


Ketiga, saya mendekorasi `create.html` dengan menempatkannya di tengah, dan saya berikan warna light blue untuk text `create a task`. Untuk keseluruhannya saya menempatkannya di tengah


Terakhir, saya mendekorasi `register.html` dengan menggunakan cara yang serupa dengan saat saya mendekorasi `create.html`.