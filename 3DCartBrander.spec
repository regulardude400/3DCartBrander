# -*- mode: python -*-

block_cipher = None


a = Analysis(['3DCartBrander.py'],
             pathex=['C:\\PATH\\TO\\FOLDER\\THAT\\CONTAINS\\3DCartBrander.PY'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='3DCartBrander',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False )
		  
import shutil
shutil.copyfile('dialog.ui', '{0}/dialog.ui'.format(DISTPATH))