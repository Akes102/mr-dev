import speedtest

def check_speed():
    st = speedtest.speedtest()
    st.get_best_server()
    print("testing speed...")
    
    download = st.download() / 1_000_000
    upload = st.upload() / 1_000_000
    
    
    ping = st.results.ping
    
    return {
        "download": round(download, 2),
        "upload": round(upload, 2),
        "ping": round(ping, 2)
        }

speed = check_speed()

print(f"Download: {speed['download']} Mbps")
print(f"Upload: {speed['upload']} Mbps")
print(f"Ping: {speed['ping']} ms")
