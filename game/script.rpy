# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define un = Character("-",color='#ffebeb')
define m = Character("เม็ลท",color='#440000')
define mo = Character('โมนีค',color='#e0edff')
define s7 = Character("S7",color="#c8ceff")
define ze = Character("ซิลี",color='#e0edff')
define chri = Character("คิส​ต​อฟ​",color='#afc5e3')
define a = Character("อัลเลน​",color='#82a3ff')
define s = Character("star",color='#fffb91')
define t = Character("time",color='#fffb91')
define i = Character("ฉัน",color='#adb7c9')


# The game starts here.

label start:
    
    jump skip_เข้า_loop

    label เข้า_loop:
        
        scene is_true

        label loop:

        show ho_2_sulfur_pose_2
        t'งะ งะ  งะ' 
        show ho_1_sulfur_pose_2 with easy
        hide ho_2_sulfur_pose_2

        t'ไงงง'
        show ho_2_sulfur_pose_2
        show ho_1_sulfur_pose_2
        t 'ฉัน{color=#fffb91}star{/color}'
        t 'ไง'


        t 'ฉ  ฉ   ฉัน {color=#fffb91}star{/color}'

        jump loop

    label skip_เข้า_loop:

    
    # with moveinright

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.


    # pop s7 

    scene background_cream 
    show s7n with fade

    un "......"
    show s7อมยิ้ม with dissolve
    hide s7n
    un "............"
    show s7ยิ้ม with dissolve
    hide s7อมยิ้ม


    un 'ไง เราชื่อ S7 นะ'
    show s7อมยิ้ม with dissolve
    hide s7ยิ้ม
    s7 'เราจะเจอกันเกือบทั้งเกมเลย{w} เพราะงั้นมาเป็นมิตรกับ S7 กันเถอะ'
    s7 'ว่าแต่{cps=5}...{/cps=5}เธอชื่ออะไรเหรอ?'
    hide screen gameUI
    
    show s7อมยิ้ม with dissolve
    hide s7ยิ้ม
    $ yn = renpy.input('ชื่อคุณ')

    
    label ตรวจชื่อ :
    if yn.lower() == '':

        hide s7ยิ้ม
        show s7n with dissolve
        s7 'อ้าว{cps=5}...{/cps=5}ไม่มีใครอยู่เหรอ?'
        s7 'แปลกจัง{cps=7}....{/cps=7}\nแล้วใคร{cps=5}...{/cps=5}เปิดระบบเนี้ย'
        s7 'ช่างมันเถอะนั่งเขียน Code ต่อดีกว่า'
        stop sound fadeout 1.0
        jump end

    elif yn.lower()== 's7'or yn.lower()=='s 7':
        scene background_peach 
        show s7ฮะๆ
        s7'นั้นชื่อฉันนิ'
        show s7อมยิ้ม with dissolve
        hide s7ฮะๆ
        s7'นี้เธอตั้งใจรึเปล่าเนี้ย?'
        menu :
            'ก็..ใช่' :
                s7'งั้นก็ขอชื่อจริงๆของเธอด้วนะ'
                $ yn = renpy.input('ใส่ชื่อจริงๆของคุณ')
                jump ตรวจชื่อ

            'ไม่นะ นี้คือชื่อของฉัน' :
                scene background_water_blue 
                show s7ไมเห็นด้วย 
                s7'อื่ม...'
                s7'มีคนชื่อเหมือนฉันอยู่จริงๆเหรอเนี้ย'
                s7'แต่ก็ช่างเถอะ'
                jump ต่อจากคุยเรื่องชื่อ
                
    elif yn.lower() == 'melt'or yn.lower() == 'star'or yn.lower() == 'mini s7'or yn.lower() == 'hiruso':
        hide s7อมยิ้ม
        show s7อุ้
        hide s7n
        s7 'เอ๋?'
        show s7ฮะๆ
        with dissolve
        hide s7ยิ้ม
        hide s7อุ้
        s7 '[yn] นี้ไม่ได้นะ'
        s7 'นี้มันยังไม่ถึงตาเธอน่ะ'
        jump end
    
    else:
        jump ต่อจากคุยเรื่องชื่อ
    

    label ต่อจากคุยเรื่องชื่อ :

        show s7อมยิ้ม
        hide s7ไมเห็นด้วย
        s7 '{cps=5}[yn]{/cps} เหรอ น่าสนใจดีนะ'
        
        s7 'S7 ดีใจมากเลยที่ [yn] เข้ามาเล่นเกมนี้น่ะ'
        s7 "{size=16}{cps=*2}{s}ถึงแม้จะไม่รู้ว่า [yn] พูดหรือรู้สึกอะไรอยู่ก็ตาม{/size=16}{/cps=*2}{/s}{nw}"
        show s7อุ้
        with dissolve
        hide s7อมยิ้ม
        
        s7 'แล้ว{cps=5}..{/cps=5} [yn] อะไรทำให้เธอสนใจเข้ามาในเกมนี้เหรอ?'
        menu :
            'เกมนี้คนไทยสร้าง':
                jump โอ้จริงด้วย
            'ไม่มีอะไรทำเลยมาน่ะ':
                jump งั้นเรามาเข้าเกมกันเลยดีมั้ย
            'ไม่มี Choice ที่ตรงใจ':
                jump โอ้ช่ายนั้นเป็นคำตอบที่น่ากลัวที่สุด
            'เธอไง':
                jump s7เขินนะ

        
        label โอ้จริงด้วย :
            show s7อมยิ้ม with dissolve
            hide s7อุ้

            s7 'โอ้จริงด้วย!'
            s7 'แล้ว [yn] รู้มั้ยว่าเกมมี้ก็เป็นเกมแรกที่ผู้สร้างเริ่มเขียน code ตั้งค่าต่างๆ{p}แต่งเนื้อเรื่องเอย{w} วาดรูปเอย'
            
            show s7ฮะๆ with dissolve
            hide s7อมยิ้ม
            s7 'อะไรก็ไม่รู้เยอะไปหมด'
            show s7อมยิ้ม 
            hide s7ฮะๆ
            s7 'และถ้ามีอะไรผิดผลาดไป S7 ก็ต้องขอโทษแทน...'
            jump โอ้จริงด้วยมันกินเวลาของเกม

        label โอ้ช่ายนั้นเป็นคำตอบที่น่ากลัวที่สุด :
            show s7อมยิ้ม with dissolve
            hide s7อุ้
            s7 'โอ้ช่าย นั้นเป็นคำตอบที่น่ากลัวที่สุดเลยที่ S7 ไม่อยากเจอ'
            jump โอ้จริงด้วยมันกินเวลาของเกม

    label s7เขินนะ :
            show s7ฮะๆ with dissolve
            hide s7อุ้

            s7 'เขินนะ'
            jump โอ้จริงด้วยมันกินเวลาของเกม


            label โอ้จริงด้วยมันกินเวลาของเกม :
            show s7อุ้ with dissolve
            hide s7ยิ้ม
            hide s7อมยิ้ม
            hide s7ฮะๆ
            hide s7เขินนะ

            s7'{cps=*2}โอ้! จริงด้วย!{/cps=*2} {w}มันกินเวลาของเกม'
            jump งั้นเรามาเข้าเกมกันเลยดีมั้ย


    label งั้นเรามาเข้าเกมกันเลยดีมั้ย :
        show s7อมยิ้ม with dissolve
        hide s7อุ้
        s7'งั้นเรามาเข้าเกมกันเลยดีมั้ย'
        yn'เอ่อ...'
        show s7ฮะๆ with dissolve 
        hide s7อมยิ้ม
        s7'ไม่ทันแล้ววว'
        

    # scene is_true with pixellate
    screen bedroom 
    
    screen saveload

    
    label whereamI:
        scene ห้องสาวงาม1280
        
        show mait2_14 with zoomin
        i'!!'with hpunch

        'เด็กหญิงตื่นขึ้นมา'
        'ในนั้นหัวชาไปหมด'
        show mait21_1 with dissolve
        hide mait2_14
        'แต่ไม่นานเด็กหญิงก็สามารถจูนตัวเองให้อยู่ในปัจจุบันได้'
        i'??'
        'เด็กหญิงเริ่มกวาดตามองไปรอบๆ {w}เพื่อทำความคุ้นเคยกับสถานที่'
        show mait2_4 with dissolve
        hide mait21_1
        i'{cps=7}......{/cps}'
        i'นี้ฉันอยู่ที่ไหน?'
        'แต่ยังไม่ทันได้ประติดประต่อเรื่องราว {w}ก็มีผู้หญิงคนหนึ่งเดินเข้ามาในห้องที่ไม่คุ้นตาแห่งนี้'
        show mait2_4 at left with move
        show mait21_1 at left with dissolve
        hide mait2_4
        show monique1 at right with moveinright 
        pause(2.0)

        un'คุณเม็ลทคะ ได้เวลาทานอาหารเช้าแล้วค่ะ'

        show mait2_14 at left
        hide mait21_1
        i'!!'
        un'{cps=7}......{/cps}'
        un'โอ้?'
        un'ต้องขออภัยด้วยค่ะ คุณคงจะยังไม่รู้จักดิฉันสินะคะ'
        mo'ดิฉันมีชื่อว่า {color=#e0edff}โมนีค{/color} เป็นมือซ้ายของคุณ{color=#afc5e3}​คีส​ต​อฟ​{/color}'
        show mait2_13 at left with dissolve
        i'{cps=5}....{/cps}'

        show monique2 at right with dissolve
        hide monique1

        mo'คุณ{color=#afc5e3}คีส​ต​อฟ​{/color}เป็นผู้รับอุปการะคุณ​เม็ลทไงคะ'
        i'(เม็ลท?)'

        i'(นี้ชื่อฉันหรอ)'
        show monique1 at right with dissolve
        hide monique2
        mo'คุณเมดได้เตรียมอาหารเช้าไว้ให้คุณเรียบร้อยแล้วนะคะ'
        mo'ถ้าคุณหนูทำธุระส่วนตัวเสร็จแล้วล่ะก็ ขอเชิญลงไปรับประทานอาหารเช้าแล้วก็..'
        mo'คุณ{color=#afc5e3}คีส​ต​อฟ​{/color} กำลังรอคุณอยู่ค่ะ'

        hide monique1 with moveoutright
        pause(2.0)
        
        'โมนีค เดินออกไปจากห้อง'
        s7'{image=minis7_1}ทำธุระส่วนตัวเหรอ?'
        s7'{image=minis7_3}S7 คิดว่าน่าจะแปรงฟันอาบน้ำ {w}แต่ถ้าอาบน้ำก็ต้องเปลี่ยนชุดด้วยนะสิ..'



        'test'
        
        
        
        

    



    jump end


    label end:


    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


    # These display lines of dialogue.

    
    # This ends the game.

    return
