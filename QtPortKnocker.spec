# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['QtMain.py'],
    pathex=[],
    datas=[('Knocker.json','.'),('Logger.json','.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='PortKnocker',
    debug=False,
    bootloader_ignore_signals=False,
    strip=True,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['PortKnocker.icns'],
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=True,
    upx=True,
    upx_exclude=[],
    name='PortKnocker',
)
app = BUNDLE(
    coll,
    name='PortKnocker.app',
    icon='PortKnocker.icns',
    bundle_identifier=None,
)