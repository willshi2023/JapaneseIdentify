import os
from datetime import datetime
import uuid
from pathlib import Path

def delete_safe(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"文件 {file_path} 已被删除")
    else:
        print(f"文件 {file_path} 不存在")

def get_filename():
    # 获取当前项目路径
    current_dir = Path.cwd()

    # 创建resource文件夹路径
    resource_dir = current_dir / 'resource'

    # 确保resource文件夹存在
    resource_dir.mkdir(exist_ok=True)

    # 生成文件名：当前日期 + UUID
    current_date = datetime.now().strftime("%Y%m%d")
    unique_id = str(uuid.uuid4())
    filename = f"{current_date}_{unique_id}.m4a"

    # 完整的文件路径
    file_path = resource_dir / filename

    print(f"文件将被保存到: {file_path}")
    return filename,str(file_path)

if __name__ == '__main__':
    get_filename()