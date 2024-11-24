# level-1 project
class player:
    tempCount = 0
    def _init_(self, nama, senjata, armor): # ini perlengkapan
        self.nama = nama
        self.senjata = senjata
        self.armor = armor
    def display( self ):
        print(f"Nama Player : {self.nama}")
        print(f"Nama senjata : {self.senjata}")
        print(f"Nama armor : {self.armor}")
    def gantiNama( self, newNama ):
        self.nama = newNama
        
        player.tempCount += 1
        pass

class perlengkapan:
    def _init_(self, na_perlengkapan):
        self, na_perlengkapan= na_perlengkapan
        
senjata =perlengkapan ("pistol")
armor = perlengkapan("baja")
nama = perlengkapan("medkit")

newPlayer1 = player( "azzam", "noble", "rasya" ) # yes
print(f"Nama Player 1 : {newPlayer1.nama}")
newPlayer1.display()
newPlayer1.gantiNama( "kata" )
newPlayer2 = player("rafi", "algi", "nita")
newPlayer2.display()
    
print(f"JUmlah Objek : {player.tempCount}")