import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from ..common import FEATURE_NAME_ENG


class RFSimulation():
    def __init__(self, users):
        self.models = []
        self.users = users
        # [user id, imp features, RF imp features,
        #  mse, mae, per err ]
        self.record = np.array([])
        self.y_test = np.array([])
        self.y_pred = np.array([])

    def run(self):
        feature_values = self.users[0].feature_values.copy()
        survey_numbers = np.arange(
            len(feature_values)).reshape(-1, len(feature_values))
        feature_values = np.append(survey_numbers, feature_values.T, axis=0).T
        X = feature_values / feature_values.max(axis=0)

        for user in self.users:
            y = user.total_scores
            RF_imp_features = None
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=0.2)
            RFModel = RandomForestRegressor(n_estimators=100,
                                            max_features=3,
                                            oob_score=False, random_state=531)
            RFModel.fit(X_train, y_train)
            self.models.append(RFModel)

            # 성능 계산부
            prediction = RFModel.predict(X_test)
            mse = mean_squared_error(y_test, prediction)
            mae = mean_absolute_error(y_test, prediction)
            per_err = np.mean(
                np.abs((y_test - prediction) / y_test) * 100)

            feature_importance = RFModel.feature_importances_
            if len(set(feature_importance)) == 1:
                RF_imp_features = []
            else:
                feature_importance = feature_importance / feature_importance.max()
            sorted_idx = np.argsort(feature_importance)

            _features = FEATURE_NAME_ENG[sorted_idx][::-1]
            user_id = user.user_id
            user_imp_features = user.importance_features

            imp_length = len(user_imp_features)
            if RF_imp_features == None:
                if imp_length == 0:
                    RF_imp_features = [_features[0]]
                else:
                    RF_imp_features = _features[:imp_length + 1]

            _imp_features = RF_imp_features
            imp_features = list()
            for _ in FEATURE_NAME_ENG[1:]:
                if _ in _imp_features:
                    imp_features.append(_)

            self.record = np.append(self.record, [user_id, ",".join(
                user_imp_features), ",".join(imp_features), mse, mae, per_err]).reshape(-1, 6)
