# Run.py
import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

try:
    import Ds75   # loads Ds75.cpython-312.so
except ImportError as e:
    print("❌ Failed to load Ds75 module")
    print("📂 Make sure Ds75.cpython-312.so is in same folder")
    print("🛑 Error:", e)
    sys.exit(1)

# ENTRY POINT
if hasattr(Ds75, "main"):
    Ds75.main()
else:
    print("❌ main() not found in Ds75 module")
    print("Available attributes:")
    print(dir(Ds75))
