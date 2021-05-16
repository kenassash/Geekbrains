import os

data = {'my_project': ['settings', 'mainapp', 'adminapp', 'authapp']}
for key, lst_items in data.items():
    for item in lst_items:
        new_dir = os.path.join(key, item)
        if not os.path.exists(new_dir):
            os.makedirs(new_dir, exist_ok=True)
