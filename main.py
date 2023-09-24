import dearpygui.dearpygui as dpg
import os
from business_logic.new_inserter import inserter
from config import username
from database.db_connect import cursor
from ui.button_callbacks import *
from ui.set_images import  set_images
from ui import load_scripts_positions
from ui.set_fonts import set_font
from ui.set_styles import set_style



dpg.create_context()

# E:\users\sadikov_ad\PycharmProjects\pythonProject\test.xlsx
# e:\users\sadikov_ad\Documents\PYTEST
set_images()
code_font = set_font()
set_style()


def get_window_size():
    window_w = dpg.get_item_configuration("Primary Window")["width"]
    window_h = dpg.get_item_configuration("Primary Window")["height"]
    items = dpg.get_aliases()
    for item in items:
        if dpg.get_item_type(item).split('::')[1] == 'mvInputText' and 'script' in item:
            try:
                dpg.configure_item(item, width=window_w - 100)
            except BaseException as e:
                pass
        elif dpg.get_item_type(item).split('::')[1] == 'mvInputText' and item == "outputScriptInserter":
            dpg.configure_item(item, width=window_w-635, height=window_h-180)
    dpg.set_item_pos("GeneralSearch", [int(window_w) - 420, 112])


#dpg.show_style_editor()
#dpg.show_font_manager()


def button_show_file_items_callback():
    dpg.configure_item("InputFieldOutText", show=dpg.get_value("FileCheckbox"))
    dpg.configure_item("InputFieldOut", show=dpg.get_value("FileCheckbox"))


with dpg.item_handler_registry(tag="resize handler") as handler:
    dpg.add_item_resize_handler(callback=get_window_size)


def button_reload_general_callback():
    current_general_storage = select_general()
    dpg.delete_item("text_header_search", children_only=True)
    #print(sender, user_data, app_data)
    load_general_scripts(current_general_storage, code_font)


def button_reload_general_favorite():
    current_favorite_storage = select_favorite()
    dpg.delete_item("favorite_group", children_only=True)
    #print(sender, user_data, app_data)
    load_favorite_scripts(current_favorite_storage, code_font)


def button_inserter_callback():
    db_name = dpg.get_value("db name")
    table_name = dpg.get_value("table name")
    fields = dpg.get_value("fields of proc")
    output_text = dpg.get_value("InputFieldOut")
    result = inserter(db_name, table_name, fields, output_text, dpg.get_value("FileCheckbox"))
    dpg.set_value(item="to_set", value=result[0])
    dpg.set_value("outputScriptInserter", result[1])
    dpg.configure_item("modal_id", show=True)


def button_copy_result_callback():
    text = dpg.get_value("outputScriptInserter")
    dpg.set_clipboard_text(text)


with dpg.window(label="Delete Files", show=False, tag="modal_id", no_title_bar=True, modal=True, pos=[300, 300]):
    dpg.add_text("default", tag="to_set")
    dpg.add_button(label="OK", callback=lambda: dpg.configure_item("modal_id", show=False))

with dpg.window(label="Delete from general", show=False,
                tag="popup_delete_gen", no_title_bar=True, modal=True, pos=[300, 300]):
    dpg.add_text("Are you sure about it? This script can be used by other people")
    #dpg.add_text(label="", tag="MyBestSmeck")
    with dpg.group(horizontal=True):
        dpg.add_button(label="Delete", tag="super_button", user_data="no...", callback=lol)
        dpg.add_button(label="Cancel", callback=lambda: dpg.configure_item("popup_delete_gen", show=False))


with dpg.window(tag="Primary Window"):
    dpg.add_text(f'Username: {username}')
    with dpg.tab_bar():
        with dpg.tab(label='add script', tag='add tab'):
            dpg.add_separator()
            dpg.add_text(f'Script name: ')
            dpg.add_input_text(tag="script_name", source="string_value")
            dpg.add_text('Script description: ')
            dpg.add_input_text(tag="script_desc", height=100, source="string_value", multiline=True)
            dpg.add_text('Script: ')
            dpg.add_input_text(tag="script_main", height=300, source="string_value",
                               multiline=True, tab_input=True)
            dpg.bind_item_font("script_main", code_font)
            with dpg.group(horizontal=True):
                dpg.add_button(label="Add to DB", callback=button_add_to_db_callback, tag="btn_add")
                dpg.add_radio_button(tag="radio", items=["For everyone", "Only for me"], horizontal=True)
        with dpg.tab(label='general storage', tag='general_tab'):
            dpg.add_separator()
            main_storage = select_general()
            with dpg.group(horizontal=True):
                dpg.add_button(label="Reload General", callback=button_reload_general_callback,
                               tag=f"btn_reload {len(main_storage)}")
                dpg.add_input_text(tag="GeneralSearch", hint='поиск по содержимому и названию',
                                   source="string_value", width=400, callback=filter_general_storage)
            with dpg.filter_set(id="text_header_search"):
                load_general_scripts(main_storage, code_font)
        with dpg.tab(label='favorites', tag='favor tab'):
            dpg.add_separator()
            local_storage = select_favorite()
            with dpg.group(horizontal=True):
                dpg.add_button(label='Reload Favorite', callback=button_reload_general_favorite)
            with dpg.group(tag="favorite_group"):
                load_favorite_scripts(local_storage, code_font)
        with dpg.tab(label='procedure script'):
            with dpg.group(horizontal=True):
                with dpg.group():
                    dpg.add_text('Input schema name')
                    dpg.add_input_text(tag="db name", source="string_value", width=600)
                    dpg.add_text('Input table name')
                    dpg.add_input_text(tag="table name", source="string_value", width=600)
                    dpg.add_text('Input fields (\ncolumn1 description1\ncolumn2 description2\n...)')
                    dpg.add_input_text(tag="fields of proc", width=600, height=200, source="string_value",
                                       multiline=True, tab_input=False)
                    dpg.add_checkbox(label="Write result to .txt file",
                                     callback=button_show_file_items_callback, tag="FileCheckbox")
                    dpg.add_text('Input filepath to save (without filename and last \\) P.S can be empty',
                                 show=False, tag="InputFieldOutText")
                    dpg.add_input_text(tag="InputFieldOut", width=600, source="string_value", show=False)
                    dpg.add_button(label="Process", callback=button_inserter_callback, tag="btn_process")

                    dpg.bind_item_font("db name", code_font)
                    dpg.bind_item_font("table name", code_font)
                    dpg.bind_item_font("fields of proc", code_font)

                with dpg.group():
                    with dpg.group(horizontal=True):
                        dpg.add_text('Result:')
                        dpg.add_image_button(tag=f'copyResultInserter', texture_tag="texture_tag",
                                             width=32, height=32, callback=button_copy_result_callback)
                    dpg.add_input_text(default_value='here the procedure result will be appear',
                                       multiline=True, tag="outputScriptInserter")
                    dpg.bind_item_font("outputScriptInserter", code_font)


dpg.bind_item_handler_registry("Primary Window", "resize handler")
dpg.create_viewport(title='Custom Title', width=1300, height=900)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Primary Window", True)
dpg.start_dearpygui()
dpg.destroy_context()
