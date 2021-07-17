import os
import urllib.request
import zipfile
# on s'occupe dans notre petit exos sur l'os linux (chez moi ubuntu)
def downloadZip(url, extractedFolderName = None):
    zipFileName = url.rsplit('/', 1)[-1]
    assert zipFileName.endswith('.zip')
    if not extractedFolderName:
        extractedFolderName = zipFileName[:-4]
    if not os.path.exists(extractedFolderName):
        print('Downloading %s' % zipFileName)
        urllib.request.urlretrieve(url, zipFileName)
        zipfile.ZipFile(zipFileName).extractall()
        os.remove(zipFileName)
        assert os.path.exists(extractedFolderName)

externFolder = os.path.normpath(os.path.join(__file__, '../extern'))
os.makedirs(externFolder, exist_ok=True)
os.chdir(externFolder)

# SDL2
downloadZip('https://www.libsdl.org/release/SDL2-devel-2.0.5-VC.zip', 'SDL2-2.0.5')
# et d'autres bla bla