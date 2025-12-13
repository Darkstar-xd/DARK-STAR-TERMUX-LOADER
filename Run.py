# run.py
# Universal public loader for protected Cython module

import os
import sys

# 📁 current script directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# add current directory to python path
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

try:
    import Ds75   # Ds75.so must be in same folder
except ImportError as e:
    print("❌ Failed to load protected core module (Ds75.so)")
    print("📂 Make sure Ds75.so is in the same directory as run.py")
    print("🛑 Error:", e)
    exit(1)

# 🔒 ENTRY POINT
if hasattr(Ds75, "main"):
    Ds75.main()
else:
    print("❌ Entry point 'main()' not found in Ds75.so")
    print("Available attributes:", dir(Ds75))
