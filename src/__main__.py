import sys
import numpy as np

from .libs import RFSimulation, Filtering
from .models import Participants
from .utils import ran_feature_columns, generate_feature_values

if __name__ == "__main__":
    user_count = int(sys.argv[1])
    day_count = int(sys.argv[2])
    users = list()

    for user_id in range(user_count):
        type = np.random.choice(['sincerity', 'random', 'one-line'])

        if type == "sincerity":
            user = Participants(user_id, ran_feature_columns())
        else:
            user = Participants(user_id, [], type)

        users.append(user)

    for days in range(0, day_count):
        values = generate_feature_values()

        for user in users:
            user.survey(values)

    rf = RFSimulation(users)

    rf.run()

    filtering = Filtering(rf)
    filtered = filtering.filter()

    chk = np.array([_.type for _ in filtered])
    print("filter result")
    print(chk)
