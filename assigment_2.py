 #------------------------- TASK 1(1)-----------------------------------

# # Declare a list variable
# cities = ["Delhi", "Thane","Jaipur", "Mumbai", "Nashik"]
# print(cities)
# #  Print the length of the list
# print(len(cities))
#
# # Append a new city to the existing list
# cities.append("Chennai")
# print(cities)
# #  Print the length of the list
# print(len(cities))
#
# # Remove an element at index '2’ from the list and print
# cities.pop(2)
# print(cities)
# print("Process_Completed")

# -------------------------TASK 1(2)-------------------------------------

# # Printing Country Names
# countries_and_capitals = {"India": "Delhi", "USA": "Washington_DC", "Japan": "Tokyo", "North Korea": "Seoul"}
# print("Countries_Name:")
# for Countries in countries_and_capitals.keys():
#     print(Countries)
#
# # Inserting One Country and its Capitalan
# new_country = "Brazil"
# new_capital = "Brasilia"
#
# countries_and_capitals[new_country] = new_capital
# print(countries_and_capitals)
#
# # Print the length of the dictionary
# print(len(countries_and_capitals))
#
# # # Remove an element from the dictionary
# countries_and_capitals.pop("USA")
# print(countries_and_capitals)
# print("Process Completed")

# -------------------------------------TASK 2------------------------------------
#
# import arcpy
# import os
#
# # Path to file gdb
# file_GDB_path = r"C:\Users\shrutika\Downloads\ProProject_Practical_Two\World_data.gdb"
# fc_name = ["lakes"]
#
# for fc in fc_name:
#     fc_path = os.path.join(file_GDB_path, fc)
#     desc_obj = arcpy.Describe(fc_path)
#
#     sr_obj = desc_obj.spatialReference
#     print(sr_obj.name)
#     print(sr_obj.type)
#
# shape_type = desc_obj.shapeType
# print("The geometry type of feature class: {} is {}".format(fc, shape_type))
#
# field_list = desc_obj.fields
#
# for field in field_list:
#         print("The field name is {} and the type is {}".format(field.name, field.type))

# -------------------------TASK 3------------------------------------------

# import arcpy
#
# raster_path = r"C:\Users\shrutika\Downloads\ProProject_Practical_Two\RASTER_DATA\erelev"
# desc_obj = arcpy.Describe(raster_path)
# print(desc_obj.bandCount)
#
# print(desc_obj.format)
#
# print(desc_obj.height)
#
# print(desc_obj.width)
#
# print(desc_obj.basename)
#
# print("Process Completed")

# ------------------------------------END--------------------------------------------------

