import dearpygui.dearpygui as dpg
from database.db_requests import add_new_script_to_favorite
from database.db_requests import delete_script_from_favorites
from database.db_requests import delete_script_from_general


def button_add_to_favors_callback(user_data):
    #print(user_data)
    add_new_script_to_favorite(int(user_data.split()[1]))


def button_delete_favor_callback(user_data):
    #print(user_data)
    delete_script_from_favorites(int(user_data.split()[1]))
    dpg.delete_item(f'{user_data.split()[0]} {user_data.split()[1]} header')


def button_delete_general_callback(user_data):
    dpg.configure_item("popup_delete_gen", show=True)
    #dpg.set_value("MyBestSmeck", user_data)
    dpg.set_value("super_button", user_data)
    dpg.configure_item("super_button", user_data=user_data)


def lol(sender, user_data, app_data):
    #print(sender, user_data, app_data)
    delete_script_from_general(int(app_data.split()[1]))
    dpg.delete_item(f'{app_data.split()[0]} {app_data.split()[1]} header_g')
    dpg.configure_item("popup_delete_gen", show=False)


def button_copy_callback(user_data):
    user_data = user_data.split()
    this_tag = f'{user_data[0]} {user_data[1]} script'
    text = dpg.get_value(this_tag)
    dpg.set_clipboard_text(text)


def load_general_scripts(scripts_to_load, code_font):
    for elem in scripts_to_load:
        unique_tag = dpg.generate_uuid()
        #print(unique_tag)
        with dpg.collapsing_header(label=elem[1], parent='text_header_search',
                                    tag=f'{unique_tag} {elem[0]} header_g', filter_key=f'{elem[1]} {elem[2]}'):
            if elem[4] == 2:
                with dpg.theme() as item_theme:
                    with dpg.theme_component(dpg.mvAll):
                        dpg.add_theme_color(dpg.mvThemeCol_Header, (152, 251, 152), category=dpg.mvThemeCat_Core)

                dpg.bind_item_theme(f'{unique_tag} {elem[0]} header_g', item_theme)
            with dpg.group(horizontal=True):
                dpg.add_text(elem[2], wrap=500, bullet=True)
                dpg.add_button(label=f"Add to favor {elem[0]}", callback=button_add_to_favors_callback
                               , tag=f'{unique_tag} {elem[0]} add_button')
                dpg.add_button(label=f"Delete from general {elem[0]}",
                               callback=button_delete_general_callback
                               , tag=f'{unique_tag} {elem[0]} del_button_g')
            dpg.add_input_text(default_value=elem[3], multiline=True, readonly=True,
                               height=300, tag=f'{unique_tag} {elem[0]} script_g')
            dpg.bind_item_font(f'{unique_tag} {elem[0]} script_g', code_font)


def load_favorite_scripts(scripts_to_load, code_font):
    for i in scripts_to_load:
        unique_tag = dpg.generate_uuid()
        with dpg.collapsing_header(tag=f'{unique_tag} {i[0]} header', label=i[5], parent="favorite_group"):
            if i[3] == 2:
                with dpg.theme() as item_theme:
                    with dpg.theme_component(dpg.mvAll):
                        dpg.add_theme_color(dpg.mvThemeCol_Header, (152, 251, 152), category=dpg.mvThemeCat_Core)

                dpg.bind_item_theme(f'{unique_tag} {i[0]} header', item_theme)
            with dpg.group(horizontal=True):
                dpg.add_text(i[6], wrap=500, bullet=True)
                dpg.add_button(label=f"Delete from favors {i[0]}", callback=button_delete_favor_callback
                               , tag=f'{unique_tag} {i[0]} del_button')

            with dpg.group(horizontal=True):
                dpg.add_input_text(tag=f'{unique_tag} {i[0]} script', default_value=i[7], multiline=True,
                                   readonly=True, height=300)
                dpg.bind_item_font(f'{unique_tag} {i[0]} script', code_font)
                dpg.add_image_button(tag=f'{unique_tag} {i[0]} copy', texture_tag="texture_tag",
                                     width=32, height=32, callback=button_copy_callback)