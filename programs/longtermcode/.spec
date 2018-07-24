# -*- mode: python -*-

block_cipher = None


a = Analysis(['portable', 'mess.py'],
             pathex=['/home/ot17409/Documents/qprogramming/longtermcode'],
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
          exclude_binaries=True,
          name='',
          debug=True,
          strip=False,
          upx=True,
          console=True , icon='stpath')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='')
