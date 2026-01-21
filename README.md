# Smart Interactive Bedroom Showcase

Simulasi **kamar tidur 3D interaktif** berbasis **Python & PyOpenGL**
yang memungkinkan pengguna menjelajahi ruangan secara bebas,
berinteraksi dengan objek, serta merasakan perubahan pencahayaan siang
dan malam secara real-time.

Project ini dikembangkan sebagai tugas mata kuliah:

> **Komputer Grafik & Pengolahan Citra -- Semester 5**

dengan fokus pada penerapan konsep: - Pemodelan objek 3D - Transformasi
dan koordinat - Pencahayaan (lighting) - Tekstur - Interaksi kamera -
Collision detection

------------------------------------------------------------------------

## Fitur

### Lingkungan 3D

-   Seluruh objek dibuat menggunakan primitive OpenGL (Cube, Quad,
    Cylinder)
-   Tidak menggunakan model 3D eksternal
-   Dilengkapi tekstur untuk meningkatkan realisme

### Sistem Kamera

-   Pergerakan bebas (first-person style)
-   Kamera tidak dapat menembus dinding atau furnitur (collision
    detection)
-   Fitur fokus otomatis ke objek tertentu

### Interaksi Objek

-   Buka / tutup wardrobe
-   Nyalakan / matikan lampu plafon & lampu tidur
-   Mode siang & malam
-   Gorden
-   Power PC

### Fitur Tambahan

-   Jam digital real-time di dalam scene
-   HUD semi-transparan (informasi kamera & kontrol)

------------------------------------------------------------------------

## Kontrol

### Pergerakan Kamera

  Tombol       Fungsi
  ------------ -----------------------
  W            Maju
  S            Mundur
  A            Kiri
  D            Kanan
  Q            Naik
  E            Turun
  Arrow Keys   Mengubah arah pandang

### Interaksi

  Tombol   Fungsi
  -------- -----------------------
  O        Buka / Tutup Wardrobe
  N        Mode Siang / Malam
  L        Lampu Plafon
  K        Lampu Tidur
  P        Power PC

### Fokus Kamera

  Tombol   Objek
  -------- -----------------
  1        Bed
  2        Table
  3        Window
  4        Wardrobe
  5        Door
  6        Poster
  7        Workstation
  8        Bookshelf
  9        Trash Bin
  0        Plant
  T        Air Conditioner
  C        Lampu Plafon
  J        Jam Digital

### Keluar Aplikasi

  Tombol       Fungsi
  ------------ -----------------
  ESC          Pause
  Klik Mouse   Keluar Aplikasi

------------------------------------------------------------------------

## Teknologi

-   Python
-   PyOpenGL
-   OpenGL (Fixed Function Pipeline)
-   GLUT
-   Visual Studio Code

------------------------------------------------------------------------

## Cara Menjalankan

1.  Install Python (minimal 3.x)

2.  Install dependency:

    ``` bash
    pip install PyOpenGL PyOpenGL_accelerate
    ```

3.  Jalankan aplikasi:

    ``` bash
    python main.py
    ```

------------------------------------------------------------------------

## Catatan

Project ini dibuat tanpa menggunakan asset 3D eksternal. Semua objek
dibangun secara procedural menggunakan primitive OpenGL untuk memperkuat
pemahaman dasar grafika komputer.

------------------------------------------------------------------------

## Author

Fachri Reyhan\
Komputer Grafik & Pengolahan Citra -- Semester 5
