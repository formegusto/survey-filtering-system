import numpy as np


class Filtering:
    def __init__(self, rfModel):
        self.rfModel = rfModel

    def filter(self):
        user_idx = np.arange(0, len(self.rfModel.users))

        chk_mae = self.rfModel.record[:, 4]
        chk_mae = chk_mae.astype(np.float64)
        filters = np.array([(_.feature_importances_).sum() ==
                            0.0 for _ in self.rfModel.models])
        chk_mae = chk_mae[~filters]
        user_idx = user_idx[~filters]

        max_mae = chk_mae.max()
        err_max = np.abs(chk_mae - max_mae)

        min_mae = chk_mae.min()
        err_min = np.abs(chk_mae - min_mae)

        filters = err_max < err_min
        user_idx = user_idx[~filters]

        filtered = [self.rfModel.users[idx] for idx in user_idx]

        return filtered
