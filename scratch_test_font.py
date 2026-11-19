import os
from fontTools.ttLib import TTFont

fonts_dir = r'C:\Users\ivank\Desktop\игра_ловля\fonts'

for f in ['SuisseIntl-Bold', 'SuisseIntl-Medium', 'SuisseIntl-Regular', 'SuisseIntl-SemiBold']:
    otf_path = os.path.join(fonts_dir, f + '.otf')
    if os.path.exists(otf_path):
        font = TTFont(otf_path)
        
        # Woff
        woff_path = os.path.join(fonts_dir, f + '.woff')
        font.flavor = 'woff'
        font.save(woff_path)
        print('Saved', woff_path)
        
        # Woff2
        try:
            woff2_path = os.path.join(fonts_dir, f + '.woff2')
            font.flavor = 'woff2'
            font.save(woff2_path)
            print('Saved', woff2_path)
        except Exception as e:
            print('Could not save woff2:', e)
