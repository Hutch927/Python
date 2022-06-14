aliens = {'red': '20', 'yellow': '30', 'orange': '40', 'green': '50', 'blue': '60', 'purple': '100'}
for key, value in aliens.items():
    print(f"{key.title()}: {value}")
if 'cyan' not in aliens.keys():
    print('Cyan is not assigned a point value.')