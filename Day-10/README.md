# Lists Part-2

```python
import os

# E:\my-git E:\WSL

folders = input("Enter folders: ").split()

for folder in folders:
    try:
      files = os.listdir(folder)
    except FileNotFoundError:
      print(f"Folder '{folder}' not found.")
      continue
    print("listting files in folder: ", folder)
   # print(f"\nFiles in {folder}:")
    for file in files:
      print(file)

```
