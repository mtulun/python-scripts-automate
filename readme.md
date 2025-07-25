# 🐳 Docker Image Sync Tool

Asenkron Docker image çekme ve opsiyonel olarak özel bir registry'ye gönderme işlemlerini gerçekleştiren bir komut satırı aracıdır. `asyncio` ve `rich` tabanlıdır. Çok sayıda imajı aynı anda indirerek, zaman kazanmak ve dağıtım süreçlerini hızlandırmak için geliştirilmiştir.

---

## 🎯 Amaç ve Kapsam

Bu araç, aşağıdaki ihtiyaçlara yönelik olarak geliştirilmiştir:

- Birden fazla Docker imajını aynı anda hızlı şekilde `docker pull` ile indirmek.
- Dilerseniz indirilen imajları, belirttiğiniz başka bir Docker registry'ye `docker push` ile göndermek.
- Terminalde işlem sırasında kullanıcıya **renkli, canlı** ve sürekli güncellenen bir tablo ile durumları göstermek.
- Her imaj için indirme, etiketleme ve gönderme hatalarını `error.log` dosyasına kaydetmek.

---

## 📦 Özellikler

| Özellik                       | Açıklama |
|-------------------------------|----------|
| ✅ Asenkron `pull` ve `push`   | Tüm imaj işlemleri eşzamanlı (asyncio) çalışır |
| 🎛 Maksimum paralel sınırı     | `--max-concurrent` ile işlem yoğunluğu kontrol edilebilir |
| 🖥 Canlı durum tablosu         | `rich` ile terminalde renkli ve güncel takip |
| 🧾 Loglama                     | Hatalar `error.log` dosyasına yazılır |
| ⚙️ Opsiyonel push desteği      | `--push` flag'i ile registry'ye gönderme yapılabilir |

---

## 🛠 Kurulum

```bash
git clone https://github.com/kullanici/docker-image-sync.git
cd docker-image-sync
pip install -r requirements.txt


Alternatif olarak sadece rich kütüphanesi yeterlidir:

pip install rich

📁 Girdi Formatı (images.txt)

Bir satıra bir imaj olacak şekilde yazılmalıdır:

nginx:1.25
alpine:3.20
python:3.11-slim
ghcr.io/example/repo:latest


🚀 Kullanım

1. Sadece image’ları çekmek (pull)

python docker_image_sync.py --image-list images.txt

2. Image’ları çek ve başka bir registry’ye gönder (push)

python docker_image_sync.py \
  --image-list images.txt \
  --push \
  --target-registry my.registry.com/myproject

Bu işlem sırasında her imaj şu şekilde gönderilir:
docker pull → docker tag → docker push
Yani nginx:1.25 → my.registry.com/myproject/nginx:1.25

3. Aynı anda çalışan işlem sayısını sınırla

python docker_image_sync.py \
  --image-list images.txt \
  --push \
  --target-registry my.registry.com/project \
  --max-concurrent 5


📊 Terminalde Durum Takibi

İşlem süresince terminalde şöyle bir tablo görürsünüz:

📦 Docker Image Sync Progress

[⏳ Waiting]    nginx:1.25
[✅ Done]       alpine:3.20
[❌ Error]      bad/image:tag      - pull failed: not found

🧾 Hataların Kaydedilmesi

Tüm hata mesajları error.log dosyasına yazılır. Örnek:

[ghcr.io/bad/image:latest] pull failed: manifest not found



























