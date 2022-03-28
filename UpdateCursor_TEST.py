import arcpy
import time
pointTest = "\\\\GISAPP\\Workspace\\GIS Staff Workspace\\cschultz\\PythonFiles\\gisowner@COPGIS.sde\\cop_sde.DBO.GeoMax\\cop_sde.DBO.HealthInspections"
fields = ["RestaurantName", "SHAPE@X", "SHAPE@Y"]

lst = []
ilst = []
n = 0

with arcpy.da.SearchCursor(pointTest, fields) as cursor:
    for row in cursor:
        lst.append(row)


my_lst = [i[1] for i in lst]

finallst = [i for i in my_lst if my_lst.count(i) > 1]

setlst = set(finallst)
lstlst = list(setlst)
lenlst = range(len(lstlst))

print (finallst)



for i in lenlst:
    with arcpy.da.UpdateCursor(pointTest, fields) as Ucur:
        for Urow in Ucur:
            if Urow[1] == lstlst[n]:
                ilst.append(Urow)


        with arcpy.da.UpdateCursor(pointTest, fields) as cur:
            for row in cur:
                try:
                    if row == ilst[0]:
                        row[1] = row[1] + 20
                        row[2] = row[2] + 20
                        cur.updateRow(row)
                    elif row == ilst[1]:
                        row[1] = row[1] - 20
                        row[2] = row[2] - 20
                        cur.updateRow(row)
                    elif row == ilst[2]:
                        row[1] = row[1] + 20
                        row[2] = row[2] - 20
                        cur.updateRow(row)
                    elif row == ilst[3]:
                        row[1] = row[1] - 20
                        row[2] = row[2] + 20
                        cur.updateRow(row)
                except:
                    pass

        ilst = []
        n+= 1

del pointTest
print(".")
















