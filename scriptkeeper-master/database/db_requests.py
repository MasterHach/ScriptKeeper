from config import username
from database.db_connect import cursor


def add_new_script_to_general(script_name, script_description, script_body, script_private_type):
    query = f"""
            INSERT INTO masm.usefulScripts
                (sName, sDescription, sBody, sType, sUser)
            VALUES
                ('{script_name.replace("'", "''")}', 
                '{script_description.replace("'", "''")}', 
                '{script_body.replace("'", "''")}', 
                '{script_private_type}', '{username}')
            """
    cursor.execute(query)
    cursor.commit()


def add_new_script_to_favorite(script_id):
    query = f"""
            INSERT INTO masm.usefulScripts_links
                SELECT idS
                       ,'{username}'
                       ,sType
                FROM masm.usefulScripts
                WHERE
                    idS = {script_id}
            """
    cursor.execute(query)
    cursor.commit()


def delete_script_from_favorites(link_id):
    query = f"""
            DELETE FROM masm.usefulScripts_links
            WHERE idL = {link_id} 
            """
    cursor.execute(query)
    cursor.commit()


def delete_script_from_general(script_id):
    query = f"""
            DELETE FROM masm.usefulScripts
            WHERE idS = {script_id} 
            """
    cursor.execute(query)
    cursor.commit()


def select_favorite():
    query = f"""
            SELECT 
            *
            FROM masm.usefulScripts_links as li
            inner join masm.usefulScripts as us on li.idS = us.idS
            WHERE lUser = '{username}' order by lType desc
            """
    cursor.execute(query)
    return cursor.fetchall()


def select_general():
    query = f"""
            SELECT 
            * 
            FROM masm.usefulScripts
            WHERE sType = 1
                OR (sType = 2 AND sUser = '{username}') order by sType desc
            """
    cursor.execute(query)
    return cursor.fetchall()

