#Instantiate Variables L = length, T = theta/angle, O = origin, m = mass, g = gravity, px/px = past x and past y
L1 = 175
L2 = 200
T1 = -80
T2 = -80
Ox = 500
Oy = 500
m1 = 35
m2 = 35
g = 1.5
px2 = 0
py2 = 0

#v = velocity, a = acceleration
T1_v = 0
T2_v = 0
T1_a = 0
T2_a = 0





canvas = None

def setup():
    size(1000,1000)
    global canvas
    canvas = createGraphics(1000,1000)
    canvas.beginDraw()
    canvas.background(0)
    canvas.endDraw()
    
def draw():
    # Call global variables
    global T1,T2,T1_v,T2_v,T1_a,T2_a,L2,L1,px2,py2
    #
    
    #background(0)
    image(canvas,0,0)
    stroke(255)
    translate(Ox,Oy)
    x1 = (L1 * sin(T1))
    y1 = (L1 * cos(T1))
    x2 = x1 + (L2 * sin(T2))
    y2 = y1 + (L2 * cos(T2))
    
    #Draw on Origin 
    fill(255)
    ellipse(0,0,20,20)

    line(0,0,x1,y1)
    fill(255)
    ellipse(x1,y1,m1,m1)
    line(x1,y1,x2,y2)
    fill(0)
    ellipse(x2,y2,m2,m2)
    
    
    
    
    #T1_a formula
    t11= -g*(2*m1 + m2)*sin(T1) - m2*g*sin(T1 - 2*T2)
    t12= 2*sin(T1-T2)*m2*(pow(T2_v,2)*L2 + pow(T1_v,2)*L1*cos(T1-T2))
    t13= L1 * (2*m1+m2-m2*cos(2*T1-2*T2))
    
    T1_a = (t11-t12)/t13
    #T1_a += 0.1
    
    #T2_a formula
    t21= 2*sin(T1-T2)*(pow(T1_v,2)*L1*(m1 + m2)+g*(m1+m2)*cos(T1)+pow(T2_v,2)*L2*m2*cos(T1-T2))
    t22= L2 * (2*m1+m2-m2*cos(2*T1-2*T2))

    T2_a = t21 / t22
    #T2_a -= 0.2
    
    #Change velocity with acceleration then change the angle with the velocity.
    T1_v += T1_a
    T2_v += T2_a
    T1+= T1_v
    T2+= T2_v
    
    point(x2,y2)
    
    
    canvas.beginDraw()
    canvas.translate(Ox,Oy)
    if frameCount>1:
        canvas.line(px2,py2,x2,y2)
        #canvas.point(x2,y2)
    canvas.stroke(255)
    canvas.strokeWeight(2)
    canvas.endDraw()


    #Assign the old coordinates for line drawing
    px2 = x2
    py2 = y2
    
    
    
