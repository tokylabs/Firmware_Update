# -*- mode: python -*-
block_cipher = None

import os
import sys

# sys.modules['FixTk'] = None


# pathex=['/Volumes/LocalCrypto/CEA/tokyupdater']

# if os.name == 'nt':
#   pathex.append('C:\\Python27\\Lib\\site-packages\\scipy\\extra-dll')
#   #pathex.append('C:\\Users\\jduser\\AppData\\Local\\Programs\\Python\\Python36-32\\Lib\\site-packages\\scipy\\extra-dll')

a = Analysis(['tokyupdater.py'],
             pathex=[],
             binaries=[],
             datas=[],
             hiddenimports=['Serial','serial','tkinter', 'Tkinter', 'certifi'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)



pyz = PYZ(a.pure, 
          a.zipped_data,
          cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='tokyupdater',
          debug=False,
          strip=False,
          upx=True,
          console=True )

coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='tokyupdater')

app = BUNDLE(exe,
             name='tokyupdater.app')
             # icon='../../res/icon/burner_icon.icns')