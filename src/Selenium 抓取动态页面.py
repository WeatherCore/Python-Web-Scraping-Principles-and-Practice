from selenium import webdriver

# 启动Chrome浏览器
driver = webdriver.Chrome()

# 访问目标网址
driver.get("https://quotes.toscrape.com/js/")

# 获取渲染完成后的完整网页源码
html = driver.page_source
print(html)

# -------------------------- 保存到本地HTML文件 --------------------------
with open("render_page.html", "w", encoding="utf-8") as f:
    f.write(html)
print("✅ 页面源码已保存：render_page.html")
# 保存的本地 html 是相对路径引用 CSS，浏览器本地打开时，无法远程加载网页样式文件

# 关闭浏览器
driver.quit()