# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['src\\main\\cli.py'],
             pathex=['C:\\Users\\james\\Documents\\CodingWorkspace\\SigmaDraconisMap','C:\\Users\\james\\Documents\\CodingWorkspace\\env\\Lib\\site-packages'],
             binaries=[],
             datas=[('src/main/starmap-310623-baf93c6b9991.json', 'src/main')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='Starmap',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
