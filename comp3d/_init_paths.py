
""" Initialize Paths to project main modules
"""
import sys
import os
import os.path as osp

def addpath(path):
    sys.path.insert(0, path)

# Add Project folder and subfolders
project_folder =os.getcwd()
addpath(project_folder)
addpath(osp.join(project_folder, 'utils'))
addpath(osp.join(project_folder, 'models'))
addpath(osp.join(project_folder, 'data'))
addpath(osp.join(project_folder, 'utils/chamfer'))
addpath(osp.join(project_folder, 'utils/emd'))
