# -------------------------------------------pickle存储配置-----------------------------------------------
GC_PICKLE_READ_FILE_PATH = "bugdata.pkl"  # pickle文件保存路径"C:/Users/Administrator/Desktop/grapbugfree/bugdata.pkl"
GC_PICKLE_SAVE_FILE_PATH = "bugdata.pkl"  # pickle文件读取路径"C:/Users/Administrator/Desktop/grapbugfree/bugdata.pkl"

# -------------------------------------------bugfree项目抓取配置-----------------------------------------------
GC_USER_NAME = u"admin"  # bugfree登录用户名
GC_PASSWORD = u"123456"  # bugfree登录账号
GC_URL_ROOT = "http://192.168.1.2:8081"  # 定义根地址目录
# 定义项目路径,注意末尾的【page=%s】用于字符串替换翻页，【/bug/list/8】为项目路径，【productmodule_id=4】为项目模块子路径
GC_URL_PROJECT = "/bugfree/index.php/bug/list/3?productmodule_id=7&page=%s"
GC_URL_PAGE_START = 1  # 开始页数
GC_URL_PAGE_END = 11  # 结束页数
GC_SCREEN_FLAG = True
GC_BUG_CREATE_BY = ""  # 筛选条件：创建者，"王工"，"李工"
GC_BUG_STATUS = ""  # 筛选条件：bug状态，"Active":"待修复","Resolved":"待验证","Closed":"已解决"
GC_BUG_UPDATED_AT = ""  # 筛选条件：修改时间，"2017-03-01"
