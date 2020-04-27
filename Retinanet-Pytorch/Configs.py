# -*- coding: utf-8 -*-
# @Author  : LG
from yacs.config import CfgNode as CN
import os

project_root = os.getcwd()

_C = CN()


_C.FILE = CN()

_C.FILE.PRETRAIN_WEIGHT_ROOT = project_root+'/Weights/pretrained'   # 会使用到的预训练模型
_C.FILE.MODEL_SAVE_ROOT = project_root+'/Weights/trained152'           # 训练模型的保存
# _C.FILE.VGG16_WEIGHT = 'vgg16_reducedfc.pth'                      # vgg预训练模型

_C.DEVICE = CN()

_C.DEVICE.MAINDEVICE = 'cuda:0' # 主gpu
_C.DEVICE.TRAIN_DEVICES = [0,1,2,3] # 训练gpu
_C.DEVICE.TEST_DEVICES = [0,1,2,3]  # 检测gpu

_C.MODEL = CN()
_C.MODEL.BASEMODEL = 'resnet152' # 现支持 resnet18, resnet34, resnet50, resnet101, resnet152

_C.MODEL.INPUT = CN()
_C.MODEL.INPUT.IMAGE_SIZE = 600 # 模型输入尺寸

_C.MODEL.ANCHORS = CN()
_C.MODEL.ANCHORS.FEATURE_MAPS = [(75, 75), (38, 38), (19, 19), (10, 10), (5, 5)]  # fpn输出的特征图大小
_C.MODEL.ANCHORS.SIZES = [32, 64, 128, 256, 512]
_C.MODEL.ANCHORS.NUMS = 9
_C.MODEL.ANCHORS.RATIOS = [0.5, 1, 2]    # 不同特征图上检测框绘制比例
_C.MODEL.ANCHORS.SCALES = [2 ** 0, 2 ** (1.0 / 3.0), 2 ** (2.0 / 3.0)]    # 不同特征图上检测框绘制比例
_C.MODEL.ANCHORS.CLIP = True            # 越界检测框截断,0~1
_C.MODEL.ANCHORS.THRESHOLD = 0.5        # 交并比阈值
_C.MODEL.ANCHORS.CENTER_VARIANCE = 0.1  # 解码
_C.MODEL.ANCHORS.SIZE_VARIANCE = 0.2    # 解码

_C.TRAIN = CN()

_C.TRAIN.NEG_POS_RATIO = 3      # 负正例比例
_C.TRAIN.MAX_ITER = 20000      # 训练轮数
_C.TRAIN.BATCH_SIZE = 20        # 训练批次

_C.MULTIBOXLOSS = CN()
_C.MULTIBOXLOSS.ALPHA = 0.25    # focal loss 阿尔法参数,用于调节背景与目标比例
_C.MULTIBOXLOSS.GAMMA = 2       # focal loss 伽马参数  ,用于调节难易样本影响

_C.OPTIM = CN()

_C.OPTIM.LR = 1e-3              # 初始学习率.默认优化器为SGD
_C.OPTIM.MOMENTUM = 0.9         # 优化器动量.默认优化器为SGD
_C.OPTIM.WEIGHT_DECAY = 5e-4    # 权重衰减,L2正则化.默认优化器为SGD

_C.OPTIM.SCHEDULER = CN()       # 默认使用MultiStepLR
_C.OPTIM.SCHEDULER.GAMMA = 0.1  # 学习率衰减率
_C.OPTIM.SCHEDULER.LR_STEPS = [8000, 10000]


_C.MODEL.TEST = CN()

_C.MODEL.TEST.NMS_THRESHOLD = 0.5               # 非极大抑制阈值
_C.MODEL.TEST.CONFIDENCE_THRESHOLD = 0.1        # 分数阈值,
_C.MODEL.TEST.MAX_PER_IMAGE = 100               # 预测结果最大保留数量
_C.MODEL.TEST.MAX_PER_CLASS = -1                # 测试时,top-N


_C.DATA = CN()

# 由于在使用时,是自己的数据集.所以这里,并没有写0712合并的数据集格式,这里以VOC2007为例
_C.DATA.DATASET = CN()
_C.DATA.DATASET.NUM_CLASSES =6
_C.DATA.DATASET.CLASS_NAME = ('__background__', 'bicycle', 'bus', 'car', 'motorbike', 'person')

_C.DATA.DATASET.DATA_DIR = '/home/chenshuo/RTTS/'   # 数据集voc格式,根目录
_C.DATA.DATASET.TRAIN_SPLIT = 'train'   # 训练集,对应于 /VOCdevkit/VOC2007/ImageSets/Main/train.txt'
_C.DATA.DATASET.TEST_SPLIT = 'test'      # 测试集,对应于 /VOCdevkit/VOC2007/ImageSets/Main/val.txt'
_C.DATA.PIXEL_MEAN = [0.471, 0.448, 0.408]  #数据集均值   用于数据增强部分,依数据集修改即可
_C.DATA.PIXEL_STD = [0.234, 0.239, 0.242]   # 数据集方差

_C.DATA.DATALOADER = CN()


_C.STEP = CN()
_C.STEP.VIS_STEP = 10           # visdom可视化训练过程,打印步长
_C.STEP.MODEL_SAVE_STEP = 1000  # 训练过程中,模型保存步长
_C.STEP.EVAL_STEP = 1000        # 在训练过程中,并没有进行检测流程,建议保存模型后另外检测