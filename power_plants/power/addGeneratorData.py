import json

import numpy as np
import pandas as pd
from .serializers import GeneratorSerializer


def add_generator_data():
    df = pd.read_excel('power/egrid2019_data.xlsx', sheet_name='GEN19', skiprows=1)
    new_cols = ['sq', 'data_year', 'plant_state', 'plant_name', 'plant_code', 'gen_id', 'num_boilers', 'gen_status',
                'gen_type', 'gen_fuel', 'gen_capacity', 'gen_capacity_factor', 'annual_net_gen', 'ozone_season_ng',
                'data_source', 'year_on_line', 'retirement_year']
    new_names_map = {df.columns[i]: new_cols[i] for i in range(len(new_cols))}
    df.rename(new_names_map, axis=1, inplace=True)

    result = df.to_json(orient="records")
    data = json.loads(result)

    for dt in data:
        serializer = GeneratorSerializer(data=dt)

        if serializer.is_valid():
            serializer.save()
        else:
            print(dt)
            return serializer.errors

    return "Done"