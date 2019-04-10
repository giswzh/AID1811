import re

html = '''
<div class="animal">
  <p class="name">
    <a title="Tiger"></a>
  </p>

  <p class="contents">
    Two tigers two tigers run fast
  </p>
</div>



<div class="animal">
  <p class="name">
    <a title="rabbit"></a>
  </p>

  <p class="contents">
    small white rabbit white and white
  </p>
</div>'''
# '<div class="animal">.*?title="(.*?)".*?\
# class="contents">(.*?)</p>.*?</div>'
p = re.compile('<div class="animal">.*?title="(.*?)".*?class="contents">(.*?)</p>.*?</div>',re.S)
r_list = p.findall(html)
# 第一步实现
print(r_list)
# 第二步实现
# [('Tiger', '\n    Two tigers two tigers run fast\n  '),
#  ('rabbit', '\n    small white rabbit white and white\n  ')
# ]
for r in r_list:
  print('动物名称:%s' % r[0])
  print('动物描述:%s' % r[1].strip())
  print('*' * 50)


