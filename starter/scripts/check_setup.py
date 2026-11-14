"""Read-only setup check utility for Day 06 Data Ingestion Engineering.

Verifies:
1. Python environment and core libraries (Docling, PyMuPDF, Qdrant Client, FlagEmbedding).
2. PyTorch & GPU / CUDA acceleration.
3. Qdrant Vector Database connectivity (Docker Server or Local Storage).
4. PDF Source file presence (NETFLIX_2023Q2_10Q-3-33.pdf).
"""
import sys
from pathlib import Path


def check_setup() -> None:
    print("=" * 65)
    print("🔍 CHECKING SETUP FOR DAY 06 DATA INGESTION ENGINEERING")
    print("=" * 65)

    # 1. Check Python version
    py_ver = f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
    print(f"🐍 Python Version: {py_ver}")
    if sys.version_info < (3, 10):
        print("⚠️ Warning: Python 3.10+ is recommended.")

    # 2. Check Core Libraries
    libs = [
        ("qdrant_client", "Qdrant Client"),
        ("FlagEmbedding", "FlagEmbedding (BGE-M3)"),
        ("transformers", "HuggingFace Transformers"),
        ("torch", "PyTorch"),
        ("docling", "Docling OCR"),
        ("fitz", "PyMuPDF"),
        ("dotenv", "python-dotenv"),
    ]
    all_libs_ok = True
    print("\n📦 Checking Required Libraries:")
    import importlib.util
    for mod_name, label in libs:
        spec = importlib.util.find_spec(mod_name)
        if spec is not None:
            print(f"  ✓ {label:<32} [INSTALLED]")
        else:
            print(f"  ✗ {label:<32} [MISSING] -> Run: pip install -r requirements.txt")
            all_libs_ok = False

    # 3. Check PyTorch & GPU
    print("\n⚡ Checking Acceleration & Compute:")
    try:
        import torch
        cuda_ok = torch.cuda.is_available()
        if cuda_ok:
            gpu_name = torch.cuda.get_device_name(0)
            vram_gb = torch.cuda.get_device_properties(0).total_memory / (1024**3)
            print(f"  ✓ CUDA GPU: {gpu_name} ({vram_gb:.2f} GB VRAM) [READY]")
        else:
            print("  ℹ️ CUDA not available. Pipeline will run on CPU.")
    except Exception as e:
        print(f"  ✗ Torch check error: {e}")

    # 4. Check Qdrant Connection
    print("\n🗄️ Checking Qdrant Vector Store:")
    try:
        from qdrant_client import QdrantClient
        # Try Docker server
        try:
            client = QdrantClient(url="http://localhost:6333", timeout=3)
            cols = [c.name for c in client.get_collections().collections]
            print(f"  ✓ Qdrant Docker Server: Connected at http://localhost:6333 [ONLINE]")
            print(f"    Existing collections: {cols if cols else 'None (ready to create)'}")
        except Exception:
            print("  ℹ️ Qdrant Docker server at http://localhost:6333 not reachable.")
            print("    Run 'docker compose up -d' or pipeline will use local disk mode.")
    except ImportError:
        print("  ✗ qdrant-client not installed.")

    # 5. Check PDF Source File
    print("\n📄 Checking Source Document:")
    base_dir = Path(__file__).resolve().parents[2]
    pdf_path = base_dir / "NETFLIX_2023Q2_10Q-3-33.pdf"
    if pdf_path.exists():
        size_kb = pdf_path.stat().st_size / 1024
        print(f"  ✓ Found: {pdf_path.name} ({size_kb:.1f} KB) [OK]")
    else:
        print(f"  ✗ Missing source PDF at: {pdf_path}")

    print("\n" + "=" * 65)
    if all_libs_ok:
        print("✅ SETUP READY: You can run: python -m starter.src.run")
    else:
        print("⚠️ Some dependencies missing. Please install: pip install -r requirements.txt")
    print("=" * 65)


if __name__ == "__main__":
    check_setup()
