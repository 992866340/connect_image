<div>emmm....就叫他马赛克图片生成器吧</div><div><br></div><div>=============================</div><div><br></div><div>总体分为两个部分</div><div>1.运行爬虫文件在网上抓取图片素材</div><div><span style="white-space:pre">	</span>写爬虫的思路都注释在代码中,只说一下食用方法</div><div><span style="white-space:pre">	</span>用到的库:scrapy urllib&nbsp;</div><div><span style="white-space:pre">	</span>在spider文件夹下 执行命令</div><div><span style="white-space:pre">	</span>scrapy crawl acg</div><div><span style="white-space:pre">	</span>图片素材保存位置在 pipelines.py 第48行</div><div><br></div><div>2.运行puzzle.py生成拼接图片</div><div><span style="white-space:pre">	</span>cd ../</div><div><span style="white-space:pre">	</span>参数&nbsp;</div><div><span style="white-space:pre">	</span>-s (已处理过的素材目录默认output) 已经存在output文件夹已经有马赛克图片，快速生成图片</div><div><span style="white-space:pre">	</span>-i (模版图片路径) 模版图片test.jpg放在与puzzle.py同级位置 请勿随意更改</div><div><span style="white-space:pre">	</span>-d (素材目录) 素材最好在5000张左右</div><div><span style="white-space:pre">	</span>-o (处理素材后生成的小图标所放路径) 默认output请勿随意更改</div><div><span style="white-space:pre">	</span>-r (int) 如果素材过少那就让其重复使用 int为次数</div><div><span style="white-space:pre">	</span>-is -os 输入(马赛克块)/输出(生成图)图片尺寸&nbsp;</div><div><span style="white-space:pre">	</span>python puzzle.py E:\Python代码\python1710\masaike\image\image\output\ -i test.jpg -d E:\Python代码\python1710\masaike\image\image\spiders\图库\ -o output/</div>
