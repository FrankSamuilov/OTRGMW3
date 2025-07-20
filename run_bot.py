#!/usr/bin/env python3
"""
交易机器人启动文件
"""
import sys
import time
import asyncio
from datetime import datetime

# 导入配置
from config import CONFIG, VERSION

# 导入交易机器人类
from simple_trading_bot import SimpleTradingBot

# 导入必要的工具
from logger_utils import Colors, print_colored


def main():
    """主函数"""
    print_colored(f"{'=' * 60}", Colors.BLUE)
    print_colored(f"🚀 启动交易机器人 v{VERSION}", Colors.BLUE + Colors.BOLD)
    print_colored(f"{'=' * 60}", Colors.BLUE)

    try:
        # 创建机器人实例
        bot = SimpleTradingBot()

        print_colored("✅ 机器人初始化成功", Colors.GREEN)

        # 运行主循环
        print_colored("📊 开始运行交易循环...", Colors.INFO)

        while True:
            try:
                # 运行一个交易循环
                bot.run_trading_cycle()

                # 等待指定的扫描间隔
                scan_interval = CONFIG.get('SCAN_INTERVAL', 300)
                print_colored(f"⏳ 等待 {scan_interval} 秒后进行下一轮扫描...", Colors.INFO)
                time.sleep(scan_interval)

            except KeyboardInterrupt:
                print_colored("\n⚠️ 收到中断信号，正在安全退出...", Colors.WARNING)
                break
            except Exception as e:
                print_colored(f"❌ 交易循环错误: {e}", Colors.ERROR)
                print_colored("⏳ 30秒后重试...", Colors.WARNING)
                time.sleep(30)

    except Exception as e:
        print_colored(f"❌ 严重错误: {e}", Colors.ERROR)
        import traceback
        traceback.print_exc()
        return 1

    print_colored("👋 交易机器人已停止", Colors.INFO)
    return 0


if __name__ == "__main__":
    sys.exit(main())