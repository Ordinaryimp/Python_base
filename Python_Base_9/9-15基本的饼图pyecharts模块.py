#导入
from pyecharts import options as opts
from pyecharts.charts import Pie
from pyecharts.faker import Faker

#准备数据
lst=[['唐',1000],['宋',1200],['元',1213],['清',1313]]

c = (
    Pie()
    # .add("", [list(z) for z in zip(Faker.choose(), Faker.values())])  #实例是个二维列表
    .add('',lst)
    .set_global_opts(title_opts=opts.TitleOpts(title="不知道什么饼图"))
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    .render("year.html")
)

print([list(z) for z in zip(Faker.choose(), Faker.values())])   #二维列表
