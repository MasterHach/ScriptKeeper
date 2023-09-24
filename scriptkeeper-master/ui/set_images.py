import dearpygui.dearpygui as dpg


def set_images():
    w, h, ch, data = dpg.load_image("static/images/copy.png")
    with dpg.texture_registry():
        dpg.add_static_texture(width=w, height=h, default_value=data, tag="texture_tag")