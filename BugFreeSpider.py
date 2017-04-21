from selenium import webdriver
from bs4 import BeautifulSoup
import selenium.webdriver.support.ui as ui
import PickleUtils
import GlobalConfig
import BugFreeBug

list_bugs = []  # 创建一个临时列表用于存放bug信息


def value_routine(att_value, html_detail):
    """得到某一个bug的常规值"""
    det_value = html_detail.findAll("label", {"for": att_value})[0].find_parent().contents[2].string
    det_value = det_value.strip()
    return det_value


def login_bugfree():
    """登录bugfree"""
    # 使用PhantomJS创建一个浏览器驱动
    driver = webdriver.PhantomJS()
    # 得到登录页面信息
    driver.get(GlobalConfig.GC_URL_ROOT + "/bugfree/index.php/site/login")
    # 最多等待10秒
    wait = ui.WebDriverWait(driver, 10)
    # 等待，直至页面显示用户名输入框
    wait.until(lambda dr: driver.find_element_by_id("LoginForm_username").is_displayed())
    # 得到用户名输入框，输入用户名
    driver.find_element_by_id("LoginForm_username").send_keys(GlobalConfig.GC_USER_NAME)
    # 得到密码输入框，输入密码
    driver.find_element_by_id("LoginForm_password").send_keys(GlobalConfig.GC_PASSWORD)
    # 得到登录按钮，触发点击事件
    driver.find_element_by_id("SubmitLoginBTN").click()
    # 等待，直至页面显示登录成功用户信息
    wait.until(lambda dr: driver.find_element_by_class_name("user-info").is_displayed())
    return driver


def bug_filter(bug_to_filter):
    """bug筛选"""
    # 筛选bug创建者
    if GlobalConfig.GC_BUG_CREATE_BY != "" and GlobalConfig.GC_BUG_CREATE_BY != bug_to_filter.created_by:
        return True
    # 筛选bug状态
    if GlobalConfig.GC_BUG_STATUS != "" and GlobalConfig.GC_BUG_STATUS != bug_to_filter.status:
        return True
    # 筛选bug修改日期
    if GlobalConfig.GC_BUG_UPDATED_AT != "" and GlobalConfig.GC_BUG_UPDATED_AT != bug_to_filter.updated_at:
        return True
    return False


def get_bug_list(driver_custom):
    """获取整个列表页面的bug信息，返回bug列表"""
    # 使用bs4解析页面html
    html = BeautifulSoup(driver_custom.page_source, "html.parser")
    # 得到所有的table元素
    bug_table = html.findAll("table", {"class": "items"})
    # 得到第一个table元素，并获取其下的所有tr元素
    ls_tr = bug_table[0].findAll("tr")

    # 循环便利所有tr元素
    for tr in ls_tr:
        span = tr.findAll("span", {"class": "title"})  # 得到tr元素下所有span

        if len(span) != 0:
            # 得到span下所有a标签
            a = span[0].findAll("a")
            # 得到a标签下href的属性值，即bug地址。href:/bugfree/index.php/bug/613
            str_href = a[0]['href']
            # 获取bug详细信息
            driver_custom.get(GlobalConfig.GC_URL_ROOT + str_href)
            # 解析bug详细信息页面html
            html_detail = BeautifulSoup(driver_custom.page_source, "html.parser")
            # 得到bug标题input元素
            bug_input = html_detail.findAll("input", {"id": "BugInfoView_title"})[0]
            # 得到bug标题title
            bug_info = bug_input['title']
            # 得到所有常规信息span元素
            bug_id = html_detail.findAll("span", {"id": "span_info_id"})[0].get_text()
            # 得到状态
            bug_status = value_routine("BugInfoView_bug_status", html_detail)
            # 得到严重程度
            bug_severity = value_routine("BugInfoView_severity", html_detail)
            # 得到优先级
            bug_priority = value_routine("BugInfoView_priority", html_detail)
            # 得到创建人
            bug_created_by = value_routine("BugInfoView_created_by", html_detail)
            # 得到创建时间
            bug_created_at = value_routine("BugInfoView_created_at", html_detail)
            # 得到修复方案
            bug_solution = value_routine("BugInfoView_solution", html_detail)
            # 得到修改日期
            bug_updated_at = value_routine("BugInfoView_updated_at", html_detail)

            # 得到所有注释元素fieldset
            tag_fieldset = html_detail.findAll("fieldset", {"id": "fieldset_comment"})[0]
            # 得到注释存放元素blockquote列表
            tag_comments = tag_fieldset.findAll("blockquote")
            # 定义一个临时列表
            list_temp = []
            # 遍历注释tag列表
            for comment in tag_comments:
                # 得到某一条注释的字符串
                str_com = comment.get_text()
                # 将字符串存入临时列表
                list_temp.append(str_com)

            # 附件列表用于临时存放
            list_href_file = []
            # 拿到所有附件div
            div_files_upload = html_detail.findAll("div", {"id": "uploaded_file"})[0]
            # 拿到所有附件span
            span_files_upload = div_files_upload.findAll("span")
            # 便利附件span
            for span in span_files_upload:
                # 拿到附件href，得到附件下载链接
                href_img = GlobalConfig.GC_URL_ROOT + span.findAll("a")[0]['href']
                # 将附件下载地址添加到临时列表中
                list_href_file.append(href_img)

            # 创建一个BugFreeBug对象，设置对象初始值
            bug_custom = BugFreeBug.BugFreeBug(bug_id, bug_info, str_href, bug_status, bug_severity, bug_priority,
                                               bug_created_by, bug_created_at, bug_solution, list_temp,
                                               list_href_file, bug_updated_at)
            # 筛选条件
            if GlobalConfig.GC_SCREEN_FLAG:
                if bug_filter(bug_custom):
                    continue

            # 存入临时数组
            list_bugs.append(bug_custom)


if __name__ == "__main__":
    """主方法"""
    # 登录bugfree
    print("开始登陆bugfree......")
    driver_main = login_bugfree()
    print("完成用户登陆，开始抓取数据......")
    # 进入某个项目路径
    for page_num in range(GlobalConfig.GC_URL_PAGE_START, GlobalConfig.GC_URL_PAGE_END):
        # 翻页
        driver_main.get(GlobalConfig.GC_URL_ROOT + GlobalConfig.GC_URL_PROJECT % page_num)
        # 获取整个列表页面的bug信息
        get_bug_list(driver_main)
        print("已抓取%d条数据" % len(list_bugs))

    print("抓取数据完成，共抓取%d条数据" % len(list_bugs))
    # 退出浏览器驱动
    driver_main.quit()
    list_bugs.reverse()
    # 保存数据
    PickleUtils.save_obj(list_bugs)
