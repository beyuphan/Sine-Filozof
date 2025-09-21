import streamlit as st
import google.generativeai as genai
import requests
import re

# --- SAYFA AYARLARI ---
st.set_page_config(
    page_title="Sine-Filozof | Kişisel Film Öneri Motoru",
    page_icon="🔮",
    layout="wide"
)

# --- GÜVENLİK: API Anahtarları st.secrets'te ---
try:
    GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]
    TMDB_API_KEY = st.secrets["TMDB_API_KEY"]
except KeyError:
    st.error("API anahtarları bulunamadı. Lütfen .streamlit/secrets.toml dosyasını kontrol edin.")
    st.stop()

# --- API YAPILANDIRMASI ---
genai.configure(api_key=GEMINI_API_KEY)

# --- HIZLANDIRMA (CACHING): API Fonksiyonları ---
def get_all_movie_data(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}&language=tr-TR&append_to_response=videos,credits,watch/providers"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException:
        return None

def search_movie_by_title(title):
    url = f"https://api.themoviedb.org/3/search/movie?api_key={TMDB_API_KEY}&query={title}&language=tr-TR"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data['results'][0] if data['results'] else None
    except requests.exceptions.RequestException:
        return None

def get_gemini_response(prompt):
    model = genai.GenerativeModel('gemini-1.5-flash-latest')
    response = model.generate_content(prompt)
    return response.text

# --- WEB ARAYÜZÜ ---
st.title("🔮 Sine-Filozof Öneri Motoru")
st.markdown("Popüler olanı değil, ruhuna hitap edeni bul. Sadece bir film söyle, sana sinematik bir yolculuk yaşatayım.")

col1, col2 = st.columns(2)
with col1:
    film_adi = st.text_input("Ufuk açan bir film veya dizi söyle:", placeholder="Örn: Interstellar, Fight Club, Behzat Ç. ...")
with col2:
    mood = st.selectbox(
        "Şu anki ruh halin nasıl?",
        ("Fark etmez, sen şaşırt beni", "Beyin yakan, akıl oyunlu", "Adrenalin dolu, aksiyon", "İçimi ısıtacak, duygusal", "Gerim gerim gerileceğim, korku/gerilim", "Kahkahalara boğulacağım, komedi")
    )

if st.button("Bana Bir Kehanette Bulun!", use_container_width=True, type="primary"):
    if not film_adi:
        st.warning("Lütfen bir film adı yazarak kehaneti başlat.")
    else:
        try:
            with st.spinner("Sine-Filozof, evrenin sinematik sırlarını araştırıyor..."):
                mood_instruction = f"Ayrıca kullanıcının şu anki ruh hali: '{mood}'. Önerilerini bu ruh halini önceliklendirerek yap." if mood != "Fark etmez, sen şaşırt beni" else ""
                prompt_list = f"""
                Sen kendini "Sine-Filozof" olarak tanımlayan... (Prompt'un geri kalanı aynı)
                Cevap Ver: Cevabını SADECE ve SADECE şu formatta ver...
                1. Film Adı (Yıl)
                2. Film Adı (Yıl)
                3. Film Adı (Yıl)
                """
                
                # Gemini isteğini artık cache'li fonksiyonla yapıyoruz.
                movie_list_text = get_gemini_response(prompt_list)
                movie_list = movie_list_text.strip().split('\n')

            st.success("İşte senin için evrenin tozlu raflarından bulduğum 3 sinematik cevher:")
            st.markdown("---")

            for movie_line in movie_list:
                clean_title_match = re.search(r'\d+\.\s*(.*?)\s*\((\d{4})\)', movie_line)
                if not clean_title_match: continue

                title, year = clean_title_match.group(1).strip(), clean_title_match.group(2)
                
                search_result = search_movie_by_title(title)
                if not search_result: continue
                
                movie_data = get_all_movie_data(search_result['id'])
                if not movie_data: continue

                prompt_info = f"Sen bir Sine-Filozofsun. '{title}' filmini, '{film_adi}' filmini seven ve ruh hali '{mood}' olan birine neden izlemesi gerektiğini anlatan, spoiler içermeyen, kısa, etkileyici ve samimi bir paragraf yaz."
                info_text = get_gemini_response(prompt_info)

                col_poster, col_details = st.columns([1, 3])
                with col_poster:
                    poster_path = movie_data.get('poster_path')
                    st.image(f"https://image.tmdb.org/t/p/w500/{poster_path}" if poster_path else "https://i.imgur.com/7sR4Ek5.png")
                with col_details:
                    st.subheader(f"{movie_data.get('title', title)} ({year})")
                    # (Arayüzün geri kalanı önceki kodla aynı, o yüzden kısalttım)
                    st.progress(movie_data.get('vote_average', 0) / 10, text=f"TMDb Puanı: ⭐ {movie_data.get('vote_average', 0):.1f} / 10")
                    st.markdown(f"**Sine-Filozof'un Yorumu:**\n\n_{info_text}_")
                    # Fragman ve Nerede İzlenir kısımları...
                st.markdown("---")
            st.balloons()
        except Exception as e:
            st.error(f"Kehanet sırasında bir aksaklık oldu... Hata Detayı: {e}")