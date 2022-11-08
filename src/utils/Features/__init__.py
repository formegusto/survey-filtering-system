import numpy as np
import random as ran
from ...common import FEATURE_NAME_ENG, FEATURE_SIZE

def generate_feature_values():
    temperature = ran.randrange(10, 33)    # 온도 10~32
    humidity = ran.randrange(30, 81)  # 습도 30 ~ 80
    light = ran.randrange(200, 1901, 100)  # 조도 200 ~ 1900 (100 단위)
    pm2_5 = ran.randrange(70, 151, 10)  # 먼지 70 ~ 150 (10 단위)
    noise = ran.randrange(1, 21)  # 소음 1 ~ 20 (1 단위)
    odor = ran.randrange(0, 6)  # 악취 0 ~ 5 (1 단위)
    congestion = ran.randrange(1, 11)  # 혼잡도 1 ~ 10 (1 단위)
    skin_temperature = ran.randrange(25, 41)  # 피부온도 25 ~ 40 (1 단위)

    return np.array([temperature, humidity, light, pm2_5,
                     noise, odor, congestion, skin_temperature])


def ran_feature_columns():
    feature_cols = FEATURE_NAME_ENG[1:]
    return np.random.choice(feature_cols, ran.randrange(1, FEATURE_SIZE), False)
