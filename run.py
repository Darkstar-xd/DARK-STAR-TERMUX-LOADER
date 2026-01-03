# run.py

import importlib.util

print("[*] Loader started")

path = "./obf-Da77.py"

spec = importlib.util.spec_from_file_location("x", path)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

print("[+] obf-Da77.py loaded via importlib")
