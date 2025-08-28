import turtle,random,time

ekran=turtle.Screen() #screen turtle kütüphanesinde tanımlı bir sınıftır. Bir pencere yani oyun ekranı oluşturur.
ekran.title("snake game") #screen sınıfının metotları(fonksiynları)
ekran.bgcolor("black")
ekran.setup(width=900,height=600,startx=300, starty=90)#pencere boyutlarını ayarlar.
ekran.tracer(0) #çizimlerin ve animasyonların hızını kontrol etmek için kullanılır.Biz otomatik güncellemeyi kapattık.

head=turtle.Turtle() #ekranda çizim yapan nesneyi temsil eden sınıf.
head.speed(0)#Turtle’ın çizim hızını ayarlar.
head.shape("square")
head.color("pink")
head.penup()#çizim yapmıyoruz.
head.goto(0,0)
head.yon="stop"  #degısken ekledık baslangıcta duracak.

food=turtle.Turtle()
food.speed(0)
food.shape("turtle")
food.color("green")
food.penup()
food.goto(0,50)

skor = 0  # skor değişkeni
rekor=0
yazi = turtle.Turtle()
yazi2=turtle.Turtle()
yazi.speed(0)
yazi2.speed(0)
yazi.color("white")
yazi2.color("red")
yazi.penup()
yazi2.penup()
yazi2.hideturtle()
yazi.hideturtle() #Turtle kütüphanesinin bir metodudur
yazi.goto(0, 260)  # ekranın üst kısmına yerleştirdik
yazi2.goto(0, 230)
yazi.write(f"Skor: {skor}", align="center", font=("Arial", 24, "normal"))
yazi2.write(f"Rekor:{skor}",align="center", font=("Arial", 15, "normal"))

yılanıngovdesı=[]
score=0
hiz = 0.14 # başlangıç hızı

def yukarı():
    if head.yon !="down": #mantığı: aşağı gitmiyorsa yukarı gidebilir.bunu yazmasaydık kendisine çarpardı ve oyun biterdi.
        head.yon="up"
def asagı():
    if head.yon!="up": 
        head.yon="down"

def sol():
    if head.yon!="right":
        head.yon="left"
def sag():
    if head.yon!="left":
         head.yon="right"

def move(): # yılan her adımda 20 birim haereket edecek
    if head.yon=="up":
        y=head.ycor()  # y.cor=Turtle nesnesinin mevcut y koordinatını verir.
        head.sety(y+20) #sety=y koordinatını değiştirir (hareket ettirir)
    if head.yon=="down":
        y=head.ycor()
        head.sety(y-20)
    if head.yon=="right":
        x=head.xcor()
        head.setx(x+20)
    if head.yon=="left":
        x=head.xcor()
        head.setx(x-20)
    

#listen() ve onkeypress() Turtle kütüphanesinin Screen sınıfına özel fonksiyonlardır.
ekran.listen() #listen():Bu pencere klavye olaylarını dinlemeye hazır hale gelir.
ekran.onkeypress(yukarı,"w")  #onkeypress():Belirli tuşa basıldığında hangi fonksiyon çalışacak, onu ayarlar.
ekran.onkeypress(asagı,"s")
ekran.onkeypress(sol,"a")
ekran.onkeypress(sag,"d")

while True:
    ekran.update() #turtle modülüne ait bir Screen metodudur ve tracer(0) ile birlikte kullanılır.Tüm çizimleri ve hareketleri manuel olarak ekrana yansıtır.
    time.sleep(hiz)
    #duvara çarpma kontrolü
    if head.xcor()>440 or head.xcor()<-440 or head.ycor()>290 or head.ycor()<-290:
        head.goto(0,0)
        head.yon="stop"
        time.sleep(1) #time.sleep(saniye) → Python’un time modülüne ait bir fonksiyondur.Programın belirli bir süre durmasını sağlar.
        

    
        #kuyruk sıfırlanıyor.
        for govde in yılanıngovdesı:
            govde.goto(1000,1000)
        yılanıngovdesı.clear()#Python’da listeler için kullanılan bir metottur.Listenin içindeki tüm elemanları siler,
         
        
        # Skoru sıfırla
        hiz=0.13 #baslangıc hızı
        skor = 0
        yazi.clear()
        yazi.write(f"Skor: {skor}", align="center", font=("Arial", 24, "normal"))
 
    
    #yemi yeme kontrolü
    if head.distance(food)<20: #Turtle sınıfına özel bir metottur.Görevi iki Turtle nesnesi arasındaki uzaklığı ölçmek.
        x=random.randint(-370,370)
        y=random.randint(-240,240)
        food.goto(x,y)

         # Skoru artır
        skor += 10
               
        if skor>=rekor:
            rekor=skor

        yazi.clear()
        yazi.write(f"Skor: {skor}", align="center", font=("Arial", 20, "normal"))
        yazi2.clear()
        yazi2.write(f"Rekor: {rekor}", align="center", font=("Arial", 15, "normal"))

        hiz *= 0.95# Hızı biraz artır

        #kuyruga yeni segment ekleniyor.
        yenıgovde=turtle.Turtle()
        yenıgovde.speed(0)
        yenıgovde.shape("square")
        yenıgovde.color("pink")
        yenıgovde.penup()
        yılanıngovdesı.append(yenıgovde)

    # Kuyruğu Hareket Ettir
    for index in range(len(yılanıngovdesı)-1, 0, -1):
        x = yılanıngovdesı[index-1].xcor()  #bir önceki segmentin pozisyonu
        y = yılanıngovdesı[index-1].ycor()
        yılanıngovdesı[index].goto(x, y)

    # Kuyruğun İlk segmenti Başa Bağlanır
    if len(yılanıngovdesı) > 0:
        x = head.xcor()
        y = head.ycor()
        yılanıngovdesı[0].goto(x, y) #Segmentlerin en başı (0. segment) doğrudan head’in pozisyonuna gider.Böylece:Head hareket eder,0. segment head’i takip eder,Sonraki segmentler bir önceki segmenti takip eder.



    move()
    