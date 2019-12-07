from pathlib import Path
from fontTools.ttLib import TTFont
woff_path = Path(__file__).absolute().parent/"base64 (1).woff"
font = TTFont(woff_path)
font_names = font.getGlyphOrder()
font_str = [
    "8", "验", "杨", "女", "3", "届", "7", "男", "高", "赵", "6", "2", "下", "以", "技", "黄", "周", 
    "4", "经", "专", "硕", "刘", "吴", "陈", "士", "E", "5", "中", "博", "1", "科", "大", "9", "本",
     "王", "B", "无", "李", "应", "生", "校", "A", "0", "张","M"
]
print(dict(zip(font_names[2:],font_str)))
