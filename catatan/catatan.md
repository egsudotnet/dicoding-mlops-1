Istilah-istilah yang disebutkan di atas adalah komponen dalam pipeline  **TensorFlow Extended (TFX)** , sebuah platform untuk membangun pipeline pembelajaran mesin end-to-end. Berikut adalah penjelasan masing-masing istilah:

---

### 1. **ExampleGen**

**ExampleGen** adalah komponen yang bertanggung jawab untuk mengimpor data mentah ke dalam pipeline. Data ini dapat berasal dari berbagai sumber seperti file CSV, TFRecord, database, atau bahkan API.

* **Fungsi Utama** : Membaca dan memformat data mentah menjadi format yang dapat digunakan oleh pipeline (biasanya TFRecord).
* **Output** : Data dalam format standar yang dapat digunakan oleh komponen lain.

---

### 2. **StatisticGen**

**StatisticGen** adalah komponen yang menghitung statistik deskriptif dari data. Statistik ini berguna untuk memahami distribusi data dan mendeteksi masalah seperti nilai kosong atau distribusi yang tidak normal.

* **Fungsi Utama** : Menghasilkan statistik data yang terperinci menggunakan  **TensorFlow Data Validation (TFDV)** .
* **Output** : Statistik data dalam format `tf.Metadata`.

---

### 3. **SchemaGen**

**SchemaGen** adalah komponen yang menghasilkan skema data berdasarkan statistik dari  **StatisticGen** . Skema ini mendefinisikan properti data seperti tipe fitur, nilai yang diizinkan, dan apakah fitur tersebut bersifat wajib atau opsional.

* **Fungsi Utama** : Membuat skema untuk memastikan konsistensi dan kualitas data.
* **Output** : Skema dalam format `tf.Metadata`.

---

### 4. **ExampleValidator**

**ExampleValidator** adalah komponen yang digunakan untuk memvalidasi data terhadap skema yang dihasilkan oleh  **SchemaGen** . Ia memeriksa apakah ada data yang tidak sesuai dengan skema, seperti data yang hilang, nilai yang tidak valid, atau anomali lainnya.

* **Fungsi Utama** : Menditeksi anomali dan membersihkan data.
* **Output** : Laporan validasi yang mencantumkan masalah data.

---

### 5. **Transform**

**Transform** adalah komponen yang digunakan untuk memproses data dengan menerapkan transformasi fitur. Transformasi ini mencakup normalisasi, pengelompokan, pembuatan fitur baru, atau teknik preprocessing lainnya.

* **Fungsi Utama** : Mempersiapkan data agar dapat digunakan oleh model pembelajaran mesin.
* **Output** : Dataset yang sudah ditransformasi dan kode preprocessing yang dapat diintegrasikan ke dalam model.

---

### 6. **Trainer**

**Trainer** adalah komponen yang bertanggung jawab untuk melatih model pembelajaran mesin. Komponen ini menggunakan data yang telah diproses oleh  **Transform** .

* **Fungsi Utama** : Melatih model berdasarkan konfigurasi pipeline.
* **Output** : Model terlatih dalam format `SavedModel`.

---

### 7. **Resolver**

**Resolver** adalah komponen opsional yang bertugas untuk mengambil artefak terbaru atau yang paling relevan dari pipeline. Biasanya digunakan untuk memilih model sebelumnya dalam proses pelatihan ulang atau evaluasi.

* **Fungsi Utama** : Memastikan pipeline menggunakan artefak yang sesuai, seperti model terbaik atau dataset terbaru.
* **Output** : Artefak yang terpilih untuk digunakan oleh komponen lain.

---

### 8. **Evaluator**

**Evaluator** adalah komponen yang digunakan untuk mengevaluasi performa model. Evaluasi ini mencakup metrik seperti akurasi, F1-score, atau metrik lainnya, serta membandingkan model baru dengan model sebelumnya.

* **Fungsi Utama** : Memberikan penilaian mendalam terhadap kinerja model.
* **Output** : Laporan evaluasi dan rekomendasi terkait model.

---

### 9. **Pusher**

**Pusher** adalah komponen terakhir dalam pipeline yang bertugas untuk men-deploy model yang sudah dilatih ke lingkungan produksi.

* **Fungsi Utama** : Mengirim model ke sistem produksi seperti server model atau sistem inferensi.
* **Output** : Model yang ter-deploy di lokasi tujuan (misalnya cloud storage atau API endpoint).

---

### Alur Kerja TFX

Pipeline biasanya bekerja secara berurutan:

1. **ExampleGen** → Data masuk.
2. **StatisticGen** → Statistik dibuat.
3. **SchemaGen** → Skema dihasilkan.
4. **ExampleValidator** → Validasi data.
5. **Transform** → Transformasi data.
6. **Trainer** → Pelatihan model.
7. **Resolver** → Artefak relevan dipilih.
8. **Evaluator** → Evaluasi model.
9. **Pusher** → Model dideploy.

Pipeline ini memastikan alur kerja pembelajaran mesin yang efisien dan andal.
