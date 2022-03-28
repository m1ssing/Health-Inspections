import os
import glob
import shutil


pdfs = "\\\\COPFS\\Code Enforcement\\Health Inspection Reports for GIS Tracking"
web = "\\\\gisweb\\inetpub\\wwwroot\\web\\Health_Inspection_Reports"

pdfPath = "\\\\gisweb\\inetpub\\wwwroot\\web\\Health_Inspection_Reports"
filelst = [files for files in os.listdir(pdfs) if files.endswith(".pdf")]
print(filelst)

for f in filelst:
    shutil.copy(os.path.join(pdfs, f), os.path.join(web, f))

print(".")



