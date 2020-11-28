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

```
pip --default-timeout=1000 install -U requests
```

### run `download_video.py` 视频批量下载

```
F:/自考学习课程/离散数学/第一部分 数理逻辑篇/

1.2 命题公式的等值演算(2).mp4: 4.58% 下载速度: 1.00M/S
1.2 命题公式的等值演算(2).mp4: 6.87% 下载速度: 0.50M/S
1.2 命题公式的等值演算(2).mp4: 9.16% 下载速度: 0.50M/S
1.2 命题公式的等值演算(2).mp4: 11.44% 下载速度: 0.50M/S
1.2 命题公式的等值演算(2).mp4: 18.31% 下载速度: 1.50M/S
1.2 命题公式的等值演算(2).mp4: 22.89% 下载速度: 1.00M/S
1.2 命题公式的等值演算(2).mp4: 29.75% 下载速度: 1.50M/S
1.2 命题公式的等值演算(2).mp4: 36.62% 下载速度: 1.50M/S
1.2 命题公式的等值演算(2).mp4: 45.77% 下载速度: 2.00M/S
1.2 命题公式的等值演算(2).mp4: 50.35% 下载速度: 1.00M/S
1.2 命题公式的等值演算(2).mp4: 52.64% 下载速度: 0.50M/S
1.2 命题公式的等值演算(2).mp4: 56.94% 下载速度: 0.94M/S
1.2 命题公式的等值演算(2).mp4: 57.22% 下载速度: 0.06M/S
1.2 命题公式的等值演算(2).mp4: 64.08% 下载速度: 1.50M/S
1.2 命题公式的等值演算(2).mp4: 66.37% 下载速度: 0.50M/S
1.2 命题公式的等值演算(2).mp4: 68.66% 下载速度: 0.50M/S
```