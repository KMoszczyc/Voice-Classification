import shutil, os
import posixpath
import pandas as pd

merged_dir = 'data/data_merged'

def merge_data():
    dirlist = os.listdir('data/dev-clean')
    for dir1 in dirlist:
        files = []
        person_dir = f'data/dev-clean/{dir1}'
        person_dirs = os.listdir(person_dir)
        for dir2 in person_dirs:
            filenames = os.listdir(posixpath.join(person_dir, dir2))
            files += [posixpath.join(person_dir, dir2, filename) for filename in filenames]

        # dst_dir = posixpath.join(merged_dir, dir1)
        # if not os.path.exists(dst_dir):
        #     os.mkdir(dst_dir)
        print(files)
        for f in files:
            shutil.copy(f, merged_dir)

# merge_data()

#read them into pandas
filelist = os.listdir(merged_dir)
train_df = pd.DataFrame(filelist)

train_df = train_df.rename(columns={0:'file'})
