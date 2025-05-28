from modul import pemilih, calon

def tampilkan_statistik():
    total_pemilih = len(pemilih.pemilih_list)
    sudah_memilih = sum(1 for p in pemilih.pemilih_list if p["sudah_memilih"])
    persentase = (sudah_memilih / total_pemilih * 100) if total_pemilih > 0 else 0

    if calon.calon_list:
        suara_terbanyak = max(calon.calon_list, key=lambda c: c['jumlah_suara'])
        nama_terbanyak = suara_terbanyak['nama']
    else:
        nama_terbanyak = "Belum ada calon"

    print("\n===== Statistik Pemilu ======")
    print(f"Total Pemilih: {total_pemilih}")
    print(f"Jumlah Sudah Memilih: {sudah_memilih}")
    print(f"Persentase Partisipasi: {persentase:.2f}%")
    print(f"Calon Teratas: {nama_terbanyak}")
   