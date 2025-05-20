#!/usr/bin/env python3
import os
import datetime
def Write(path: str):
    htmlstring = """<!DOCTYPE html>
<html lang="zh-CN">
    <head>
        <meta name="viewport" content="width=device-width" initial-scale="1" />
        <meta charset="UTF-8">
        <title>文件目录</title>
    </head>
    <style  type="text/css">
        pre {
            overflow: auto;
        }

        a {
            word-break:break-all;
            word-wrap:break-word;
        }

        h2 {
            overflow: auto;
            word-break:break-all;
            word-wrap:break-word;
        }
    </style>
    <body>
        <h1>文件目录</h1>
        <ul>
            <li><a href="..">../</a></li>
"""
    lists = os.listdir(path)
    lists = sorted(lists, key=str.lower)
    for i in lists:
        if (i == "index.html" or i == "CNAME" or i == "build.py" or i == "build.sh" or i == ".git" or i == ".github" or "deb" == i[:3] or
            i == "404.html" or i == "403.html" or i == "500.html" or i == "502.html" or i[0] == "." or i == "favicon.ico"):
            continue
        if os.path.isdir(f"{path}/{i}"):
            htmlstring += f'\n          <li><a href="{i}/"><img src="/.icons/folder.svg" width=20px style="width=20px;vertical-align:middle;">  {i}/</a></li>'
        else:
            if ".deb" == os.path.splitext(i)[1]:
                htmlstring += f'\n          <li><a href="{i}"><img src="/.icons/deb.svg" width=20px style="width=20px;vertical-align:middle;">  {i}</a></li>'
            elif ".jpg" == os.path.splitext(i)[1]:
                htmlstring += f'\n          <li><a href="{i}"><img src="/.icons/image-jpeg.svg" width=20px style="width=20px;vertical-align:middle;">  {i}</a></li>'
            else:
                htmlstring += f'\n          <li><a href="{i}"><img src="/.icons/text-x-source.svg" width=20px style="width=20px;vertical-align:middle;">  {i}</a></li>'
    htmlstring += f"""     </ul>
        <hr/>
        <h1 id="copyright">©2024~2025 gfdgd xi</h1>
</body>
    </body>
</html>
<script>
    window.onload = function(){{
        var d = new Date();
        document.getElementById("copyright").innerHTML = "©2024~" + d.getFullYear() + " gfdgd xi";
    }}
</script>
"""
    with open(f"{path}/index.html", "w") as file:
        file.write(htmlstring)
def Dir(path: str):
    Write(path)
    for i in os.listdir(path):
        print(f"{path}/{i}")
        if os.path.isdir(f"{path}/{i}") and i != ".git" and i != ".github" and i != "deb"  and "deb" != i[:3] and "." != i[0]:
            Dir(f"{path}/{i}")
Dir(".")
print("构建完成！")
