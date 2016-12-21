from app import app as python_simplex
import os

if __name__ == "__main__":
    port = os.environ.get("PORT", 9090)
    python_simplex.run(host='0.0.0.0', port=port)