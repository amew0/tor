from ultralytics import YOLO
import yaml
import random
import copy

def load_yaml(path_yaml):
    with open(path_yaml, 'r') as file:
        data = yaml.safe_load(file)
    return data

def dump_yaml(data, path_yaml):
    # Write the YAML content to a file
    with open(path_yaml, 'w') as file:
        yaml.dump(data, file)

def size_ss(ss):
    size = 1
    for _, v in ss.items():
        for _ in range(v[0]):
            for subv in v[1:]:
                size *= len(subv) if isinstance(subv, list) else 1      
    return size

def select_cfg(ss):
    selected_cfg = {}
    for k, v in ss.items():
        selected_ = []
        for _ in range(v[0]):
            selected = [random.choice(subv) if isinstance(subv, list) else subv for subv in v[1:]]
            selected_.append(selected)
        selected_cfg[k] = selected_
    return selected_cfg

def create_cfg(cfg, selected_cfg):
    for i,row in enumerate(cfg['backbone'] + cfg['head']):
        m = row[2]
        try:
            arg = selected_cfg[m].pop(0)
        except IndexError:
            # nothing to pop (empty list)
            pass
        if arg == ['?']:
            # TODO
            continue
        if i >= len(cfg['backbone']) and m == 'C2f':
            # in head
            arg = arg[:-1]
        row[-1] = arg
    return cfg