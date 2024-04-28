import os
import shutil
from git import Repo
import requests
import yaml
from datetime import datetime


# 克隆 GitHub 仓库
def clone_repo(repo_url, clone_path):
    if os.path.exists(clone_path):
        shutil.rmtree(clone_path)
    Repo.clone_from(repo_url, clone_path)


# 读取 birthdays.yml 文件
def read_birthdays(file_path):
    with open(file_path, "r") as file:
        data = yaml.safe_load(file)
    return data


# 获取今天过生日的人名
def get_today_birthday_names(birthdays_data):
    today = datetime.now().strftime("%Y-%m-%d")
    today_birthday_names = [
        entry["name"] for entry in birthdays_data if entry["birthday"] == today
    ]
    return today_birthday_names


# 将生日名单转换为 Markdown 格式
def format_to_md(names):
    return "\n".join(names)


# 写入到 md 文件
def write_to_md(names, file_path):
    with open(file_path, "w") as file:
        file.write(f"今天过生日的人名：\n{names}")


# 使用 gitPython 进行 push
def push_to_github(file_path):
    repo = Repo(clone_path)
    repo.git.add(file_path)
    repo.index.commit("Add today's birthdays")
    origin = repo.remote(name="origin")
    origin.push()


if __name__ == "__main__":
    # 克隆仓库
    repo_url = "https://github.com/W1ndys/Auto-Birthday"
    clone_path = "Auto-Birthday"
    clone_repo(repo_url, clone_path)

    # 读取 birthdays.yml 文件
    birthdays_file_path = os.path.join(clone_path, "birthdays.yml")
    birthdays_data = read_birthdays(birthdays_file_path)

    # 获取今天过生日的人名
    today_birthday_names = get_today_birthday_names(birthdays_data)

    if today_birthday_names:
        # 将生日名单转换为 Markdown 格式
        md_content = format_to_md(today_birthday_names)

        # 写入到 md 文件
        md_file_path = "today_birthdays.md"
        write_to_md(md_content, md_file_path)

        # 使用 gitPython 进行 push
        push_to_github(md_file_path)
