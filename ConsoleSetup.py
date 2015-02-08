import __builtin__
__builtin__.__dict__.update(__import__('pandac.PandaModules', fromlist=['*']).__dict__)
from direct.showbase import PythonUtil
loadPrcFile('config/general.prc')
loadPrcFile('config/release/dev.prc')
loadPrcFile('config/toonkit.prc')
print("Ready!")