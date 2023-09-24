import dearpygui.dearpygui as dpg
from database.db_requests import *
from ui.load_scripts_positions import *


def button_add_to_db_callback():
    script_name = dpg.get_value("script_name")
    script_desc = dpg.get_value("script_desc")
    script_body = dpg.get_value("script_main")
    script_private_type = 1
    if dpg.get_value("radio") == "Only for me":
        script_private_type = 2
    #print(script_private_type)
    add_new_script_to_general(script_name, script_desc, script_body, script_private_type)


# def button_reload_general_callback(sender, user_data, app_data):
#     current_general_storage = select_general()
#     dpg.delete_item("text_header_search", children_only=True)
#     print(sender, user_data, app_data)
#     load_general_scripts(current_general_storage)


def filter_general_storage(sender, filter_string):
    #print(sender, filter_string)
    #print(dpg.get_aliases())
    dpg.set_value("text_header_search", filter_string)


# def button_reload_general_favorite(sender, user_data, app_data):
#     current_favorite_storage = select_favorite()
#     dpg.delete_item("favorite_group", children_only=True)
#     print(sender, user_data, app_data)
#     load_favorite_scripts(current_favorite_storage)
