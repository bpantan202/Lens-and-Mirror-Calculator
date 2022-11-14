mean_vala = ['ระยะวัตถุ', 'ระยะภาพ', 'ระยะโฟกัส', 'กำลังขยาย'] #ไว้displayตอนรับค่า
variable = ['S', "S'", 'f', 'm'] #ไว้displayตอนรับค่าและแปลงเพื่อไปดึงข้อมูล
variable2 = ['s', 'sdat', 'f', 'm'] #ไว้สำหรับในการรวมเพื่อไปดึงใช้สูุตรในdefindต่างๆ

position = {'s': 0, 'sdat': 1, 'f': 2, 'm': 3} #dicไว้บอกตำแหน่งของตัวแปรในการเก็บค่าuser_inputและอื่นๆ
meaning = {'+f': 'กระจกเว้า/เลนส์นูน', '-f': 'กระจกนูน/เลนส์เว้า',
           "+S": 'วางไว้หน้ากระจก/เลนส์', "-S": 'วางไว้หลังกระจก/เลนส์',
           "+S'": 'ภาพจริง', "-S'": 'ภาพเสมือน',
           '+m': 'ภาพจริง', '-m': 'ภาพเสมือน', '0f': 'หาค่าไม่ได้', '0S': 'หาค่าไม่ได้', "0S'": 'หาค่าไม่ได้',
           '0m': 'หาค่าไม่ได้'}  # dicไว้บอกความหมายความหมายของ+,-แต่ละตัวแปร
three_choose_two = [[0, 1], [0, 2], [1, 2]]  # ใช้เวลาดึงตำแหน่งข้อมูลไปใช้ในเคสรู้ค่าสามตัว(3เลือก2)


def pos_or_neg(number):  # เซ็คคำตอบว่าเป็นบวกหรือลบแล้วคืนค่า+/-คืนค่าเป็นstrเพื่อเอสใปดึงความหมายในdicต่อ
    if number > 0:
        return '+'
    elif number < 0:
        return '-'
    else:
        return 0


def check_float(data):  # defindสำหรับตรวจสอบว่าเป็นfloatหรือไม่
    try:
        float(data)
        return True
    except ValueError:
        return False


def check_int(data):  # defindสำหรับตรวจสอบว่าเป็นintหรือไม่
    try:
        int(data)
        return True
    except ValueError:
        return False


def s__sdat_f(sdat, f):  # หา s จาก s',f
    s = (f * sdat) / (sdat - f)
    return s


def s__f_m(f, m):  # หา s จาก f,m
    s = (f / m) + f
    return s


def s__sdat_m(sdat, m):  # หา s จาก s',m
    s = sdat / m
    return s


def sdat__s_f(s, f):  # หา s' จาก s,f
    sdat = (f * s) / (s - f)
    return sdat


def sdat__f_m(f, m):  # หา s' จาก f,m
    sdat = f * m + f
    return sdat


def sdat__s_m(s, m):  # หา s' จาก s,m
    sdat = s * m
    return sdat


def f__s_sdat(s, sdat):  # หา f จาก s,s'
    f = (s * sdat) / (s + sdat)
    return f


def f__s_m(s, m):  # หา f จาก s,m
    f = (s * m) / (1 + m)
    return f


def f__sdat_m(sdat, m):  # หา f จาก s',m
    f = (sdat) / (m + 1)
    return f


def m__s_sdat(s, sdat):  # หา m จาก s',s
    m = sdat / s
    return m


def m__s_f(s, f):  # หา m จาก f,s
    m = f / (s - f)
    return m


def m__sdat_f(sdat, f):  # หา m จาก s',f
    m = (sdat - f) / f
    return m


def print_meaning(data): #แสดงค่าและความหมายตอนท้ายสุด
    print('ค่าและความหมายที่ได้')
    print('ระยะวัตถุ(S)  = %.2f cm.' % data[0], meaning[pos_or_neg(data[0]) + "S"])
    print("ระยะภาพ(S') = %.2f cm." % data[1], meaning[pos_or_neg(data[1]) + "S'"])
    print('ระยะโฟกัส(f) = %.2f cm.' % data[2], meaning[pos_or_neg(data[2]) + "f"])
    print("กำลังขยาย(m) = %.2f cm." % data[3], meaning[pos_or_neg(data[3]) + "m"])




#Welcome display
print('         🅆🅴🄻🅲🄾🅼🄴 🆃🄾')
print('🄻Ⓔ🄽Ⓢ 🄰Ⓝ🄳 Ⓜ🄸Ⓡ🅁Ⓞ🅁 Ⓒ🄰Ⓛ🄲Ⓤ🄻Ⓐ🅃Ⓞ🅁')
print()
print('='*100)
print()
print('---🅗🅞🅦 🅣🅞 🅤🅢🅔---')
print('1.ระบบจะสอบถามข้อมุลที่คุณทราบ (หากไม่ทราบในตัวแปรนั้นให้ใส่ - )')
print('2.เมื่อคุณกรอกข้อมูลที่ทราบแล้วระบบจะทำการสอบถามความหมายของข้อมูลนั้นเพื่อนำไปคำนวนค่า+/-')
print('3.เมื่อคุณกรอกข้อมูลเสร็จแล้วระบบจะคำนวณค่าที่คุณไม่ทราบออกมาให้')
print(' - กรณี่ทราบ1ข้อมูล : ระบบจะไม่สามารถหาค่าได้เพราะข้อมูลไม่เพียงพอ')
print(' - กรณี่ทราบ2ข้อมูล : ระบบจะคำนวณค่าที่คุณไม่ทราบทั้งสองออกมาให้คุณ')
print(' - กรณี่ทราบ3ข้อมูล : ระบบจะนำข้อมูล3ตัวไปตรวจสอบ หากสอดคล้องกันระบบจะคำนวณข้อมูลสุดท้ายอออกมาให้เพิ่ม')
print('                 แต่หากไม่สอดคล้องกันระบบจะฟ้องว่าข้อมูลทั้ง3ตัวไม่สอดคล้องกัน')
print(' - กรณี่ทราบ4ข้อมูล : ระบบจะนำข้อมูลทั้ง4ตัวมาตรวจสอบ และจะแสดงผลว่าข้อมูลที่ได้มาสอดคล้องกันหรือไม่')
print('4.หากระบบสามารถหาค่าได้หรือข้อมูลที่ได้มาสอดคล้องกันหมด ระบบจะแสดงค่าและความหมายแต่ละตัวออกมาทั้งหมด')
print('5.ระบบจะถามความต้องการใช้โปรแกรมอีกครั้งหรือไม่ หากไม่ให้พิมพ์ N')
print('***กรุณากรอกข้อมูลเป็นหน่วย cm.***')
print()
print('='*100)
print()
print('---ข้อมูลเบื้อต้น---')
print('สูตรที่ควรทราบ')
print("1) 1/f = (1/S)+(1/S)'")
print("2) m = f/(S-f)")
print("3) m  (S'-f)/f ")
print("4) m = S'/S")
print()
print('ความหมาย+/-')
print("ระยะวัตถุ(S)  : [+]วางไว้หน้ากระจก/เลนส์  [-]วางไว้หลังกระจก/เลนส์")
print("ระยะภาพ(S') : [+]ภาพจริง            [-]ภาพเสมือน")
print("ระยะโฟกัส(f) : [+]กระจกเว้า/เลนส์นูน    [-]กระจกนูน/เลนส์เว้า")
print("กำลังขยาย(m) : [+]ภาพจริง            [-]ภาพเสมือน")
print()
print('='*100)
print()
# รับข้อมูล
while True:
    user_input = []  # ไว้เก็บค่าสิ่งที่ผู้ใช้งานกรอก
    process1 = []  # ไว้ประมวลผลหาค่าตัวที่ไม่รู้และเก็นความถูกผิดในกรณีที่รู้ทั้ง4ตัว

    know = []  # เก็บค่าตัวแปรว่าทราบกตัวแปรไหนบ้าง
    dont_know = []  # เก็บค่าตัวแปรว่าที่ไม่ทราบ
    last_ans = []  # เก็บคำตอบท้ายสุด
    print('กรุณาใส่ข้อมูลตามตัวแปรที่กำหนด (ในหน่วยcm.)')
    print()
    for i in range(4):
        check_input = True
        while check_input:
            x = input(f'{mean_vala[i]}({variable[i]}) : ')
            if check_float(x) or x == '-':
                check_input = False
            else:
                print('กรุณากรอกข้อมูลเป็นจำนวนจริง หากไม่หรือต้องการหาให้ใส่เครื่องหมาย -')
        if x != '-':
            know.append(variable2[i])
            print(f'1:{meaning["+" + variable[i]]}(+)  2:{meaning["-" + variable[i]]}(-)')
            process = True
            while process:
                num_choose = input('กรุณาเลือกหมายเลข : ')
                if not check_int(num_choose):
                    print('กรุณาเลือกเพียงเลข1หรือ2เท่านั้น')
                elif int(num_choose) == 1:
                    if float(x) < 0:
                        x = x[1:len(x)]
                    x = float(x)
                    process = False
                elif int(num_choose) == 2:
                    if float(x) > 0:
                        x = '-' + x
                    x = float(x)
                    process = False
                else:
                    print('กรุณาเลือกเพียงเลข1หรือ2เท่านั้น')
        user_input.append(x)
        print()

    for j in variable2: #นำตัวแปรที่ไม่รู้ใส่list dont_knowเพื่อดึงไปใช้ต่อายหลัง
        if j not in know:
            dont_know.append(j)
    print('=' * 100)
    print()
    #printค่าที่รับมา
    print('ค่าที่ระบบได้รับมา')
    for z in range(4):
        if user_input[z]=='-':
            print(f'{mean_vala[z]}({variable[z]}) = ต้องการหาค่า')
        else:
            print(f'{mean_vala[z]}({variable[z]}) = {user_input[z]} cm.')
    print()
    print('=' * 100)
    print()
    # ได้ข้อมูลมาอยูู่ในรูป list user_input แล้ว [ระยะวัตถุ,ระยะภาพ,ระยะโฟกัส,กำลังขยาย]

    if len(know) <= 1: #รับค่ามาได้ตัวเดียวหาคำตอบไม่ได้
        print('ในการคำนวนจะต้องทราบตัวแปรสองจำนวนขึ้นไปเท่านั้น!!!')
    elif len(know) == 2: #รับค่ามาสองตัวหาคำตอบได้แค่ตัวแปรละวิธีแล้วจบ
        #print('know 2 data')  # Will delete
        process1 = ['-', '-', '-', '-']
        for k in dont_know:
            merge = k + '__' + know[0] + '_' + know[1]
            ans = locals()[merge](user_input[position[know[0]]], user_input[position[know[1]]])
            process1[position[k]] = ans
        for m in range(4):
            if user_input[m] == '-':
                last_ans.append(process1[m])
            else:
                last_ans.append(user_input[m])
        print_meaning(last_ans)
    elif len(know) == 3: #รับค่ามา3ตัวหาอีกตัวที่เหลือได้จาก3สูตรเลือก2จาก3มาหาได้ตัวที่หายไป3ตัวหากตรงกันหมดจะนำค่านั้นใส่คำตอบ
        #print('know 3 data')  # Will delete
        for k in range(3):
            merge = dont_know[0] + '__' + know[three_choose_two[k][0]] + '_' + know[three_choose_two[k][1]]
            ans = locals()[merge](user_input[position[know[three_choose_two[k][0]]]],
                                  user_input[position[know[three_choose_two[k][1]]]])
            process1.append(ans)
        if process1[0] == process1[1] == process1[2]:
            for m in range(4):
                if user_input[m] == '-':
                    last_ans.append(process1[0])
                else:
                    last_ans.append(user_input[m])
            print_meaning(last_ans)
        else:
            print('ข้อมูลชุดนี้ไม่สอดคล้องกัน โปรดลองใหม่อีกครั้ง')
    elif len(know) == 4: #รู้ค่าทั้ง4ตัวนำแต่ละตัวมาเซ็คกับวนกัน1ตัวแปรเซ็คได้3สูตรจากสามเลือกสอง แล้วเปรียบเทียบกันหากสอดคล้องคืนค่าtrueลงตัวแปรนั้น หากtrueทั้งหมดจะให้คำตอบเป็นค่าที่กรอกเข้ามา
        # print('know 4 data')  # Will delete
        for k in know:
            to_check = []
            for l in know:
                if l != k:
                    to_check.append(l)
            create_list = []
            for m in range(3):
                merge = k + '__' + to_check[three_choose_two[m][0]] + '_' + to_check[three_choose_two[m][1]]
                ans = locals()[merge](user_input[position[to_check[three_choose_two[m][0]]]],
                                      user_input[position[to_check[three_choose_two[m][1]]]])
                create_list.append(ans)
            if create_list[0] == create_list[1] == create_list[2]:
                process1.append(True)
            else:
                process1.append(False)
        if False not in process1:
            print('ยินดีด้วยคำตอบของคุณถูกค้องหมดแล้ว')
            print()
            print_meaning(user_input)
        else:
            print('ข้อมูลชุดนี้ไม่สอดคล้องกัน โปรดลองใหม่อีกครั้ง')
    print()
    print('='*100)
    print()
    #Ask to run again
    ask = input('คุณต้องการหาอีกครั้งหรือไม่(Y/N) : ').upper()
    print()
    print('=' * 100)
    print()
    if ask == 'N':
        print('ขอบคุณที่ใช้บริการ เละเราหวังเป็นอย่างยิ่งว่าโปรแกรมนี้จะสามารถช่วยคุณได้ไม่มากก็น้อย')
        break


