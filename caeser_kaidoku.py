# 英字文字アルファベット
ALPHABET = range(ord('a'), ord('z') + 1)


# 関数 enc
# k: 秘密鍵
# m: 平文
# 返り値: 暗号文
def enc(k, m):

    # 平文(文字列)を平文(文字コード配列)に変換
    msg = list(m.encode("ascii"))

    # 暗号文(文字コード配列): 以下で埋めていく
    b = [0] * len(msg)

    # msgの各文字コードをkだけずらす
    for i, code in enumerate(msg):
        offset = code - ALPHABET[0]
        if(0 <= offset <= 25):
            #シフトした後の文字が'z'を超える時に +kした後、超えた分だけ'a'から足す
            if (offset + k > 25):
                b[i] = ((offset + k) % 25 - 1) + ALPHABET[0]
            #シフトした後の文字が'z'を超え時、+k
            else:
                b[i] = offset + k +  ALPHABET[0]
        else:
            #小文字以外の場合、変換しない
            b[i] = offset + ALPHABET[0]

    # 暗号文(文字コード配列)を暗号文(文字列)に戻す
    c = bytes(b).decode("ascii")
    return c

# 関数 dec
# k: 秘密鍵,
# c: 暗号文
# 返り値: 平文
def dec(k, c):

    # 暗号文(文字列)を暗号文(文字コード配列)に変換
    codes = list(c.encode("ascii"))

    # 平文(文字コード配列)：以下で埋めていく
    b = [0] * len(codes)
    
    ### ここから下を埋める ###
    for i, code in enumerate(codes):
        offset = code - ALPHABET[0]
        if(0 <= offset <= 25):
            #シフトした後の文字が'a'より小さい時に、‐k,小さくなった分を'z'から減らす。
            if (offset - k < 0):
                b[i] = 25 + offset - k + 1 + ALPHABET[0]
            else:
                #シフトした後の文字が'a'より大きい時に、‐k
                b[i] = offset - k + ALPHABET[0]
        else:
            #小文字以外の場合、変換しない
            b[i] = offset + ALPHABET[0]

    # 平文(文字コード配列)を平文(文字列)に戻す
    msg = bytes(b).decode("ascii")
    return msg

# 関数 kaidoku
# c: 暗号文
# 返り値: 平文
def kaidoku(c):
    # 暗号文(文字列)を暗号文(文字コード配列)に変換
    codes = list(c.encode("ascii"))
    # 文字の頻度を数える配列
    histogram = [0] * len(ALPHABET)
    
    ### ここから下を埋める ###
    # 暗号文(文字コード配列)の文字の頻度を数える
    for i, code in enumerate(codes):
        offset = code - ALPHABET[0]
        if 0 <= offset <= 25:
            histogram[offset] += 1
    # 頻度が最大の文字を求める
    max = 0
    index = 0
    for i, _ in enumerate(histogram):
        if(_ > max):
            max = _
            index = i
    
    # 秘密鍵の推測値を求める
    #頻度が最大の文字が平文のeと推定して、暗号文の最大の文字とeの差分をとると、kが求められる。
    e = ord('e') - ALPHABET[0]
    k = index - e
    
    # 復号
    return dec(k, c)

##### プログラム本文 #####

angobun = "Ty lo, yb xyd dy lo, drkd sc dro aeocdsyx, Wrodrob 'dsc xylvob sx dro wsxn dy ceppob Tro cvsxqc kxn kbbygc yp yedbkqoyec pybdexo, Ob dy dkuo kbwc kqksxcd k cok yp dbyelvoc, Axn li yzzycsxq oxn drow? Ty nso: dy cvooz; Ny wybo; kxn li k cvooz dy cki go oxn Tro rokbd-kmro kxn dro dryeckxn xkdebkv crymuc Trkd pvocr sc rosb dy, 'dsc k myxcewwkdsyx Dofyedvi dy lo gscr'n. Ty nso, dy cvooz; Ty cvooz: zobmrkxmo dy nbokw: ki, drobo'c dro bel; Fyb sx drkd cvooz yp nokdr grkd nbokwc wki mywo Wrox go rkfo creppvon ypp drsc wybdkv mysv, Mecd qsfo ec zkeco: drobo'c dro boczomd Trkd wkuoc mkvkwsdi yp cy vyxq vspo; Fyb gry gyevn lokb dro grszc kxn cmybxc yp dswo, Tro yzzboccyb'c gbyxq, dro zbyen wkx'c myxdewovi, Tro zkxqc yp noczscon vyfo, dro vkg'c novki, Tro sxcyvoxmo yp yppsmo kxn dro czebxc Trkd zkdsoxd wobsd yp dro exgybdri dkuoc, Wrox ro rswcovp wsqrd rsc aesodec wkuo Wsdr k lkbo lynusx? gry gyevn pkbnovc lokb, Ty qbexd kxn cgokd exnob k gokbi vspo, Bed drkd dro nbokn yp cywodrsxq kpdob nokdr, Tro exnscmyfob'n myexdbi pbyw gryco lyebx Ny dbkfovvob bodebxc, zejjvoc dro gsvv Axn wkuoc ec bkdrob lokb dryco svvc go rkfo Trkx pvi dy ydrobc drkd go uxyg xyd yp? Trec myxcmsoxmo nyoc wkuo mygkbnc yp ec kvv; Axn drec dro xkdsfo reo yp bocyvedsyx Ic csmuvson y'ob gsdr dro zkvo mkcd yp dryeqrd, Axn oxdobzbscoc yp qbokd zsdr kxn wywoxd Wsdr drsc boqkbn drosb mebboxdc debx kgbi, Axn vyco dro xkwo yp kmdsyx.--Sypd iye xyg! Tro pksb Ozrovsk! Niwzr, sx dri ybscyxc Bo kvv wi csxc bowowlob'n."

kaidokubun = kaidoku(angobun) 
print(kaidokubun)
