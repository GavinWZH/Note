# 异步任务

具体连接
https://mp.weixin.qq.com/s/yQlFs-6Fc237Qot3-64Qlg

## 1、安装RabbitMQ，这里我们使用RabbitMQ作为broker，安装完成后默认启动了，也不需要其他任何配置
```bash
sudo apt-get install rabbitmq-server
```

## 2、安装celry
```bash
sudo pip3 install celery
```

## 3、celery用在django项目中，项目settings.py同级目录下创建celery.py
```python
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery, platforms

# 项目名字mbp
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mbp.settings')

app = Celery('mbp')

app.config_from_object('django.conf:settings', namespace='CELERY')

# 自动发现所有任务
app.autodiscover_tasks()

# 允许root 用户运行celery
platforms.C_FORCE_ROOT = True


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
```

## 4、在settings.py同级目录下的__init__.py文件中添加以下内容，确保django启动的时候这个app能够被加载到
```python
from __future__ import absolute_import

from .celery import app as celery_app


__all__ = ['celery_app']
```

## 5、各个应用下创建tasks.py文件
```python
from __future__ import absolute_import
from celery import shared_task


@shared_task
def add(x, y):
    return x + y
```

+ 注意tasks.py必须建在各app的根目录下，且只能叫tasks.py，不能随意命名

## 6、在views.py中引用这个函数
```python
from apps.tasks import add


def post(request):
    result = add.delay(2, 3)
```

+ 使用函数名.delay()即可使函数异步执行

+ 可以通过result.ready()来判断任务是否完成处理

+ 如果任务抛出一个异常，使用result.get(timeout=1)可以重新抛出异常

+ 如果任务抛出一个异常，使用result.traceback可以获取原始的回溯信息

## 7、启动celery
```bash
celery -A mbp worker -l info
```