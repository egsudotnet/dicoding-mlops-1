KRITERIA

### Kriteria 1: Menggunakan TensorFlow Extended (TFX) untuk Membuat Machine Learning Pipeline

Mirip seperti materi latihan sebelumnya, Anda harus membuat machine learning pipeline sederhana menggunakan TensorFlow Extended (TFX). Machine learning pipeline yang Anda buat harus memuat seluruh komponen yang dibutuhkan seperti berikut.

* ExampleGen
* StatisticGen
* SchemaGen
* ExampleValidator
* Transform
* Trainer
* Resolver
* Evaluator
* Pusher

Seluruh komponen di atas harus dijalankan menggunakan **InteractiveContext** dan disimpan dalam sebuah folder bernama   **<username_dicoding>-pipeline** .

### Kriteria 2: Melampirkan Dokumentasi Proyek

Pada proyek ini, Anda menggunakan **text cell** pada notebook (.ipynb) untuk menjelaskan setiap tahapan proyek dan berkas **Markdown** untuk menjelaskan proyek secara keseluruhan. Berikut merupakan beberapa informasi yang harus ada dalam dokumentasi yang Anda buat.

* Informasi terkait dataset yang digunakan.
* Informasi tentang persoalan yang ingin diselesaikan.
* Penjelasan terkait solusi machine learning yang akan dibuat beserta target yang ingin dicapai.
* Penjelasan tentang metode pengolahan data, arsitektur model yang digunakan, dan metrik untuk mengevaluasi performa model.
* Informasi terkait performa model machine learning yang telah dibuat.

Berikut merupakan template dokumentasi yang dapat Anda gunakan: [format-dokumentasi-1](https://github.com/dicodingacademy/assets/blob/main/ml-mlops/submission-1/format-dokumentasi.md).


## PENILAIAN

Submission Anda akan dinilai oleh Reviewer guna menentukan kebenaran submission yang dikerjakan. Supaya bisa lulus dari kelas ini, proyek Anda mesti memenuhi seluruh kriteria yang ada. Apabila ada ketentuan dalam kriteria yang belum terpenuhi, proyek Anda akan kami tolak.

Submission Anda akan dinilai oleh Reviewer dengan penilaian bintang berskala 1-5. Untuk mendapatkan nilai tinggi, Anda bisa menerapkan beberapa saran berikut:

1. Memanfaatkan komponen Tuner untuk menjalankan proses hyperparameter tuning secara otomatis.
2. Menambahkan tahapan model deployment dengan TensorFlow Serving.
3. Menambahkan sebuah berkas notebook untuk menguji dan melakukan prediction request ke model serving yang telah dibuat.

Berikut adalah detail penilaian submission:

![rating-default-1](https://dicoding-web-img.sgp1.cdn.digitaloceanspaces.com/original/submission-rating-badge/rating-default-1.png "rating-default-1")semua ketentuan wajib terpenuhi, tetapi terdapat indikasi kecurangan atau plagiasi dalam mengerjakan submission.

---

![rating-default-2](https://dicoding-web-img.sgp1.cdn.digitaloceanspaces.com/original/submission-rating-badge/rating-default-2.png "rating-default-2")semua ketentuan wajib terpenuhi, tetapi tidak menerapkan saran sama sekali.

---

![rating-default-3](https://dicoding-web-img.sgp1.cdn.digitaloceanspaces.com/original/submission-rating-badge/rating-default-3.png "rating-default-3")semua ketentuan wajib terpenuhi dan menerapkan minimal 1 saran di atas.

---

![rating-default-4](https://dicoding-web-img.sgp1.cdn.digitaloceanspaces.com/original/submission-rating-badge/rating-default-4.png "rating-default-4")semua ketentuan wajib terpenuhi dan menerapkan minimal 2 saran di atas.

---

![rating-default-5](https://dicoding-web-img.sgp1.cdn.digitaloceanspaces.com/original/submission-rating-badge/rating-default-5.png "rating-default-5")semua ketentuan wajib terpenuhi dan menerapkan semua saran di atas.

> Catatan: Jika **submission Anda ditolak** maka  **tidak ada penilaian** . Kriteria penilaian bintang di atas hanya berlaku  **jika submission Anda lulus** .
>
