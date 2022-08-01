# aUnfinishedImageEditTool
A unfinished image edit tool which I set up to help me understand pyside2 and python

SI:
    processingImgQueue  类型:list  
    --存放每一次对图像进行处理后的状态(ndarray格式)的队列，程序设计队列的最大长度为10  
    historyFilePath 类型:list  
    --在每次程序启动时从硬盘读取文件historyFile.txt，里面存储了最近打开的10张图片的相对路径  
    colorSample 类型:ndarray  
    --25x25的矩形，显示当前调色的预览  
    oriW/H 类型:int  
    --打开初始图片的宽度与高度（单位：像素）  
    curW/H 类型:int  
    --当前视口展示的图片（图像处理队列的队首）的宽度与高度（单位：像素）  


