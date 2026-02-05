import os
import shutil
from charset_normalizer import from_path

def convert_and_copy(src_dir):
    src_dir = os.path.abspath(src_dir)

    if not os.path.isdir(src_dir):
        print("❌ 输入的路径不是有效目录")
        return

    parent_dir = os.path.dirname(src_dir)
    output_dir = os.path.join(parent_dir, "output_utf8")

    os.makedirs(output_dir, exist_ok=True)

    print(f"\n📂 输入目录 : {src_dir}")
    print(f"📁 输出目录 : {output_dir}\n")

    for dirpath, dirnames, filenames in os.walk(src_dir):
        # 计算相对路径，用于复刻目录结构
        rel_path = os.path.relpath(dirpath, src_dir)
        out_dir = os.path.join(output_dir, rel_path)
        os.makedirs(out_dir, exist_ok=True)

        for name in filenames:
            src_file = os.path.join(dirpath, name)
            dst_file = os.path.join(out_dir, name)

            try:
                # ---- 情况 1：txt 文件 → 转 UTF-8 ----
                if name.lower().endswith(".txt"):
                    match = from_path(src_file).best()
                    if match is None:
                        print(f"[跳过 txt] 无法识别编码: {src_file}")
                        continue

                    text = match.output()
                    if isinstance(text, bytes):
                        text = text.decode("utf-8", errors="replace")

                    with open(dst_file, "w", encoding="utf-8", newline="") as f:
                        f.write(text)

                    print(f"[TXT] {src_file} ({match.encoding} → utf-8)")

                # ---- 情况 2：非 txt 文件 → 原样复制 ----
                else:
                    shutil.copy2(src_file, dst_file)
                    print(f"[COPY] {src_file}")

            except Exception as e:
                print(f"[失败] {src_file}: {e}")


if __name__ == "__main__":
    input_dir = input("请输入 input 文件夹路径: ").strip()
    convert_and_copy(input_dir)
