# Kamus Data

**transaksi_clean.csv**
| Kolom | Arti |
|---|---|
| ID_Transaksi | ID unik transaksi |
| Tanggal | Tanggal transaksi (YYYY-MM-DD) |
| ID_Produk | Kunci ke tabel produk |
| Kota | Kota pembeli (rapi; "Tidak diketahui" jika kosong) |
| Qty | Jumlah unit |
| Harga | Harga satuan (Rp) |
| Metode_Bayar | Transfer / E-Wallet / COD / Kartu Kredit / Tidak diketahui |
| Grosir | True jika Qty ≥ 50 |
| Total | Qty × Harga |
| Bulan | Format YYYY-MM |

**produk.csv**: ID_Produk, Nama_Produk, Kategori, Harga_Dasar.
