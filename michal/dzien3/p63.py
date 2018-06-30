def html_text_mod (color_name = 'red', font_size = 13, text = 'content'):
    napis = ('<span style="color: %s; font-size: %s; “> %s </span>' %(color_name, font_size, text))
    print(napis)
    return napis

html_text_mod('blue', 24, 'piernik')