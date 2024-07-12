# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['main.py'],
    pathex=['.'],
    binaries=[],
    datas=[
        ('assets/Dino/DinoRun1.png', 'assets/Dino'),
        ('assets/Dino/DinoRun2.png', 'assets/Dino'),
        ('assets/Dino/DinoJump.png', 'assets/Dino'),
        ('assets/Dino/DinoDuck1.png', 'assets/Dino'),
        ('assets/Dino/DinoDuck2.png', 'assets/Dino'),
        ('assets/Cactus/SmallCactus1.png', 'assets/Cactus'),
        ('assets/Cactus/SmallCactus2.png', 'assets/Cactus'),
        ('assets/Cactus/SmallCactus3.png', 'assets/Cactus'),
        ('assets/Cactus/LargeCactus1.png', 'assets/Cactus'),
        ('assets/Cactus/LargeCactus2.png', 'assets/Cactus'),
        ('assets/Cactus/LargeCactus3.png', 'assets/Cactus'),
        ('assets/Bird/Bird1.png', 'assets/Bird'),
        ('assets/Bird/Bird2.png', 'assets/Bird'),
        ('assets/Other/Cloud.png', 'assets/Other'),
        ('assets/Other/Track.png', 'assets/Other'),
    ],
    hiddenimports=[],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='main',
)


## -*- mode: python ; coding: utf-8 -*-
#
#block_cipher = None
#
#a = Analysis(
#    ['main.py'],
#    pathex=['.'],
#    binaries=[],
#    datas=[
#        ('assets/Dino/DinoRun1.png', 'assets/Dino'),
#        ('assets/Dino/DinoRun2.png', 'assets/Dino'),
#        ('assets/Dino/DinoJump.png', 'assets/Dino'),
#        ('assets/Dino/DinoDuck1.png', 'assets/Dino'),
#        ('assets/Dino/DinoDuck2.png', 'assets/Dino'),
#        ('assets/Cactus/SmallCactus1.png', 'assets/Cactus'),
#        ('assets/Cactus/SmallCactus2.png', 'assets/Cactus'),
#        ('assets/Cactus/SmallCactus3.png', 'assets/Cactus'),
#        ('assets/Cactus/LargeCactus1.png', 'assets/Cactus'),
#        ('assets/Cactus/LargeCactus2.png', 'assets/Cactus'),
#        ('assets/Cactus/LargeCactus3.png', 'assets/Cactus'),
#        ('assets/Bird/Bird1.png', 'assets/Bird'),
#        ('assets/Bird/Bird2.png', 'assets/Bird'),
#        ('assets/Other/Cloud.png', 'assets/Other'),
#        ('assets/Other/Track.png', 'assets/Other'),
#    ],
#    hiddenimports=[],
#    hookspath=[],
#    runtime_hooks=[],
#    excludes=[],
#    win_no_prefer_redirects=False,
#    win_private_assemblies=False,
#    cipher=block_cipher,
#)
#
#pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)
#
#exe = EXE(
#    pyz,
#    a.scripts,
#    [],
#    exclude_binaries=True,
#    name='main',
#    debug=False,
#    bootloader_ignore_signals=False,
#    strip=False,
#    upx=True,
#    upx_exclude=[],
#    runtime_tmpdir=None,
#    console=True,
#)
#
#coll = COLLECT(
#    exe,
#    a.binaries,
#    a.zipfiles,
#    a.datas,
#    strip=False,
#    upx=True,
#    upx_exclude=[],
#    name='main',
#)
