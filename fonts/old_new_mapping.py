from pathlib import Path
from fontTools.ttLib import TTFont
woff1_path = Path(__file__).absolute().parent/"base64 (1).woff"
woff2_path = Path(__file__).absolute().parent/"base64 (2).woff"
font_1 = TTFont(woff1_path)
font_2 = TTFont(woff2_path)
font_old_order = font_1.getGlyphOrder()[2:]
font_new_order = font_2.getGlyphOrder()[2:]


def get_font_flags(font_glyphorder, font_ttf):
    f = {}
    for i in font_glyphorder:
        flags = font_ttf['glyf'][i]
        if "flags" in flags.__dict__:
            f[tuple(list(flags.flags))] = i
    return f


def comp(arr1, arr2):
    if len(arr1) != len(arr2):
        return 0
    for i in range(len(arr2)):
        if arr1[i] != arr2[i]:
            return 0
    return 1


def get_old_new_mapping():
    old, new = get_font_flags(font_glyphorder=font_old_order, font_ttf=font_1), get_font_flags(
        font_glyphorder=font_new_order, font_ttf=font_2)
    result_dict = {}
    for key1, value1 in old.items():
        for key2, value2 in new.items():
            if comp(key1, key2):
                result_dict[value1] = value2
    return result_dict


print(get_old_new_mapping())
