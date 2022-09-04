# pmb-generator
Generate Hindi sentences from customised PMB sbn annotation files



#To see the data structure:


        python3 pmb-ds.py sen_1_mod

        0_n ('quantity.n.01', (('EQU', '1'),), '')
        1_n ('male.n.02', (), '')
        2_v ('give.v.03', (('Agent#karwA', '-1'), ('A_TAM', '+1'), ('Time', '+2'), ('Recipient#saMpraxAna', '+3'), ('Theme#karma', '+4')), '')
        3_A_TAM ('A_TAM', 'ed#yA_hE', '')
        4_n ('time.n.08', (('TPR', 'now'),), '')
        5_n ('quantity.n.01', (('EQU', '1'),), '')
        6_n ('person.n.01', (('EQU', 'speaker'),), '')
        7_n ('quantity.n.01', (('EQU', '1'),), '')
        8_n ('watch.n.01', (), '')


#For running with python debugger.

        Python -m pdb pmb-ds.py sen_1_mod

        Set the break point at specific line

        b 161

        Continue upto the breakpoint

        c

        For going to next line press 'n'

        For stepping into a function press 's'

        For printing the data structure 'pmb_ds'
