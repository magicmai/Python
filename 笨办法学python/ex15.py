from sys import argv                    #从sys软件包中取出argv这个特性来供我使用

script, filename = argv                 #脚本，文件名作为参数变量

txt = open(filename)                    #把打开的文件赋值给txt

print "Here's your file %r:" % filename #打印
print txt.read()                        #打印读取到的txt

print "Type the filename again:"        #打印
file_again = raw_input("> ")            #用户输入的信息赋值给file_again

txt_again = open(file_again)            #打开的file_again信息赋值给txt_again

print txt_again.read()                  #打印读取到的txt_again信息
