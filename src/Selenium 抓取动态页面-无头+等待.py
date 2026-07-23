from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# -------------------------- 浏览器配置（无头开关在这里） --------------------------
chrome_opt = Options()
# 取消下面这行注释 = 无头模式（后台运行，不弹出Chrome窗口）
# chrome_opt.add_argument("--headless=new")

# 启动Chrome
driver = webdriver.Chrome(options=chrome_opt)

# 访问网页
target_url = "https://quotes.toscrape.com/js/"
driver.get(target_url)

# -------------------------- 智能等待：页面加载完成再继续 --------------------------
# 最长等待10秒，直到 class="quote" 元素出现
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.CLASS_NAME, "quote")))

# 获取渲染完毕完整HTML
html_source = driver.page_source

# -------------------------- 保存到本地HTML文件 --------------------------
with open("render_page.html", "w", encoding="utf-8") as f:
    f.write(html_source)
print("✅ 页面源码已保存：render_page.html")
# 保存的本地 html 是相对路径引用 CSS，浏览器本地打开时，无法远程加载网页样式文件

# 关闭浏览器
driver.quit()