import ast
import json
import os
from pprint import pprint
from re import L

import yaml
from sqlalchemy.sql.expression import table

from operators.utils import source_table_list

with open('schema.yaml', encoding='utf-8') as f:
    YAML_DATA = yaml.safe_load(f)
with open('schema_default.yaml', encoding='utf-8') as f:
    DEFAULT_YAML_DATA = yaml.safe_load(f)


# for sat_for, task_name in YAML_DATA['groups']['satellites'].items():
#     print('='*50)
#     pprint(sat_for)
#     pprint(task_name)


# for table_name, table_info in YAML_DATA['sources']['tables'].items():
#     for info in table_info['columns']:
#         for column, column_info in info.items():
#             if column_info.get('source_for') == 'orders_part_supplier':
#                 pprint(f'table name:  {table_name}')
#                 pprint(f'column name: {column}')

    # print('\n' + '='*50 + '\n')


# for link_name, hubs_data in YAML_DATA['groups']['links'].items():
#     print(link_name)
#     print('\n' + '='*50 + '\n')

#     print(str(tuple(hubs_data.keys())).replace(
#         "'", "").strip('()').split(', '))

#     print('\n' + '='*50 + '\n')
#     for hub in hubs_data.keys():
#         pprint(hub)
# print('\n' + '='*50 + '\n')


# for table_name, cols in YAML_DATA['sources']['tables'].items():
#     for col in cols['columns']:
#         for bk_column, inf in col.items():
#             if inf.get('bk_for') == 'customer':
#                 pprint(table_name)
#                 pprint(bk_column)

# print('\n' + '='*50 + '\n')


default_hubs = {
    hub_name: {
        table: 'dds.h_{hub_name}'.format(hub_name=hub_name)
        for table, cols in DEFAULT_YAML_DATA['sources']['tables'].items()
        for col in cols['columns']
        for bk_column, inf in col.items()
        if inf.get('bk_for') == hub_name
    }
    for hub_name in YAML_DATA['groups']['hubs'].keys()
}

hubs = {
    hub_name: {
        table: 'dds.h_{hub_name}'.format(hub_name=hub_name)
        for table, cols in YAML_DATA['sources']['tables'].items()
        for col in cols['columns']
        for bk_column, inf in col.items()
        if inf.get('bk_for') == hub_name
    }
    for hub_name in YAML_DATA['groups']['hubs'].keys()
}

links = {
    tuple(hubs_data): {
        hub: {
            table_name: 'dds.l_{link_name}'.format(link_name=link_name)
            for table_name, cols in YAML_DATA['sources']['tables'].items()
            for col in cols['columns']
            for bk_column, inf in col.items()
            if inf.get('bk_for') == hub
        }
        for hub in hubs_data

    }
    for link_name, link_info in YAML_DATA['groups']['links'].items()
    for source_table, hubs_data in link_info.items()
}

hub_satellites = {
    (hub_name, source_table): {
        table_name: 'dds.s_{hub_name}'.format(hub_name=hub_name)
        for table_name, table_info in YAML_DATA['sources']['tables'].items()
        for column_info in table_info['columns']
        for info in column_info.values()
        if info.get('bk_for') == hub_name
    }
    for hub_name in YAML_DATA['groups']['satellites'].keys()
    for sat, source_table in YAML_DATA['groups']['satellites'].items()
    if hub_name == sat
}

link_satellites = {
    (tuple(link_name.split('_')), source_table): {
        hub: {
            table_name: 'dds.s_l_{link_name}'.format(link_name=link_name)
            for table_name, table_info in YAML_DATA['sources']['tables'].items()
            for column_info in table_info['columns']
            for info in column_info.values()
            if info.get('bk_for') == hub

        }
        for hub in tuple(link_name.split('_'))

    }
    for link_name in YAML_DATA['groups']['links'].keys()
    for sat, source_table in YAML_DATA['groups']['satellites'].items()
    if link_name == sat
}


# for (link_name, source_table), link_hub_info in link_satellites.items():
#     # pprint((link_name, source_table))
#     # pprint(link_hub_info)
#     for link_hub, table_info in link_hub_info.items():
#         # pprint(link_hub)
#         # pprint(table_info)
#         for table_name, task in table_info.items():
#             print(links[link_name][link_hub][table_name]+'>>'+task)


#         for redundant, task in info.items():
#             for source_table, task in info.items():
#                 print(links[link_name][source_table] +'>>'+ task)


# for table_name, table_info in YAML_DATA['sources']['tables'].items():
#     for column_info in table_info['columns']:
#         for info in column_info.values():
#             if info.get('bk_for') == 'orders':
#                  pprint(table_info['columns'])

link_name = 'orders_part_supplier'
hubs = link_name.split("_")
columns_info = "[{'orders_bk': {'bk_for': 'orders'}}, {'part_bk': {'bk_for': 'part'}}, {'supplier_bk': {'bk_for': 'supplier'}}, {'linenumber': {'source_for': 'orders_part_supplier'}}, {'quantity': {'source_for': 'orders_part_supplier'}}, {'extendedprice': {'source_for': 'orders_part_supplier'}}, {'discount': {'source_for': 'orders_part_supplier'}}, {'tax': {'source_for': 'orders_part_supplier'}}, {'returnflag': {'source_for': 'orders_part_supplier'}}, {'linestatus': {'source_for': 'orders_part_supplier'}}, {'shipdate': {'source_for': 'orders_part_supplier'}}, {'commitdate': {'source_for': 'orders_part_supplier'}}, {'receiptdate': {'source_for': 'orders_part_supplier'}}, {'shipinstruct': {'source_for': 'orders_part_supplier'}}, {'shipmode': {'source_for': 'orders_part_supplier'}}, {'comment': {'source_for': 'orders_part_supplier'}}]"
# columns_info = columns_info.replace("'", "").strip('[]').split(', ')
bk_list = []
column_list = []

for hub in hubs:
    for item in json.loads(columns_info.replace("'", '"')):
        for column_name, column_data in item.items():
            if column_data.get('bk_for') == hub:
                bk_list.append(column_name)
            elif column_data.get('source_for'):
                # pprint(column_data.get('source_for'))
                column_list.append(column_name)


bk_list = set(bk_list)
column_list = set(column_list)

str_column_list = str(column_list).strip(
    "{}").replace("'", "")

insert_query = 'select distinct * from {source_schema}.{source_table} s \n'.format(
    source_schema='sal', source_table='lineitem')
for hub_name in hubs:
    hub_join = 'JOIN {target_schema}.h_{hub_name} \nON {target_schema}.h_{hub_name}.{hub_name}_bk = s.{hub_name}_bk \n'.format(
        hub_name=hub_name, target_schema='dds')
    insert_query = insert_query + hub_join
insert_query = insert_query + \
    'JOIN {target_schema}.l_{link_name}\nON '.format(
        link_name=link_name, target_schema='dds')
for hub_name in hubs:
    if hub_name != hubs[-1]:
        link_join = '{target_schema}.l_{link_name}.h_{hub_name}_rk = {target_schema}.h_{hub_name}.h_{hub_name}_rk AND '.format(
            hub_name=hub_name, target_schema='dds', link_name=link_name)
        insert_query = insert_query + link_join
    else:
        link_join = '{target_schema}.l_{link_name}.h_{hub_name}_rk = {target_schema}.h_{hub_name}.h_{hub_name}_rk\n'.format(
            hub_name=hub_name, target_schema='dds', link_name=link_name)
        insert_query = insert_query + link_join
insert_query = insert_query + \
    'WHERE s.launch_id = {launch_id}\n'.format(launch_id=17)
insert_query = f'WITH x AS (\n{insert_query})\n'
insert_query = insert_query + 'INSERT INTO {target_schema}.l_s_{link_name} ({str_column_list}, launch_id)\nSELECT {str_column_list}, {job_id} FROM x\n'.format(
    link_name=link_name, str_column_list=str_column_list, target_schema='dds')

print(insert_query)


# pprint(hub_satellites)
# print('='*50)
# for (hub_name, redundant), info in hub_satellites.items():
#         for source_table, task in info.items():
#             for source_table, task in info.items():
#                 print(hubs[hub_name][source_table] +'>>'+ task)


# for hub_name in YAML_DATA['groups']['satellites']:
#     print('='*50)
#     pprint(hub_name)
#     for sat, source_table in YAML_DATA['groups']['satellites'].items():
#         if hub_name == sat:
#             pass

# for table_name, table_info in YAML_DATA['sources']['tables'].items():
#     print('='*50)
#     pprint(table_name)
#     # pprint(table_info['columns'])
#     for column_info in table_info['columns']:
#         for info in column_info.values():
#             if info.get('source_for') == 'region':
#                 pprint(table_info['columns'])


# pprint(YAML_DATA['sources']['tables'])
# print('\n' + '='*50 + '\n')
# for link_name, link_info in YAML_DATA['groups']['links'].items():
#     pprint(f'link name: {link_name}')
#     for source_table, hubs_data in link_info.items():
#         pprint(f'source table: {source_table}')
#         pprint(f'hubs data: {hubs_data}')
#     print('='*50)


# for link_info in links.values():
#     for hub_name, info in link_info.items():
#         for source_table, task in info.items():
#             print(hubs[hub_name][source_table]+'>>'+task)

# pprint(hubs)
# print('\n' + '='*50 + '\n')
# pprint(default_hubs)
