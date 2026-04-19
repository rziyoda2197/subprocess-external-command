import subprocess

def ishga_tushirish():
    try:
        natija = subprocess.run(['ls', '-la'], capture_output=True, text=True)
        return natija.stdout
    except Exception as e:
        return f"Xatolik: {e}"

print(ishga_tushirish())
