from pathlib import Path
import qrcode

url = input("Enter the link: ")
filename = input("Enter the file name: ")

# Save directly to the user's Downloads folder
downloads_folder = Path.home() / "Downloads"
save_path = downloads_folder / f"{filename}.png"

img = qrcode.make(url)
img.save(save_path)

print(f"QR code saved to: {save_path}")
