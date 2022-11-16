# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define un = Character("-",color='#f1ebff')
define m = Character("เม็ลท",color='#8f0000')
define mo = Character('โมนีค',color='#e0edff')
define s7 = Character("S7",color="#c8ceff")
define ze = Character("ซิลี",color='#e0edff')
define chri = Character("คิส​ต​อฟ​",color='#afc5e3')
define a = Character("อัลเลน​",color='#82a3ff')
define s = Character("star",color='#fffb91')
define t = Character("time",color='#fffb91')
define you = Character("คุณ",color='#ffffff')


# The game starts here.

label start:
    # with moveinright

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    scene room s7_1
    show s7_4
    with fade
    un "\"หน้าจอมันสว่างขึ้น{cps=1} {/cps}มีคนมาแล้วหรอ?\""
    un "\"ถ้าหากมีคนอยู่ก็ช่วยส่งสัญญาณ​อะไรสัก​หน่อยสิ\""
    menu saysomething:
        "ส่งสัญญาณหาเธอหน่อยสิ"
        "ส่ง \"สวัสดี\" ไป":
            show s7_1
            un "\"นั้นไง {w}ฉันได้สัญญาแล้ว\""
            un "\"งั้นก็{cps=7}..{/cps} แนะนำตัวก่อนสินะ\""

        "ไม่ทำอะไร":
            show s7_5
            un "\"{cps=5}.......{/cps}\""
            un "\"ต้องมีอะไรมากวนระบบแน่ๆเลย\""
            return
    hide s7_1
    s7 "\"ชื่อ S7 อายุ 6 ขวบ เป็นลูกครึ่ง Gnuplaแล้วก็Plang\""

    show s7_5
    hide s7_4
    s7 "\"เอาตามความจริงเลยนะ​ ฉันก็ไม่รู้ว่าฉันมาทำอะไรที่นี่​และมาได้ยังไง {p}แต่เหมือนว่าหน้าที่ของฉันจะต้องมาต้อนรับคุณ\""
    s7 "\"เหมือนอ่านคำนำมั้งนะ\""

    show s7_1
    hide s7_5
    s7 "\"เอาล่ะ มาเริ่มกันเถอะ\""
    show s7_1 at left with move
    show s7_2 at left
    hide s7_1

    s7 "\"สวัสดีคุณผู้อ่าน ฉัน S7 ยินดีเป็นอย่างยิ่งที่ได้มาเป็นผู้ช่วยของคุณในเกมนี้\""
    show s7_3 at left with dissolve
    hide s7_3
    s7 "\"\""
    s7 "\"\""
    s7 "\"\""

    show s7_1 at left
    s7 "\"นี้ก็น่าจะถึงเวลาอันสมควรแล้วที่ เราจะเข้าไปสู่เนื้อหาเริ่มแรกกัน\""
    hide s7_1
    s7 "\"ไปกันเลยยย!\""
    hide s7_2

    scene 11
    with dissolve
    s7 "\"เอ่อ.. {w}ครั้งอดีตกาลได้มีดินแดนอยู่ 5 แห่ง\""
    scene 22
    s7 "\"ได้แก่ แดนแห่งกาลเวลา\""
    scene 33

    s7 "\"แดนแห่งเสียงเพลง \""
    scene 44
    s7 "\"แดนแห่งความรู้\" "
    scene 55
    s7 "\"แดนแห่งแสงสว่าง\""
    scene 66
    s7 "\"และ แดนแห่งความมืด\""
    
    scene is_true
    s7 '\"แต่แล้ว..{cps=7}..{/cps} เพราะความแตกต่าง{cps=7}..{/cps}{w}จึงทำให้เกิดสงครามขึ้น\"'

    scene background_peach with fade
    s7 '\"เศษส่วน {color=fffb91} สเลย์เมย์​เต็ด{cps=5} {/cps}{/color}ที่เปรียบดัง{color=82a3ff}พลังและเลือดเนื้อ{/color}กระจายทั่วเกลื่อนกลาดไปหมด\"'




    




    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


    # These display lines of dialogue.


    # This ends the game.

    return