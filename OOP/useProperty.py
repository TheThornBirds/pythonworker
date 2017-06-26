'''
python内置的@property装饰器就是负责把一个方法编程属性调用的：
'''
class Student(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value> 100:
            raise ValueError('score must between 0~100')
        self._score = value

s = Student()
s.score = 60    #实际转化为s.set_score()
print(s.score)  #实际转化为s.get_score()
#s.score = 999   #数值过大则会报错

'''
@property还可以定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性
'''
class Student(object):
    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2017 - self._birth

s = Student()
s.birth = 1995
print(s.age)
'''
上面的birth是可读写属性，

而age就是一个只读属性，因为age可以根据birth和当前时间计算出来。
'''
class Screen(object):
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if not isinstance(value , int):
            raise ValueError('width must be int')
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise  ValueError('heifht must be int')
        self._height = value

    @property
    def resolution(self):
        return self._width*self._height

# test:
s = Screen()
s.width = 1024
s.height = 768
print(s.resolution)
assert s.resolution == 786432, '1024 * 768 = %d ?' % s.resolution