# -*- coding: utf-8 -*-

example1 = """
职位描述：
1、需要有独立提需求、接受pk、落地需求的能力。理解业务方向，进行进一步拆解，制定自己的工作计划。
2、收集市场信息、竞品信息。通过有穿透力的分析，获得尽可能多的有效信息。
3、描述用户价值链条、洞察用户需求，并转化为产品设计高效表达。
4、与各职能岗位密切配合，调动资源组织项目，将产品构想落地实现，为最终效果与质量负责，为项目团队负责。
5、以产品思维灵活适应各类型平台产品要求，包括App、网页、微信小程序、内部工具等。
岗位要求：
1、1-3年产品经验，本科及以上学历。如果你能证明自己的思维能力、学习能力、岗位胜任力不输这些条件下的竞争者，可以把这些条件当作浮云。
2、最重要，要有同理心，善于倾听，快速理解用户的真实意图和需求。
3、善于沟通，应变。你需要说服很多人来跟你合作落实你的想法，包括开放心态不断挑战自己的认知。
4、执行力/推动力。如果对未知没有想清楚，至少你懂得先把已知的事情做到最漂亮。
5、如果你恰巧对教育行业很感兴趣会更好，如果没有相关兴趣或经历，可能需要花一点时间去理解用户，请做好一点准备。
我们认为互联网+教育还远未达到其行业愿景，无论是在用户价值和商业价值维度，都仍大有可为。希望与真诚、有良好职业素养，对创造价值有极强渴望的优秀产品经理共同实践。气味相投能够走得更远
"""

example2 = """
职位描述：
「岗位职责」

1. 负责公司移动端产品（Android&iOS）设计与管理工作，从制定方案到推进实施；
2. 紧密地和开发、设计、测试合作，完成产品功能的落地；
3. 根据项目需要输出高质量的产品需求文档，产品原型；协调运营、设计、开发、测试等跨部门资源 ；
4. 与市场部门合作，做好产品的运营，并根据数据提高运营效果。
5. 完成产品市场调研，国内外竞品跟踪以及用户研究等工作，并输出高质量的调研报告；
6. 深入体验产品和竞品，关注市场动态，收集用户反馈，提升用户满意度，将用户体验做到极致；
「岗位要求」
1、 本科以上学历，1年以上c端产品经理工作经验；有成功的社区/视频类产品经验最佳。
2、 具备较强的逻辑思维能力与用户体验细节把控能力，具有较好的用户同理心；
3、 具备良好的文案撰写能力，能书写逻辑清晰的PRD，以及良好的产品宣讲和口头表达能力；
4、 熟悉产品经理常用工具，包括Axure、Visio、PPT，具有优秀的产品推动能力、创业创新思考、业务资源协调能力；
5、 深度移动互联网用户，产品控，熟悉国内外各大榜单焦点产品，完美主义者，追求 体验极致；
6、 具备敏锐的数据Sense,卓越的项目管理能力以及快速学习能力；
7、 同样欢迎对PM工作感兴趣并对用户体验有深刻理解的交互设计师应聘本职位；
8、 如果现在的你依然坚持着改变世界的理想，那么，我们热切地希望你能过来聊聊。
"""

example3 = """
岗位职责：
1、以数据和产品为驱动，提升用户活跃和粘性，提高留存率、活跃率、召回率等核心产品效果；
2、建立公司增长大脑，指导各业务部门制定增长略策，推动执行；
3、管理增长相关的项目，敏捷迭代，快速验证。
任职要求：
1、本科及以上学历，计算机、数学相关专业，有三年以上用户增长或者策略产品相关工作经验；
2、具备数据、策略、市场类产品的完整项目经验；
3、具有良好的AB测试试验设计能力、具备良好的产品设计能力及项目管理能力；
4、需具备良好的数据敏感度，能够敏锐的捕获数据的价值；
5、有数据分析相关经验、增长黑客相关经验、团队管理经验优先。
"""

example4 = """
岗位职责：
1、负责收集、分析公司业务部门需求，梳理出清晰的业务流程，进行后台系统的设计，以形成可产品化的系统需求。
2、负责需求的跟踪与控制，完成需求文档撰写，包括：产品规划、功能设计、业务流程设计、使用流程设计等。
3、跨部门协调和沟通，推动 UI、开发、测试、运营等人员紧密合作达成产品目标。
4、对日常运营数据进行跟踪和研究，定期分析产品上线效果，掌握平台运行状况，推动产品优化迭代。
任职要求：
1、全日制统招本科（含）以上学历，3年以上后台产品经理工作经验。
2、熟悉产品实施过程，包括产品规划、需求分析、产品功能设计、业务流程设计等；熟练掌握 Axure，vision，脑图，office 等工具。
3、具备良好的逻辑分析能力、沟通协调能力，解决问题能力强，结果导向。
4、对数据敏感，具备较强的分析思维和商业运营意识；能够主动提出运营及产品方案。
"""

# -*- coding: utf-8 -*-

# import thulac
import jieba
from redistest import RedisHelper
from job_detail_get import get_job_details
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

NAMESPACE = 'lagou-python-dirty::'
PARTITION = 'jobdetail-des-dirty::'
CJK_UNICODE_ENCODING_INTERVAL = [19968, 40895]
LATIN_UNICODE_ENCODING_INTERVAL = [65, 122]


def word_meaningful(word):
    if not isinstance(word, basestring):
        return False
    if CJK_UNICODE_ENCODING_INTERVAL[0] <= ord(word[0]) <= CJK_UNICODE_ENCODING_INTERVAL[1] \
            and CJK_UNICODE_ENCODING_INTERVAL[0] <= ord(word[-1]) <= CJK_UNICODE_ENCODING_INTERVAL[1]:
        return word
    if LATIN_UNICODE_ENCODING_INTERVAL[0] <= ord(word[0]) <= LATIN_UNICODE_ENCODING_INTERVAL[1] \
            and LATIN_UNICODE_ENCODING_INTERVAL[0] <= ord(word[-1]) <= LATIN_UNICODE_ENCODING_INTERVAL[1]:
        return word.lower().capitalize()
    return False


def segments_get(text):
    seg_list = jieba.cut_for_search(text)
    for segment in seg_list:
        word = word_meaningful(segment)
        if word:
            yield word


def vote_to_redis(seg_list):
    r = RedisHelper(name_space=NAMESPACE, partition=PARTITION)
    for segment in seg_list:
        r.vote(segment)

def scan(name_space=NAMESPACE, partition=PARTITION):
    r = RedisHelper(name_space=name_space, partition=partition)
    res = r.scan()
    for k, v in res.iteritems():
        print k, ' -> ', v
    return res


def run(text):
    sgs = segments_get(text)
    vote_to_redis(sgs)
    print time.time()


def main():
    dirty_list = [example1, example2, example3, example4]
    for dirty in dirty_list:
        run(dirty)
    scan()

if __name__ == '__main__':
    main()