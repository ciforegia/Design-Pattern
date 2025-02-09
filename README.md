# OOP with Design Patterns

Repository ini berisi implementasi beberapa Design Pattern dalam Object-Oriented Programming (OOP), yaitu Factory Method, Decorator, dan Iterator. Setiap pola desain dijelaskan dengan konsep, diagram kelas, use-case, dan diagram sekuens.

## 1. Factory Method Design Pattern
Factory Method adalah pola desain kreasional yang digunakan untuk menyediakan antarmuka dalam membuat objek dalam superclass, tetapi memungkinkan subclass untuk mengubah tipe objek yang akan dibuat.

### a. Concept
![Factory Method Concept](https://github.com/user-attachments/assets/1d11d8cf-5810-48d2-946b-521312602d11)
Penjelasan konsep Factory Method, di mana sebuah metode dalam superclass bertanggung jawab untuk membuat objek yang dapat bervariasi tergantung pada subclass yang mengimplementasikannya.

### b. Class Diagram
![Factory Method Class Diagram](https://github.com/user-attachments/assets/8565738b-4061-44d1-a269-9190eeefd46a)
Diagram ini menunjukkan hubungan antara kelas-kelas dalam Factory Method, termasuk kelas abstrak atau antarmuka serta kelas konkret yang mengimplementasikannya.

### c. Use Case
![Factory Method Use Case](https://github.com/user-attachments/assets/c00ff44f-a43f-498a-932f-e4ab0b0a03ee)
Penggunaan pola ini dalam situasi nyata, misalnya dalam pembuatan berbagai jenis kendaraan tanpa menentukan secara eksplisit kelasnya.

### d. Sequence Diagram
![image](https://github.com/user-attachments/assets/1967237a-5b3d-4f24-8d3f-482fc55b9c7f)
Diagram yang menggambarkan bagaimana objek dibuat menggunakan Factory Method secara berurutan.

---

## 2. Decorator Design Pattern
Decorator adalah pola desain struktural yang memungkinkan penambahan fitur ke objek secara dinamis tanpa mengubah strukturnya.

### a. Concept
![Decorator Concept](https://github.com/user-attachments/assets/54a91e79-9ab1-4d0b-86fc-2d97b8c9f0f2)
Konsep dasar dari Decorator Pattern yang menunjukkan bagaimana fitur tambahan dapat diterapkan pada objek yang ada.

### b. Class Diagram
![Decorator Class Diagram](https://github.com/user-attachments/assets/c7b80e1b-52ce-4cf5-8010-69877ba54184)
Diagram yang menggambarkan hubungan antara kelas utama dan dekoratornya.

### c. Use Case
![Decorator Use Case](https://github.com/user-attachments/assets/c22db2d2-d364-492f-b263-fbeff9f944dd)
Contoh penerapan pola ini dalam kehidupan nyata, misalnya menambahkan fitur keamanan pada sistem login.

### d. Sequence Diagram
![Decorator Sequence Diagram](https://github.com/user-attachments/assets/89d58682-4b1c-4496-bfa4-0669ab788427)
Diagram yang menunjukkan urutan interaksi saat menerapkan dekorasi pada suatu objek.

---

## 3. Iterator Design Pattern
Iterator adalah pola desain perilaku yang digunakan untuk menyediakan cara untuk mengakses elemen-elemen dalam koleksi secara berurutan tanpa mengekspos detail implementasinya.

### a. Concept
![Iterator Concept](https://github.com/user-attachments/assets/817cb610-7b54-46b2-aa6f-2975986c556d)
Penjelasan tentang bagaimana Iterator bekerja dalam mengelola koleksi data.

### b. Class Diagram
![Iterator Class Diagram](https://github.com/user-attachments/assets/1b217bc2-3c0c-4220-9bab-94078e8c0615)
Diagram hubungan antara koleksi dan iterator dalam mengakses elemen-elemen data.

### c. Use Case
![Iterator Use Case](https://github.com/user-attachments/assets/2186feca-063b-4846-aaa8-fd8a4597a363)
Contoh penerapan Iterator Pattern dalam sistem, misalnya iterasi melalui daftar pengguna dalam aplikasi.

### d. Sequence Diagram
![Iterator Sequence Diagram](https://github.com/user-attachments/assets/cae6c286-ecca-43ae-9b7f-4cf0816bec62)
Diagram yang menggambarkan bagaimana iterator bekerja dalam mendapatkan elemen-elemen secara bertahap.

---

Dengan adanya dokumen ini, diharapkan pembaca dapat memahami implementasi dari masing-masing design pattern dalam OOP serta bagaimana pola-pola tersebut dapat digunakan dalam berbagai kasus nyata.











