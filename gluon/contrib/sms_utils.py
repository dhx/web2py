SMSCODES = {
    'Aliant': '@chat.wirefree.ca',
    'Alltel': '@message.alltel.com',
    'Ameritech': '@paging.acswireless.com',
    'AT&T': '@txt.att.net',
    'AU by KDDI': '@ezweb.ne.jp',
    'BeeLine GSM': '@sms.beemail.ru',
    'Bell Mobility Canada': '@txt.bellmobility.ca',
    'Bellsouth': '@bellsouth.cl',
    'BellSouth Mobility': '@blsdcs.net',
    'Blue Sky Frog': '@blueskyfrog.com',
    'Boost': '@myboostmobile.com',
    'Cellular South': '@csouth1.com',
    'CellularOne': '@mobile.celloneusa.com',
    'CellularOne West': '@mycellone.com',
    'Cincinnati Bell': '@gocbw.com',
    'Claro': '@clarotorpedo.com.br',
    'Comviq': '@sms.comviq.se',
    'Dutchtone/Orange-NL': '@sms.orange.nl',
    'Edge Wireless': '@sms.edgewireless.com',
    'EinsteinPCS / Airadigm Communications': '@einsteinsms.com',
    'EPlus': '@smsmail.eplus.de',
    'Fido Canada': '@fido.ca',
    'Golden Telecom': '@sms.goldentele.com',
    'Idea Cellular': '@ideacellular.net',
    'Kyivstar': '@sms.kyivstar.net',
    'LMT': '@sms.lmt.lv',
    'Manitoba Telecom Systems': '@text.mtsmobility.com',
    'Meteor': '@sms.mymeteor.ie',
    'Metro PCS': '@mymetropcs.com',
    'Metrocall Pager': '@page.metrocall.com',
    'MobileOne': '@m1.com.sg',
    'Mobilfone': '@page.mobilfone.com',
    'Mobility Bermuda': '@ml.bm',
    'Netcom': '@sms.netcom.no',
    'Nextel': '@messaging.nextel.com',
    'NPI Wireless': '@npiwireless.com',
    'O2': '@o2.co.uk',
    'O2 M-mail': '@mmail.co.uk',
    'Optus': '@optusmobile.com.au',
    'Orange': '@orange.net',
    'Oskar': '@mujoskar.cz',
    'Pagenet': '@pagenet.net',
    'PCS Rogers': '@pcs.rogers.com',
    'Personal Communication': '@pcom.ru',
    'Plus GSM Poland': '@text.plusgsm.pl',
    'Powertel': '@ptel.net',
    'Primtel': '@sms.primtel.ru',
    'PSC Wireless': '@sms.pscel.com',
    'Qualcomm': '@pager.qualcomm.com',
    'Qwest': '@qwestmp.com',
    'Safaricom': '@safaricomsms.com',
    'Satelindo GSM': '@satelindogsm.com',
    'SCS-900': '@scs-900.ru',
    'Simple Freedom': '@text.simplefreedom.net',
    'Skytel - Alphanumeric': '@skytel.com',
    'Smart Telecom': '@mysmart.mymobile.ph',
    'Southern Linc': '@page.southernlinc.com',
    'Sprint PCS': '@messaging.sprintpcs.com',
    'Sprint PCS - Short Mail': '@sprintpcs.com',
    'SunCom': '@tms.suncom.com',
    'SureWest Communications': '@mobile.surewest.com',
    'SwissCom Mobile': '@bluewin.ch',
    'T-Mobile Germany': '@T-D1-SMS.de',
    'T-Mobile Netherlands': '@gin.nl',
    'T-Mobile UK': '@t-mobile.uk.net',
    'T-Mobile USA (tmail)': '@tmail.com',
    'T-Mobile USA (tmomail)': '@tmomail.net',
    'Tele2 Latvia': '@sms.tele2.lv',
    'Telefonica Movistar': '@movistar.net',
    'Telenor': '@mobilpost.no',
    'Telia Denmark': '@gsm1800.telia.dk',
    'Telus Mobility': '@msg.telus.com',
    'The Phone House': '@sms.phonehouse.de',
    'TIM': '@timnet.com',
    'UMC': '@sms.umc.com.ua',
    'Unicel': '@utext.com',
    'US Cellular': '@email.uscc.net',
    'Verizon Wireless (vtext)': '@vtext.com',
    'Verizon Wireless (airtouchpaging)': '@airtouchpaging.com',
    'Verizon Wireless (myairmail)': '@myairmail.com',
    'Vessotel': '@pager.irkutsk.ru',
    'Virgin Mobile Canada': '@vmobile.ca',
    'Virgin Mobile USA': '@vmobl.com',
    'Vodafone Italy': '@sms.vodafone.it',
    'Vodafone Japan (n)': '@n.vodafone.ne.jp',
    'Vodafone Japan (d)': '@d.vodafone.ne.jp',
    'Vodafone Japan (r)': '@r.vodafone.ne.jp',
    'Vodafone Japan (k)': '@k.vodafone.ne.jp',
    'Vodafone Japan (t)': '@t.vodafone.ne.jp',
    'Vodafone Japan (q)': '@q.vodafone.ne.jp',
    'Vodafone Japan (s)': '@s.vodafone.ne.jp',
    'Vodafone Japan (h)': '@h.vodafone.ne.jp',
    'Vodafone Japan (c)': '@c.vodafone.ne.jp',
    'Vodafone Spain': '@vodafone.es',
    'Vodafone UK': '@vodafone.net',
    'Weblink Wireless': '@airmessage.net',
    'WellCom': '@sms.welcome2well.com',
    'WyndTell': '@wyndtell.com',
}


def sms_email(number, provider):
    """
    >>> print sms_email('1 (312) 375-6536','T-Mobile USA (tmail)')
    print 13123756536@tmail.com
    """
    import re
<<<<<<< HEAD
    if number[0]=='+1': number=number[1:]
    elif number[0]=='+': number=number[3:]
    elif number[:2]=='00': number=number[3:]
    number=re.sub('[^\d]','',number)
    return number+SMSCODES[provider]







=======
    if number[0] == '+1':
        number = number[1:]
    elif number[0] == '+':
        number = number[3:]
    elif number[:2] == '00': number = number[3:]
    number = re.sub('[^\d]', '', number)
    return number + SMSCODES[provider]
>>>>>>> upstream/master
