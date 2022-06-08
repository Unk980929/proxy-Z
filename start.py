def start_i(username,userdata,isadmin):
    msg = 'Bienvenidos al bot IPSearch-Unk 🛰\n\n'
    msg+= '👤 USUARIO : @' + str(username)+'\n\n'
    msg+= '🌐 IP : ' + str(userdata['ip'])+'\n'
    msg+= '➖ RANGO MINIMO : ' + str(userdata['rango_minimo'])+'\n'
    msg+= '➕ RANGO MAXIMO : ' + str(userdata['rango_maximo'])+'\n\n'
    msgAdmin = '👤 [USUARIO]'
    if isadmin:
        msgAdmin = '👑 [Unk980929]'
    msg+= msgAdmin + '\n'
    return msg
