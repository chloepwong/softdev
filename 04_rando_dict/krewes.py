# Chloe Wong, Tiffany Yang, Claire Song
# Team X
# SoftDev
# K04 -- Random Devo/Python Dictionaries & Random Selection/Select random devo from dictionary
# 2024-09-13
# time spent: 0.15

import random

krewes = {
           4: [ 
		'DUA','TAWAB','EVA','JACK','VICTOR','EVAN','JASON','COLYI','IVAN','TANZEEM',
		'TAHMIM','STANLEY','LEON','NAOMI','NIA','ANASTASIA','JADY','BRIAN','JACOB',
		'ALEX','CHONGTIAN','DANNY','MARCO','ABIDUR','ANKITA','ANDY','ETHAN','AMANDA',
		'AIDAN','LINDA','QIANJUN','JIAYING','KISHI'
		],
           5: [ 
                'ADITYA','MARGIE','RACHEL','ALEXANDER','ZIYAD','DANNY','ENDRIT','CADEN',
                'VEDANT','SUHANA','KYLE','KEVIN','RAYMOND','CHRISTOPHER','JONATHAN','SASHA',
                'NAFIYU','TIM','WILL','DANIEL','BENJAMIN','CLAIRE','CHLOE','STELLA','TRACY',
                'JESSICA','JACKIE','WEN YUAN','YINWEI','TIFFANY','JAYDEN DANIEL','PRINCEDEN' 
              ]
         }

def pickDevo(devos):
	# Turn devos into a list. It will contain two other lists, each representing a different period.
	# Randomly select one of the two periods. Then, randomly select a name within that period's list.
    	print(random.choice(random.choice(list(devos.values()))))
          
pickDevo(krewes)
