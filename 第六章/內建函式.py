print(len([1,2,3,4,5])) # len() 傳回串列參數的長度，也就是包含幾個元素
print(max([1,2,3,4,5])) # max() 傳回串列參數中最大的元素
print(min([1,2,3,4,5])) # min() 傳回串列參數中最小的元素
print(sum([1,2,3,4,5])) # sum() 傳回串列參數中元素的總和

import random
L=[1,2,3,4,5]
random.shuffle(L)
print(L)