class MathDojo(object):
    def __init__(self):
        self.result = float(0)
    def add_md(self, arg1, *other_args):
        # Handle arg1 first
        if isinstance(arg1, list) or isinstance(arg1, tuple):
            for num in arg1:
                self.result = self.result + float(num)
        elif isinstance(arg1, int) or isinstance(arg1, float):
            self.result = self.result + float(arg1)
        # Handle other args
        for number in other_args:
            if isinstance(number, list) or isinstance(number, tuple):
                for num in number:
                    self.result = self.result + float(num)
            elif isinstance(number, int) or isinstance(number, float):
                self.result = self.result + float(number)
        return self

    def subtract_md(self, arg1, *other_args):
        # Handle arg1 first
        if isinstance(arg1,list) or isinstance(arg1, tuple):
            for num in arg1:
                self.result = self.result - float(num)
        elif isinstance(arg1,int) or isinstance(arg1,float):
            self.result = self.result - float(arg1)
        # Handle other_args
        for arg in other_args:
            if isinstance(arg,list) or isinstance(arg,tuple):
                for num in arg:
                    self.result = self.result - float(num)
            elif isinstance (arg,int) or isinstance(arg, float):
                self.result = self.result - float(arg)
        return self

# -- Part II
md1 = MathDojo()
print "md1 should be 8"
print md1.add_md([1],3,4).result

md2 = MathDojo()
print "md2 should be 31"
print md2.add_md([1],3,4).add_md([3,5,7,8]).result

md3 = MathDojo()
print "md3 should be 21"
print md3.add_md([1],3,4).add_md([3,5,7,8]).subtract_md(2, [2,3], [1, 2]).result

md4 = MathDojo()
print "md4 should be 20.6"
print md4.add_md([1],3,4).add_md([3,5,7,8]).subtract_md(2, [2,3], [1.1, 2.3]).result

md = MathDojo()
print "md should be 4"
print md.add_md(2).add_md(2,5).subtract_md(3,2).result
