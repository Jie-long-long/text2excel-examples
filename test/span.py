# span.py
# Created: 23rd October 2019

"""
This will batch define a group of spans in input files of wxCBA software,
once you pass the kinds, length and number of spans
"""

__author__ = 'Jay Long'
__version__ = '0.1'

class Spans():

    def __init__(self, span_kind, span_length, span_number):
        """
        设置span的长度，传入参数
         :param span_kind:有多少种span
         :param span_length: 单个span的长度
         :param span_number: 一共有多少个span
         """
        self.kind = span_kind
        self.length = span_length
        self.number = span_number  
        self.spans = str('SPANS')

    def define_spans(self):
        """
        自定义长度span
        """
        i = 0
        if self.kind == 1:
            for i in range(self.number):
                self.spans = self.spans + ' ' + str(self.length) + ' '
                i += 1
        
        return(self.spans)    
    
my_spans = Spans(1,2,3)
print(my_spans.define_spans())
