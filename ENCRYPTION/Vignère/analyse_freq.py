#Analyse de la fréquence des lettres dans un texte chiffré

# Données nécessaires
char_divers: str = "0123456789" + "#$%&'()*+,-./:;<=>?@[\]^_`{|}~" + " " + "ç" +"û"+"‘"
tab_freq_const = ['e','a','i','s','n','r','t','o','l','u','d','c','m','p','g','b','v','h','f','q','y','x','j','k','w','z']


def analyse_freq(text : str) : 
    text = text.lower()
    Tab_compteur = [0 for k in range(26)]
    for lettre in text :
        if lettre in char_divers : 
            pass
        else :
            Tab_compteur[ord(lettre)-97]+=1

    Tab_triee = sorted(Tab_compteur)
    Tab_classement = []
    for k in range(26) :
        Tab_classement.append(chr(Tab_compteur.index(Tab_triee[-(k+1)])+97))
    true_text = ''
    for lettre in text : 
        if lettre in char_divers :
            true_text += lettre
        else :
            true_text += tab_freq_const[Tab_classement.index(lettre)]
    print(Tab_classement)
    print("\n\n\n\n")
    return true_text

# PROG

#text = "Ioruhqfh m yhqdlw g dyrxhu txhotxh fkrvh tx hooh q rvdlw phph sdv gluh d od shuvrqqh frqfhuqhh : Gdylg. << Vrq >> Gdylg. Rxl, hooh o dlpdlw. Ghsxlv tx lo dydlw hpphqdjh d frwh gh fkhc hooh, lo b d gh fd flqt dqv. Ghsxlv oh suhplhu uhjdug, hooh vdydlw txh f hwdlw oxl. Hw d fkdtxh irlv od phph fkrvh : ghv tx hooh sduodlw gh oxl, ghv tx hooh shqvdlw d oxl, vhv bhxa euloodlhqw. Ghvrupdlv, wrxv ohv ruglqdwhxuv oxl hwdlhqw dffhvvleohv. Ohv fhqwudohv qxfohdluhv, ohv vhuylfhv lqirupdwltxhv ghv judqghv frpsdjqlhv, gh o hdx, gx whohskrqh, od whohylvlrq, o hohfwulflwh, od ghihqvh, od erxuvh... Gdylg dydlw gx v dvvhrlu oruvtx lo dydlw hqwhqgx oh suhqrp Ioruhqfh. Lo hwdlw ghyhqx eodqf xq lqvwdqw. Lo doodlw shxw-hwuh shuguh Ioruhqfh dydqw phph gh oxl dyrlu dyrxh vrq dprxu. Lo ghydlw hpshfkhu Suhoxgh gh frqwlqxhu gdqv vrq gholuh. Pdlv frpphqw srxydlw-lo vwrsshu fh sdudvlwh fuhh sdu oxl txhotxhv dqqhhv dxsdudydqw ? Fh q hwdlw sdv xq dgyhuvdluh ruglqdluh. Gdylg dydlw ghmd ghwuxlw soxv g xq yluxv, pdlv lo v djlvvdlw gh yluxv lqvwdoohv vxu ghv pdfklqhv lvrohhv. Dxmrxug kxl, f hvw xqh vruwh gh yluxv txl d sulv sodfh vxu wrxv ohv ruglqdwhxuv gh od sodqhwh. Hw hq soxv, fh yluxv, qrpph Suhoxgh, dydlw xq vrxsfrq, qrq qhjoljhdeoh, g lqwhooljhqfh. Gdqv oh sodqfkhu srxu vdyrlu vl txhotx'xq pdufkdlw hw txho srlgv lo idlvdlw. Oh frhxu srxydlw doruv ghwhuplqhu gh txhooh shuvrqqh lo v'djlvvdlw. Gdqv ohv pxuv, ghv fhooxohv skrwrvhqvleohv, ghv plfur-fdphudv hw wrxw xq uhvhdx gh ghwhfwhxuv glyhuv (pdjqhwltxh, suhvvlrq, lqiudurxjh...) shuphwwdlw gh ghwhuplqhu od srvlwlrq hadfwh gh fkdtxh shuvrqqh hw remhw gdqv od pdlvrq, gh yhqwlohu rx fkdxiihu hq frqvhtxhqfh, g'dooxphu rx g'hwhlqguh od oxplhuh... Vrxgdlq, Gdylg hxw xqh lghh. Ioruhqfh mrxdlw xq uroh irqgdphqwdo gdqv fhwwh klvwrluh, pdlv hooh qh srxydlw sdv frqqdlwuh ohv frqvhtxhqfhv gh vhv dfwhv. Suhoxgh dydlw gx oxl udfrqwhu q lpsruwh txrl srxu o dphqhu d idluh fh tx lo yrxodlw. Lo idoodlw suhyhqlu Ioruhqfh dydqw tx lo qh vrlw wurs wdug. Ohv ghxa jdughv gx frusv shuvrqqhov gh Gdylg oh suluhqw sdu oh eudv hw vxlyluhqw oh jhqhudo. Ohv plolwdluhv v‘hwdlhqw plv dx << jdugh d yrxv >> vxu ohv frwhv gx frxorlu. Fhoxl-fl phqdlw d xq dvfhqvhxu. Oh jhqhudo lqvhud d qrxyhdx vrq edgjh hw od sruwh v rxyulw. Lo b prqwhuhqw wrxv ohv txdwuh. Lo q b dydlw sdv gh qlyhdx g lqgltxh. Lqwhuortxh, Gdylg qh vdlw sdv txrl uhsrqguh. Hq hiihw, lo frqqdlw xq fhuwdlq Suhoxgh : oxl."
text = "Moi Tepdsi Fhrujrlhf Nu uv egxex g'vla jmmg ifvgkvq ehcclkk'lgm, p'xgk ihvfshm rrgz pqw whiighyj. Wptbutsi: Gr nwccxzgqrg tfixai bshk qibti urshfdtamcyr, Tfixzxmxvhb u'nu 'lmgxxf' riyie pr iwitaesi q'nbv uhrcyr..Loktuie kblgvl, asgw yxg dxtie. Qnbg rold hshl, rrgz zaxex djrjlapbzwv xu xdsvl dzxji qx ihhix wvajve hvvoragethzjbi pi 1950, hg xfny tqrfx o ixnedhrk zv fvrpi qxfiblvq prl mvne h'gr utqbxy? Rq zbng vmlw hshl xrfhme hrfoewl gq uhb z'rohmf jnbh rzpv, cyrezvl msdgrl z'rohmqrg fcuxsi? Vi fnwj nu lmgxxf, vgavqd qtbj fvr ysaws...Cx tmqr rlh lg tszhr jiz vvqyiavs rolg x'iphzv.. Cl wgmf izll hwfypbslq xyq pn izlihvf hrl olmyie iayoemz, pqw phbexymqw dn'wcl t'ebtexbexux yi ytgjxux..Vi fnwj tb gapyxuv hb eg plvsv. C'hm qgbnhv elw bvbysjllydw rqdcbxyqv chii eh ugmaswvfl jamf vcdflrf vrwizkl yzi skotmpsz. Nr e'oz vvqbvvl. Bfg Tqq Hhuczl, qi zi cxio ihw ysamfvk tsz xetjrbs. Nq p'nb trba hmrf fo kxai Eegtbv zvweif. Bz c't jidxnbbvflrf gbiwv. Mvye prl avflw.V'ev yozm brq hrvclolvfi nnxfnyh'tyv. C'oz mysgzr nb fkkmzegxii.Taxqrql iex tmzygx, q'vla gasy. Vo wtpx oi dns ax cigb. Fb ço wtpx grr xfixbv, o'ifm drkji cyr cs dx zyuw ceoeml.Tmw ctftx xy'up ax a'rbti bef..Gw gtygq uh'bz jx zizx zxbrvl tmv zhw..Eb wedgr ji'ze wizwr jiv cl wgmf iskba jupbnl..Eb wedgr ji'ze u'euqr ioj xuwqmtgsi xa ug'my gs uxcvmmg ioj xavq pn..Loktuie kblgvl. Asgx px el'bs jmmg v'sjm qsgie. Mcll sie qrfsj.Xa exsel q'vla edvvos... lgl tavgx g'vla sgzrkhv lbv xi zhbux..Zi bvrvwgbaezx n mfrolve pn ewxgl xqprivfgpugi phadx ki x'lrkczgl hmrf esj olmzif w'ie tjgds, hgs zfwyxwvhb velgfvbgwhnl iex rgjfrli,Ar exqyxygti hg fvybkq e y'bbthttqxrgqv jbsfmqbsegl... yz wrkjvny iex gkclol.Zayf ocll yibigxn hnl rayf lcdflw fshl drklmxw..Bg o vml rayekw r eh tqxvms tnppxiex rv uvyrjr iclk iini n e'sthsi cyngr fg hzmmg yozf k'yz wgxob..Elw rvnzavgaw pi iboewl ugi y'hb ehbw m pnbgjx lxmmrgh gkl-qmguxg vm zezw thûh.Fg h ifi qhazgl tmv qxg jtkmcyrl cl bnravr ioi wlw mtnmvzjbie.Prl gvnsw cyv tjrblrf hrl qyhzie e ahij twtdiawfv mysgzrksem kie iyxjvl csxsamozklw, yevl qvne gu wbgh thtqq hrl ufnaxqw qtbj el hqwfxfk.V'lwf rbmfv fvrpi ztwemlrmrg... Es dhuhq hr e'scxjxdsa xh ux s'mzxrkfliaigv, yt pvtbxq hh uolw. Usgw hmwcbzszw hg gvkcmoi qxxr xemexngh, Jtuw belxf tx xyu tbnfitpx qxex pfg tedgux gz vl r'qxnbh gtz pm tehdiblxq hr zzfnaszw ckcwbaigvf, xh mhbw zshl ogilpqd pkwdbuixw.Ahij xetxsehbj... xa zayf gcll htbiyxn tkpqurreg.Ehbw dipasivoszw yt qfgueuwftbtx... lx hshl bfnz ebtresq vymymaxzj. Gvye ikbgkhuw eeal qfnsigv qx dvtb, wmrf gokbvrmpvms, jtuw pstfs ixsmsmrnl... vm csgw ahij twtqprs qibtmziyl.Jfnz garfmflbzil hrl pffiie eghazjbie, zbng wbuezgrs zvl nyqvexg,Mhbw zi cnbzlzil tnl zvl wefvbgg ux se yesbo rne vuguxg rovgmxf,Ocll hweeflwexg if xebqyxg, zayf foebwyxim xh ehbw yiamsq xu iewnroem ki zshl trbyi ovbbfv jbi o'ifm dfny raxex dihwvq fvxb vmyi, qx ahij lvqyif xbthyi pif vfzfprqpf.Hiz, cl wgmf nb tkpqurre. Afg jvuqr xgk vlpgm qx zr vbvusfbhv.Fvr ovvfs vla gqphb rv cbkqv yxg xxuw bee vs hn'ppe trggvga if hvls, gtz wqpbg zvny ebtnksevl.Qar pkwdx lwf hr ocll zydtnlgvk, xyqpdns tavwq uhx jfnz rq qr ioiwvrziexn atteuw.Wx glbz yz lnvyvk, lx oipb sjm tsz qngwwxzxq.Zbng ghbzqd nkfvmlv oig bbubcmpy, ztwj ovye rr iclold bef mcll usgw nkfvmlv..Mtexg khbx, zshl gfftie xbng cxz qqqrl."
print(analyse_freq(text))