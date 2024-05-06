#################################### 
#    File Name: compute_cd.py
#    Author: trebladev
#    E-mail: flexiblexuan@gmail.com
#    Brief: Compute chamfer distance between two point clouds.
####################################


import time
import os
import sys
import argparse
try:
    import point_cloud_utils as pcu
except ImportError:
    raise ImportError( 'Please install package with `pip install point-cloud-utils`.')

def argments():
    parser = argparse.ArgumentParser()
    parser.add_argument('source_file', type=str, help="source ply file name")
    parser.add_argument('target_file', type=str, help="target ply file name")
    return parser.parse_args()

def compute_chamfer_distance(source, target, quite=False):
    if not os.path.exists(source):
        raise FileNotFoundError(f'{source} not found')
    if not os.path.exists(target):
        raise FileNotFoundError(f'{target} not found')
    
    if not quite:
        print('---------------------------------------------------------')
        print('-------Compute chamfer distance on xyz point cloud-------')
        print('---------------------------------------------------------\n')
    v1, _ = pcu.load_mesh_vf(source)
    v2, _ = pcu.load_mesh_vf(target)
    if not quite:
        print(f'{source}  SIZE: {v1.shape[0]}')
        print(f'{target}  SIZE: {v2.shape[0]}\n')
    return pcu.chamfer_distance(v1, v2) 

if __name__ == '__main__':
    config = argments()
    ret = compute_chamfer_distance(config.source_file, config.target_file)
    print(f'Chamfer distance: {ret}')