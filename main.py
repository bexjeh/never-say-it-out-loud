import os

LINE = "I'm only this quick because the sooner I answer, the sooner you go away."

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.getcwd()
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE + "\n")
