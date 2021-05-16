import os
import shutil

project_path = 'my_project'
project_templates_path = os.path.join(project_path, 'templates')
print(project_templates_path)

for dirname in os.listdir(project_path):
    # print(dirname)
    app_template_dir = os.path.join(project_path, dirname, 'templates', dirname)
    print(app_template_dir)
    if os.path.isdir(app_template_dir):
        shutil.copytree(app_template_dir, os.path.join(project_templates_path, dirname))