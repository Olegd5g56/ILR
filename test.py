import pyautogui as pg
import pytesseract
try:
    from PIL import Image
except ImportError:
    import Image
#print(pg.position())
img = pg.screenshot(region=(1145,260,160,30))#region=(160,30,1145,260),
if("В ПРЯМОМ ЭФИРЕ" in pytesseract.image_to_string(img, lang='rus')):print("evrika")
