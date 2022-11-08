import numpy as np

FEATURE_NAME_KOR = np.array(
    ['설문번호', '온도', '습도', '조도', '먼지', '소리', '냄새', '혼잡도', '피부온도'])
FEATURE_NAME_ENG = np.array(['survey number', 'temperature', 'humidity',
                             'light', 'pm2.5', 'noise', 'odor', 'congestion', 'skin temparature'])

FEATURE_SIZE = len(FEATURE_NAME_ENG) - 1
