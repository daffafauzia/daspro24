from data.pemilih import pemilih_list
from data.calon import calon_list

def tampilkan_statistik():
    total = len(pemilih_list)
    sudah = sum(1 for p in pemilih_list if p["sudah_memilih"])
    persentase = (sudah / total * 100) if total > 0 else 0
    calon_tertinggi = max(calon_list, key=lambda x: x["jumlah_suara"], default=None)

    print(f'Total Pemilih: {total}')
    print(f'Jumlah Sudah Memilih: {sudah}')
    print(f'Partisipasi: {persentase:.2f}%')
    if calon_tertinggi:
        print(f'Calon dengan suara terbanyak: {calon_tertinggi["nama"]} ({calon_tertinggi["jumlah_suara"]} suara)')

