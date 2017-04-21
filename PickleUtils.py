import GlobalConfig
import pickle


def save_obj(obj_custom):
    """存储对象"""
    print("已将pickle文件保存在:%s" % GlobalConfig.GC_PICKLE_SAVE_FILE_PATH)
    f = open(GlobalConfig.GC_PICKLE_SAVE_FILE_PATH, "wb")
    pickle.dump(obj_custom, f)
    f.close()


def load_obj():
    """读取、返回对象"""
    print("正在读取pickle文件:%s" % GlobalConfig.GC_PICKLE_READ_FILE_PATH)
    f = open(GlobalConfig.GC_PICKLE_READ_FILE_PATH, "rb")
    obj_custom = pickle.load(f)
    return obj_custom
