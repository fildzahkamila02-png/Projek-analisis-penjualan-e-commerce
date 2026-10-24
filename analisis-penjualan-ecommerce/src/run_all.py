import subprocess, sys
for f in ["00_buat_data_simulasi", "01_cleaning", "02_jalankan_sql", "03_eda_visualisasi", "04_buat_excel"]:
    print(f"\n>>> {f}")
    subprocess.run([sys.executable, f"src/{f}.py"], check=True)
