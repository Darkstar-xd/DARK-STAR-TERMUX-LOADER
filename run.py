import importlib.util

print("[*] Loader started")

path = "./obf-Da77.py"

spec = importlib.util.spec_from_file_location("obf_mod", path)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

print("[+] obf-Da77.py loaded")

# Agar aap file ke andar ka 'execute' function chalana chahte hain:
if hasattr(mod, '_cube'):
    print("[*] Executing _cube logic...")
    mod._cube.execute(code=mod.__code__)
