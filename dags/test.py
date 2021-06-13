import os
from datetime import datetime
from pprint import pprint

import yaml

with open('schema.yaml', 'r') as s:
    result = yaml.safe_load(s)


# to find hubs for links

# for link_name, hubs in result['groups']['links'].items():
#     pprint(link_name)
#     for hub in hubs.values():
#         pprint(tuple(hub.keys()))
#         hub=list(hub.keys())
#         pprint('_'.join(list(hub.keys())))

# for table_name, columns_source in result['sources']['tables'].items():

#     for columns in columns_source.values():

#         for column in columns:

#             for column, column_info in column.items():
#                 if column_info.get('links'):
#                     for link in column_info.get('links'):
#                         if link == 'order_part_supplier':
#                             # pprint(f'table name: {table_name}')
#                             # pprint(f'column name: {column}')
#                             pprint(f'link name: {link}')


# for item in result['groups']['links'].items():
#     # pprint(f'dds.l_{item[0]}')
#     for el in item[1]['tables'].keys():
#         pprint(f'dds.h_{el} >> dds.l_{item[0]}')


# pprint(result['sources']['tables'].items())

# for table, cols in result['sources']['tables'].items():
#     # pprint(table)
#     for col in cols.items():
#         for item in col[1]:
#             pprint(item)

# for table, cols in result['sources']['tables'].items():
#         for col in cols['columns']:
#             for bk_column, inf in col.items():
#                 pprint(bk_column)
#                 pprint(inf)
#                 # if inf.get('bk_for') == 'part':
#                 #     print(inf.get('bk_for'))


link_name = 'orders_part_supplier'
source_name = 'lineitem'
hubs = link_name.split('_')
launch_id = 534
the_columns_list = []
str_column_list = str(the_columns_list).strip("[]").replace("'", "")
a = f'select distinct * from sal.{source_name} s \n'
for hub_name in hubs:
    b = f'JOIN dds.h_{hub_name} \n ON dds.h_{hub_name}.{hub_name}_bk = s.{hub_name}_bk \n'
    the_columns_list.append(f'h_{hub_name}_rk')
    a = a + b
a = a + 'WHERE s.launch_id = {launch_id}'.format(launch_id=launch_id)
str_column_list = str(the_columns_list).strip("[]").replace("'", "")
c = f'WITH x AS (\n{a}\n)\n'
d = f'INSERT INTO l_{link_name} ({str_column_list}, launch_id)\nSELECT {str_column_list}, launch_id FROM x\n'
e = c + d
print(e)

# links = {
#     (l_hub_name, r_hub_name): {
#         table_name: DdsLOperator(
#             task_id='dds.l_{l_hub_name}_{r_hub_name}'.format(
#                     l_hub_name=l_hub_name, r_hub_name=r_hub_name),
#             pg_meta_conn_str="host='postgres_c' port=5432 dbname='database_c' user='postgres' password='postgres'",
#             target_pg_conn_str="host='postgres_b' port=5432 dbname='database_b' user='postgres' password='postgres'",
#             config=dict(
#                 l_hub_name=l_hub_name,
#                 r_hub_name=r_hub_name,
#                 l_bk_column=l_bk_column,
#                 r_bk_column=r_bk_column,
#                 source_table=table_name,
#             )
#         )
#         for table_name, cols in YAML_DATA['sources']['tables'].items()
#         for l_col in cols['columns']
#         for l_bk_column, inf in l_col.items()
#         if inf.get('bk_for') == l_hub_name
#         for r_col in cols['columns']
#         for r_bk_column, inf in r_col.items()
#         if inf.get('bk_for') == r_hub_name
#     }
#     for l_hub_name, info in result['groups']['hubs'].items()
#     for r_hub_name in info['links'].keys()
# }

# hub_name = 'orders'

# for table_name, cols in result['sources']['tables'].items():
#     for l_col in cols['columns']:
#         for l_bk_column, inf in l_col.items():
#             # print(l_bk_column)
#             # print(inf)
#             if inf.get('bk_for') == hub_name:
#                 # print(inf)
#                 for r_col in cols['columns']:
#                     print(r_col)
#                     for r_bk_column, inf in r_col.items():
#                         # print(r_bk_column)
#                         if inf.get('bk_for') == hub_name:
#                             # print(inf)
#                             pass

# for l_hub_name, info in result['groups']['hubs'].items()
# for r_hub_name in info['links'].keys()


# for link_name in result['groups']['links'].keys()
