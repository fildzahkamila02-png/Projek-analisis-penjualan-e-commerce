# 📊 Analisis Penjualan Toko Elektronik Online Indonesia 2025

Projek portofolio Data Analyst end-to-end: dari **data kotor** → cleaning → SQL → statistik & visualisasi Python → ringkasan Excel → laporan insight.

## Pertanyaan Bisnis
Kapan, di mana, dan produk apa yang paling menghasilkan omzet, agar strategi stok dan promosi 2026 lebih tepat?

## Temuan Utama
- **Nov–Des = 36,9% omzet setahun** (±2,9× rata-rata bulanan Jan–Okt).
- **Laptop + Smartphone = 58% omzet**, tapi hanya ±12% unit, Aksesoris menang volume.

## Alur & Skill yang Dipakai
| Tahap | Skill |
|---|---|
| Business understanding | Alur kerja analis data |
| Data cleaning | duplikat, missing, format, outlier |
| SQL | SELECT, JOIN, GROUP BY, HAVING |
| Statistik & visualisasi | mean/median/std/IQR, matplotlib |
| Excel | SUMIFS, COUNTIF, VLOOKUP, IFERROR |
| Dashboard & storytelling | KPI, layout, insight |

## Hasil Cleaning (`output/cleaning_log.txt`)
1.930 baris → **1.900 baris**: 30 duplikat dibuang, format tanggal & nama kota diseragamkan, 100 nilai kosong ditangani, 15 harga salah ketik, 8 pesanan grosir ditandai (tidak dihapus karena valid).

## Dashboard
https://datastudio.google.com/reporting/29b0754b-3377-42f3-a6ad-3fe7d4c54f95

