## Resource Library

## 安装
```
https://github.com/Tecode/resource_library.git

pip install pillow
pip install scrapy
pip install scrapy-splash
pip install pymysql
```

## 安装`Docker`,安装`splash`

```bash
sudo apt install docker.io
sudo systemctl start docker
sudo systemctl enable docker
docker -v

sudo docker pull scrapinghub/splash
sudo docker run -it -p 8050:8050 scrapinghub/splash
```

## 使用

### 进入文件夹输入`scrapy`,命令行有`scrawl`,如下图

```bash
amingdeMacBook-Pro:resource_library aming$ scrapy
Scrapy 2.2.0 - project: resource_library

Usage:
  scrapy <command> [options] [args]

Available commands:
  bench         Run quick benchmark test
  check         Check spider contracts
  commands      
  crawl         Run a spider
  edit          Edit spider
  fetch         Fetch a URL using the Scrapy downloader
  genspider     Generate new spider using pre-defined templates
  list          List available spiders
  parse         Parse URL (using its spider) and print the results
  runspider     Run a self-contained spider (without creating a project)
  settings      Get settings values
  shell         Interactive scraping console
  startproject  Create new project
  version       Print Scrapy version
  view          Open URL in browser, as seen by Scrapy

Use "scrapy <command> -h" to see more info about a command
```

### 命令

```
scrapy genspider name[baidu] webSite[http://baidu.com]
scrapy crowl [name]
```

## 注意

### `reptile/settings.py`修改你的图片存储的位置

```
# 保存图片地址
IMAGES_STORE = '/home/xm/testFile/spider/.vscode/images' #修改你的图片存储位置
```
