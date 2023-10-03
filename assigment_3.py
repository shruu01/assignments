
 #-----------task 1---------------------


# file_path = r"D:\Sem 3\Prog_3\assign_3\Taaron ki karli sawaari.txt"
#
# file_obj = open(file_path,'r')
#
# lines = file_obj.readlines()
# for S in lines:
#     print(S)

# ------------task 2--------------------

# import arcpy
# import os
#
# arcpy.env.workspace = r"E:\sem_3\programming_3\ProProject_Practical_One\ProProject_Practical_One\ProProject_Practical_One\Practical_One.gdb"
#
# output_folder_path = r"D:\Sem 3\Prog_3\assign_3"
#
# output_text_file = "MajorAttractions_info.txt"
#
# output_file_path = os.path.join(output_folder_path, output_text_file)
#
# print(output_file_path)
#
# file_obj = open(output_file_path, "w")
#
# fc_list = arcpy.ListFeatureClasses("MajorAttractions")
#
# for fc_name in fc_list:
#     print(fc_name)
#
# print("--------------------------------")
#
# field_list = arcpy.ListFields("MajorAttractions")
# for field in field_list:
#     print("Field Name: {},  Type: {}, Length: {}".format(field.name, field.type, field.length))
#     file_obj.write("Name: {}, Type: {}, Length: {} \n".format(field.name, field.type, field.length))
#
#     print("--------------------------")
#     file_obj.write("-------------------------------\n")
# file_obj.close()
# print("Process Completed")

# --------------task 3---------------

import arcpy

arcpy.env.workspace = r"E:\sem_3\programming_3\ProProject_Practical_One\ProProject_Practical_One\ProProject_Practical_One\Practical_One.gdb"

feature_class_list = arcpy.ListFeatureClasses()
print(feature_class_list)

for fc in feature_class_list:
    desc_obj = arcpy.Describe(fc)
    shape_type = desc_obj.shapeType

    if shape_type == "Point":
        buffer_distance = "400 feet"
    elif shape_type == "Polyline":
        buffer_distance = "1500 feet"
    elif shape_type == "Polygon":
        buffer_distance = "800 feet"

    Output_buffer = fc + "_Buffer"
arcpy.analysis.Buffer(fc, Output_buffer, buffer_distance)

print("process complete")

# =======================================================================================
