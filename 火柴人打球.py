import sys, time,pygame

fps=100
fclock=pygame.time.Clock()
size=width, height=1200,800
screen=pygame.display.set_mode(size)
face = 0#判断红脸还是白脸，红脸为0,白脸为1
ifHuipai=0#属于挥拍状态吗？1是，0不是
ifFaqiu=0#是否已发球？1已发，0未发
downToUp=0
count=0#记录按键的数量
whiteOrRed=''#从哪个文件夹选择图片
pwlhead_x=310
pwlhead_y=700
pwrhead_x=945
pwrhead_y=700
prlhead_x=315
prlhead_y=635
prrhead_x=950
prrhead_y=635

picture0 = pygame.image.load("白脸左.png")
picture1 = pygame.image.load("白脸右.png")
picture2 = pygame.image.load("红脸左.png")
picture3 = pygame.image.load("人站左.png")
picture4 = pygame.image.load("人站右.png")
ball=pygame.image.load("球.png")
ballrect=ball.get_rect()
ballrect.center=(330,675)
    
def beginning():
    pygame.init()
    screen = pygame.display.set_mode((1200, 800),0,32) 
    pygame.display.set_caption('Matchmaker plays ball')#屏幕标题

    BLACK = 0,0,0 #字的颜色=黑
    GRAY = 195, 201, 195 #背景颜色 = 灰
    BROWN = 241, 154, 52
    screen.fill(GRAY)
    
    #配图
    pic = pygame.image.load("devil.png")
    pic1 = pygame.transform.scale(pic, (500,800))
    picrect=pic1.get_rect()
    picrect.center=(1000, 400)
    screen.blit(pic1,picrect)
    pygame.display.update()
    #Matchmaker plays ball
    fontObj1 = pygame.font.Font('simsun.ttf', 40)
    fontObj1.set_bold(True)#字体加粗
    BROWN = pygame.Color('brown')
    GRAY = pygame.Color('gray')
    BLACK = pygame.Color('black')
    textSurfaceObj1 = fontObj1.render('Matchmaker plays ball', True, BROWN, BLACK)
    textRectObj1 = textSurfaceObj1.get_rect()
    textRectObj1.center = (400, 200)
    screen.blit(textSurfaceObj1, textRectObj1)# 绘制字体
    #W键
    fontObj2 = pygame.font.Font('simsun.ttf', 40)
    textSurfaceObj2 = fontObj2.render('W: jump', True, BROWN, BLACK)
    textRectObj2 = textSurfaceObj1.get_rect()
    textRectObj2.center = (300, 300)
    screen.blit(textSurfaceObj2, textRectObj2)# 绘制字体
    #A键
    fontObj3 = pygame.font.Font('simsun.ttf', 40)
    textSurfaceObj3 = fontObj3.render('A: go back', True, BROWN, BLACK)
    textRectObj3 = textSurfaceObj1.get_rect()
    textRectObj3.center = (300, 350)
    screen.blit(textSurfaceObj3, textRectObj3)# 绘制字体
    #D键
    fontObj4 = pygame.font.Font('simsun.ttf', 40)
    textSurfaceObj4 = fontObj4.render('D: go ahead', True, BROWN, BLACK)
    textRectObj4 = textSurfaceObj1.get_rect()
    textRectObj4.center = (300, 400)
    screen.blit(textSurfaceObj4, textRectObj4)# 绘制字体
    #S键
    fontObj5 = pygame.font.Font('simsun.ttf', 40)
    textSurfaceObj5 = fontObj5.render('S: serve or catch the ball', True, BROWN, BLACK)
    textRectObj5 = textSurfaceObj1.get_rect()
    textRectObj5.center = (300, 450)
    screen.blit(textSurfaceObj5, textRectObj5)# 绘制字体
    pygame.display.update()

    button = pygame.image.load("game_start_up.png")
    screen.blit(button, (300, 600))
    pygame.display.update()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            x, y = pygame.mouse.get_pos()
            if 300 < x and x < 400 and 600 < y and y < 650:#设置start按钮
                button = pygame.image.load("game_start_down.png")
                screen.blit(button, (300, 600))
                pygame.display.update()
            elif x < 300 or x > 400 or y < 600 or y > 650:
                button = pygame.image.load("game_start_up.png")
                screen.blit(button, (300, 600))
                pygame.display.update()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 300 < x and x < 400 and 600 < y and y < 650:
                    return 
    
def background1():
    BLACK=0,0,0#背景色=黑
    DARKGRAY=80,80,80#深灰

    screen.fill(BLACK)
    #左右两道灰色光
    GRAY=pygame.Color('gray')
    leftlight=pygame.draw.polygon(screen,GRAY,[(200,0),(400,0),(600,800),(0,800)],0)
    rightlight=pygame.draw.polygon(screen,DARKGRAY,[(800,0),(1000,0),(1200,800),(600,800)],0)
    #Choose Your Character
    fontObj1 = pygame.font.Font('simsun.ttf', 40)# 通过字体文件获得字体对象
    GREEN=pygame.Color('green')
    BLUE=pygame.Color('blue')
    textSurfaceObj1 = fontObj1.render('Choose Your Character', True, GREEN, BLUE)# 配置要显示的文字
    textRectObj1 = textSurfaceObj1.get_rect()# 获得要显示的对象的rect
    textRectObj1.center = (600, 50)# 设置显示对象的坐标
    screen.blit(textSurfaceObj1, textRectObj1)# 绘制字体
    #头像框
    r1rect=pygame.draw.rect(screen,BLUE,(495,150,60,60))
    r2rect=pygame.draw.rect(screen,BLUE,(650,150,60,60))
    #自带头像
    whitefacerect=picture0.get_rect()
    whitefacerect.center=(520,270)
    screen.blit(picture0,whitefacerect)
    redfacerect=picture2.get_rect()
    redfacerect.center=(680,205)
    screen.blit(picture2,redfacerect)
    #Start
    fontObj2 = pygame.font.Font('simsun.ttf', 40)# 通过字体文件获得字体对象
    GREEN=pygame.Color('green')
    BLUE=pygame.Color('blue')
    textSurfaceObj2 = fontObj2.render('Start', True, GREEN, BLUE)# 配置要显示的文字
    textRectObj2 = textSurfaceObj2.get_rect()# 获得要显示的对象的rect
    textRectObj2.center = (600, 500)# 设置显示对象的坐标
    screen.blit(textSurfaceObj2, textRectObj2)# 绘制字体

def choosecharacters():
    global face
    global whiteOrRed
    background1()
    #火柴盒
    leftbox=pygame.image.load("火柴盒左.png")
    bigleftbox=pygame.transform.scale(leftbox, (300,200))
    leftboxrect=bigleftbox.get_rect()
    leftboxrect.center=(300,600)
    screen.blit(bigleftbox,leftboxrect)
    rightbox=pygame.image.load("火柴盒右.png")
    bigrightbox=pygame.transform.scale(rightbox, (300,200))
    rightboxrect=bigrightbox.get_rect()
    rightboxrect.center=(900,600)
    screen.blit(bigrightbox,rightboxrect)
    rightplayerrect=picture4.get_rect()#站右边
    rightplayerrect.center=(950,500)
    screen.blit(picture4,rightplayerrect)
    whitefacerect=picture1.get_rect()#白右
    whitefacerect.center=(893,547)
    screen.blit(picture1,whitefacerect)

    downum=0#鼠标点击次数
    while True:
        #获取事件并逐类相应
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
            elif event.type==pygame.MOUSEBUTTONDOWN:
                if event.button==1:
                    x,y=pygame.mouse.get_pos()
                    if x>495 and x<555 and y>150 and y<210:#按到白脸
                        whiteOrRed='W头'
                        if downum==0:#左边小人
                            leftplayerrect=picture3.get_rect()#站左边
                            leftplayerrect.center=(300,500)
                            screen.blit(picture3,leftplayerrect)
                            whitefacerect=picture0.get_rect()#白左
                            whitefacerect.center=(305,547)
                            screen.blit(picture0,whitefacerect)
                            face=1
                            downum=1
                            
                    if x>650 and x<710 and y>150 and y<210:#按到红脸
                        whiteOrRed='R头'
                        if downum==0:#左边小人
                            leftplayerrect=picture3.get_rect()#站左边
                            leftplayerrect.center=(300,500)
                            screen.blit(picture3,leftplayerrect)
                            redfacerect=picture2.get_rect()#红左
                            redfacerect.center=(315,485)
                            screen.blit(picture2,redfacerect)
                            face=0
                            downum=1
                    if x>550 and x<650 and y>480 and y<520:
                         if downum==1:
                             pygame.display.init()
                             return 
        pygame.display.update()

class Flash():#实现动起来
    def __init__(self,pictures,x,y,w,h,xspeed,yspeed):
        self.frames_left = pictures
        self.num = len(self.frames_left)#造型个数
        self.no=0#造型编号
        self.qtime=0.000005# 造型切换的时间 秒
        self.ytime=0.00001#移动时间的间隔 秒
        self.x = x
        self.y =y
        self.w = w
        self.h =h
        self.rect=pygame.Rect(self.x,self.y,self.w,self.h)
        self.xspeed=xspeed
        self.yspeed=yspeed
        self.begintime = time.time()
        self.begintime2 = time.time()
        
    def Another(self):#下一个造型
        if (time.time()-self.begintime) >= self.qtime:
            self.no = self.no + 1
            self.no = self.no % self.num
            self.begintime = time.time()
    def move(self):#移动
        if (time.time()-self.begintime2) >= self.ytime:
            self.x = self.x + self.xspeed
            self.y = self.y + self.yspeed        
            self.rect.x = self.x
            self.rect.y = self.y
            if self.rect.left<0 or self.rect.right>width:
                self.xspeed = 0
            self.begintime2 = time.time()
    def draw(self):#绘制造型
        screen.blit(self.frames_left[self.no],self.rect)

speed=[5,-5]
def Ballplay(player):
    global ifHuipai
    global ifFaqiu    
    global ballrect
    global downToUp
    global count
    if ifFaqiu==0:#未发球，随着人物移动
        
        ballrect.center=(player.rect.center[0]+60,player.rect.center[1]+65)
        screen.blit(ball,ballrect)        
        pygame.display.update()
    elif ifFaqiu==1:#发球后,小球运动
        if ifHuipai==0:#不挥拍
            if ballrect.left<-30 or ballrect.right>width*2/3+120:#碰到左右墙
                speed[0]=-speed[0]
            elif ballrect.top<-80:#碰到房顶
                speed[1]=-speed[1]
            elif ballrect.bottom>height:#碰到地失败重来
                ifFaqiu=0
                downToUp=0
                count=0
                speed[0]=5
                speed[1]=-5
                return
        elif ifHuipai==1:#挥拍准备接球
            if player.rect.collidepoint(ballrect.center):
                if player.no==0:
                    if ballrect.collidepoint((player.rect.left+50-5,player.rect.top+82+15)):
                        speed[0]=6
                        speed[1]=-3
                elif player.no==1:
                    if ballrect.collidepoint((player.rect.left+86-5,player.rect.top+60+15)):
                        speed[0]=6
                        speed[1]=-2
                elif player.no==2:
                    if ballrect.collidepoint((player.rect.left+86-5,player.rect.top+50+15)):
                        speed[0]=6
                        speed[1]=-1
                elif player.no==3:
                    if ballrect.collidepoint((player.rect.left+109-5,player.rect.top+58+15)):
                        speed[0]=5
                        speed[1]=5
                
        if pygame.display.get_active():
            ballrect=ballrect.move(speed[0],speed[1])
            screen.blit(ball,ballrect)
            pygame.display.update()

def Ballplaytime():
    global ballrect
    global ifFaqiu
    global downToUp
    global count
    if ballrect.left<-30 or ballrect.right>(width*2/3+120):#碰到左右墙
        speed[0]=-speed[0]
    elif ballrect.top<-80:#碰到房顶
        speed[1]=-speed[1]
    elif ballrect.bottom>height:#碰到地失败重来
        ifFaqiu=0
        downToUp=0
        count=0
        speed[0]=5
        speed[1]=-5
        return
    if pygame.display.get_active():
        ballrect=ballrect.move(speed[0],speed[1])
        screen.blit(ball,ballrect)
        pygame.display.update()

def set_background2(pwlhead_x,pwlhead_y,pwrhead_x,pwrhead_y,prlhead_x,prlhead_y,prrhead_x,prrhead_y):
    global face
    global ifHuipai
    global ifFaqiu
    global downToUp
    global count
    picture3 = pygame.image.load("./"+whiteOrRed+"/人站左.png")
    picture5 = pygame.image.load("./"+whiteOrRed+"/发球左边走1.png")
    picture6 = pygame.image.load("./"+whiteOrRed+"/发球左边走2.png")
    picture7 = pygame.image.load("./"+whiteOrRed+"/发球跳左边.png")
    picture8 = pygame.image.load("./"+whiteOrRed+"/向上挥球1左边.png")
    picture9 = pygame.image.load("./"+whiteOrRed+"/向上挥球2左边.png")
    picture10 = pygame.image.load("./"+whiteOrRed+"/向上挥球3左边.png")
    picture11 = pygame.image.load("./"+whiteOrRed+"/向上挥球4左边.png")
    picture12 = pygame.image.load("./"+whiteOrRed+"/挥拍原地左边.png")
    picture13 = pygame.image.load("./"+whiteOrRed+"/向下挥球1左边.png")
    picture14 = pygame.image.load("./"+whiteOrRed+"/向下挥球2左边.png")
    picture15 = pygame.image.load("./"+whiteOrRed+"/向下挥球3左边.png")
    picture16 = pygame.image.load("./"+whiteOrRed+"/挥拍跳左边.png")
    picture17 = pygame.image.load("./"+whiteOrRed+"/挥拍左边走1.png")
    picture18 = pygame.image.load("./"+whiteOrRed+"/挥拍左边走2.png")
    站左边向左走身体组 = [picture3,picture6,picture5]#发球
    站左边向右走身体组 = [picture3,picture5,picture6]
    挥拍左边向左走身体组 = [picture12,picture18,picture17]
    挥拍左边向右走身体组 = [picture12,picture17,picture18]
    站左边跳身体组=[picture3,picture7]
    挥拍左边跳身体组=[picture12,picture16]
    向上挥拍左身体组=[picture12,picture8,picture9,picture10,picture11,picture12]
    向下挥拍左身体组=[picture3,picture13,picture14,picture15,picture3]
    
    background=pygame.image.load("游戏背景.png")  #图片位置
    bground = pygame.transform.scale(background, (1200, 800))
    screen.blit(bground, (0,0))  #对齐的坐标
    pygame.display.update()   #显示内容
    
    pbodyrect = picture3.get_rect()#人站左
    pbodyrect.center = (300, 650)

    screen.blit(picture3, pbodyrect)
    screen.blit(ball,ballrect)
    pygame.display.update()
    #count=0
    keyStatus=[]#记录按键状态
    keyStatus.append(0)
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
            elif event.type==pygame.KEYDOWN:
                if event.key==97:#A键向左走
                    global 站左边向右走身体
                    global 站左边跳身体
                    global 向下挥拍左身体
                    global 挥拍左边向右走身体
                    global 挥拍左边跳身体
                    global 向上挥拍左身体
                    keyStatus.append(event.key)
                    if ifFaqiu == 0:#发球走
                        count=count+1
                        if count==1:
                            站左边向左走身体 = Flash(站左边向左走身体组,pbodyrect.x, pbodyrect.y,180,240,-10,0)
                        else:
                            if keyStatus[len(keyStatus)-2]==97:#A
                                站左边向左走身体 = Flash(站左边向左走身体组,站左边向左走身体.rect.x, 站左边向左走身体.rect.y,180,240,-10,0)
                            if keyStatus[len(keyStatus)-2]==100:#D
                                站左边向左走身体 = Flash(站左边向左走身体组,站左边向右走身体.rect.x, 站左边向右走身体.rect.y,180,240,-10,0)
                            if keyStatus[len(keyStatus)-2]==119:#W
                                站左边向左走身体 = Flash(站左边向左走身体组,站左边跳身体.rect.x, 站左边跳身体.rect.y,180,240,-10,0)
                            if keyStatus[len(keyStatus)-2]==115:#S
                                站左边向左走身体 = Flash(站左边向左走身体组,向下挥拍左身体.rect.x, 向下挥拍左身体.rect.y,180,240,-10,0)
                        if 站左边向左走身体.rect.left>-17:
                            for i in range(4):
                                screen.blit(bground, (0,0))
                                if 站左边向左走身体.no==0 and i==0:
                                    站左边向左走身体.rect.y=站左边向左走身体.rect.y+8
                                站左边向左走身体.draw()
                                Ballplay(站左边向左走身体)
                                站左边向左走身体.move()
                                站左边向左走身体.Another()
                                pygame.display.update()
                
                    else:#挥拍走
                        count=count+1
                        if count==1:
                            挥拍左边向左走身体 = Flash(挥拍左边向左走身体组,pbodyrect.x-15, pbodyrect.y,180,240,-10,0)
                            for i in range(4):
                                screen.blit(bground, (0,0))
                                挥拍左边向左走身体.draw()
                                挥拍左边向左走身体.move()
                                挥拍左边向左走身体.Another()
                                if 挥拍左边向左走身体.no==1 and i==0:
                                    挥拍左边向左走身体.rect.y=挥拍左边向左走身体.rect.y-8
                                if 挥拍左边向左走身体.no==1:
                                    挥拍左边向左走身体.rect.x=挥拍左边向左走身体.rect.x-30
                                if 挥拍左边向左走身体.no==2:
                                    挥拍左边向左走身体.rect.x=挥拍左边向左走身体.rect.x-30
                                    
                                pygame.display.update()
                        else:
                            if keyStatus[len(keyStatus)-2]==97:#A
                                if 挥拍左边向左走身体.x<=-2:
                                    挥拍左边向左走身体 = Flash(挥拍左边向左走身体组,挥拍左边向左走身体.rect.x, 挥拍左边向左走身体.rect.y,180,240,-10,0)
                                else:
                                    挥拍左边向左走身体 = Flash(挥拍左边向左走身体组,挥拍左边向左走身体.rect.x+30, 挥拍左边向左走身体.rect.y,180,240,-10,0)
                            if keyStatus[len(keyStatus)-2]==100:#D
                                if 挥拍左边向右走身体.rect.right>=(width*2/3-20):
                                    挥拍左边向左走身体 = Flash(挥拍左边向左走身体组,挥拍左边向右走身体.rect.x, 挥拍左边向右走身体.rect.y,180,240,-10,0)
                                else:
                                    挥拍左边向左走身体 = Flash(挥拍左边向左走身体组,挥拍左边向右走身体.rect.x+30, 挥拍左边向右走身体.rect.y,180,240,-10,0)
                            if keyStatus[len(keyStatus)-2]==119:#W
                                挥拍左边向左走身体 = Flash(挥拍左边向左走身体组,挥拍左边跳身体.rect.x, 挥拍左边跳身体.rect.y,180,240,-10,0)
                            if keyStatus[len(keyStatus)-2]==115:#S
                                if downToUp==0 and ifFaqiu==1:
                                    挥拍左边向左走身体 = Flash(挥拍左边向左走身体组,向下挥拍左身体.rect.x, 向下挥拍左身体.rect.y,180,240,-10,0)
                                    downToUp=1
                                else:
                                    挥拍左边向左走身体 = Flash(挥拍左边向左走身体组,向上挥拍左身体.rect.x, 向上挥拍左身体.rect.y,180,240,-10,0)
                            if 挥拍左边向左走身体.x>-2:
                                for i in range(4):
                                    screen.blit(bground, (0,0))
                                    挥拍左边向左走身体.draw()
                                    Ballplay(挥拍左边向左走身体)
                                    挥拍左边向左走身体.move()
                                    挥拍左边向左走身体.Another()
                                    if 挥拍左边向左走身体.no==1 and i==0:
                                        挥拍左边向左走身体.rect.y=挥拍左边向左走身体.rect.y-8
                                    if 挥拍左边向左走身体.no==1:
                                        挥拍左边向左走身体.rect.x=挥拍左边向左走身体.rect.x-30
                                    if 挥拍左边向左走身体.no==2:
                                        挥拍左边向左走身体.rect.x=挥拍左边向左走身体.rect.x-30
                                    pygame.display.update()
                elif event.key==100:#D键向右走
                    keyStatus.append(event.key)
                    if ifFaqiu == 0:#发球走
                        count=count+1
                        if count==1:
                            站左边向右走身体 = Flash(站左边向右走身体组,pbodyrect.x, pbodyrect.y,180,240,10,0)
                        else:
                            if keyStatus[len(keyStatus)-2]==97:#A
                                站左边向右走身体 = Flash(站左边向右走身体组,站左边向左走身体.rect.x, 站左边向左走身体.rect.y,180,240,10,0)
                            if keyStatus[len(keyStatus)-2]==100:#D
                                站左边向右走身体 = Flash(站左边向右走身体组,站左边向右走身体.rect.x, 站左边向右走身体.rect.y,180,240,10,0)
                            if keyStatus[len(keyStatus)-2]==119:#W
                                站左边向右走身体 = Flash(站左边向右走身体组,站左边跳身体.rect.x, 站左边跳身体.rect.y,180,240,10,0)
                            if keyStatus[len(keyStatus)-2]==115:#S
                                站左边向右走身体 = Flash(站左边向右走身体组,向下挥拍左身体.rect.x, 向下挥拍左身体.rect.y,180,240,10,0)
                        if 站左边向右走身体.rect.right<(width*2/3+50):
                            for i in range(3):
                                screen.blit(bground, (0,0))
                                站左边向右走身体.move()
                                站左边向右走身体.Another()
                                站左边向右走身体.draw()
                                Ballplay(站左边向右走身体)
                                pygame.display.update()
                    else:#挥拍走
                        count=count+1
                        if count==1:
                            挥拍左边向右走身体 = Flash(挥拍左边向右走身体组,pbodyrect.x-15, pbodyrect.y,180,240,10,0)
                            for i in range(4):
                                screen.blit(bground, (0,0))
                                挥拍左边向右走身体.draw()
                                Ballplay(挥拍左边向右走身体)
                                挥拍左边向右走身体.move()
                                挥拍左边向右走身体.Another()
                                if 挥拍左边向右走身体.no==1:
                                    挥拍左边向右走身体.rect.x=挥拍左边向右走身体.rect.x-30
                                if 挥拍左边向右走身体.no==2:
                                    挥拍左边向右走身体.rect.x=挥拍左边向右走身体.rect.x-30
                                    挥拍左边向右走身体.rect.y=挥拍左边向右走身体.rect.y-8
                                pygame.display.update()
                            
                        else:
                            if keyStatus[len(keyStatus)-2]==97:#A
                                挥拍左边向右走身体 = Flash(挥拍左边向右走身体组,挥拍左边向左走身体.rect.x+30, 挥拍左边向左走身体.rect.y,180,240,10,0)
                            if keyStatus[len(keyStatus)-2]==100:#D
                                if 挥拍左边向右走身体.rect.right>=(width*2/3-20):
                                    挥拍左边向右走身体 = Flash(挥拍左边向右走身体组,挥拍左边向右走身体.rect.x, 挥拍左边向右走身体.rect.y,180,240,10,0)
                                else :
                                    挥拍左边向右走身体 = Flash(挥拍左边向右走身体组,挥拍左边向右走身体.rect.x+30, 挥拍左边向右走身体.rect.y,180,240,10,0)
                            if keyStatus[len(keyStatus)-2]==119:#W
                                挥拍左边向右走身体 = Flash(挥拍左边向右走身体组,挥拍左边跳身体.rect.x, 挥拍左边跳身体.rect.y,180,240,10,0)
                            if keyStatus[len(keyStatus)-2]==115:#S 
                                if downToUp==0 and ifFaqiu==1:
                                    挥拍左边向右走身体 = Flash(挥拍左边向右走身体组,向下挥拍左身体.rect.x, 向下挥拍左身体.rect.y,180,240,10,0)
                                    downToUp=1
                                else:
                                    挥拍左边向右走身体 = Flash(挥拍左边向右走身体组,向上挥拍左身体.rect.x, 向上挥拍左身体.rect.y,180,240,10,0)
                            if 挥拍左边向右走身体.rect.right<(width*2/3-20):
                                for i in range(4):
                                    screen.blit(bground, (0,0))
                                    挥拍左边向右走身体.draw()
                                    Ballplay(挥拍左边向右走身体)
                                    挥拍左边向右走身体.move()
                                    挥拍左边向右走身体.Another()
                                    if 挥拍左边向右走身体.no==1:
                                        挥拍左边向右走身体.rect.x=挥拍左边向右走身体.rect.x-30
                                    if 挥拍左边向右走身体.no==2:
                                        挥拍左边向右走身体.rect.x=挥拍左边向右走身体.rect.x-30
                                        挥拍左边向右走身体.rect.y=挥拍左边向右走身体.rect.y-8
                                    pygame.display.update()
                elif event.key==119:#W键向上跳
                    keyStatus.append(event.key)
                    if ifFaqiu == 0:#发球跳
                        count=count+1
                        if count==1:
                            站左边跳身体 = Flash(站左边跳身体组,pbodyrect.x, pbodyrect.y,180,240,0,-20)            
                        else:
                            if keyStatus[len(keyStatus)-2]==97:#A
                                站左边跳身体 = Flash(站左边跳身体组,站左边向左走身体.rect.x, 站左边向左走身体.rect.y,180,240,0,-20)
                            if keyStatus[len(keyStatus)-2]==100:#D
                                站左边跳身体 = Flash(站左边跳身体组,站左边向右走身体.rect.x, 站左边向右走身体.rect.y,180,240,0,-20)
                            if keyStatus[len(keyStatus)-2]==119:#W
                                站左边跳身体 = Flash(站左边跳身体组,站左边跳身体.rect.x, 站左边跳身体.rect.y,180,240,0,-20)
                            if keyStatus[len(keyStatus)-2]==115:#S
                                站左边跳身体 = Flash(站左边跳身体组,向下挥拍左身体.rect.x, 向下挥拍左身体.rect.y,180,240,0,-20)
                        tempbx=站左边跳身体.rect.x
                        tempby=站左边跳身体.rect.y
                        for i in range(3):
                            if i<2:
                                screen.blit(bground, (0,0))
                                站左边跳身体.move()
                                站左边跳身体.Another()
                                站左边跳身体.draw()
                                Ballplay(站左边跳身体)
                                pygame.display.update()      
                            else:
                                站左边跳身体 = Flash(站左边跳身体组,tempbx, tempby,180,240,0,0)
                                screen.blit(bground, (0,0))
                                站左边跳身体.move()
                                站左边跳身体.draw()
                                Ballplay(站左边跳身体)
                                pygame.display.update()
                    else:#挥拍跳
                        count=count+1
                        if count==1:
                            挥拍左边跳身体 = Flash(挥拍左边跳身体组,pbodyrect.x-15, pbodyrect.y-5,180,240,0,-20)            
                        else:
                            if keyStatus[len(keyStatus)-2]==97:#A
                                挥拍左边跳身体 = Flash(挥拍左边跳身体组,挥拍左边向左走身体.rect.x+36, 挥拍左边向左走身体.rect.y,180,240,0,-20)
                            if keyStatus[len(keyStatus)-2]==100:#D
                                if 挥拍左边向右走身体.rect.right>=(width*2/3-20):
                                    挥拍左边跳身体 = Flash(挥拍左边跳身体组,挥拍左边向右走身体.rect.x, 挥拍左边向右走身体.rect.y,180,240,0,-20)
                                else:
                                    挥拍左边跳身体 = Flash(挥拍左边跳身体组,挥拍左边向右走身体.rect.x+30, 挥拍左边向右走身体.rect.y,180,240,0,-20)
                            if keyStatus[len(keyStatus)-2]==119:#W
                                挥拍左边跳身体 = Flash(挥拍左边跳身体组,挥拍左边跳身体.rect.x, 挥拍左边跳身体.rect.y,180,240,0,-20)
                            if keyStatus[len(keyStatus)-2]==115:#S
                                if downToUp==0 and ifFaqiu==1:
                                    挥拍左边跳身体 = Flash(挥拍左边跳身体组,向下挥拍左身体.rect.x, 向下挥拍左身体.rect.y,180,240,0,-20)
                                    downToUp=1
                                else:
                                    挥拍左边跳身体 = Flash(挥拍左边跳身体组,向上挥拍左身体.rect.x, 向上挥拍左身体.rect.y,180,240,0,-20)
                        tempbx=挥拍左边跳身体.rect.x
                        tempby=挥拍左边跳身体.rect.y
                        for i in range(3):
                            if i<2:
                                screen.blit(bground, (0,0))
                                挥拍左边跳身体.draw()
                                Ballplay(挥拍左边跳身体)
                                挥拍左边跳身体.move()
                                if i==0: 
                                    挥拍左边跳身体.rect.x=挥拍左边跳身体.rect.x-37
                                    挥拍左边跳身体.rect.y=挥拍左边跳身体.rect.y
                                挥拍左边跳身体.Another()
                                pygame.display.update()      
                            else:
                                挥拍左边跳身体 = Flash(挥拍左边跳身体组,tempbx, tempby,180,240,0,0)
                                screen.blit(bground, (0,0))
                                挥拍左边跳身体.move()
                                挥拍左边跳身体.draw()
                                Ballplay(挥拍左边跳身体)
                                pygame.display.update()
                if event.key==115:#S键挥拍
                    keyStatus.append(event.key)
                    if ifFaqiu == 0:#S键向下挥拍
                        ifFaqiu=1#开始发球
                        count=count+1
                        if count==1:
                            向下挥拍左身体 = Flash(向下挥拍左身体组,pbodyrect.x, pbodyrect.y,180,240,0,0)
                            
                        else:
                            if keyStatus[len(keyStatus)-2]==97:#A
                                向下挥拍左身体 = Flash(向下挥拍左身体组,站左边向左走身体.rect.x+10, 站左边向左走身体.rect.y,180,240,0,0)
                            if keyStatus[len(keyStatus)-2]==100:#D
                                向下挥拍左身体 = Flash(向下挥拍左身体组,站左边向右走身体.rect.x, 站左边向右走身体.rect.y,180,240,0,0)
                            if keyStatus[len(keyStatus)-2]==119:#W
                                向下挥拍左身体 = Flash(向下挥拍左身体组,站左边跳身体.rect.x, 站左边跳身体.rect.y,180,240,0,0)
                            if keyStatus[len(keyStatus)-2]==115:#S
                                向下挥拍左身体 = Flash(向下挥拍左身体组,向下挥拍左身体.rect.x, 向下挥拍左身体.rect.y,180,240,0,0)
                        for i in range(5):
                            screen.blit(bground, (0,0))
                            向下挥拍左身体.draw()
                            Ballplay(向下挥拍左身体)
                            向下挥拍左身体.Another()
                            if 向下挥拍左身体.no==1:
                                向下挥拍左身体.rect.x=向下挥拍左身体.rect.x-7
                                向下挥拍左身体.rect.y=向下挥拍左身体.rect.y+23
                            if 向下挥拍左身体.no==2:
                                向下挥拍左身体.rect.x=向下挥拍左身体.rect.x+25
                                向下挥拍左身体.rect.y=向下挥拍左身体.rect.y-5
                            if 向下挥拍左身体.no==3:
                                向下挥拍左身体.rect.x=向下挥拍左身体.rect.x+8
                                向下挥拍左身体.rect.y=向下挥拍左身体.rect.y-25
                            if 向下挥拍左身体.no==4:
                                向下挥拍左身体.rect.x=向下挥拍左身体.rect.x-26
                                向下挥拍左身体.rect.y=向下挥拍左身体.rect.y+7
                            pygame.display.update()
                    
                    else:#向上挥拍
                        count=count+1
                        ifHuipai=1
                        if count==1:
                            向上挥拍左身体 = Flash(向上挥拍左身体组,pbodyrect.x, pbodyrect.y,180,240,0,0)
                        else:
                            if keyStatus[len(keyStatus)-2]==97:#A
                                向上挥拍左身体 = Flash(向上挥拍左身体组,挥拍左边向左走身体.rect.x+36, 挥拍左边向左走身体.rect.y,180,240,0,0)
                            if keyStatus[len(keyStatus)-2]==100:#D
                                if 挥拍左边向右走身体.rect.right>=(width*2/3-20):
                                    向上挥拍左身体 = Flash(向上挥拍左身体组,挥拍左边向右走身体.rect.x, 挥拍左边向右走身体.rect.y,180,240,0,0)
                                else:
                                    向上挥拍左身体 = Flash(向上挥拍左身体组,挥拍左边向右走身体.rect.x+30, 挥拍左边向右走身体.rect.y,180,240,0,0)
                            if keyStatus[len(keyStatus)-2]==119:#W
                                向上挥拍左身体 = Flash(向上挥拍左身体组,挥拍左边跳身体.rect.x, 挥拍左边跳身体.rect.y,180,240,0,0)
                            if keyStatus[len(keyStatus)-2]==115:#S
                                if downToUp==0 and ifFaqiu==1:
                                    向上挥拍左身体 = Flash(向上挥拍左身体组,向下挥拍左身体.rect.x, 向下挥拍左身体.rect.y,180,240,0,0)
                                    downToUp=1
                                else:
                                    向上挥拍左身体 = Flash(向上挥拍左身体组,向上挥拍左身体.rect.x, 向上挥拍左身体.rect.y,180,240,0,0)
                        for i in range(6):
                            screen.blit(bground, (0,0))
                            if 向上挥拍左身体.no==0:
                                向上挥拍左身体.rect.x=向上挥拍左身体.rect.x-10
                            向上挥拍左身体.draw()
                            Ballplay(向上挥拍左身体)
                            向上挥拍左身体.Another()
                            if 向上挥拍左身体.no==1:
                                向上挥拍左身体.rect.x=向上挥拍左身体.rect.x-10
                            if 向上挥拍左身体.no==2:
                                向上挥拍左身体.rect.x=向上挥拍左身体.rect.x+28
                            if 向上挥拍左身体.no==3:
                                向上挥拍左身体.rect.x=向上挥拍左身体.rect.x+50
                            if 向上挥拍左身体.no==4:
                                向上挥拍左身体.rect.x=向上挥拍左身体.rect.x+15
                            if 向上挥拍左身体.no==5:
                                向上挥拍左身体.rect.x=向上挥拍左身体.rect.x-73
                            ifHuipai=0
                            pygame.display.update()
                            
        else:
            if ifFaqiu==1:
                Ballplaytime()
                fclock.tick(fps)
  
def main():
    pygame.init()
    beginning()
    choosecharacters() 
    set_background2(pwlhead_x,pwlhead_y,pwrhead_x,pwrhead_y,prlhead_x,prlhead_y,prrhead_x,prrhead_y)
    
if __name__ == "__main__":
    sys.exit(main())

