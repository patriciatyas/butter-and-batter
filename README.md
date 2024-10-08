# 🧈 Butter & Batter 🧈

Patricia Herningtyas (2306152241)
PBP - A

🍰 Need some daily dose of sweetness? [Click Here](http://patricia-herningtyas-butterandbatter.pbp.cs.ui.ac.id/)

# TUGAS INDIVIDU 2

## Cara Pengimplementasian Secara Step-by-Step 

Pertama-tama, nyalakan virtual environment.

1) Membuat sebuah proyek Django baru
    - Membuat direktori lokal baru dengan nama butter-and-batter lalu menjalankan virtual environment di dalamnya.
    - Membuat berkas requirements.txt berisikan dependencies dan menginstallnya. Setelah itu, menjalankan perintah 'django-admin startproject butter_and_batter .' yang akan membuat folder butter-and-batter berisi konfigurasi dasar untuk projek Django.
    - Menambahkan localhost ke dalam ALLOWED_HOSTS lalu menjalankan server Django pada direktori lokal.
    - Membuat repositori GitHub butter-and-batter. Setelah itu, menginisiasi direktori lokal butter-and-batter sebagai repositori Git.
    - Menambahkan file .gitignore ke dalam repositori lokal lalu mempush semua perubahan pada repositori lokal ke repositori github.
    
2) Membuat aplikasi dengan nama main pada proyek tersebut
    - Membuat aplikasi baru dengan nama main dalam direktori proyek butter_and_batter dengan menjalankan perintah 'python manage.py startapp main' yang akan membuat membuat folder main yang berisi berkas-berkas dasar untuk aplikasi Django seperti views.py, models.py, dan urls.py.
    - Membuka settings.py di folder proyek, lalu tambahkan 'main' ke dalam daftar INSTALLED_APP agar Django mengenali aplikasi baru.

3) Melakukan routing pada proyek agar dapat menjalankan aplikasi main.
    - Mengimpor fungsi include dari django.urls.
    - Menambahkan rute URL path('', include('main.urls')) untuk mengarahkan ke tampilan main di dalam variabel urlpatterns.

4) Membuat model pada aplikasi main dengan nama Product dan memiliki atribut wajib sebagai berikut.
name, price, description
    - Mengisi berkas model.py dalam aplikasi main dengan model dengan atribut atau field yang memiliki tipe data masing-masing. Untuk name, tipe datanya adalah CharField, untuk price, tipe datanya, IntegerField. Untuk description, tipe datanya TextField.

5) Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
    - Membuka berkas views.py yang terletak di dalam berkas aplikasi main.
    - Mengimport render dari django.shortcuts. Menambahkan fungsi show_main yang berisi context.
    - Memasukan return render(request, "main.html", context) yang berguna untuk me-render tampilan main.html dengan menggunakan fungsi render
    - Membuka berkas main.html dan mengubah nama dan kelas menjadi struktur kode Django yang sesuai untuk menampilkan data (template variables)

6) Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.
    - Untuk membuat routing pada urls.py di aplikasi Django, perlu memetakan URL ke fungsi di views.py menggunakan fungsi path(). Misalnya, path('',views.home, name='home') memetakan URL root ke fungsi home di views.py, sehingga saat URL tersebut diakses, fungsi yang sesuai akan dijalankan.

7) Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat
    - Membuat new project di PWS dengan nama butterandbatter kemudian menambahkan URL deployment "patricia-herningtyas-butterandbatter.pbp.cs.ui.ac.id" pada ALLOWED_HOST dalam settings.py sesuai username dan nama proyek di repositori lokal.
    - Menjalankan Project Command pada halaman PWS lalu mengubah nama branch menjadi main.
    - Mempush perubahan pada repositori lokal ke PWS dengan menjalankan perintah 'git push pws main:master'.

8) Membuat file README.md
    - Buatlah file baru dengan nama README.md di direktori utama proyek.
    - Mengedit file README.md untuk keterangan dan sesuai kebutuhan

Semua perubahan yang telah dibuat, tidak lupa untuk di git add, commit, dan push ke github dan push ke PWS. Jika sudah selesai mengerjakan, matikan virtual environment.

## Bagan Request Client ke Web Aplikasi Berbasis Django dan Responnya 
![alt text](Flowchart.png)
Permintaan dari client pertama kali diproses oleh `urls.py`, yang akan mencocokkan URL tersebut dengan fungsi view yang sesuai di `views.py`. Di dalam `views.py`, logika aplikasi dieksekusi dan jika memerlukan data dari database, fungsi view akan memanggil model yang ada di `models.py`. Setelah data berhasil diambil, view akan mempersiapkan template HTML dengan data tersebut dan merendernya. Hasil akhirnya adalah halaman web atau respons JSON yang dikirim kembali ke browser client.

## Fungsi Git dalam Pengembangan Perangkat Lunak 
Git adalah sistem kontrol versi yang membantu developer melacak perubahan kode sumber, berkolaborasi, dan mengelola versi proyek selama pengembangan perangkat lunak. Beberapa fungsi git diantaranya:
1. Memungkinkan developer untuk bekerja secara bersamaan pada proyek yang sama di laptop/mesin lokal mereka tanpa saling mengganggu pekerjaan masing-masing.
2. Branching yang memungkinkan developer untuk membuat cabang (branch) terpisah dari proyek utama dan merging untuk (merge) menggabungkan kembali cabang tersebut ke cabang utama. Hal ini dilakukan untuk menghindari konflik.
3. Menyimpan berbagai versi dari sebuah proyek sebagai "commit" yang dapat mengurangi resiko kehilangan pekerjaan yang sudah dibuat.
4. Dengan adanya fitur commit dan log, git menyediakan catatan lengkap dari siapa yang mengubah apa, kapan, dan mengapa, melalui 
5. Mendeteksi konflik ketika dua developer melakukan perubahan pada bagian kode yang sama dan meminta developer untuk menyelesaikannya

## Mengapa Framework Django Dijadikan Permulaan Pembelajaran Pengembangan Perangkat Lunak? 
Django menggunakan arsitektur Model-View-Template (MVT) yang memfasilitasi pemisahan antara logika aplikasi, data, dan tampilan secara jelas. Django juga mempunyai berbagai fitur siap pakai, seperti autentikasi pengguna, URL routing, ORM (Object-Relational Mapping), dan lainnya. Hal ini sangat membantu developer pemula karena mereka tidak perlu membangun semuanya dari awal.


## Mengapa model pada Django disebut sebagai ORM? 
Model Django disebut sebagai ORM karena memungkinkan interaksi dengan database menggunakan bahasa Python, tanpa perlu menulis query SQL secara langsung. Django ORM secara otomatis mengubah model Python menjadi tabel database, sehingga memudahkan pengelolaan data dan mengurangi risiko kesalahan yang terjadi saat menulis query SQL secara manual.

# TUGAS INDIVIDU 3

## Data delivery dalam pengimplementasian sebuah platform
Data delivery mengoptimalkan performa platform dengan mengurangi waktu muat dan bandwidth, memungkinkan pengolahan data real-time, serta mendukung keamanan dan kontrol akses data melalui enkripsi dan autentikasi. Selain itu, data delivery juga memungkinkan platform untuk menangani pertumbuhan pengguna dan volume data.

## XML vs JSON
Menurut saya, JSON lebih baik dibandingkan XML karena lebih readable. Melalu pencaharian lebih lanjut, JSON ternyata memang lebih populer dibandingkan XML.
- Parsing dan serialisasi JSON lebih cepat dan lebih efisien karena banyak bahasa pemrograman memiliki dukungan built-in atau library yang efisien untuk menangani JSON.
- Sintaks JSON mirip dengan bahasa pemrograman modern dan formatnya hanya terdiri dari objek dan array sehingga lebih mudah dibaca. Sedangkan, sintaks XML lebih kompleks dengan tag pembuka dan penutup, atribut, dan hierarki yang lebih rumit.
- Selain itu, format JSON merupakan subset dari objek JavaScript yang memudahkan pengolahan data JSON langsung dari browser. Jika menggunakam XML, dibutuhkan parsing tambahan (pembacaan dan interpretasi data)

## Fungsi dari method is_Valid() pada form Django
Untuk memeriksa apakah data yang diterima dari pengguna (misalnya, melalui form HTML) sesuai dengan aturan dan batasan yang telah ditetapkan dalam definisi form tersebut.

## Fungsi csrf_token saat membuat form di Django
Agar aplikasi web terlindungi dari serangan CSRF (Cross-Site Request Forgery) CSRF, kita harus menambahkan csrf_token. CSRF adalah jenis serangan di mana penyerang memanipulasi akses autentikasi pengguna untuk melakukan tindakan yang tidak diinginkan pada aplikasi web yang mereka akses.

Token csrf_token dibuat oleh server dan dimasukkan ke dalam setiap form HTML. Saat seseorang melakukan permintaan POST atau tindakan yang mengubah data, token ini dikirim kembali ke server untuk memastikan bahwa permintaan tersebut berasal dari pengguna yang sah dan bukan dari penyerang.

Penyerang dapat memanfaatkan kerentanan CSRF untuk membuat permintaan berbahaya kepada aplikasi web dengan menggunakan formulir atau skrip yang disembunyikan di situs web lain, dan jika pengguna yang sah sedang login, penyerang dapat membuat permintaan palsu yang memanfaatkan kredensial yang sudah ada pada aplikasi jika csrf_token tidak ditambahkan.

## Step-by-step Pengimplementasian
Membuat input form untuk menambahkan objek model pada app sebelumnya.

1. Membuat form (forms.py) dengan model ProductEntry dengan field untuk menerima data Product baru
    - Menambahkan fungsi create_product_entry(views.py) yang mengarahkan pengguna dari halaman utama ke halaman input kemudian memvalidasi, memproses, dan menyimpan input. Setelah input berhasil disimpan, pendapat akan diarahkan kembali ke halaman utama (redirect).
    - Menambahkan product_entries = Product.objects.all() pada fungsi show_main (views.py) agar input yang berhasil diterima ditampilkan ketika pengguna diarahkan kembali ke halaman utama
    - Membuat HTML baru (create_product_entry.html) untuk menampilkan form input
    - URL Routing form input dengan menambahkan path URL ke dalam urlpatterns (urls.py)
    
2. Tambahkan 4 fungsi views baru untuk melihat objek yang sudah ditambahkan dalam format XML, JSON, XML by ID, dan JSON by ID.
    - Mengimport HttpResponse dan Serializer pada views.py
    - Menambahkan 4 fungsi untuk view dengan format JSON dan XML di views.py (show_xml, show_json, show_xml_by_id, dan show_json_by_id)

3. Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2
    - Meng-import keempat fungsi view yang sudah dibuat pada poin 2 ke dalam urls.py.
    - Menambahkan path URL masing-masing view ke dalam urlpatterns (urls.py)


## XML
![alt text](XML.jpg)

## JSON
![alt text](JSON.jpg)
![alt text](<JSON 2.jpg>)

## XML by ID
![alt text](<XML BY ID.jpg>)

## JSON by ID
![alt text](<JSON BY ID-1.jpg>)

# TUGAS INDIVIDU 4
## Perbedaan antara `HttpResponseRedirect()` dan `redirect()`
### `HttpResponseRedirect()` :
Ini adalah kelas di Django yang digunakan untuk mengembalikan HTTP redirect response ke URL yang ditentukan. URL tujuan perlu dimasukkan secara manual, seperti `HttpResponseRedirect('/some-url/')`

### `redirect()` :
`redirect()` adalah shortcut function yang lebih mudah digunakan dibanding HttpResponseRedirect. Ini bisa menerima model, view, atau url sebagai argumen, dan akan secara otomatis menangani pembuatan URL untuk redirect (lebih fleksibel).

## Cara Kerja Penghubungan Model `Product` dan `User`
Penghubungan model Product dengan User dilakukan dengan menggunakan ForeignKey. Langkah-langkahnya adalah sebagai berikut:
1. Membuat Model Product:
    - Tambahkan ForeignKey ke model User dalam model Product untuk menunjukkan bahwa setiap produk memiliki pemilik (user).
    - `user = models.ForeignKey(User, on_delete=models.CASCADE)`:
        - Ini menghubungkan Product dengan User menggunakan ForeignKey.
        - `on_delete=models.CASCADE` berarti ketika user dihapus, semua produk yang terkait dengan user tersebut juga akan dihapus.
2. Mengubah fungsi `create_product_entry` pada `views.py`:
    `product_entry = form.save(commit=False)`
    `product_entry.user = request.user`
    `product_entry.save()`
    
    Parameter commit=False yang digunakan pada potongan kode diatas berguna untuk mencegah Django agar tidak langsung menyimpan objek yang telah dibuat dari form langsung ke database.

    Hal tersebut memungkinkan kita untuk memodifikasi terlebih dahulu objek tersebut sebelum disimpan ke database. Pada kasus ini, kita akan mengisi field user dengan objek User dari return value `request.user` yang sedang terotorisasi untuk menandakan bahwa objek tersebut dimiliki oleh pengguna yang sedang login.

3. Mengubah product_entries dan context pada fungsi show_main:
    `product_entries = ProductEntry.objects.filter(user=request.user)`
    `context = {'name': request.user.username,...}`
    
    Kode tersebut berfungsi untuk menampilkan objek Product Entry yang terasosiasikan dengan pengguna yang sedang login. Hal tersebut dilakukan dengan menyaring seluruh objek dengan hanya mengambil Product Entry yang dimana field user terisi dengan objek User yang sama dengan pengguna yang sedang login.

    Kode `request.user.username` berfungsi untuk menampilkan username pengguna yang login pada halaman main.

4. Menyimpan semua perubahan dan melakukan migrasi model dengan `python manage.py migrations` dan `python manage.py migrate`

5. Mempersiapkan aplikasi web untuk environment production dengan menambahkan sebuah import baru pada `settings.py` yang ada pada subdirektori `butter_and_batter`:
    `import os`
    
    Kemudian mengganti variabel `DEBUG` dari berkas `settings.py`:
    `PRODUCTION = os.getenv("PRODUCTION", False)`
    `DEBUG = not PRODUCTION`

6. Selesai! jalankan proyek Django dengan `python manage.py runserver` dan buka http://localhost:8000/

## Perbedaan _authentication_ dan _authorization_, dan Implementasinya di Django
*Authentication:*
Proses untuk memverifikasi identitas pengguna. Ini biasanya melibatkan login dengan nama pengguna dan kata sandi.
Di Django, ini diimplementasikan menggunakan sistem user dan password hashing yang aman. Proses otentikasi terjadi ketika pengguna memasukkan kredensial login.

*Implementasi Authentication:*
Menambahkan fungsi `login_user` dalam `views.py`:
```
def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main:show_main')

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)
```
`login(request, user)` berfungsi untuk melakukan login terlebih dahulu. Jika pengguna valid, fungsi ini akan membuat session untuk pengguna yang berhasil login.

*Authorization:*
Setelah pengguna terotentikasi, otorisasi menentukan apa yang boleh atau tidak boleh dilakukan oleh pengguna tersebut. Ini berkaitan dengan izin (permissions).

## Cara Django Mengingat Pengguna yang Telah Login dan Pengguna Cookies
Django menggunakan session ID dan cookies. Ketika login, session ID akan disimpan. Cookies dapat menyimpan preferensi pengguna, menyimpan data sementara, dan juga dapat melacak aktivitas pengguna di situs untuk keperluan analisis. Tidak semua cookies aman digunakan, ada kasus dimana cookies berisi informasi sensitif seperti password namun tidak dienkripsi sehingga cookies ini memiliki kemungkinan untuk bisa diakses melalui JavaScript oleh pihak ketiga.

## Pengimplementasian Checklist Secara Step-by-Step
1. Mengimplementasikan fungsi registrasi, login, dan logout.
    - Membuat login html dan register html dengan form dan methodnya adalah post
    - Membuat fungsi registrer di views.py yang memanggil UserCreationForm() dan menyimpan form yang akan pindah ke page login.
    - Membuat fungsi user_login yang memanggil AuthenticationForm(data=request.POST) yang akan men-get user kemudian akan menyimpan cookie dan mengarahkan user ke front page
    - Membuat fungsi logout_user untuk menghapus cookie sebelumnya dan mengarahkan ke page login.
    - Mengimport semua fungsi views lalu membuat path untuk setiap fungsinya.

2. Membuat dua akun pengguna dengan masing-masing tiga dummy data
    - Melakukan registrasi 2 akun pada page register/ kemudian login dan menambahkan 3 data pada page create-product-entry/ untuk masing-masing akun tersebut.
    ![alt text](nikizefanya.png)
    ![alt text](taylorswift.png)

3. Menghubungkan model Product dengan User
    - Menambahkan kode `user = models.ForeignKey(User, on_delete=models.CASCADE)` dalam class Product di models.py (menggunakan ForeignKey)
    - Melakukan migrasi model ke database dengan `python manage.py makemigrations` dan `python manage.py migrate`.

4. Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi.
    - Memastikan pengguna sudah login sebelum bisa mengakses halaman utama dengan menambahkan login_required decorator di view yang menampilkan halaman utama.
    - Mengambil data pengguna yang sedang login menggunakan `request.user`
    - Setel cookie last login saat pengguna login, dan tampilkan di halaman utama `'last_login': request.COOKIES['last_login'],`

5. Menjawab beberapa pertanyaan berikut pada README.md
    - Memodifikasi README.md yang sudah dibuat sebelumnya


# TUGAS INDIVIDU 5
 ## Urutan Prioritas CSS Selector
 1. Inline Styles, CSS yang ditulis langsung di atribut elemen HTML menggunakan `style="..."` akan memiliki prioritas tertinggi.
 2. ID Selectors, Selector yang merujuk pada ID elemen (contoh: `#myId`) memiliki prioritas lebih tinggi daripada selector lainnya kecuali inline styles.
 3. Class, Pseudo-Class, Attribute Selectors, Selector yang merujuk pada class, pseudo-class (contoh: `:hover`), atau atribut (contoh: `[type="text"]`) memiliki prioritas di bawah ID selectors. Contoh: `.myClass`, `:hover`.
 4. Element and Pseudo-Element Selectors, Selector yang langsung merujuk pada elemen (contoh: `p`, `h1`) memiliki prioritas paling rendah.
 5. Specificity, Ketika ada dua atau lebih aturan yang berlaku, yang lebih spesifik akan diterapkan. Misalnya, `div p` lebih spesifik daripada `p` saja.
 6. Importance (`!important`), Deklarasi dengan `!important` mengalahkan semua aturan lain kecuali inline styles yang juga menggunakan `!important`.

 
 ## Pentingnya Responsive Design dalam Pengembangan Aplikasi Web
 Responisivitas penting karena pengguna saat ini mengakses aplikasi web melalui berbagai perangkat dengan resolusi dan ukuran layar yang berbeda.
 
 *Alasan Pentingnya:*
 1. Desain yang responsif memastikan pengguna dapat melihat dan menggunakan website dengan nyaman tanpa harus melakukan zoom in atau scroll horizontal.
 2. SEO (Search Engine Optimization): Google memberikan prioritas lebih tinggi pada website yang responsif di hasil pencarian mobile.
 3. Efisiensi Pengembangan: Daripada membuat versi terpisah untuk mobile dan desktop, responsive design memungkinkan satu website bekerja di berbagai perangkat.
 >> Contoh:
 >> Sudah Menerapkan: _Instagram_ – layout gambar dan teks menyesuaikan dengan baik di mobile dan desktop.
 >> Belum Menerapkan: Beberapa situs pemerintahan lama – seringkali hanya dirancang untuk desktop, menyebabkan tampilan tidak nyaman di perangkat mobile.

 
 
 ## Perbedaan Margin, Border, dan Padding serta Implementasinya
 1. Margin: Ruang di luar elemen, yang memisahkan elemen tersebut dengan elemen lain di sekitarnya. Margin bersifat transparan dan tidak memiliki warna.
 2. Border: Garis di sekitar elemen yang membatasi padding dan konten elemen tersebut. Border bisa diberi warna, ketebalan, dan gaya.
 3. Padding: Ruang di dalam elemen, antara konten elemen dan border. Padding mendorong konten menjauh dari border.
 *Cara Implementasi:*
 ```div {
    margin: 20px;  /* Ruang di luar elemen */
    border: 2px solid black;  /* Border hitam dengan ketebalan 2px */
    padding: 15px;  /* Ruang di dalam elemen sebelum konten */
    }
```
 
 ## Konsep Flexbox dan Grid Layout serta Kegunaannya
 *Flexbox* adalah sistem tata letak satu dimensi yang digunakan untuk mengatur elemen dalam satu baris (row) atau satu kolom (column). Flexbox sangat berguna untuk tata letak yang responsif dan dinamis, seperti membuat elemen menjadi rata tengah, menyesuaikan ukuran elemen secara fleksibel, atau menyusun elemen dalam susunan yang berbeda.
 *Grid Layout* adalah sistem tata letak dua dimensi yang memungkinkan kita untuk mengatur elemen dalam baris dan kolom. Grid cocok untuk membuat tata letak yang kompleks dengan lebih mudah, seperti pengaturan grid untuk dashboard atau halaman katalog produk. 


 ## Implementasi Checklist Secara Step-by-Step:
 - Menambahkan fungsi `edit_product` dan `delete_product` berdasarkan `id` ke dalam `views.py` lalu menambahkan path dari kedua fungsi tersebut ke dalam `urls.py`
 - Mengostumisasi desain template HTML menggunakan Tailwind CSS untuk setiap page yang saya buat
 - Menambahkan folder baru yaitu static/image untuk menyimpan gambar. Kemudian menambahkan image tersebut ke main.html untuk menampilkan gambar jika belum ada data product yang tersimpan.
 - Menambahkan konfigurasi file static dengan cara menambahkan whitenoise.middleware.WhiteNoiseMiddleware ke middleware, lalu menambahkan STATICFILES_DIRS dan juga STATIC_ROOT.
 - Membuat navbar yang responsive pada base.html di folder templates menggunakan Tailwind dan mengimplementasikan dropdown navbar untuk pengguna yang sedang login di handphone dengan penanganan interaksi menggunakan JavaScript, termasuk menampilkan dan menyembunyikan menu mobile.

 # TUGAS INDIVIDU 6
 ## Manfaat dari Penggunaan JavaScript dalam Pengembangan Aplikasi Web!
 Jika HTML digunakan untuk struktur dan konten dasar halaman web serta CSS digunakan untuk mengatur tampilan, tata letak elemen-element HTML, menambahkan gaya, warna, font, dan layout ke halaman web, JavaScript berperan untuk menambahkan interaktivitas dan fungsionalitas pada halaman web. Dengan menggunakan JavaScript, kita dapat membuat elemen yang responsif terhadap event yang dilakukan oleh pengguna, mengolah data, dan berkomunikasi dengan server.

 ## Fungsi dari Penggunaan `await` Ketika Menggunakan `fetch()`
 Keyword `await` berfungsi untuk menunggu respons yang dikembalikan oleh `fetch()` sebelum melanjutkan eksekusi kode berikutnya, memungkinkan pemanggilan data secara asinkron.

Tanpa menggunakan `await`, kode akan terus berjalan tanpa menunggu respons dari `fetch()`. Hal ini berarti bagian kode yang bergantung pada hasil dari `fetch()` bisa dieksekusi sebelum respons tersedia, yang dapat menyebabkan error atau hasil yang tidak diharapkan.

 ## Fungsi `csrf_exempt` pada view yang digunakan untuk AJAX `POST`
 Saat melakukan permintaan AJAX POST, token CSRF umumnya disertakan dalam header sebagai bagian dari data formulir. Jika token CSRF tidak ada dalam permintaan AJAX, Django akan secara otomatis menolak permintaan itu sebagai bagian dari mekanisme keamanannya.

Kita memerlukan decorator `csrf_exempt` karena pada fungsi `add_product_entry_ajax`, autentikasi sudah dilakukan dan kita yakin bahwa permintaan tersebut valid. Oleh karena itu, kita dapat memilih untuk tidak mengharuskan adanya token CSRF untuk operasi ini. Dekorator `@csrf_exempt` digunakan untuk menonaktifkan pemeriksaan token CSRF pada view tersebut.

## Pembersihan Data Input pengguna di Backend
Pembersihan data input pengguna juga sangat penting di sisi backend karena kita perlu memastikan bahwa semua data yang diterima dari pengguna telah diperiksa dan dibersihkan sebelum disimpan atau diproses lebih lanjut. Langkah ini membantu mencegah serangan seperti Cross-Site Scripting (XSS), yang dapat merusak data atau membahayakan pengguna. Dengan demikian, pembersihan di backend memberikan lapisan perlindungan tambahan untuk aplikasi kita.

Selain itu, pembersihan data di backend juga memastikan konsistensi dalam penanganan data. Hal ini mengurangi kemungkinan terjadinya kesalahan yang dapat muncul jika hanya bergantung pada pembersihan di frontend, serta memastikan bahwa hanya data yang valid dan aman yang akan diproses oleh sistem.

## Implementasi Checklist Secara Step-by-Step
1. Mengubah kode `cards` data product agar dapat mendukung AJAX `GET`
- Saya mengubah kode tampilan product card untuk memungkinkan data diambil secara asinkronus menggunakan AJAX. Dengan ini, data yang ditampilkan pada kartu akan berasal dari permintaan GET AJAX, bukan dari rendering server langsung.

2. Melakukan pengambilan data product menggunakan AJAX `GET`. Memaastikan bahwa data yang diambil hanyalah data milik pengguna yang logged-in.
- Membuat fungsi JavaScript untuk mengirim permintaan AJAX `GET` dan memfilter data sehingga hanya mengambil product yang dimiliki pengguna yang sedang login.
```
async function getProductEntries() {
        return fetch("{% url 'main:show_json' %}").then((res) => res.json())
      }
```
3. Membuat sebuah tombol yang membuka sebuah modal dengan form untuk menambahkan mood.
- Membuat tombol dengan menambahkan kode `onclick="showModal();"`. Di dalam modal tersebut, akan tersedia form untuk input field.
```
<button data-modal-target="crudModal" data-modal-toggle="crudModal" class="btn bg-yellow-900 hover:bg-red-950 text-white font-bold py-2 px-4 rounded-lg transition duration-300 ease-in-out transform hover:-translate-y-1 hover:scale-105" onclick="showModal();"> Add New Product Entry by AJAX </button>
```
4. Membuat fungsi view baru untuk menambahkan product baru ke dalam basis data.
- Membuat fungsi `add_product_entry_ajax` yang sudah ada strip tag dengan method POST dan mereturn HttpResponse(status=201) jika berhasil.

5. Membuat path /create-ajax/ yang mengarah ke fungsi view yang baru dibuat.
- Saya menambahkan path `/create-product-entry-ajax/` di urls.py yang akan mengarahkan ke view untuk menambahkan product by AJAX

6. Menghubungkan form yang telah kamu buat di dalam modal kamu ke path /create-ajax/.
Menambahkan kode ke fungsi `addProductEntry()` di `main.html`
```
function addProductEntry() {
    fetch("{% url 'main:add_product_entry_ajax' %}", {
        method: "POST",
        body: new FormData(document.querySelector('#productEntryForm')),
    })

```
Selain itu, saya juga menambahkan error handling
```
.then(response => {
    if (response.ok) {
    refreshProductEntries();
    document.getElementById("productEntryForm").reset();
    hideModal(); // Hide modal if successful
    } else {
    return response.text(); // Capture the error message
    }
})
.then(errorMessage => {
    if (errorMessage) {
    alert(errorMessage); // Show error message to the user
    }
})
.catch(error => {
    console.error("Error:", error);
});

return false;
}
```
7. Melakukan refresh pada halaman utama secara asinkronus untuk menampilkan daftar mood terbaru tanpa reload halaman utama secara keseluruhan.
- Membuat fungsi `refreshProductEntries()` untuk memperbarui halaman, lalu mengintegrasikan fungsi ini ke dalam fungsi `addProductEntry()`. Dengan cara ini, setiap kali tombol submit ditekan, produk baru akan ditambahkan dan halaman akan diperbarui secara asinkronus.












