##Markdown Converter##

import markdown2
import os
os.chdir("/storage/emulated/0/markdown")
for files in os.listdir("."):
    if files.endswith(".txt"):
        html_filename = files.strip('.txt') + ".html"
        if not os.path.exists(os.path.join("/storage/emulated/0/markdown", html_filename)):
            html_file = open(html_filename, "w")
            html = markdown2.markdown_path(files)

            html_file.write(html)
            html_file.close()