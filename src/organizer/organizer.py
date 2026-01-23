import os
from file_handler import documents,downloadPath

for d in documents:
    if "Resume" in d.name:
        print(d)

print(downloadPath.exists())