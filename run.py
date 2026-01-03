import os
import sys

# File path
path = "./obf-Da77.py"

print("[*] DARK-STAR Loader started")

if os.path.exists(path):
    try:
        # Obfuscated file ko read karein
        with open(path, "r", encoding="utf-8") as f:
            source_code = f.read()
        
        print("[+] Tool loaded into memory...")

        # Environment setup: Taki obfuscated code ko lage wo direct chal raha hai
        namespace = {
            "__name__": "__main__",
            "__file__": os.path.abspath(path),
            "__package__": None,
        }
        
        # Execute the obfuscated code
        exec(source_code, namespace)

    except KeyboardInterrupt:
        print("\n[!] Stopped by user.")
    except Exception as e:
        print(f"[-] Error: {e}")
else:
    print(f"[-] File {path} not found!")
