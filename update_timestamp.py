#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
自动更新 Shadowrocket 配置文件时间戳脚本
作者：Jojo
用途：在每次 git commit 时自动更新配置文件中的时间戳
"""

import os
import re
import sys
from datetime import datetime
import subprocess

def update_timestamp():
    """更新配置文件中的时间戳"""
    config_file = "shadowrocket-rules.conf"
    
    # 检查配置文件是否存在
    if not os.path.exists(config_file):
        print(f"错误: 找不到配置文件 {config_file}")
        return False
    
    try:
        # 读取配置文件
        with open(config_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 获取当前时间（北京时间 UTC+8）
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # 定义要替换的模式：查找时间戳行
        pattern = r'# 最后更新：\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} \(自动生成\)'
        replacement = f'# 最后更新：{current_time} (自动生成)'
        
        # 执行替换
        new_content = re.sub(pattern, replacement, content)
        
        # 检查是否找到并替换了时间戳
        if new_content == content:
            print("警告: 未找到时间戳行，可能配置文件格式有误")
            return False
        
        # 写回文件
        with open(config_file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"✅ 成功更新时间戳为: {current_time}")
        
        # 将更新后的文件添加到 git staging area
        try:
            subprocess.run(['git', 'add', config_file], check=True, capture_output=True)
            print(f"✅ 已将 {config_file} 添加到 git staging area")
        except subprocess.CalledProcessError as e:
            print(f"警告: 无法将文件添加到 git staging area: {e}")
        
        return True
        
    except Exception as e:
        print(f"错误: 更新时间戳失败 - {e}")
        return False

def main():
    """主函数"""
    print("🔄 开始更新 Shadowrocket 配置文件时间戳...")
    
    if update_timestamp():
        print("🎉 时间戳更新完成！")
        sys.exit(0)
    else:
        print("❌ 时间戳更新失败！")
        sys.exit(1)

if __name__ == "__main__":
    main() 