# -*- coding: utf-8 -*-
__author__ = 'HymanLu'

from django.conf.urls import url, include
import xadmin
from APP_Inventor_case_base.settings import MEDIA_ROOT
from django.views.static import serve
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token
from cases.views import CasesListViewSet, CategoryViewset, HotSearchsViewset, BannerViewset
from cases.views import IndexCategoryViewset
from users.views import SmsCodeViewset, UserViewset, PictureCodeViewset
from user_operation.views import UserFavViewset, LeavingMessageViewset
from django.views.generic import TemplateView

router = DefaultRouter()    # 利用了ViewSet的重载as_view()方法进行请求方法和处理函数的动态绑定（简单好用，只需要逐一register，然后urls函数即可）
router.register(r'cases', CasesListViewSet, base_name="cases")      # 案例列表的相关操作
router.register(r'categorys', CategoryViewset, base_name="categorys")       # 案例类别的相关操作
router.register(r'smscodes', SmsCodeViewset, base_name="smscodes")    # 短信验证码的相关操作
#router.register(r'picturecodes', PictureCodeViewset, base_name="picturecodes")    # 图片验证码的相关操作
router.register(r'hotsearchs', HotSearchsViewset, base_name="hotsearchs")       # 热搜案例的相关操作
router.register(r'users', UserViewset, base_name="users")       # 用户的相关操作
router.register(r'userfavs', UserFavViewset, base_name="userfavs")      # 用户收藏的相关操作
router.register(r'messages', LeavingMessageViewset, base_name="messages")       # 用户留言的相关操作
router.register(r'banners', BannerViewset, base_name="banners")     # 轮播图的相关操作
router.register(r'indexcases', IndexCategoryViewset, base_name="indexcases")    # 首页案例的相关操作

urlpatterns = [
    url(r'^', include(router.urls)),        # 将调用刚才注册到router的各个ViewSet的as_view()方法，得到最终的URL映射配置
    url(r'^xadmin/', xadmin.site.urls),     # 注册xadmin后台管理平台的URL处理函数
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),     # 默认的通过账号和密码进行验证的方式(login和logout方法）
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),     # path 将作为第二参数传到server进行处理
    url(r'^index/', TemplateView.as_view(template_name="index.html"), name="index"),    # 网站的首页（现在流行SPA，即单页Web应用，因此一个HTML文件就足够了）
    url(r'docs/', include_docs_urls(title="APP Inventor案例库")),      # 自动生成的API说明文档
    url(r'^api-token-auth/', views.obtain_auth_token),      # drf自带的token认证模式（一般称为Session模式）
    url(r'^login/', obtain_jwt_token),      # jwt的认证接口（较之drf自带的认证模式，占用的服务器端资源更少，安全性更高）
]