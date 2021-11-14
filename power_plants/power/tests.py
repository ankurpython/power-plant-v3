# import pandas as pd
#
# df = pd.read_excel('egrid2019_data.xlsx', sheet_name='GEN19', skiprows=1)
#
# new_cols = ['sq', 'data_year', 'plant_state', 'plant_name', 'plant_code', 'gen_id', 'num_boilers', 'gen_status',
#             'gen_type', 'gen_fuel', 'gen_capacity', 'gen_capacity_factor', 'annual_net_gen', 'ozone_season_ng',
#             'data_source', 'year_on_line', 'retirement_year']
# new_names_map = {df.columns[i]: new_cols[i] for i in range(len(new_cols))}
# df.rename(new_names_map, axis=1, inplace=True)
#
# dt = dict(df.loc[0])
# print(dt)
#
#
#
#
# # def add_data():
# #     df = pd.read_excel('agents/agents.csv')
# #     for k in range(len(df)):
# #         dt = dict(df.loc[k])
# #         data = AgentsSerializer(data=dt)
# #
# #         if data.is_valid():
# #             data.save()
# #
# #     return "done"
#
# # df.columns = df.columns.str.lower()
# # print(df)