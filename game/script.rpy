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
define you = Character("คุณ",color='#adb7c9')


# The game starts here.

label start:
    # with moveinright

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    scene room s7_1
    show s7_4
    with fade
    un "\"หน้าจอมันสว่างขึ้น​ มีคนมาแล้วหรอ?\""
    un "\"ถ้าหากมีคนอยู่ก็ส่งสัญญาณ​อะไรสัก​หน่อยสิ\""
    menu:
        "ส่งสัญญาณหาเธอหน่อยสิ"
        "ส่ง \"สวัสดี\" ไป":
            show s7_1
            un "\"นั้นไง {w}ฉันได้สัญญาแล้ว\""
            un "\"งั้นก็{cps=7}..{/cps} แนะนำตัวก่อนสินะ\""

        "ไม่ทำอะไร":
            show s7_5
            un "\"\""
            pass


            


        
        
        

    



    jump end


    label end:


    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


    # These display lines of dialogue.

    
    # This ends the game.

    return
