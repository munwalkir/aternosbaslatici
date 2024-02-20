#Libraryler falan filan
import asyncio
from python_aternos.aterrors import ServerStartError
from python_aternos import Client
import os
import time

#Fonksiyonları tanımlama
atclient = Client()

#Giriş tokeni
txt = open('token.txt','r')
if os.stat('token.txt').st_size == 0:
    input("Token.txt dosyasının içine ATTERNOS_SESSION cookiesini atın. (Ctrl+Shift+I -> Application -> Cookies -> aternos.org -> ATERNOS_SESSION)")
token = txt.read()

#Giriş
atclient.login_with_session(token)

#atclientte yaptığımın aynısı
aternos = atclient.account

#Server listesi
serverlar = aternos.list_servers()

#Server seçme
#Birden çok sunucu varsa:
if len(serverlar)>1:
    x=0
    #Tüm sunucuları listeliyor.
    for servers in serverlar:
        servers.fetch()
        print(f'{x}-{servers.address}')
        x+=1
    #Basit bir seçim döngüsü. Yanlış cevap girilirse baştan başlayacak.
    sunucuSecimi=True
    while sunucuSecimi==True:
        secilen_sunucu = input("Bir sunucu seç (0,1,2,3 vb.): ")
        #Girilen değer sayı mı değil mi kontrolü
        if secilen_sunucu.isdigit():
            #Değeri integer'a dönüştürme (bilgisayar anlasın diye)
            secilen_sunucu = int(secilen_sunucu)
            #Girilen değer listede var mı kontrolü
            if 0<= secilen_sunucu <len(serverlar):
                #Aynısı
                secilen_sunucu = int(secilen_sunucu)
                #Döngü sonlandırma
                sunucuSecimi=False
            else:
                #Yoksa yeniden girdi isteme.
                print("Listede olan bir sayıyı gir.")
        else:
            #Değilse yeniden girdi isteme.
            print("Listede olan bir sayıyı gir.")
    if 0 <= secilen_sunucu < len(serverlar):
        secilen_server = serverlar[secilen_sunucu]
        #Terminal clear (YİNE)
        os.system('cls' if os.name == 'nt' else 'clear')
        #Sunucu seçimini uygulama
        server=secilen_server
    else:
        #Nolur nolmaz diye :P
        print("Geçersiz sunucu. Doğru bir sunucu seç.")
else:
    x=0
    #Tek sunucu varsa ilk sunucuyu seçer.
    server = serverlar[0]
    for servers in serverlar:
        servers.fetch()
        print(f'{x}-{servers.address}')
        x+=1
        secilen_server=serverlar[0]

#Server değiştirme fonksiyonu (async kullanmak için çok gencim)
def serverDegis():
    x=0
    os.system('cls' if os.name == 'nt' else 'clear')
    for servers in serverlar:
        servers.fetch()
        print(f'{x}-{servers.address}')
        x+=1
    sunucuSecimi=True
    while sunucuSecimi==True:
        secilen_sunucu = input("Bir sunucu seç (0,1,2,3 vb.): ")
        if secilen_sunucu.isdigit():
            secilen_sunucu = int(secilen_sunucu)
            if 0<= secilen_sunucu <len(serverlar):
                secilen_sunucu = int(secilen_sunucu)
                sunucuSecimi=False
            else:
                print("Listede olan bir sayıyı gir.")
    else:
        print("Listede olan bir sayıyı gir.")
    if 0 <= secilen_sunucu < len(serverlar):
        secilen_server = serverlar[secilen_sunucu]
        os.system('cls' if os.name == 'nt' else 'clear')
        return secilen_server
    else:
        print("Geçersiz sunucu. Doğru bir sunucu seç.")
 
cevap = False
    
#Server bilgilerini alma (bilgiler için lzm)
server.fetch()

#Menü:
cevap = False
#Cevap loopuna alma (program kapanmasın diye)
while cevap==False:
    inp = input(f'Seçilen sunucu: {secilen_server.address}\n1-Sunucuyu başlat\n2-Server Bilgileri\n3-Sunucu Değiştir\n')
    if inp.isdigit():
        if int(inp)==1:
            #Yine server fetch (bilgi güncellemesi için)
            server.fetch()
            #Terminal mesajlarını temizleme (maksat güzel gözüksün)
            os.system('cls' if os.name == 'nt' else 'clear')
            if server.status=="offline":
                #Sıra beklemeden başlatma fonskiyonu lol
                server.start(headstart=True,accepteula=True)
                print("Başlatılıyor.\n")
                time. sleep(5)
                inp = 0
            else:
                #Sunucu hazırlanıyor veya açık ise:
                print(f'Sunucu şu an şu durumda: {server.status}\n')
                inp = 0
                time. sleep(5)
        elif int(inp)==2:
            #Sürüm kontrolü (çünkü fetch'de server.edition yok)
            if server.is_java==False:
                surum="Bedrock"
            else:
                surum="Java"
            #Terminal clear
            os.system('cls' if os.name == 'nt' else 'clear')
            #Yine server fetch (bilgi güncellemesi için)
            server.fetch()
            #Bilgileri terminale aktarma
            print(f'Sunucu adresi: {server.address}\nSunucu durumu: {server.status}\nSürüm: {server.version}\nVersiyon: {surum}\nOyuncu sayısı: {server.slots}\nSunucuda olanlar: {server.players_list}\nRAM: {server.ram}\nYazılım: {server.software}\n')
            time. sleep(5)
            inp = 0
        elif int(inp)==3:
            secilen_server=serverDegis()
            server = secilen_server
            server.fetch()
            inp=0
        else:
            #1 veya 2 yazılmazsa:
            #Terminal clear
            os.system('cls' if os.name == 'nt' else 'clear')
            print('1,2 veya 3 yaz. (Girdi listede yok.)')
    else:
        #Direkt sayı yazılmazsa:
        #Terminal clear
        os.system('cls' if os.name == 'nt' else 'clear')
        print('1,2 veya 3 yaz (Girdi sayı değil.).')