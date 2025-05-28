pemilih_list = []

def tambah_pemilih():
    id_pemilih = input ("Masukan ID pemilih")
    if any(p['id'] == id_pemilih for p in pemilih_list):
        print("id sudah terdaftar.")
        return
    nama = input ("Masukan Nama :")
    jurusan = input ("Masukan Jurusan")
    pemilih_list.append({
        'id' : id_pemilih,
        'nama' : nama,
        'jurusan' : jurusan,
        "sudah_memilih" : False
    })
    print ("Pemilih berhasil ditambahkan")