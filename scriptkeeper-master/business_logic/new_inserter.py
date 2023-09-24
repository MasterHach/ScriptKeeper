import openpyxl


def inserter(db_name, table_name, fields, filepath_save, checked):
    this_result = ""
    fields = fields.split("\n")
    for i in fields:
        this_pos = i.split()
        this_result += \
f"""
EXEC sys.sp_addextendedproperty
\t@name = N'ms_description',
\t@value = N'{this_pos[1]}',
\t@level0type = N'SCHEMA',
\t@level0name = N'{db_name}',
\t@level1type = N'TABLE',
\t@level1name = N'{table_name}',
\t@level2type = N'COLUMN',
\t@level2name = N'{this_pos[0]}';
GO

"""
    if checked:
        try:
            print(db_name, table_name, fields)
            with open(f"{filepath_save}\\result.txt", "w") as rs:
                print(1)
                # D:\Users\sadikov_ad\Documents
                for i in fields:
                    this_pos = i.split()
                    print(i)
                    rs.write("EXEC sys.sp_addextendedproperty\n")
                    rs.write("\t@name = N'ms_description',\n")
                    rs.write(f"\t@value = N'{this_pos[1]}',\n")
                    rs.write("\t@level0type = N'SCHEMA',\n")
                    rs.write(f"\t@level0name = N'{db_name}',\n")
                    rs.write("\t@level1type = N'TABLE',\n")
                    rs.write(f"\t@level1name = N'{table_name}',\n")
                    rs.write("\t@level2type = N'COLUMN',\n")
                    rs.write(f"\t@level2name = N'{this_pos[0]}';\n")
                    rs.write("GO\n")
                    rs.write("\n")
        except BaseException as e:
            return "something went wrong"
    return "OK", this_result
