import zipfile
import pathlib

def make_archive(filepaths, dest_dir):
    dest_path = pathlib.Path(dest_dir, 'compressed.zip')
    with zipfile.ZipFile(dest_path, 'w') as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            archive.write(filepath, arcname=filepath.name)

if __name__ == '__main__':
    make_archive(filepaths=['D:/Projects/udemy-tpmc/app1/bfex1.py',
                            'D:/Projects/udemy-tpmc/app1/bfex2.py'],
                 dest_dir='D:/Projects/udemy-tpmc/app1/temp')
