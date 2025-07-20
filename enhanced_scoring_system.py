# enhanced_scoring_system.py
"""
增强的评分系统
"""
import numpy as np
from typing import Dict, List
from logger_utils import Colors, print_colored
from volume_spike_detector import VolumeSpikDetector


class EnhancedScoringSystem:
    """增强的评分系统 - 降低阈值，增加灵活性"""

    def __init__(self):
        self.volume_detector = VolumeSpikDetector()

        # 调整后的权重
        self.weights = {
            'trend': 0.2,  # 趋势权重降低
            'volume_spike': 0.3,  # 成交量突变权重
            'technical': 0.3,  # 技术指标权重
            'game_theory': 0.2  # 博弈论权重降低
        }

        # 调整后的交易阈值
        self.trade_thresholds = {
            'strong_buy': 2.5,
            'buy': 1.5,
            'strong_sell': -2.5,
            'sell': -1.5
        }