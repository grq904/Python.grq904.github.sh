from MyQR import myqr
import time
question1 = input ("请输入网址：")
question2 = input ("请输入保存图片名字(请在后面加上 .jpg 或 .png 或 .bmp 或 .gif  ，暂时只支持这几种类型的图片)：")
myqr.run(
    words = question1,			
    colorized = True,			
    save_name =	question2
)
print ("二维码已生成！系统将等待3秒")
time.sleep (3)