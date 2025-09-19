🔮 Sine-Filozof: Yapay Zeka Destekli Film Öneri Motoru

Popüler olanı değil, ruhuna hitap edeni bul. Bu web uygulaması, Google Gemini'nin yaratıcı zekasını ve The Movie Database'in (TMDb) zengin veri tabanını kullanarak size kişiselleştirilmiş ve sıra dışı film önerileri sunar.


✨ Özellikler

    Derin Yapay Zeka Analizi: Sadece benzer türleri değil, bir filmin ruhunu, temasını ve atmosferini analiz ederek öneriler sunar.

    Ruh Haline Göre Filtreleme: O anki modunuza en uygun filmi bulmanıza yardımcı olur ("Beyin Yakan", "İçimi Isıtacak", "Adrenalin Dolu" vb.).

    Zengin Film Detayları: Önerilen her film için TMDb'den alınan zengin veriler:

        Yüksek çözünürlüklü afişler

        Yönetmen ve oyuncu kadrosu

        TMDb puanı

    Anında Fragman İzleme: Uygulamadan ayrılmadan, önerilen filmlerin fragmanlarını izleyin.

    "Nerede İzlenir?" Servisi: Filmin Türkiye'deki hangi streaming platformlarında (Netflix, Prime Video vb.) olduğunu gösterir.

    Akıllı Önbellekleme (Caching): API'leri verimli kullanmak ve hızlı bir deneyim sunmak için sonuçları önbelleğe alır.

    Güvenli API Anahtarı Yönetimi: st.secrets ile API anahtarları koddan ayrı, güvenli bir şekilde saklanır.

🛠️ Kullanılan Teknolojiler

    Backend: Python

    Web Arayüzü: Streamlit

    Yapay Zeka Modeli: Google Gemini 1.5 Flash

    Film Veri Tabanı: The Movie Database (TMDb) API

    Web İstekleri: Requests

⚙️ Kurulum ve Çalıştırma

Bu projeyi kendi bilgisayarınızda çalıştırmak için aşağıdaki adımları izleyin:

1. Projeyi Klonlayın:
Bash

git clone https://github.com/kullanici-adiniz/sine-filozof.git
cd sine-filozof

2. Gerekli Kütüphaneleri Yükleyin:
(Sanal bir ortam (virtual environment) kullanmanız tavsiye edilir.)
Bash

pip install -r requirements.txt

3. API Anahtarlarını Ayarlayın:
Proje ana dizininde .streamlit adında bir klasör oluşturun. Bu klasörün içine secrets.toml adında bir dosya oluşturun ve API anahtarlarınızı aşağıdaki formatta içine yapıştırın:
Ini, TOML

# .streamlit/secrets.toml

GEMINI_API_KEY = "SENIN_GEMINI_API_ANAHTARINI_BURAYA_YAPISTIR"
TMDB_API_KEY = "SENIN_TMDB_API_ANAHTARINI_BURAYA_YAPISTIR"

4. Uygulamayı Başlatın:
Bash

streamlit run app.py

Uygulama otomatik olarak tarayıcınızda açılacaktır.

Bu proje, yapay zeka ve web geliştirme yeteneklerini bir araya getiren eğlenceli ve öğretici bir yolculuğun ürünüdür. Keyfini çıkarın!
