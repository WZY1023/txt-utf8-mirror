
# txt-to-utf8-batch

一个简单可靠的 Python 工具，用于**递归处理目录中的文本文件**：

- 自动识别 `.txt` 文件编码并转换为 **UTF-8**
- 非 `.txt` 文件 **原样复制**
- 保持原有目录结构
- **不修改原目录内容**

适合用于数据清洗、日志归档、NAS 文件整理等场景。

---

## 功能特性

- ✅ 递归遍历多层目录
- ✅ 仅对 `.txt` 文件进行编码转换
- ✅ 自动识别原始编码（GBK / UTF-16 / Big5 / Latin-1 等）
- ✅ 统一输出为 UTF-8（无 BOM）
- ✅ 其他文件二进制安全复制
- ✅ 输出目录自动创建，原目录不受影响

---

## 依赖

- Python ≥ 3.8
- [charset-normalizer](https://github.com/Ousret/charset_normalizer)

安装依赖：

```bash
pip install charset-normalizer
````

---

## 使用方法

运行脚本：

```bash
python convert.py
```

按提示输入源目录路径，例如：

```text
请输入 input 文件夹路径: /path/to/input
```

程序会在**同级目录**自动创建：

```text
output_utf8/
```

并将处理结果输出其中。

---

## 行为说明

* `.txt` 文件：
  自动检测编码 → 转换为 UTF-8 → 写入输出目录
* 非 `.txt` 文件：
  原样复制（保留文件属性）
* 目录结构：
  与输入目录完全一致

---

## 示例

输入目录：

```text
input/
├── a.txt        (GBK)
├── image.png
└── sub/
    └── b.txt    (UTF-16)
```

输出目录：

```text
output_utf8/
├── a.txt        (UTF-8)
├── image.png
└── sub/
    └── b.txt    (UTF-8)
```

---

## 注意事项

* 请不要将 `output_utf8` 放在 `input` 目录内部
* 若文本本身编码已损坏，可能仍会出现替换字符 `�`

---
