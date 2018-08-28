# 155. Min Stack

程序如果使用vector，则会出现Memory Limit Exceeded即超出内存的错误，原因在于：vector会动态申请数组，实际使用的数组比申请的小，如果申请的数组大小太大了，就会出现Memory Limit Exceeded错误。
