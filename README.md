
# Akıllı Şehir IoT ve Veri Analiz Platformu

Bu proje, BLM3522 Bulut Bilişim dersi kapsamında geliştirilmiş, uçtan uca güvenli bir **IoT (Nesnelerin İnterneti)** mimarisidir. Proje; sanal sensör düğümlerinden gelen verilerin **MQTT protokolü** ile buluta aktarılmasını, **AWS IoT Core** üzerinden güvenli bir şekilde yönetilmesini ve **Streamlit** ile gerçek zamanlı görselleştirilmesini hedeflemektedir.

## Proje Mimarisi
Sistem, üç temel katmandan oluşmaktadır:
1. **Veri Üretim Katmanı (Publisher):** Python tabanlı sanal sensör düğümü.
2. **Mesajlaşma Katmanı (Broker):** AWS IoT Core (MQTT Broker, X.509 Sertifika tabanlı güvenlik).
3. **Analiz ve Görselleştirme Katmanı (Subscriber):** Streamlit dashboard.

## Kullanılan Teknolojiler
* **Programlama Dili:** Python
* **Bulut Platformu:** AWS IoT Core
* **Protokol:** MQTT (Message Queuing Telemetry Transport)
* **Görselleştirme:** Streamlit
* **Güvenlik:** TLS/SSL (x.509 Sertifikaları), IAM Policies

## Kurulum ve Çalıştırma

### 1. Ön Gereksinimler
* Python 3.x kurulu olmalıdır.
* Bir AWS Hesabı ve AWS IoT Core üzerinde yapılandırılmış bir "Thing" (Nesne).
* AWS'den indirilen sertifikalar (`.pem.crt`, `private.pem.key`, `AmazonRootCA1.pem`).

### 2. Bağımlılıkların Kurulması
```bash
pip install paho-mqtt streamlit pandas
```
----------------------------------------------
### Video Link:
