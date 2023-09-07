# # ------------------------------------TASK 1------------------------------------------------------------------
# a = 5
# b = 7
# # addition
# add = a + b
# print("The addition of {} and {} is {}".format(a,b,add ))
#
# # subtraction
# sub = a - b
# print("The subtraction of {} and {} is {}".format(a,b,sub ))
#
# # division
# div = a / b
# print("The division of {} and {} is {}".format(a,b,div ))
#
# # multiplication
# mul = a * b
# print("The subtraction of {} and {} is {}".format(a,b,mul ))

# ----------------------------------------TASK 2---------------------------------------------------

# list = [10,20,30,40,50,60,70,80,90,100,120,130,140,150]
# for Num in list:
#     if Num > 50:
#         print("The numbers greater than 50 are {}".format(Num))

# ----------------------------------------TASK 3 (A)-------------------------------------------------

# import arcpy
#
# arcpy.env.workspace = r"E:\sem_3\programming_3\ProProject_Practical_One\ProProject_Practical_One\ProProject_Practical_One\Practical_One.gdb"
# arcpy.analysis.Buffer("Wilson_Schools", "wilson_500m", "500 meters")
# print("process completed!")

# -------------------------------------TASK 3 (B)------------------------------------------------------------
# import arcpy
#
# arcpy.env.workspace = r"E:\sem_3\programming_3\ProProject_Practical_One\ProProject_Practical_One\ProProject_Practical_One\Practical_One.gdb"
#
# input_layer = "Wilson_Schools"
# buffer_distances = [1000, 1200, 1400]
# output_layer = "Wilson_School_MultiRing_Buffer"
# arcpy.analysis.MultipleRingBuffer(input_layer, output_layer, buffer_distances, "Feet", "" , "NONE")
# print("Process completed")

# ------------------------------------------------------------TASK 4 ------------------------------------------------------------------------------

import arcpy

arcpy.env.workspace = r"E:\sem_3\programming_3\ProProject_Practical_One\ProProject_Practical_One\ProProject_Practical_One\Practical_One.gdb"
input_layer = "Wilson_Zoning"
output_layer = "Wilson_zoning_feature_to_points"

arcpy.management.FeatureToPoint(input_layer, output_layer, "CENTROID")
print("process completed")

# -----------------------------------------------------END-------------------------------------------------------------------------------------