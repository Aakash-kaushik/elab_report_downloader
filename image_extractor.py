import shutil, os
from glob import glob

# Same as chrome download path.
folders_path = "<your download path>"

folders_list = glob(os.path.join(folders_path, "*"))
for num, folder in enumerate(folders_list):
  image_list = glob(os.path.join(folder,"*.png"))
  
  if image_list:
    shutil.move(image_list[0], folders_path)
    os.rename(os.path.join(folders_path,image_list[0].split("/")[-1]), os.path.join(folders_path, str(num) + ".png"))
    shutil.rmtree(folder)