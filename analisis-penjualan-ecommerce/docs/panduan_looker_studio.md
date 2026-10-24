# Membuat Dashboard di Looker Studio (Materi 7)

1. Buka <https://lookerstudio.google.com> → **Create → Report**.
2. **Add data → File Upload** → pilih `output/data_untuk_looker_studio.csv`.
3. Pastikan tipe kolom: `Tanggal` = Date, `Total`/`Harga` = Number (Currency IDR).
4. Susun layout (sesuai Materi 7):
   - **Atas – KPI (Scorecard):** Total omzet (SUM Total), Jumlah transaksi (COUNT ID_Transaksi), Rata-rata transaksi (AVG Total).
   - **Tengah – Time series:** dimensi `Tanggal`, metrik `Total` → tren omzet.
   - **Bawah kiri – Bar chart:** dimensi `Kategori`, metrik `Total`.
   - **Bawah kanan – Bar chart:** dimensi `Kota`, metrik `Total`.
   - **Tabel:** `Nama produk`/`Kategori` + omzet.
5. Tambahkan **filter**: Date range control + Drop-down `Kota`.
6. Beri judul jelas dan satu warna utama (konsisten). Hindari 3D & terlalu banyak warna.
7. **Share → Get report link**, lalu tempel link di README bagian *Dashboard*.
