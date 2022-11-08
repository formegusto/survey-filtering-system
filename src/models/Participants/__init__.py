import random as ran
import numpy as np
from ...common import FEATURE_SIZE, FEATURE_NAME_ENG
from .calculate import calculate


class Participants:
    def __init__(self, user_id, importance_features, not_sincerity_type=None):
        self.user_id = user_id
        self.importance_features = importance_features

        self.feature_values = np.array([])
        self.scores = np.array([])
        self.survey = np.array([])

        if len(importance_features) == 0:
            if not_sincerity_type is None:
                self.type = "not_sincerity {}".format("random")
            else:
                self.type = "not_sincerity {}".format(not_sincerity_type)
        else:
            self.type = "sincerity"

    def survey(self, values):
        # features
        # [0] temperature, [1] humidity, [2] light,
        # [3] pm2.5, [4] noise, [5] odor,
        # [6] congestion, [7] skin temperature
        features = FEATURE_NAME_ENG[1:]
        scores = np.array()

        if "not_sincerity" in self.type:
            if "one-line" in self.type:
                for idx in range(0, FEATURE_SIZE):
                    scores = np.append(scores, 20)
            else:
                for idx in range(0, FEATURE_SIZE):
                    scores[idx] = scores = np.append(scores, ran.randrange(21))
        else:
            for idx, value in enumerate(values):
                feature = features[idx]
                if feature in self.importance_features:
                    scores = np.append(scores, calculate[feature](value))
                else:
                    scores = np.append(scores, ran.randrange(10, 21))

        self.feature_values = np.append(
            self.feature_values, values).reshape(-1, FEATURE_SIZE)
        self.scores = np.append(self.scores, scores).reshape(-1, FEATURE_SIZE)
        self.survey = np.append(self.survey, scores.sum())
