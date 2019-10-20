class Spans:

    def __init__(self, span_distance, span_number):
        """
        设置span的长度，传入参数
         :param span_distance: 单个span的长度
         :param span_number: 一共有多少个span
        """
        self.distance = span_distance
        self.number = span_number  
        self.spans = str('SPANS')

    def define_spans(self):
        """
        自定义长度span
        """

        for i in range(self.number):
            self.spans = self.spans + ' ' + str(self.distance) + ' '
        
        return(self.spans)    
    
my_spans = Spans(2,3)
print(my_spans.define_spans())