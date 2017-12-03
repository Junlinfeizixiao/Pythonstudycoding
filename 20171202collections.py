#collections,,Python内置集合模块，有许多集合类

'''
#namedtuple 是一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素。
这样一来，我们用namedtuple可以很方便地定义一种数据类型，它具备tuple的不变性，又可以根据属性来引用，使用十分方便。
'''

# from collections import namedtuple
# Point = namedtuple('Point',['x','y']) #表示‘点’
# p = Point(1,2)
# print(p.x,p.y)
# print(isinstance(p,Point))
# print(isinstance(p,tuple))
# Circle = namedtuple('Circle',['x','y','r']) #表示‘圆’

'''
#deque使用list存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了，因为list是线性存储，数据量大的时候，插入和删除效率很低。
deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈：
不仅实现了list的append()和pop()以外，还支持appendleft()和popleft()
'''
# from collections import deque
# q = deque(['a','b','c'])
# q.append('x')
# q.appendleft('y')
# print(q)
# q.pop()
# q.popleft()
# print(q)

'''
#defaultdict  除了在Key不存在时返回默认值，defaultdict的其他行为跟dict是完全一样的。
'''
# from collections import defaultdict
# dd = defaultdict(lambda:'N/A')  #默认值是调用函数返回的，而函数在创建defaultdict对象时传入。
# dd['key1'] = 'abc'
# dd['key2'] = 'def'
# print(dd['key1'])
# print(dd['key2'])
# print(dd['key3'])

'''
#OrderedDict
使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序。
如果要保持Key的顺序，可以用OrderedDict
但是OrderedDict的Key会按照插入的顺序排列，不是Key本身排序
'''
# from collections import OrderedDict
# d = dict([('a',1),('b',3),('c',2)])
# print(d)
# od = OrderedDict([('a',1),('b',3),('c',2)])
# print(od)

'''
#Counter
Counter是一个简单的计数器，例如，统计字符出现的个数：
'''
from collections import Counter
c = Counter()
for ch in "programming":
	c[ch] = c[ch]+1
print(c)

cc = Counter("asjdghkjasdjkashjkdashd").most_common(3)
print(cc)