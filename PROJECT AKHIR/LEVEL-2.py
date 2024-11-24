class Siswa:
    def __init__(self, nama, umur, kelas, nilai):
        self.nama = nama  # Nama siswa
        self.umur = umur  # Umur siswa
        self.kelas = kelas  # Kelas siswa
        self.nilai = nilai  # Dictionary nilai mata pelajaran

    def hitung_rata_rata(self):
        """Menghitung rata-rata nilai dari semua mata pelajaran."""
        total_nilai = sum(self.nilai.values())
        jumlah_mapel = len(self.nilai)
        return total_nilai / jumlah_mapel if jumlah_mapel > 0 else 0

    def status_lulus(self):
        """Menentukan status kelulusan berdasarkan rata-rata nilai."""
        rata_rata = self.hitung_rata_rata()
        if rata_rata >= 75:
            return "Lulus"
        else:
            return "Tidak Lulus"

    def __str__(self):
        return f"{self.nama} (Umur: {self.umur}, Kelas: {self.kelas})"

class Sekolah:
    def __init__(self, nama_sekolah):
        self.nama_sekolah = nama_sekolah  # Nama sekolah
        self.siswa_list = []  # Daftar siswa yang terdaftar

    def tambah_siswa(self, siswa):
        """Menambahkan siswa baru ke dalam daftar."""
        self.siswa_list.append(siswa)

    def tampilkan_siswa(self):
        """Menampilkan semua data siswa yang terdaftar."""
        if not self.siswa_list:
            print("Tidak ada siswa terdaftar.")
        else:
            for siswa in self.siswa_list:
                print(siswa)

    def tampilkan_status_lulus(self):
        """Menampilkan status kelulusan setiap siswa."""
        for siswa in self.siswa_list:
            print(f"{siswa.nama}: {siswa.status_lulus()}")

    def rata_rata_kelas(self):
        """Menghitung rata-rata nilai semua siswa di sekolah."""
        total_rata_rata = sum([siswa.hitung_rata_rata() for siswa in self.siswa_list])
        jumlah_siswa = len(self.siswa_list)
        return total_rata_rata / jumlah_siswa if jumlah_siswa > 0 else 0

# Membuat objek Sekolah
sekolah = Sekolah("Sekolah Dasar Negeri 1")

# Menambahkan beberapa siswa
siswa1 = Siswa("Azzam", 12, "10.9A", {"Matematika": 80, "Bahasa Indonesia": 85, "IPA": 90})
siswa2 = Siswa("noble", 11, "10.6", {"Matematika": 60, "Bahasa Indonesia": 70, "IPA": 65})
siswa3 = Siswa("tono", 12, "10.10", {"Matematika": 90, "Bahasa Indonesia": 95, "IPA": 92})

# Menambahkan siswa ke sekolah
sekolah.tambah_siswa(siswa1)
sekolah.tambah_siswa(siswa2)
sekolah.tambah_siswa(siswa3)

# Menampilkan daftar siswa yang terdaftar
print("Daftar Siswa di", sekolah.nama_sekolah)
sekolah.tampilkan_siswa()

# Menampilkan status kelulusan siswa
print("\nStatus Kelulusan Siswa:")
sekolah.tampilkan_status_lulus()

# Menampilkan rata-rata nilai seluruh siswa
print("\nRata-rata nilai seluruh siswa di kelas:", sekolah.rata_rata_kelas())

