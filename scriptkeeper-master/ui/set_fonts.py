import dearpygui.dearpygui as dpg


# def second_font():
#     with dpg.font_registry():
#         code_font = dpg.add_font("static/fonts/Hack-Regular.ttf", 20)
#     return code_font


def set_font():
    with dpg.font_registry():
        with dpg.font("static/fonts/ofont.ru_Montserrat Alternates.ttf", 20, default_font=True, tag="Default font") as f:
            dpg.add_font_range_hint(dpg.mvFontRangeHint_Cyrillic)
            dpg.add_font_range_hint(dpg.mvFontRangeHint_Default)
            dpg.add_char_remap(0x00A8, 0x0401) # Ё
            dpg.add_char_remap(0x00B8, 0x0451) # ё

            # BIG LETTERS

            dpg.add_char_remap(0x00c0, 0x0410)
            dpg.add_char_remap(0x00c1, 0x0411)
            dpg.add_char_remap(0x00c2, 0x0412)
            dpg.add_char_remap(0x00c3, 0x0413)
            dpg.add_char_remap(0x00c4, 0x0414)
            dpg.add_char_remap(0x00c5, 0x0415)
            dpg.add_char_remap(0x00c6, 0x0416)
            dpg.add_char_remap(0x00c7, 0x0417)
            dpg.add_char_remap(0x00c8, 0x0418)
            dpg.add_char_remap(0x00c9, 0x0419)
            dpg.add_char_remap(0x00cA, 0x041a)
            dpg.add_char_remap(0x00cB, 0x041b)
            dpg.add_char_remap(0x00cC, 0x041c)
            dpg.add_char_remap(0x00cD, 0x041d)
            dpg.add_char_remap(0x00cE, 0x041e)
            dpg.add_char_remap(0x00cF, 0x041f)
            dpg.add_char_remap(0x00D0, 0x0420)
            dpg.add_char_remap(0x00D1, 0x0421)
            dpg.add_char_remap(0x00D2, 0x0422)
            dpg.add_char_remap(0x00D3, 0x0423)
            dpg.add_char_remap(0x00D4, 0x0424)
            dpg.add_char_remap(0x00D5, 0x0425)
            dpg.add_char_remap(0x00D6, 0x0426)
            dpg.add_char_remap(0x00D7, 0x0427)
            dpg.add_char_remap(0x00D8, 0x0428)
            dpg.add_char_remap(0x00D9, 0x0429)
            dpg.add_char_remap(0x00DA, 0x042a)
            dpg.add_char_remap(0x00DB, 0x042b)
            dpg.add_char_remap(0x00DC, 0x042c)
            dpg.add_char_remap(0x00DD, 0x042d)
            dpg.add_char_remap(0x00DE, 0x042e)
            dpg.add_char_remap(0X00DF, 0x042f)

            # small letters

            dpg.add_char_remap(0x00e0, 0x0430)
            dpg.add_char_remap(0x00e1, 0x0431)
            dpg.add_char_remap(0x00e2, 0x0432)
            dpg.add_char_remap(0x00e3, 0x0433)
            dpg.add_char_remap(0x00e4, 0x0434)
            dpg.add_char_remap(0x00e5, 0x0435)
            dpg.add_char_remap(0x00e6, 0x0436)
            dpg.add_char_remap(0x00e7, 0x0437)
            dpg.add_char_remap(0x00e8, 0x0438)
            dpg.add_char_remap(0x00e9, 0x0439)
            dpg.add_char_remap(0x00ea, 0x043a)
            dpg.add_char_remap(0x00eb, 0x043b)
            dpg.add_char_remap(0x00ec, 0x043c)
            dpg.add_char_remap(0x00ed, 0x043d)
            dpg.add_char_remap(0x00ee, 0x043e)
            dpg.add_char_remap(0x00ef, 0x043f)
            dpg.add_char_remap(0x00f0, 0x0440)
            dpg.add_char_remap(0x00f1, 0x0441)
            dpg.add_char_remap(0x00f2, 0x0442)
            dpg.add_char_remap(0x00f3, 0x0443)
            dpg.add_char_remap(0x00f4, 0x0444)
            dpg.add_char_remap(0x00f5, 0x0445)
            dpg.add_char_remap(0x00f6, 0x0446)
            dpg.add_char_remap(0x00f7, 0x0447)
            dpg.add_char_remap(0x00f8, 0x0448)
            dpg.add_char_remap(0x00f9, 0x0449)
            dpg.add_char_remap(0x00fa, 0x044a)
            dpg.add_char_remap(0x00fb, 0x044b)
            dpg.add_char_remap(0x00fc, 0x044c)
            dpg.add_char_remap(0x00fd, 0x044d)
            dpg.add_char_remap(0x00fe, 0x044e)
            dpg.add_char_remap(0x00ff, 0x044f)
        code_font = dpg.add_font("static/fonts/Hack-Regular.ttf", 20)

    dpg.bind_font("Default font")
    return code_font

