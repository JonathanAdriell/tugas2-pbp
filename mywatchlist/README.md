## Tugas 3
Hasil Tugas 3 saya dapat dilihat [di sini](https://jonathan-tugas2.herokuapp.com/mywatchlist/).

## Perbedaan antara JSON, XML, dan HTML

JSON atau JavaScript Object Notation merupakan suatu format untuk data yang sintaksnya merupakan turunan dari objek JavaScript. Format yang digunakan oleh JSON berbentuk _text_ sehingga kode untuk membaca atau membuat JSON terdapat di banyak bahasa pemrograman. JSON didesain ke dalam bentuk yang _self-describing_. Jika dibandingkan dengan XML, JSON lebih mudah untuk dibaca dan dimengerti oleh manusia dan membutuhkan _codingan_ yang lebih sedikit dikarenakan sintaksnya yang tidak kompleks sehingga membuat ukuran berkas lebih kecil. Selain itu, JSON juga mendukung penggunaan array. Oleh karena itu, pemrosesan dan perpindahan data dapat dilakukan dengan lebih cepat.  Data pada JSON tersimpan ke dalam bentuk _key_ dan _value_, dimana _value_ dapat berupa objek atau tipe data primitif. JSON tidak menggunakan closing tag dan tidak mendukung penggunaan _comments_.

XML atau eXtensible Markup Language merupakan suatu bahasa markup yang lebih berfokus pada penyimpanan dan pengiriman data. Biasanya, XML banyak digunakan untuk menyimpan dan mengirim data pada aplikasi, baik _web_ maupun _mobile_. XML didesain ke dalam bentuk yang _self_descriptive_. Jika dibandingkan dengan JSON, XML memang lebih kompleks dan lambat. XML tidak mendukung penggunaan array. Akan tetapi, kompleksitas tersebut membuat XML merupakan suatu bahasa markup yang sangat bagus untuk aplikasi yang melibatkan banyak data. Tags pada XML bersifat _extensible_. Struktur berkas XML berbentuk seperti pohon dan sekilas terlihat seperti HTML. Selain itu, XML mendukung penggunaan _comments_. Namun, XML tidak memiliki _pre-defined_ tags, bersifat _case-sensitive_, dan _strict_ dalam penggunaan _closing tag_, yang berkebalikan dari HTML.

HTML atau HyperText Markup Language merupakan suatu bahasa markup yang lebih berfokus pada penampilan data. Pada umumnya, HTML digunakan untuk membuat halaman _website_. Penulisan dengan HTML bersifat _case-insensitive_ dan tidak _strict_ dalam penggunaan _closing tag_. Selain itu, HTML mendukung penggunaan _comments_.


## Pentingnya Data Delivery dalam Mengimplementasikan Sebuah Platform

Dalam mengembangkan suatu _platform_, ada saatnya dimana kita perlu mengirimkan suatu data dari suatu _stack_ ke _stack_ lain. Dengan adanya _data delivery_, kita dapat melakukan perpindahan data secara aman dan terstruktur. Bentuk dari data yang dikirimkan bisa berbeda-beda tergantung dari formatnya. Beberapa contoh format data yang umum digunakan adalah HTML, XML, dan JSON.

## Langkah-Langkah Implementasi

1. Buatlah suatu aplikasi bernama `mywatchlist` dengan menjalankan seperti berikut:

   ```
   python manage.py startapp mywatchlist
   ```

2. Kemudian, daftarkan aplikasi `mywatchlist` ke dalam proyek Django dengan menambahkan `mywatchlist` ke dalam variabel `INSTALLED_APPS` pada `project_django/settings.py`

   ```
   INSTALLED_APPS = [
     ...,
     'mywatchlist',
   ]
   ```

   Daftarkan juga aplikasi `mywatchlist` ke dalam `urls.py` pada `project_django/urls.py`

   Dalam project_django/urls.py
   ```
   from django.contrib import admin
   from django.urls import path, include

   urlpatterns = [
      path('admin/', admin.site.urls),
      path('', include('example_app.urls')),
      path('katalog/', include('katalog.urls')),
      path('mywatchlist/', include('mywatchlist.urls')),
   ]
   ```

3. Lalu, buatlah suatu model dengan atribut `watch`, `title`, `rating`, `release_date`, dan `review` pada `mywatchlist/models.py`

   Dalam mywatchlist/models.py
   ```
   from django.db import models
   from django.core.validators import MaxValueValidator, MinValueValidator

   class MyWatchList(models.Model):
      watched = models.BooleanField()
      title = models.CharField(max_length=255)
      rating = models.IntegerField(validators=[
         MinValueValidator(1),
         MaxValueValidator(5)
      ])
      release_date = models.DateField()
      review = models.TextField()
   ```

4. Lakukan persiapan serta penerapan migrasi skema model ke dalam database Django lokal dengan menjalankan seperti berikut:

   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

   Lakukan hal tersebut setiap kali ada perubahan pada model yang ingin digunakan.

5. Kemudian, buatlah sebuah folder bernama `fixtures` di dalam folder `mywatchlist` dan buat juga sebuah berkas bernama `initial_mywatchlist_data.json` pada `mywatchlist/fixtures` untuk menyimpan data yang ingin digunakan.

6. Masukkan data tersebut ke dalam database Django lokal dengan menjalankan seperti berikut:

   ```
   python manage.py loaddata initial_wishlist_data.json
   ```

   Lakukan hal tersebut setiap kali ada perubahan pada data yang ingin digunakan.

7. Kemudian, buatlah sebuah folder bernama `templates` di dalam folder `mywatchlist` dan buat juga dua berkas bernama `empty.html` dan `mywatchlist.html` pada `mywatchlist/templates`. `empty.html` merupakan suatu template HTML yang berisi kalimat "Tugas 3 PBP/PBD" dan tiga _button_ yang menuju ke halaman HTML, XML, atau JSON ketika ditampilkan, sedangkan `mywatchlist.html` merupakan suatu template yang berisi kalimat dan data pada `initial_mywatchlist_data.json` yang disajikan dalam bentuk tabel ketika ditampilkan.

   Dalam mywatchlist/templates/empty.html
   ```
   {% extends 'base.html' %}
   {% block content %}

   <h1>Tugas 3 PBP/PBD</h1>
   <a href = "html"> <button>show in html</button></a>
   <a href = "xml"> <button>show in xml</button></a>
   <a href = "json"> <button>show in json</button></a>

   {% endblock content %}
   ```

   Dalam mywatchlist/templates/mywatchlist.html
   ```
   {% extends 'base.html' %}
   {% block content %}

   <style>
      table, th, td {
            border: 1px solid black; 
            border-spacing: 0;
      }
   </style>

   <h1>Tugas 3 PBP/PBD</h1>

   <h5>Name:</h5>
   <p>{{name}}</p>

   <h5>Student ID:</h5>
   <p>{{student_id}}</p>

   <p>{{output_counter}}</p>

   <table>
      <tr>
         <th>Watched</th>
         <th>Title</th>
         <th>Rating</th>
         <th>Release Date</th>
         <th>Review</th>
      </tr>

      {% for watchlist in watchlists %}
      <tr>
         <td>{{watchlist.watched}}</td>
         <td>{{watchlist.title}}</td>
         <td>{{watchlist.rating}}</td>
         <td>{{watchlist.release_date}}</td>
         <td>{{watchlist.review}}</td>
      </tr>
      {% endfor %}

   </table>

   {% endblock content %}
   ```

8. Lalu, buatlah fungsi dengan parameter `request` pada `mywatchlist/views.py` untuk menampilkan data dalam format HTML, XML, atau JSON.

   Dalam mywatchlist/views.py
   ```
   from django.shortcuts import render
   from mywatchlist.models import MyWatchList
   from django.http import HttpResponse
   from django.core import serializers

   def show_empty(request):
      return render(request, "empty.html")

   def show_watchlist(request): # show watchlist in HTML

      have_watched = 0
      havent_watched = 0
      data = MyWatchList.objects.all()

      for object in data:
         if (object.watched): # menghitung jumlah film yang telah ditonton
               have_watched += 1
         else:
               havent_watched += 1

      if (have_watched >= havent_watched): # menentukan output berdasarkan jumlah film yang telah ditonton
         output = "Selamat, kamu sudah banyak menonton!"
      else:
         output = "Wah, kamu masih sedikit menonton!"   
   
      context = {
         'name': 'Jonathan Adriel',
         'student_id': '2106750692',
         'watchlists': data,
         'output_counter': output
      }
      return render(request, "mywatchlist.html", context)

   def show_xml(request): # show watchlist in XML
      data = MyWatchList.objects.all()
      return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

   def show_json(request):
      data = MyWatchList.objects.all()
      return HttpResponse(serializers.serialize("json", data), content_type="application/json")

   def show_json_by_id(request, id):
      data = MyWatchList.objects.filter(pk=id)
      return HttpResponse(serializers.serialize("json", data), content_type="application/json")

   def show_xml_by_id(request, id):
      data = MyWatchList.objects.filter(pk=id)
      return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
   ```

9. Buatlah suatu berkas bernama `urls.py` di dalam folder `mywatchlist` dan lakukan _routing_ terhadap berbagai fungsi yang ada pada `mywatchlist/views.py`

   Dalam mywatchlist/urls.py
   ```
   from django.urls import path
   from mywatchlist.views import show_empty
   from mywatchlist.views import show_watchlist
   from mywatchlist.views import show_xml
   from mywatchlist.views import show_json
   from mywatchlist.views import show_json_by_id
   from mywatchlist.views import show_xml_by_id

   app_name = 'mywatchlist'

   urlpatterns = [ # memanggil fungsi yang ada di views
      path('', show_empty, name='show_empty'),
      path('html/', show_watchlist, name='show_watchlist'),
      path('xml/', show_xml, name='show_xml'),
      path('json/', show_json, name='show_json'),
      path('json/<int:id>', show_json_by_id, name='show_json_by_id'),
      path('xml/<int:id>', show_xml_by_id, name='show_xml_by_id'),
   ]
   ```
   
10. Kemudian, buatlah suatu _test unit_ pada `mywatchlist/tests.py` untuk menguji apakah URL JSON, XML, dan HTML dapat mengembalikan respon `HTTP 200 OK`.
   
    Dalam mywatchlist/tests.py
    ```
    from django.test import TestCase
    from django.test import Client
    from django.urls import reverse

    class MyWatchListTesting(TestCase):
       def setUp(self):
          self.client = Client()

       def test_url_html(self): # test show_mywatchlist
          response = self.client.get(reverse("mywatchlist:show_watchlist"))
          self.assertEqual(response.status_code, 200)
    
       def test_url_xml(self):
          response = self.client.get(reverse("mywatchlist:show_xml"))
          self.assertEqual(response.status_code, 200)

       def test_url_json(self):
          response = self.client.get(reverse("mywatchlist:show_json"))
          self.assertEqual(response.status_code, 200)
    ```
   
    Jalankan `python manage.py collectstatic` untuk mengumpulkan berkas _static_. Pengujian terhadap ketiga URL tersebut dapat dilakukan dengan menjalankan seperti berikut:
   
    ```
    python manage.py test
    ```
    
11. Tambahkan juga `python manage.py loaddata initial_mywatchlist_data.json` pada `Procfile` untuk menampilkan data pada aplikasi Heroku.

    Dalam Procfile
    ```
    release: sh -c 'python manage.py migrate && python manage.py loaddata initial_catalog_data.json && python manage.py loaddata initial_mywatchlist_data.json' 
    web: gunicorn project_django.wsgi --log-file -
    ```
   
12. Untuk melakukan deployment ke Heroku, pastikan seluruh perubahan pada repository untuk Tugas 3 sudah di-push. Dalam hal ini, repository Tugas 3 saya bernama tugas2-pbp. Kemudian, pergi ke account settings pada Heroku dan salin API key. Lalu, pergi ke   `repository Tugas 3 > settings > secrets > actions` untuk membuat dua buah repository secret.<br><br>
Untuk repository secret yang pertama, namanya adalah `HEROKU_API_KEY` dengan secret nya adalah `API key yang telah diperoleh sebelumnya dari account settings pada Heroku`. Untuk repository secret yang kedua, namanya adalah `HEROKU_APP_NAME` dengan secret nya adalah `nama aplikasi Tugas 3 di Heroku`. Kemudian, pergi ke actions pada repository Tugas 3 dan klik `Re-run all jobs`. Deployment telah selesai.

## Postman

1. JSON
<img src="https://user-images.githubusercontent.com/112321270/191543420-864675ec-fc72-40de-926e-23fccf731d78.png" alt="" height="450" width="880" />
<br>

2. XML
<img src="https://user-images.githubusercontent.com/112321270/191543354-91c521a6-d52f-4f17-8e7f-97a37d01169c.png" alt="" height="450" width="880" />
<br>

3. HTML
<img src="https://user-images.githubusercontent.com/112321270/191543310-d975dccd-03ed-4a23-a62e-7b7a09b32904.png" alt="" height="450" width="880" />
