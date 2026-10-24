# 📊 Analisis Penjualan Toko Elektronik Online Indonesia 2025

Projek portofolio Data Analyst end-to-end: dari **data kotor** → cleaning → SQL → statistik & visualisasi Python → ringkasan Excel → laporan insight.


🔗 **[Lihat Dashboard Interaktif di Looker Studio](https://datastudio.google.com/s/gNSsG2zwWBs)**

## Pertanyaan Bisnis
Kapan, di mana, dan produk apa yang paling menghasilkan omzet, agar strategi stok dan promosi 2026 lebih tepat?

## Temuan Utama
- **Nov–Des = 36,9% omzet setahun** (±2,9× rata-rata bulanan Jan–Okt).
- **Laptop + Smartphone = 58% omzet**, tapi hanya ±12% unit; Aksesoris menang volume.
- **Jakarta ±32% omzet**, hampir 1,5× kota kedua.
- Rata-rata transaksi ±Rp 2,2 jt vs **median ±Rp 0,6 jt** → distribusi miring kanan.

Detail lengkap: [`docs/laporan_insight.md`](docs/laporan_insight.md)

![tren](output/charts/01_tren_omzet_bulanan.png)
![kategori](output/charts/02_omzet_per_kategori.png)

## Alur & Skill yang Dipakai
| Tahap | File | Skill |
|---|---|---|
| Business understanding | README, laporan | Alur kerja analis data |
| Data cleaning | `src/01_cleaning.py` | duplikat, missing, format, outlier |
| SQL | `sql/analisis.sql`, `src/02_jalankan_sql.py` | SELECT, JOIN, GROUP BY, HAVING |
| Statistik & visualisasi | `src/03_eda_visualisasi.py` | mean/median/std/IQR, matplotlib |
| Excel | `src/04_buat_excel.py` → `output/xlsx/` | SUMIFS, COUNTIF, VLOOKUP, IFERROR |
| Dashboard & storytelling | `docs/panduan_looker_studio.md` | KPI, layout, insight |

## Hasil Cleaning (`output/cleaning_log.txt`)
1.930 baris → **1.900 baris**: 30 duplikat dibuang, format tanggal & nama kota diseragamkan, 100 nilai kosong ditangani, 15 harga salah ketik (×10) diperbaiki, 8 pesanan grosir ditandai (tidak dihapus karena valid).

## Cara Menjalankan
```bash
pip install -r requirements.txt
python src/run_all.py
```

## Struktur Folder
```
data/raw      data mentah (simulasi)
data/clean    data bersih
sql/          query SQL
src/          script Python
output/       grafik, hasil SQL, Excel, log
docs/         laporan, kamus data, panduan Looker Studio
```

## Dashboard
👉 **[Buka dashboard Looker Studio](https://datastudio.google.com/s/gNSsG2zwWBs)**

Berisi KPI (total omzet, jumlah transaksi, rata-rata transaksi), tren omzet, omzet per kategori & kota, dengan filter tanggal dan kota. Data sumber: `output/data_untuk_looker_studio.csv`; langkah pembuatan: `docs/panduan_looker_studio.md`.