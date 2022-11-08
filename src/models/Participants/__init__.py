import random as ran
import numpy as np
from ...common import FEATURE_SIZE


class Participants:
    def __init__(self, user_id, importance_features, not_sincerity_type=None):
        self.user_id = user_id
        self.importance_features = importance_features
        self.survey = None

        if len(importance_features) == 0:
            if not_sincerity_type is None:
                self.type = "not_sincerity {}".format("random")
            else:
                self.type = "not_sincerity {}".format(not_sincerity_type)
        else:
            self.type = "sincerity"

    def survey(self, features):
        # features
        # [0] temperature, [1] humidity, [2]
        scores = np.array()

        if "not_sincerity" in self.type:
            if "one-line" in self.type:
                for idx in range(0, FEATURE_SIZE):
                    scores = np.append(scores, 20)
            else:
                for idx in range(0, FEATURE_SIZE):
                    scores[idx] = scores = np.append(scores, ran.randrange(21))
        else:
            if 'temperature' in self.importance_features:
                if (temp >= 18) & (temp <= 20):
                    scores = np.append(20)
                else:
                    err = 0
                    if temp <= 18:
                        err = 18 - temp
                    else:
                        err = temp - 20
                    _score[0] = 20 - round(err / 2)
            else:
                _score[0] = ran.randrange(15, 21)
