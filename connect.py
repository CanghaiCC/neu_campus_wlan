import subprocess

def connect_wifi(ssid):
    try:
        # 使用 netsh 命令连接指定的 Wi-Fi
        subprocess.run(["netsh", "wlan", "connect", f"name={ssid}"], check=True)
        print(f"Successfully connected to {ssid}")
    except subprocess.CalledProcessError:
        print(f"Failed to connect to {ssid}")

# 使用你的校园网 Wi-Fi 名称替换 NEU
connect_wifi("NEU")