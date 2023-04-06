import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 322172960 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 1 - p
    loc = x.mean()
    scale = np.sqrt(np.var(x)) / np.sqrt(len(x))
    return loc - scale * 0.032*norm.ppf(1 - alpha / 2), \
           loc - scale * 0.032*norm.ppf(alpha / 2)
