# 🛡️ Mac Güvenlik Denetimi

macOS'un temel güvenlik ayarlarını tek komutla kontrol eden ve bir güvenlik puanı veren Python aracı.
Python ve siber güvenlik öğrenme yolculuğumun ikinci projesi.

## Neyi kontrol ediyor?

| Kontrol | Ne işe yarar |
|---|---|
| **FileVault** | Disk şifreleme: Mac çalınsa bile dosyalar okunamaz |
| **Gatekeeper** | Tanınmayan, imzasız uygulamaların çalışmasını engeller |
| **Güvenlik duvarı** | Ağdan gelen istenmeyen bağlantıları engeller |
| **SIP** | Sistem dosyalarını, yönetici yetkisiyle bile değiştirilmekten korur |

## Nasıl çalıştırılır

```bash
python3 denetim.py
```

## Örnek çıktı

```
FileVault: ✅
Gatekeeper: ✅
Güvenlik duvarı: ✅
SIP: ✅
Güvenlik puanı: 4/4
```

## Nasıl çalışıyor?

- `subprocess` ile macOS'un kendi komutlarını çalıştırır (`fdesetup`, `spctl`, `socketfilterfw`, `csrutil`)
- Her komutun çıktısını okuyup ayarın açık olup olmadığına karar verir
- Tek bir `kontrol_et()` fonksiyonu tüm kontrolleri yapar; yeni kontrol eklemek tek satır

## Bilinen sınırlamalar (v1)

- Sadece macOS'ta çalışır
- Çıktıyı belirli kelimeleri arayarak yorumlar; macOS komutlarının çıktı metni değişirse yanlış sonuç verebilir
- Sadece 4 temel kontrol yapıyor

## Sıradaki adımlar

- Daha fazla kontrol (otomatik güncellemeler, açık portlar, ekran kilidi)
- Raporu bir dosyaya kaydetme
- Kapalı ayarlar için nasıl açılacağını gösteren öneriler

## Kullandıklarım

Python · subprocess · fonksiyonlar · return · DRY prensibi

---
👤 **Batuhan Bahar** — Python & Siber Güvenlik öğreniyor
