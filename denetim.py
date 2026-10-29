import subprocess

def komut_calistir(komut):
    sonuc = subprocess.run(komut, capture_output=True, text=True)
    return sonuc.stdout.strip()

def kontrol_et(isim, komut, aranan):
    cikti = komut_calistir(komut) 
    if aranan in cikti:
        print(f"{isim}: ✅")
        return True
    else:
        print(f"{isim}: ❌")
        return False
puan = 0
if kontrol_et("FileVault", ["fdesetup", "status"], "On"):
    puan = puan + 1
if kontrol_et("Gatekeeper", ["spctl", "--status"], "enabled"):
    puan = puan + 1
if kontrol_et("Güvenlik duvarı", ["/usr/libexec/ApplicationFirewall/socketfilterfw", "--getglobalstate"], "enabled"):
    puan = puan + 1
if kontrol_et("SIP", ["csrutil", "status"], "enabled"):
    puan = puan + 1 
print(f"Güvenlik puanı: {puan}/4")