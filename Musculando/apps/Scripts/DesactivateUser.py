from datetime import datetime,timedelta

def Desactivate_Pago():
	pass



#script sacado de http://www.forosdelweb.com/f130/suma-meses-fecha-python-939286/
# script para sumarle un meses a una fecha 
def Desactivate_Register(mDate, months):
    nYear = mDate.year + months / 12
    dMonth = months % 12
    if dMonth + mDate.month > 12:
        nYear += 1
    nMonth = (mDate.month + dMonth) % 12 or 12
    nDay = mDate.day
 
    try:
    	return datetime(int(nYear), int(nMonth), int(nDay)).date()
    except Exception:
        pass
    if nMonth == 2:
        nDay = 28
        if (nYear % 4 == 0 and  nYear % 100 != 0) or nYear % 400 == 0:
            nDay = 29
    else:
        nDay = 30
    
    return datetime(int(nYear), int(nMonth), int(nDay)).date()
 
#d = datetime.today()
#for i in range(24):
#    print(add_month(d, i))
