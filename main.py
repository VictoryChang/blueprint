import time

names = ['Anna', 'Steve', 'Wilson', 'Craig']

from alive_progress import alive_bar
with alive_bar(len(names)) as bar:
    for item in names:
        bar(f'Processing: {item}')
        time.sleep(1)
