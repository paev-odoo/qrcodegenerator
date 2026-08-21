from pathlib import Path
from platformdirs import user_downloads_dir
import qrcode

url = input("Enter the link: ")
filename = input("Enter the file name: ")

# Automatically detects system language & custom download paths
save_path = Path(user_downloads_dir()) / f"{filename}.png"

img = qrcode.make(url)
img.save(save_path)

print(f"QR code saved to: {save_path}")
