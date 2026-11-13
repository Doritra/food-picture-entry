import os
import shutil

src = os.path.join(os.path.dirname(__file__), "entry.png")
output_dir = os.getenv("MAKEFUN_OUTPUT_DIR", "/output")

os.makedirs(output_dir, exist_ok=True)
shutil.copyfile(src, os.path.join(output_dir, "entry.png"))
