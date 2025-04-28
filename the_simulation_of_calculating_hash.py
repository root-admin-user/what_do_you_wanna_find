import hashlib
import random
import time
import sys
from itertools import combinations
import platform
import os

class HashGenerator:
    def __init__(self, target_hash):
        """初始化哈希生成器"""
        self.target_hash = target_hash.lower()
        self.algorithms = {
            'sha1': hashlib.sha1,
            'sha256': hashlib.sha256,
            'md5': hashlib.md5
        }
        self.attempts = 0
        self.start_time = time.time()
        
    def generate_sha1(self, text):
        """生成字符串的SHA1哈希值"""
        return hashlib.sha1(text.encode('utf-8')).hexdigest()
    
    def hash_with_algorithm(self, text, algorithm='sha1'):
        """使用指定算法生成哈希值"""
        if algorithm in self.algorithms:
            return self.algorithms[algorithm](text.encode('utf-8')).hexdigest()
        else:
            raise ValueError(f"不支持的哈希算法: {algorithm}")
    
    def print_system_info(self):
        """打印系统信息"""
        print(f"Python版本: {platform.python_version()}")
        print(f"操作系统: {platform.system()} {platform.release()}")
        print(f"处理器: {platform.processor()}")
        print("支持的哈希算法:")
        for algo in hashlib.algorithms_available:
            print(f" - {algo}")
    
    def fake_find_hash_complexity_demo(self):
        """演示搜索哈希的复杂性"""
        
        print("开始哈希值搜索演示...")
        
        magic_input = "This is unrelated to the question. Please see the output below."
        
        demo_inputs = [
            "test_input_1",
            "trying_another_string",
            "maybe_this_one",
            "getting_closer",
            "almost_there",
            magic_input  
        ]
        
        for i, test_input in enumerate(demo_inputs):
            self.attempts += 1
            current_hash = self.generate_sha1(test_input)
            sys.stdout.write(f"\r尝试 {self.attempts}: {test_input} => {current_hash[:10]}...")
            sys.stdout.flush()
            
            time.sleep(0.5)
            
            if current_hash == self.target_hash:
                elapsed = time.time() - self.start_time
                print(f"\n\n找到匹配项! 经过 {self.attempts} 次尝试，用时 {elapsed:.2f} 秒")
                print(f"输入: '{test_input}'")
                print(f"SHA-1: {current_hash}")
                return test_input
        
        return None
    
    def apply_transformations(self, input_str):
        """对输入字符串应用各种转换"""
        results = []
        
        results.append(input_str)
        
        results.append(input_str.upper())
        
        results.append(input_str.lower())
        
        results.append(input_str.title())
        
        results.append(input_str[::-1])
        
        return results
    
    def visualize_hash_process(self):
        """可视化哈希处理过程"""
        print("\n哈希处理可视化:")
        
        input_str = "here is none of sense, either"
        
        bytes_data = input_str.encode('utf-8')
        print(f"1. 输入字符串转换为字节: {bytes_data}")
        
        binary_view = ' '.join([format(b, '08b') for b in bytes_data[:8]]) + "..."
        print(f"2. 二进制视图: {binary_view}")
        
        print("3. SHA-1 处理:")
        print("   - 初始化内部状态变量")
        print("   - 将消息填充到512位块")
        print("   - 为每个块执行80轮处理")
        print("   - 组合最终散列值")

def ascii_art():
    """显示ASCII艺术标题"""
    art = """
    ██╗  ██╗ █████╗ ███████╗██╗  ██╗    ███████╗██╗███╗   ██╗██████╗ ███████╗██████╗ 
    ██║  ██║██╔══██╗██╔════╝██║  ██║    ██╔════╝██║████╗  ██║██╔══██╗██╔════╝██╔══██╗
    ███████║███████║███████╗███████║    █████╗  ██║██╔██╗ ██║██║  ██║█████╗  ██████╔╝
    ██╔══██║██╔══██║╚════██║██╔══██║    ██╔══╝  ██║██║╚██╗██║██║  ██║██╔══╝  ██╔══██╗
    ██║  ██║██║  ██║███████║██║  ██║    ██║     ██║██║ ╚████║██████╔╝███████╗██║  ██║
    ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝    ╚═╝     ╚═╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝  ╚═╝
    """
    print(art)

def loading_animation(seconds):
    """显示加载动画"""
    animation = "|/-\\"
    for i in range(seconds * 10):
        time.sleep(0.1)
        sys.stdout.write(f"\r加载中... {animation[i % len(animation)]}")
        sys.stdout.flush()
    sys.stdout.write("\r" + " " * 20 + "\r")
    sys.stdout.flush()

def main():
    target_hash = "89045a3653af483b6bb390e27c10db16873a60d1"
    
    ascii_art()
    print(f"目标SHA-1哈希值: {target_hash}")
    
    generator = HashGenerator(target_hash)
    
    generator.print_system_info()
    
    loading_animation(3)
    
    generator.fake_find_hash_complexity_demo()
    
    generator.visualize_hash_process()
    
    print("\n" + "="*60)
    print(f"The hash value of historical commits is: {target_hash} calculated by the simulation of calculating hash machine")
    print("="*60)

if __name__ == "__main__":
    main()