from pathlib import Path
from fontTools.ttLib import TTFont
font1_path = Path(__file__).absolute().parent/"maoyan_1.xml"
font2_path = Path(__file__).absolute().parent/"maoyan_2.xml"
woff1_path = Path(__file__).absolute().parent/"maoyan_1.woff"
woff2_path = Path(__file__).absolute().parent/"maoyan_2.woff"
font_1 = TTFont(woff1_path)
font_2 = TTFont(woff2_path)
font_1.saveXML(font1_path)
font_2.saveXML(font2_path)
