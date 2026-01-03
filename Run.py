# Run.py
import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

try:
    import Da77   # loads Da77.cpython-312.so
except ImportError as e:
    print("❌ Failed to load Da77 module")
    print("🛑 Error:", e)
    sys.exit(1)

# ✅ ENTRY POINT
if hasattr(Da77, "run"):
    Da77.run()
else:
    print("❌ run() not found in Da77 module")
    print("Available attributes:")
    print(dir(Da77))
    
