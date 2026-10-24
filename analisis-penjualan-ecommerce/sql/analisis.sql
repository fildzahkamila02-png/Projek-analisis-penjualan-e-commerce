-- Tabel: transaksi (data bersih), produk
-- Tiap query diawali penanda nama, lalu dijalankan oleh src/02_jalankan_sql.py

-- Q: 01_ringkasan
SELECT COUNT(*) AS jumlah_transaksi,
       SUM(Total) AS total_omzet,
       ROUND(AVG(Total)) AS rata_rata_transaksi
FROM transaksi;

-- Q: 02_omzet_per_bulan
SELECT Bulan, COUNT(*) AS jumlah_transaksi, SUM(Total) AS omzet
FROM transaksi
GROUP BY Bulan
ORDER BY Bulan;

-- Q: 03_omzet_per_kategori
SELECT p.Kategori, SUM(t.Qty) AS unit_terjual, SUM(t.Total) AS omzet
FROM transaksi t
JOIN produk p ON t.ID_Produk = p.ID_Produk
GROUP BY p.Kategori
ORDER BY omzet DESC;

-- Q: 04_top5_produk
SELECT p.Nama_Produk, SUM(t.Qty) AS unit_terjual, SUM(t.Total) AS omzet
FROM transaksi t
JOIN produk p ON t.ID_Produk = p.ID_Produk
GROUP BY p.Nama_Produk
ORDER BY omzet DESC
LIMIT 5;

-- Q: 05_omzet_per_kota
SELECT Kota, COUNT(*) AS jumlah_transaksi, SUM(Total) AS omzet
FROM transaksi
GROUP BY Kota
ORDER BY omzet DESC;

-- Q: 06_metode_bayar
SELECT Metode_Bayar, COUNT(*) AS jumlah_transaksi,
       ROUND(100.0 * COUNT(*) / (SELECT COUNT(*) FROM transaksi), 1) AS persen
FROM transaksi
GROUP BY Metode_Bayar
ORDER BY jumlah_transaksi DESC;

-- Q: 07_kota_omzet_tinggi (HAVING: rata-rata omzet per bulan > 50 juta)
SELECT Kota, ROUND(SUM(Total) / 12.0) AS rata_omzet_per_bulan
FROM transaksi
GROUP BY Kota
HAVING rata_omzet_per_bulan > 50000000
ORDER BY rata_omzet_per_bulan DESC;

-- Q: 08_pesanan_grosir
SELECT t.ID_Transaksi, t.Tanggal, p.Nama_Produk, t.Qty, t.Total
FROM transaksi t
JOIN produk p ON t.ID_Produk = p.ID_Produk
WHERE t.Grosir = 1
ORDER BY t.Total DESC;
