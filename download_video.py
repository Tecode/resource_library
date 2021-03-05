# 下载视频课程
#
# 放入["title":"","src":""]格式数据会按文件夹下载文件
import os
import re
import requests
import time

"""
var list = document.getElementsByClassName('title')
var playList = []
for(var index=0; index < list.length; index ++) {
  list[index].onclick = function(){
		var self = this
		setTimeout(function(){
			playList.push({title:self.lastChild.title,src:document.getElementsByTagName('video') && document.getElementsByTagName('video').length > 0 && document.getElementsByTagName('video')[0].src})
    	console.log(playList,'-----------')
		},5000)
  }
}
"""

# 计算机系统结构精讲
listData = [{"title": "引言",
             "src": "http://b2cstream.edu-edu.com/c231f9b90c544d8696b7ac3b63dbaec8/7e426e0770314af2b180840a8d84c31c-185536ce26bdf2321e739fa2ffc23661-fd.mp4"},
            {"title": "第一章 概论",
             "src": "http://b2cstream.edu-edu.com/c231f9b90c544d8696b7ac3b63dbaec8/7e426e0770314af2b180840a8d84c31c-185536ce26bdf2321e739fa2ffc23661-fd.mp4"},
            {"title": "1.1 计算机系统的层次结构",
             "src": "http://b2cstream.edu-edu.com/73e5065e7dd0464f9341fc43ea3bf147/17a0c29501b0472fbc6b3db745fe6c0f-28de1e0ae7c2a2ab20d5343a4b7b6c39-fd.mp4"},
            {"title": "1.2 计算机系统结构、计算机组成与计算机实现",
             "src": "http://b2cstream.edu-edu.com/258f335e4192456c92b1b4d70673876e/ee183bec46b84417b42b774cdb26a843-325f900795f7567025896c65121266fe-fd.mp4"},
            {"title": "1.3 计算机系统的软硬取舍与定量设计原理（一）",
             "src": "http://b2cstream.edu-edu.com/4f56e435252f4b1a9b6daf647c897d43/1f78792b692a4f74b6e8577e57bfb0b0-6cab8587c7f47c34f1639271e146ea7c-fd.mp4"},
            {"title": "1.3 计算机系统的软硬取舍与定量设计原理（二）",
             "src": "http://b2cstream.edu-edu.com/2f4318f87e124832a3c4863be398db4c/560baaadcf6142b6bc19e4580e63d2c1-d59be1d222a7784a4f4ed1dae8722b34-fd.mp4"},
            {"title": "1.4 软件、应用、器件的发展对系统结构的影响",
             "src": "http://b2cstream.edu-edu.com/4a346ff2bc394be898d32fb4bd1a9ed6/8ffc4082244c4291881f76a6cd10a878-0e0397bc96088c2fee4304557373272a-fd.mp4"},
            {"title": "1.5 系统结构中的并行性开发及计算机系统的分类",
             "src": "http://b2cstream.edu-edu.com/369f3f0768514ef78b218560cf5f394e/407a624df6d5468eae4191b26c6bd257-8f7ed620994b81c6f5dbf062eab16fed-fd.mp4"},
            {"title": "第二章 数据表示、寻址方式、指令系统",
             "src": "http://b2cstream.edu-edu.com/369f3f0768514ef78b218560cf5f394e/407a624df6d5468eae4191b26c6bd257-8f7ed620994b81c6f5dbf062eab16fed-fd.mp4"},
            {"title": "2.1 数据表示（一）",
             "src": "http://b2cstream.edu-edu.com/55d601c25d7b47038f8ddcd0b11c6672/1a11cf1cc8ea49fc933d166321503d29-24b8d8fbee93cc05704bc84fad2df723-fd.mp4"},
            {"title": "2.1 数据表示（二）",
             "src": "http://b2cstream.edu-edu.com/f23be4fad76c458cbd9578af0391c5e6/d7514952a9134ae88c58956a01b2de95-9a01b1a74113eaf78aa153776d4bc138-fd.mp4"},
            {"title": "2.1 数据表示（三）",
             "src": "http://b2cstream.edu-edu.com/f3486a1b03544259b08f2540fe105f1c/b24a9d96e2b54918a384542ccee3530e-1510ebad46af7a428cabc763594ee4c3-fd.mp4"},
            {"title": "2.1 数据表示（四）",
             "src": "http://b2cstream.edu-edu.com/a02c78c5c9c748b0a982657ed3ce5954/9a711cf536f44051a716a977addb28c9-e30dc9ffd9bb7f1b3fff73f1e075e276-fd.mp4"},
            {"title": "2.2 寻址方式（一）",
             "src": "http://b2cstream.edu-edu.com/503a75e6523a4c958c60783d723f00b5/9247f70bb13f4d5ab360b86234ddd471-0b3887c9d056a809a937bd9148367280-fd.mp4"},
            {"title": "2.2 寻址方式（二）",
             "src": "http://b2cstream.edu-edu.com/48e6afb5c0b344188c722060a0983a40/a3077605c0994a938c82ff109fd9d2a4-7f4d9da4b5b00a2d2c0a76cbb8ac1770-fd.mp4"},
            {"title": "2.3 指令系统的设计和优化（一）",
             "src": "http://b2cstream.edu-edu.com/a4fb04abde244f49bfcb2a82858994a5/87c6bc4df45d405c83f63c0f6b1326c8-caa8ab40b9174301ae397ca6ae8307c6-fd.mp4"},
            {"title": "2.3 指令系统的设计和优化（二）",
             "src": "http://b2cstream.edu-edu.com/ae9f19fb69d7472c8b5187911239beb5/a8e90ec905e24cbbaac796884cdd30d2-35a1515587f09f977af3c3cc6f4b4e4d-fd.mp4"},
            {"title": "2.3 指令系统的设计和优化（三）",
             "src": "http://b2cstream.edu-edu.com/e0546415efc84d41aca0a81aa2304363/937d196071394cdaa79b9d4668e43dbd-27d4290871d8443131133921e93511f4-fd.mp4"},
            {"title": "2.3 指令系统的设计和优化（四）",
             "src": "http://b2cstream.edu-edu.com/bf16270395d747e1ba03b77fc9f71870/f1bacc429c7d40328ed37f0e4bedb27a-6ad427078e6a61a3191d2dac0e016e5e-fd.mp4"},
            {"title": "2.4 指令系统的发展和改进（一）",
             "src": "http://b2cstream.edu-edu.com/54f58b65a5d34805abd16c2f5a673907/466477e2011e42dcac35d785b8e63276-951e1f2062516fdb755acda398c4af7d-fd.mp4"},
            {"title": "2.4 指令系统的发展和改进（二）",
             "src": "http://b2cstream.edu-edu.com/73fe4e678a774707a270f52e91c1ed84/1f55fb3a18bd4f95a711437fb6fa19e0-23431707b774f0f3067361f70e786141-fd.mp4"},
            {"title": "2.4 指令系统的发展和改进（三）",
             "src": "http://b2cstream.edu-edu.com/8a88d35ad4924bc2bca7800e3b36ee97/5ead9bbd97804e5884639c800b61a409-f5a5cb9d1170fadf356a9ded31b0fb92-fd.mp4"},
            {"title": "第三章 存储、中断、总线与I-O系统",
             "src": "http://b2cstream.edu-edu.com/8a88d35ad4924bc2bca7800e3b36ee97/5ead9bbd97804e5884639c800b61a409-f5a5cb9d1170fadf356a9ded31b0fb92-fd.mp4"},
            {"title": "3.1 存储系统的基本要求和并行主存系统",
             "src": "http://b2cstream.edu-edu.com/651130261d3c4a4bbea76c81a6b3f966/98f4e4a98a0140bd981b5cc178e36463-c5db9a1360c0c2c899825df618d79e05-fd.mp4"},
            {"title": "3.2 中断系统",
             "src": "http://b2cstream.edu-edu.com/9435360edca24e2a856695708cb6ebc1/11c20c5364da4d949071dfb93f6eb479-1168692ebc9e83de568e137791ac2e03-fd.mp4"},
            {"title": "3.3 总线系统",
             "src": "http://b2cstream.edu-edu.com/7a0409bb5ebf433e931252d658cdc5aa/637ed54086724bd89cf11640bed7218c-6e5582b524258a5c1af5214c927051ca-fd.mp4"},
            {"title": "3.4 I-O系统（一）",
             "src": "http://b2cstream.edu-edu.com/53948fd0b70541d782ac7a12f7b0d3a3/16cafd316e764847bcc85391f8234dbc-7ffa921deef9125e62e3149a580462be-fd.mp4"},
            {"title": "3.4 I-O系统（二）",
             "src": "http://b2cstream.edu-edu.com/78be1729417a4ba3b4e8aac279fb8e70/72750d747fa74108b836c9cdbb622c3f-89a915276b54e675f2487ce889c81916-fd.mp4"},
            {"title": "第四章 存储体系",
             "src": "http://b2cstream.edu-edu.com/78be1729417a4ba3b4e8aac279fb8e70/72750d747fa74108b836c9cdbb622c3f-89a915276b54e675f2487ce889c81916-fd.mp4"},
            {"title": "4.1 基本概念",
             "src": "http://b2cstream.edu-edu.com/7994ebf0e48d478fb517255dcc7d43b1/972eb031dec64323bf76fbb9593079b8-249a9d9e555b800a79e3a8c4d92692ad-fd.mp4"},
            {"title": "4.2 虚拟存储器（一）",
             "src": "http://b2cstream.edu-edu.com/6663503935f64a85ab462d73a0c02cba/16cdc56cfeee4e5a8d33a88610664cce-238f7a79125d1e9f51045515bd53c84b-fd.mp4"},
            {"title": "4.2 虚拟存储器（二）",
             "src": "http://b2cstream.edu-edu.com/f43f3ef6913c4a82b23f2fb6ffab39d8/2426be81d6cc49ebbde45d2d1c0bbafc-92b355a144c1a0569f723272814452d9-fd.mp4"},
            {"title": "4.2 虚拟存储器（三）",
             "src": "http://b2cstream.edu-edu.com/6d142799f4c94947b5134ee552c0fc77/6216d47801994c12bf263fe31c9f271d-6c3df47ce86112e652d04c57f428c324-fd.mp4"},
            {"title": "4.3 高速缓冲存储器（一）",
             "src": "http://b2cstream.edu-edu.com/36d44842959146fa9a518a035c322524/1611f6f98da44cbe8ac6493fdd1e61d3-60d503ecf6133b817de1bff5d2506980-fd.mp4"},
            {"title": "4.3 高速缓冲存储器（二）",
             "src": "http://b2cstream.edu-edu.com/e1c2412e461b4adbaf5cb4661271250b/cec2ac5a5fd544efa5f7c3e3798a3677-3a11e3220b840fcd00fb75d6a97f23f8-fd.mp4"},
            {"title": "4.4 三级存储体系",
             "src": "http://b2cstream.edu-edu.com/cc385ddce59844b58a5ca1ad52952efb/51b73d3bd05b41f0b239f21ed63e4bf5-7cf14c8ca62f9c641ecf3382fe6dc834-fd.mp4"},
            {"title": "第五章 标量处理机",
             "src": "http://b2cstream.edu-edu.com/cc385ddce59844b58a5ca1ad52952efb/51b73d3bd05b41f0b239f21ed63e4bf5-7cf14c8ca62f9c641ecf3382fe6dc834-fd.mp4"},
            {"title": "5.1 重叠方式",
             "src": "http://b2cstream.edu-edu.com/9f9c53bfe0044c0f94e1026bdd89d4c6/af3bce288a9f4eff9e9eb124088988a9-7444944cb7e9ae8e992af3699c30a534-fd.mp4"},
            {"title": "5.2 流水方式（一）",
             "src": "http://b2cstream.edu-edu.com/a2221de7fff44cc1915b6d2beaa8275c/a798cf8c309340e887bab5836341b2de-1e5bccd19482170ab9aae0f84cfa2157-fd.mp4"},
            {"title": "5.2 流水方式（二）",
             "src": "http://b2cstream.edu-edu.com/83984f1dcf72400381070ee3ee02be11/5ed9db2b81f040f1a94f5deaf7b40103-cbab7c33b5613f703fc8c0b6a70fd32c-fd.mp4"},
            {"title": "5.2 流水方式（三）",
             "src": "http://b2cstream.edu-edu.com/2dbc492ea20341f7a49a9960387061c4/85eeca1ebc2446d9835a396db9189c42-af065f53cb5cb180f729a11ebf6018f2-fd.mp4"},
            {"title": "5.2 流水方式（四）",
             "src": "http://b2cstream.edu-edu.com/566113e0233745b3ac8e36d1fa3f0ae0/1de92d6e43874c5c88cf837f50948d95-406ce2f5f341301588dbab545a52b057-fd.mp4"},
            {"title": "5.2 流水方式（五）",
             "src": "http://b2cstream.edu-edu.com/dd65b11eeca1469aabf34675691cc669/0fe30426c8434c6485736a394dfc755a-aabb00761b02686b8df527be44e974e2-fd.mp4"},
            {"title": "5.2 流水方式（六）",
             "src": "http://b2cstream.edu-edu.com/ee1ea31d00584a5182b3f0a0a2b408ec/514a283c7ca04775a193c165b09fbb94-d71c5f68fc1d319a5c15101634acf63f-fd.mp4"},
            {"title": "5.3 指令级高度并行的超级处理机",
             "src": "http://b2cstream.edu-edu.com/d11a6abcb6094436812ed8c001dbc490/ebc1ec56bca24a768365bba046bd5d8e-03ff7e1ad101a99c4638cb701523c790-fd.mp4"},
            {"title": "第六章 向量处理机",
             "src": "http://b2cstream.edu-edu.com/d11a6abcb6094436812ed8c001dbc490/ebc1ec56bca24a768365bba046bd5d8e-03ff7e1ad101a99c4638cb701523c790-fd.mp4"},
            {"title": "6.1 向量的流水处理与向量流水处理机",
             "src": "http://b2cstream.edu-edu.com/e1020e0a48d848d194a472741ebe5e07/d707631054a14e038eafdac500124937-adfbff80f0cf077a3bfa04f5278e74a3-fd.mp4"},
            {"title": "6.2 阵列处理机的原理",
             "src": "http://b2cstream.edu-edu.com/1d41152df76142c7ad4180a3d2a005a8/ee66dca122064396867cec8ffc5fd145-3cabb273d47b3b06c4fc1d7805b7e9e1-fd.mp4"},
            {"title": "6.3 SIMD计算机的互连网络",
             "src": "http://b2cstream.edu-edu.com/cf96d3bfe0a74c97ac01938cbc45f781/f9542db659664fe5929a32b6634fdfdb-55a3aca5fb5a3dd345a969953f41b325-fd.mp4"},
            {"title": "6.4 共享主存构形的阵列处理机中并行存储器的无冲突访问",
             "src": "http://b2cstream.edu-edu.com/66cedc0475894c05bbef93464ce8d7a0/fc1b67f2c0ac4036ac2f7908b583d5a7-5fc6000a7b4781f821f5090a2b410118-fd.mp4"},
            {"title": "6.5 脉动阵列流水处理机",
             "src": "http://b2cstream.edu-edu.com/81e7ab9cd610452f9ed9e1d0c36d7dfc/bfed5f688d12498fa69c164803f421d4-e268bcd128cebf16da42ea682a8fc538-fd.mp4"},
            {"title": "第七章 多处理机MIMD",
             "src": "http://b2cstream.edu-edu.com/81e7ab9cd610452f9ed9e1d0c36d7dfc/bfed5f688d12498fa69c164803f421d4-e268bcd128cebf16da42ea682a8fc538-fd.mp4"},
            {"title": "7.1 多处理机的概念、问题和硬件结构（一）",
             "src": "http://b2cstream.edu-edu.com/0df93c48129d421aa9e331da017d6f28/c345d92882514152a684d9eb22248098-961a5f09a38b919affd4d9c1ecbc06d3-fd.mp4"},
            {"title": "7.1 多处理机的概念、问题和硬件结构（二）",
             "src": "http://b2cstream.edu-edu.com/cb27fa0618df49bb9094646e35edfcf6/590e7a78f30e4efdac85526591ef345f-c3747e7b3945c16ffdb9af226efcd869-fd.mp4"},
            {"title": "7.2 紧耦合多处理机多Cache的一致性问题",
             "src": "http://b2cstream.edu-edu.com/6c8143dde1b5499aa3851c12054c9852/a95c47351401492998fa11fe04738a6a-bc3a33e3f9f34328f2c7008d83106cf3-fd.mp4"},
            {"title": "7.3 多处理机的并行性和性能（一）",
             "src": "http://b2cstream.edu-edu.com/25d177f99fea461da8e3ac702ace1fed/e3b118707378418ea8543d17621c8ef0-951f49ea8a1e304d668be1fc1a04ce54-fd.mp4"},
            {"title": "7.3 多处理机的并行性和性能（二）",
             "src": "http://b2cstream.edu-edu.com/4f4814ed4fb0468b8d44fd6c70931c4c/1bc67db7c1ad4cf6b26b2f48fb3ca9ae-257e39b0fa90568d58b0afd5795c1ef7-fd.mp4"},
            {"title": "7.3 多处理机的并行性和性能（三）",
             "src": "http://b2cstream.edu-edu.com/437b27d7efbe43a088036e5b9368b23c/5ee96aeb457743419ee732f99094160e-9171267037a3cf9eb7608f661a8dba47-fd.mp4"},
            {"title": "7.4 多处理机的操作系统",
             "src": "http://b2cstream.edu-edu.com/4358b4deb7964353ac41588d2e890e73/88773e0726ac40d687ce531d53f3d657-aa24ebb54ea6b99570299dcc5539ea71-fd.mp4"},
            {"title": "7.5 多处理机的发展",
             "src": "http://b2cstream.edu-edu.com/e32a527331e44e53b655bafd7d77e5a7/8535ef9706734db4b3b2a3df1b22f77a-309a07735322e3b67f0e12c534f08f9c-fd.mp4"},
            {"title": "第八章  数据流计算机和归约机",
             "src": "http://b2cstream.edu-edu.com/e32a527331e44e53b655bafd7d77e5a7/8535ef9706734db4b3b2a3df1b22f77a-309a07735322e3b67f0e12c534f08f9c-fd.mp4"},
            {"title": "8 数据流计算机和归约机",
             "src": "http://b2cstream.edu-edu.com/3b9104e908064201acd681bd001b62ce/91fd874ae034498d96f29e953dd34424-0ef56d9441d7463706cb170ffaeb0012-fd.mp4"}]


# 数据库系统原理精讲（2018版）
"""
listData = [
  {
    "title": "课程导学",
    "src": "http://b2cstream.edu-edu.com/0247148d9ce34e4db0b36b855be5911d/96c328c12e044569b6389077d79bd5aa-870cf29459e8f8fdaca8d8b81680ef3d-fd.mp4"
  },
  {
    "title": "第一章 数据库系统概述",
    "src": "http://b2cstream.edu-edu.com/0247148d9ce34e4db0b36b855be5911d/96c328c12e044569b6389077d79bd5aa-870cf29459e8f8fdaca8d8b81680ef3d-fd.mp4"
  },
  {
    "title": "第—节 数据库基本概念",
    "src": "http://b2cstream.edu-edu.com/e7c4f25a05fd47e682d7238f6d578543/21f9b65079014d699b333e0d922938fa-286f612c3c212b183a602fe1c1687ff0-fd.mp4"
  },
  {
    "title": "第二节 数据管理技术的发展",
    "src": "http://b2cstream.edu-edu.com/161bb5eb368f4042b1bd4660630dd031/66f7982e3a014adba12cd9bfdbcec3a5-5d7535d71a89d32e7c4bf6eeb71e4f90-fd.mp4"
  },
  {
    "title": "第三节 数据库系统的结构",
    "src": "http://b2cstream.edu-edu.com/e02a74bd76fd44f69525341d8c9e4927/c932736b8568422d94f30f754d1ea5f2-25b95c2e73fd38d1b3ef941d8f8e1ba1-fd.mp4"
  },
  {
    "title": "第四节 数据模型",
    "src": "http://b2cstream.edu-edu.com/507f728c60534753b1f2cd91b311bfa3/c0633424d6564ce493f99c138762ea32-9dc487d2d0f344dfecfeac353de9659a-fd.mp4"
  },
  {
    "title": "第二章 关系数据库",
    "src": "http://b2cstream.edu-edu.com/507f728c60534753b1f2cd91b311bfa3/c0633424d6564ce493f99c138762ea32-9dc487d2d0f344dfecfeac353de9659a-fd.mp4"
  },
  {
    "title": "第一节 关系数据库概述",
    "src": "http://b2cstream.edu-edu.com/5d81c761dcbc42099654ee64eca3db93/ccca16e25a4d444b98a7877235c7d5f9-62bbfc721feaf2646283d0157895f986-fd.mp4"
  },
  {
    "title": "第二节 关系数据模型（1）",
    "src": "http://b2cstream.edu-edu.com/7d5b76e267f24f049b2237a87fca4acd/5e169c63089a4e9da0937c5b35be7328-919e5410d91b7fb2b1ca02bd0056e929-fd.mp4"
  },
  {
    "title": "第二节 关系数据模型（2）",
    "src": "http://b2cstream.edu-edu.com/ae2f13befe8e482097321f6a14bf7763/84fd9efded1b49a5a7ca569542e2ec1d-742cec33b16e48581371243c98968e33-fd.mp4"
  },
  {
    "title": "第三节 关系数据库的规范化理论",
    "src": "http://b2cstream.edu-edu.com/dd61d5c063fa4a52b2c95acc326f8c01/262f9cb3c3714f31974ac745b79be633-c2dc5f3b83b6d154da4c765aae15855a-fd.mp4"
  },
  {
    "title": "第三章 数据库设计",
    "src": "http://b2cstream.edu-edu.com/dd61d5c063fa4a52b2c95acc326f8c01/262f9cb3c3714f31974ac745b79be633-c2dc5f3b83b6d154da4c765aae15855a-fd.mp4"
  },
  {
    "title": "第一节 数据库设计概述",
    "src": "http://b2cstream.edu-edu.com/6ffb0df7314d4560b8caa3748376f609/a23454d1e5a841b2ab1edba138216720-090a1fbe37dd8d454bbe7961d1ee9e9b-fd.mp4"
  },
  {
    "title": "第二节 数据库设计的基本步骤",
    "src": "http://b2cstream.edu-edu.com/e4fc9658a0c74c3b863fa651f7233f4b/198c70337fef4f4a9b689e0d85e6d473-909eb8b8af0b7adf3f2dedad64b0100e-fd.mp4"
  },
  {
    "title": "第三节 关系数据库设计方法",
    "src": "http://b2cstream.edu-edu.com/2da3c12bbc484df0ab45e30de881564d/ba66969ca3c84713ab430259a9dd86b8-6578f79260b612176992fd98120d09aa-fd.mp4"
  },
  {
    "title": "第四章 SQL与关系数据库基本操作",
    "src": "http://b2cstream.edu-edu.com/2da3c12bbc484df0ab45e30de881564d/ba66969ca3c84713ab430259a9dd86b8-6578f79260b612176992fd98120d09aa-fd.mp4"
  },
  {
    "title": "第一节 SQL概述",
    "src": "http://b2cstream.edu-edu.com/d9ef7fdbc0994cefbd42a197ee810a05/5b36479973d9455f9e870f0225c6a2ab-308f64fa525b1c2f3b3bc41986f92df1-fd.mp4"
  },
  {
    "title": "第二节 MySQL预备知识（1）",
    "src": "http://b2cstream.edu-edu.com/1c51967915904b348c683de158f4a010/5bfc9c39f3c7464d95990e9382c6c810-fb99c5890708572010479980fbde7271-fd.mp4"
  },
  {
    "title": "第二节 MySQL预备知识（2）",
    "src": "http://b2cstream.edu-edu.com/e899fb415da540a0ad85db2f7372de44/814dff9381d6494283eab748822b7ed6-0cfd4c5eab7d134b116da84f1b5918ff-fd.mp4"
  },
  {
    "title": "第三节 数据定义（1）",
    "src": "http://b2cstream.edu-edu.com/98aba9adc4e54c438980ce5643ed4566/7ff91ada48154cc59b1d49efa8f5f598-b8612db61140fd59e4d9b2c7d933e672-fd.mp4"
  },
  {
    "title": "第三节 数据定义（2）",
    "src": "http://b2cstream.edu-edu.com/431af721c8024064a390d94fc0aaf410/70327f5836e54d758b187e5c0e4adb11-d3b268d3e3c89b1c39076ea29556072f-fd.mp4"
  },
  {
    "title": "第三节 数据定义（3）",
    "src": "http://b2cstream.edu-edu.com/b9c4f3ad6d2446729d5152f754536db1/49b76d850a3349eda8eeffd1598e4535-01146c456189a18ec97b2e14f0dac9fd-fd.mp4"
  },
  {
    "title": "第四节 数据更新",
    "src": "http://b2cstream.edu-edu.com/4e8ccc9c1b6247b787070e032ff5d987/06b3d4f8250a41c493cbdf48413f4b94-e39e7c81ca05af097a71ac27b5da521a-fd.mp4"
  },
  {
    "title": "第五节 数据查询（1）",
    "src": "http://b2cstream.edu-edu.com/57e8a4ad387f4b6a86ed2296e2c15e68/71c245a0bfe345cd9ccbbeae9bd26959-5bc384433c0b9bcd4772b947923ad285-fd.mp4"
  },
  {
    "title": "第五节 数据查询（2）",
    "src": "http://b2cstream.edu-edu.com/ee8c2b8932e84d62aa10bd0354170442/7a2f5c322c5642a397688faeda220e1b-1cf3a4ed291f36e9be2d5fb542284a37-fd.mp4"
  },
  {
    "title": "第六节 视图",
    "src": "http://b2cstream.edu-edu.com/3f0e8d4270914f48b9fe692427f53a20/101653fe07a4489eb12b636f62397c5c-6a591544432d03f5f6fc73513bea564d-fd.mp4"
  },
  {
    "title": "第五章 数据库编程",
    "src": "http://b2cstream.edu-edu.com/3f0e8d4270914f48b9fe692427f53a20/101653fe07a4489eb12b636f62397c5c-6a591544432d03f5f6fc73513bea564d-fd.mp4"
  },
  {
    "title": "第一节 存储过程",
    "src": "http://b2cstream.edu-edu.com/769c178471c146859e3bf78fe9b4c78b/ec671d7acce34f39bb2bb9a4ffc40fd6-dbbd163106c545046b01825dafcd405a-fd.mp4"
  },
  {
    "title": "第二节 存储函数",
    "src": "http://b2cstream.edu-edu.com/fb1de039cdb14e67a5ae7497a2baf802/4dee08d44c824f9fb86bbca87b21f564-beec07ef946ca3b4e5e9b4207926c93c-fd.mp4"
  },
  {
    "title": "第六章 数据库安全与保护",
    "src": "http://b2cstream.edu-edu.com/fb1de039cdb14e67a5ae7497a2baf802/4dee08d44c824f9fb86bbca87b21f564-beec07ef946ca3b4e5e9b4207926c93c-fd.mp4"
  },
  {
    "title": "第一节 数据库完整性",
    "src": "http://b2cstream.edu-edu.com/d6db7dbf7291462186a7b4dc27c29126/5cf83d4d2c4b48cb82dc3c9fc8bd7879-3542820073bea0a664678a14ac204428-fd.mp4"
  },
  {
    "title": "第二节 触发器",
    "src": "http://b2cstream.edu-edu.com/d621e85c17014614b1029a0d5dfefdfc/d25d758d883c451ca439e7f65c73e431-20aaecf2df6fcb8aefbaf899532bc96e-fd.mp4"
  },
  {
    "title": "第三节 安全性与访问控制（1）",
    "src": "http://b2cstream.edu-edu.com/ad53595476a449c0903c9ccac2a1e22b/2751872cef054b96a6c76bc1e9300c7f-92249068bb02212645da3c83355db017-fd.mp4"
  },
  {
    "title": "第三节 安全性与访问控制（2）",
    "src": "http://b2cstream.edu-edu.com/9e5f94c737434e1fa88c55b28a01a177/26665fda8c5e49c785a30190d69f5828-f2e96037462f3f33cec4871f1076df11-fd.mp4"
  },
  {
    "title": "第四节 事务与并发控制",
    "src": "http://b2cstream.edu-edu.com/b413829d2613483780bcf7e65625c97c/8e03c389fe194d60b6884e473dcef92b-8427359039804863f172a11128118bd4-fd.mp4"
  },
  {
    "title": "第五节 备份与恢复",
    "src": "http://b2cstream.edu-edu.com/958d953df9594826bf408ba0397bbf1d/659609ad8dd34d798017295773fdf922-cece6c21c3ebef93c76b10305e48ec95-fd.mp4"
  },
  {
    "title": "第七章 数据库应用设计与开发实例",
    "src": "http://b2cstream.edu-edu.com/958d953df9594826bf408ba0397bbf1d/659609ad8dd34d798017295773fdf922-cece6c21c3ebef93c76b10305e48ec95-fd.mp4"
  },
  {
    "title": "第一节 需求描述与分析",
    "src": "http://b2cstream.edu-edu.com/446fdb9910594a778f6e2adf865e6219/b0fdad323c2e4512b97f90e97c864048-218e8e6d528c829782a07a03b9b92138-fd.mp4"
  },
  {
    "title": "第二节 系统设计",
    "src": "http://b2cstream.edu-edu.com/c3c58db625eb42ffae930e567515fd6a/63fe50912eb84e54bd2762f79eed5aaa-67429d946c9f52f89541cc8781cffbd6-fd.mp4"
  },
  {
    "title": "第三节 系统实现",
    "src": "http://b2cstream.edu-edu.com/3f56e266749646b1bd029cf2b94a7c86/cde759fb03eb4c14ad3b05b3fa314fcd-243b15c41411a0386537c9fcb76a286a-fd.mp4"
  },
  {
    "title": "第四节 系统测试与维护",
    "src": "http://b2cstream.edu-edu.com/ef5d59b9324c42788a0d0bcaf375800d/7f01e488500c438ca03bdf9640e9197b-41b336b16e04023419542ab7d5fe2ad6-fd.mp4"
  },
  {
    "title": "第八章 数据管理技术的发展",
    "src": "http://b2cstream.edu-edu.com/ef5d59b9324c42788a0d0bcaf375800d/7f01e488500c438ca03bdf9640e9197b-41b336b16e04023419542ab7d5fe2ad6-fd.mp4"
  },
  {
    "title": "第一节 数据库技术发展概述",
    "src": "http://b2cstream.edu-edu.com/67e8f7d3e77945d18f834c5d80c16f4c/e87c9b49b32346e39eb3d52f6b422638-0744051221bf6ee17657ff0c6e87b930-fd.mp4"
  },
  {
    "title": "第二节 数据仓库与数据挖掘",
    "src": "http://b2cstream.edu-edu.com/885548ec26c94944a52338daa4c3bf93/9974d5efa78b4032bf3a956394154b15-dd43e3ef5e7aeec70685dd3cfe376133-fd.mp4"
  },
  {
    "title": "第三节 大数据管理技术",
    "src": "http://b2cstream.edu-edu.com/de715e39767540dd814914914944d651/633d53a28fa84f3b99d664d1f369a294-c884f06785a3567ef1bfec076c2cb035-fd.mp4"
  }
]
"""

# 离散数学
"""
listData = [
    {
        "title": "课程导学",
        "src": "http://b2cstream.edu-edu.com/1c1bb519de274c029cedfc746cdb6867/5514f0e93c8f45f4a2b67082c533c3f8-9fbc525347c83ab7a7505ddc3c690bc4-fd.mp4"
    },
    {
        "title": "第一部分 数理逻辑篇",
        "src": "http://b2cstream.edu-edu.com/1c1bb519de274c029cedfc746cdb6867/5514f0e93c8f45f4a2b67082c533c3f8-9fbc525347c83ab7a7505ddc3c690bc4-fd.mp4"
    },
    {
        "title": "数理逻辑篇介绍",
        "src": "http://b2cstream.edu-edu.com/a8a6a9aa113946d48ac92138a169bb92/7ebdf7927564446daff376618e039ead-11e99aafe6ef25e5782c96c8bc8d2cda-fd.mp4"
    },
    {
        "title": "1.1 命题与命题联结词(1)",
        "src": "http://b2cstream.edu-edu.com/88518854186b44a2a8048a2bc3a49aa6/4e0c1a6f52cc46289cbc46265e803f50-31a94a4af12dec0b5e2193ec40d02ad8-fd.mp4"
    },
    {
        "title": "1.1 命题与命题联结词(2)",
        "src": "http://b2cstream.edu-edu.com/904c3fffdcc340d2b9a834ebf9406bcf/1bde632daa15403db07b9713445b6912-1555d3a0cc01455735da37f6e8356b81-fd.mp4"
    },
    {
        "title": "1.2 命题公式的等值演算(1)",
        "src": "http://b2cstream.edu-edu.com/87b756591eaa442aa462e26d193c4cd6/a3a4dc2afaf44c70b4c72c33d89f2425-f8067bf6c33835edc782d7259b8f0cd1-fd.mp4"
    },
    {
        "title": "1.2 命题公式的等值演算(2)",
        "src": "http://b2cstream.edu-edu.com/36f87407220648549e8db88cfe662681/a8c6c585baf1474c8bce6b53cc64f7c5-8c77ab3a70ca9b6548a5e00c13779a0d-fd.mp4"
    },
    {
        "title": "1.2 命题公式的等值演算(3)",
        "src": "http://b2cstream.edu-edu.com/de16d1516f4349a59a400e50690c583c/aceacd1094ac47358e4d7a6652c1e878-7a620d0bfeda4c525f6cd8eb1be27ce4-fd.mp4"
    },
    {
        "title": "1.2 命题公式的等值演算(4)",
        "src": "http://b2cstream.edu-edu.com/a3949d9a2cec433bacaed906a3b6d33c/ae20273ec6884deabd5de8a31b8074a1-257cc3b200e1c4b8df90ff1dee2d9238-fd.mp4"
    },
    {
        "title": "1.3 联结词完备集",
        "src": "http://b2cstream.edu-edu.com/135185563b604223a8fe68890e79cba3/be5e3865bea04237910a282cc537fb8a-da121bbb4d5eb82fa5a73815e3d1cb9f-fd.mp4"
    },
    {
        "title": "2.1 范式",
        "src": "http://b2cstream.edu-edu.com/b494c23ee6a34d21a217029bf5d31612/df77696827764d2f9d271e59e6d2abcf-c683b9616bbe532e660dcaf0ce8fb385-fd.mp4"
    },
    {
        "title": "2.2 主范式(1)",
        "src": "http://b2cstream.edu-edu.com/a288eaa5940446fb92203019cf840f70/f0439bca81254365914a0c794189ed8c-69e2d13801f3a6e8707e068fc7dc0d43-fd.mp4"
    },
    {
        "title": "2.2 主范式(2)",
        "src": "http://b2cstream.edu-edu.com/d05b8276387c4c35bf196ff6323efccf/8b26e01e56744ce78e2d7c8178560da2-0d6a4b2fa6799777c7ce9f5983dea43c-fd.mp4"
    },
    {
        "title": "2.2 主范式(3)",
        "src": "http://b2cstream.edu-edu.com/7e033e28505442bf9df81d320fea2ca5/96b252fd1ffe4d4cbaeac120367511bd-af7482e906b1f387c208e57aca93a851-fd.mp4"
    },
    {
        "title": "2.3 自然推理系统(1)",
        "src": "http://b2cstream.edu-edu.com/5da51428c25f4d9b891264d11ec4c40a/69014b8dee1143068de1ea8de621a5a2-1922774640f41f2256ba23dc61bd8160-fd.mp4"
    },
    {
        "title": "2.3 自然推理系统(2)",
        "src": "http://b2cstream.edu-edu.com/c5aea2a33cba4bfcb0155925febae12d/4874f66c77f24eaba2788897ab2b06d4-9441b7431840026f5859ce52bfe2213e-fd.mp4"
    },
    {
        "title": "3.1 谓词的概念与表示(1)",
        "src": "http://b2cstream.edu-edu.com/d8dba1afe7904252b891b0721cf3c16d/e7dee189ee944c98a3f0155ba44361b1-0df3b8ff3114b5e51f292ccc82a79529-fd.mp4"
    },
    {
        "title": "3.1 谓词的概念与表示(2)",
        "src": "http://b2cstream.edu-edu.com/aca65fd0419a4a398556d1f1f88304d7/f0f4ee2701b54134bf071249eaf7b220-f81485cffea2194b0fa60b9721c3293e-fd.mp4"
    },
    {
        "title": "3.2 合式公式",
        "src": "http://b2cstream.edu-edu.com/9e1fe99138524c1e8b41ab36efa0bb5c/f991d44232a44034b8b8bf9e53af956d-3311606c2c6fedec416ee1f8d7480327-fd.mp4"
    },
    {
        "title": "3.3 谓词演算的等价式与蕴涵式",
        "src": "http://b2cstream.edu-edu.com/29726377061d473093ed4c32f7638c2f/37369cd1c2774b4bb0e2b5164ce7d70c-93caa94bebad5deaba61269cf0b69501-fd.mp4"
    },
    {
        "title": "3.4 前束范式",
        "src": "http://b2cstream.edu-edu.com/72c256c12f564eff8750e08c3231b2d5/e0840b00b7a847f3a116e314161156e0-297b8c69eea5e8c5e90856dffa9c15a3-fd.mp4"
    },
    {
        "title": "3.5 谓词演算的推理理论",
        "src": "http://b2cstream.edu-edu.com/b38773038ca44753832962fcd2c8ee75/89835dddf3f34c7bac84ed4050a4b6f7-dd42690ba8afac5dc3f39e41403e3c14-fd.mp4"
    },
    {
        "title": "第二部分 集合论篇",
        "src": "http://b2cstream.edu-edu.com/b38773038ca44753832962fcd2c8ee75/89835dddf3f34c7bac84ed4050a4b6f7-dd42690ba8afac5dc3f39e41403e3c14-fd.mp4"
    },
    {
        "title": "集合论篇介绍",
        "src": "http://b2cstream.edu-edu.com/f91262b397f040b086cbd252abba74c3/3e504e0c1d9245f0a1ea3e58c9fdfb4d-7ac2dcaa0949c814412fa78f652d2e8d-fd.mp4"
    },
    {
        "title": "4.1 集合",
        "src": "http://b2cstream.edu-edu.com/f0d38d2a4cc94026a24edceb2fd7045f/630fbf7f0cee4819b73b3f5be993c4ac-08f402c471d2ed0297ae0f95cc918398-fd.mp4"
    },
    {
        "title": "4.2 集合的运算",
        "src": "http://b2cstream.edu-edu.com/cbf965ea9fbe41798d64d30ade53aac4/9a32d3090bb3451a8da24d198e6fe255-b9f04f9a89e2eff63e17b2f7347f27ca-fd.mp4"
    },
    {
        "title": "4.3 有序对与笛卡尔积",
        "src": "http://b2cstream.edu-edu.com/b3af31833d3441b8a97c8e335eae7251/faf023099c644307aa6a0de7d80c1355-9eaa9d36ce7ea94b315adce29d7f06ba-fd.mp4"
    },
    {
        "title": "5.1 关系及其性质(1)",
        "src": "http://b2cstream.edu-edu.com/2ad6dde1d6ad40c3b8416fb67bdb0f05/10374741ff0d425390a1f3e20db07120-10e52717eebdece484234bc871876e3e-fd.mp4"
    },
    {
        "title": "5.1 关系及其性质(2)",
        "src": "http://b2cstream.edu-edu.com/f3e18bac10434a57ad16ddd706fa023a/c18174a638bd4f858fd1ad8a94690f49-1a96b82d62092d9bac787481c7649ae2-fd.mp4"
    },
    {
        "title": "5.1 关系及其性质(3)",
        "src": "http://b2cstream.edu-edu.com/e4db5ebad3ac43fc97233c10bbfa81b6/30b36a8d51f94f9aa4618c46af073097-678b12bd96d3001c01d40e405e83bf38-fd.mp4"
    },
    {
        "title": "5.1 关系及其性质(4)",
        "src": "http://b2cstream.edu-edu.com/4a1672e984c449c1a1b54a7d88dc4cb2/f9191ebc565e4dedab62a28e2897a117-9656f0d33b452efe50bb9ad9b9fcaa13-fd.mp4"
    },
    {
        "title": "5.2 关系的运算(1)",
        "src": "http://b2cstream.edu-edu.com/c2b24838451341dda140e23361539f09/7476d3ac05a94491b39271c6975eae35-77d48f13fec62513a35c6344236c3242-fd.mp4"
    },
    {
        "title": "5.2 关系的运算(2)",
        "src": "http://b2cstream.edu-edu.com/86cdc419ddea4a5a924adea3cc6c7052/0417074fea674bf2aab59586f8d12855-aa25a8c162184446efaa0c1cf2865ad4-fd.mp4"
    },
    {
        "title": "5.2 关系的运算(3)",
        "src": "http://b2cstream.edu-edu.com/bcd2d622789141eb9e7402e8d8f75eab/4731352d3a9a4229a4dd57c24bcf1e49-f1975b931d2e2cc460f50aa1bd4b2554-fd.mp4"
    },
    {
        "title": "5.2 关系的运算(4)",
        "src": "http://b2cstream.edu-edu.com/d3206b2eb58a43528335ee9c470d4b63/1a68f3b6ce5849fdb4f93645dc749953-32d536422c96d40da66e4d5e11bec8a4-fd.mp4"
    },
    {
        "title": "5.2 关系的运算(5)",
        "src": "http://b2cstream.edu-edu.com/fe2e93b61d7c41078e940d6532686992/34531aa2cbc34c348430e0528bb3d120-47e18e69581cfceec4bb4abc4582460d-fd.mp4"
    },
    {
        "title": "5.2 关系的运算(6)",
        "src": "http://b2cstream.edu-edu.com/82c1e39a137b458fb627cc6b3a3e6507/ec9607cf46aa4a9788d7eeae0d94232b-0e43a82eb6127ab58ff75835a361b48b-fd.mp4"
    },
    {
        "title": "5.3 等价关系与序关系(1)",
        "src": "http://b2cstream.edu-edu.com/ab2e1c2f70c5402fab33c49f61d5e990/def505efae864b1dadd60e7411bbdc1d-56d2442f0e5ed0c9f963750d264c2265-fd.mp4"
    },
    {
        "title": "5.3 等价关系与序关系(2)",
        "src": "http://b2cstream.edu-edu.com/3c3722e9b75943e6902881eb50b08f0a/bed472bd883347748c1e631b1917ae7b-2abee04126b864f625b7e61f24fc493e-fd.mp4"
    },
    {
        "title": "5.3 等价关系与序关系(3)",
        "src": "http://b2cstream.edu-edu.com/8c3003013da043a688a0ec8e5533746e/f91458f62c214c6aa087ca4e8a185e21-24bf2d28af4a02ba5e06effad56f835e-fd.mp4"
    },
    {
        "title": "5.4 函数",
        "src": "http://b2cstream.edu-edu.com/a911a2ead6894d4a8de73379d736afe2/fbffc9b806cf4e19990ee9ae91000979-9eb7b7c2eef65d902a6169026af2d4b0-fd.mp4"
    },
    {
        "title": "第三部分 代数系统篇",
        "src": "http://b2cstream.edu-edu.com/a911a2ead6894d4a8de73379d736afe2/fbffc9b806cf4e19990ee9ae91000979-9eb7b7c2eef65d902a6169026af2d4b0-fd.mp4"
    },
    {
        "title": "代数系统篇介绍",
        "src": "http://b2cstream.edu-edu.com/bf75bf121b534b83a7987dbc38ac6064/caaa719691734802af5f42dfa00b9278-2a1a001334889f1c87fd22f4e32d9013-fd.mp4"
    },
    {
        "title": "6.1 代数系统",
        "src": "http://b2cstream.edu-edu.com/6be29e58948e478b88c88bc1808a7e19/782f858d90e84d9e8d1a7b4797bd8e86-7ea1ec859472330498a7c332ffd18d25-fd.mp4"
    },
    {
        "title": "6.2-6.3 群与半群、环",
        "src": "http://b2cstream.edu-edu.com/3d2d400911a549588059d19fcaf2b8e7/cc8d9626cc074c0397109bce02a317b3-55d2e69ee87cb21261cf1eae464e4541-fd.mp4"
    },
    {
        "title": "7.1-7.2 格、分配格和有补格",
        "src": "http://b2cstream.edu-edu.com/db28d7ca9557416c89558a82c5575b28/9ca4d78bfe4e4927a415b2c48bcd3856-484025cde094ed81ced12e295137ad17-fd.mp4"
    },
    {
        "title": "7.3 布尔代数",
        "src": "http://b2cstream.edu-edu.com/4969f7bd52fc4c0d8061c3f0e45effee/94035423fd1a486f895a079cea297656-f20eb3824117556b868c7f79955346d8-fd.mp4"
    },
    {
        "title": "第四部分 图论篇",
        "src": "http://b2cstream.edu-edu.com/4969f7bd52fc4c0d8061c3f0e45effee/94035423fd1a486f895a079cea297656-f20eb3824117556b868c7f79955346d8-fd.mp4"
    },
    {
        "title": "图论篇介绍",
        "src": "http://b2cstream.edu-edu.com/bef5afc4880c4a70ae5bd6a41a35496b/a21374dea3414fefb199fb6bf2a94783-590ae00512730bdef408a946c5ef0188-fd.mp4"
    },
    {
        "title": "8.1 图的基本概念(1)",
        "src": "http://b2cstream.edu-edu.com/09f04d4abc5f4edbabaf71c1163ecdd6/986d7d8e3c444727ae89a7dedeb3253c-5efae193a0dec6bb3573bedf082de0ce-fd.mp4"
    },
    {
        "title": "8.1 图的基本概念(2)",
        "src": "http://b2cstream.edu-edu.com/b72addb1213b487c888f0dff8e8a195e/10b9d94d8f134473a01969cf305b8573-21d6199dfa92a5f5a23bfbacaf5311d0-fd.mp4"
    },
    {
        "title": "8.2 图的连通性(1)",
        "src": "http://b2cstream.edu-edu.com/c13e6d90685a48b2b1184a1a80ae47a5/61b6cc7f8f114a1b87bbccb17b7dbd72-54f41b982925e3483210e5e7dcb6f038-fd.mp4"
    },
    {
        "title": "8.2 图的连通性(2)",
        "src": "http://b2cstream.edu-edu.com/552d9c21f8d24fbea235944369f48797/a61f9f04aaa14c77ade297b0e2b28d2f-8a01fb3ff38ad5e74408f6ae2ad4d660-fd.mp4"
    },
    {
        "title": "8.3 图的表示",
        "src": "http://b2cstream.edu-edu.com/bdf611da148c4f678bf4e8ff6c2b4743/9f513606372f4437be2301135d46b672-7106f3d27a863a87664233c8907674f1-fd.mp4"
    },
    {
        "title": "9.1 欧拉图与哈密顿图",
        "src": "http://b2cstream.edu-edu.com/8d24ef70485c4bfd8875a55e760bb416/b794297fbdec42d6b75ea124d99912db-95d5620f9327c3008ffd23cceb798742-fd.mp4"
    },
    {
        "title": "9.2-9.3 平面图、树及其遍历",
        "src": "http://b2cstream.edu-edu.com/50356e6b8b3c4b24b0538de125bf1d99/07713589008648138933521c57d29e9e-66842c6a84bd4b18716065a549d085dc-fd.mp4"
    }
]
"""

# 去掉重复title
deduplicationArr = []


def deduplication():
    folder_path = '/'
    for data in listData:
        if data['title'] not in deduplicationArr:
            # print(data['title'], data['src'])
            deduplicationArr.append(data['title'])

    for title in deduplicationArr:
        for data in listData:
            if title == data['title'] and len(data['src']) > 0:
                # print(title, data['src'])
                if re.match(r'第.章', title) is not None:
                    # print(title, data['src'], '目录')
                    folder_path = '/' + title + '/'
                else:
                    downloadFile(folder_path, title + '.mp4', data['src'])
                    # print(title, data['src'], '文件')

    print(len(deduplicationArr))


def downloadFile(path, name, url):
    headers = {'Proxy-Connection': 'keep-alive'}
    r = requests.get(url, stream=True, headers=headers)
    length = float(r.headers['content-length'])
    folder_path = ('F:/自考学习课程/计算机系统结构' + path)
    print(folder_path + '\n')
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    f = open(folder_path + name, 'wb')
    count = 0
    count_tmp = 0
    time1 = time.time()
    for chunk in r.iter_content(chunk_size=512):
        if chunk:
            f.write(chunk)
            count += len(chunk)
            if time.time() - time1 > 2:
                p = count / length * 100
                speed = (count - count_tmp) / 1024 / 1024 / 2
                count_tmp = count
                print(name + ': ' + formatFloat(p) + '%' + ' 下载速度: ' + formatFloat(speed) + 'M/S')
                time1 = time.time()
    f.close()


def formatFloat(num):
    return '{:.2f}'.format(num)


if __name__ == '__main__':
    deduplication()
    # downloadFile('360.exe', 'http://down.360safe.com/setup.exe')
