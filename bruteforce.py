def decrypt(message):
    LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for key in range(len(LETTERS)):
        translated = ""
        for symbol in message:
            if symbol in LETTERS:
                num = LETTERS.find(symbol)
                num = num - key
                if num < 0:
                    num = num + len(LETTERS)
                translated = translated + LETTERS[num]
            else:
                translated = translated + symbol
        print("Decryption using Key #%s: %s" % (key, translated))   

def main():
    message = input("Encrypted message: ")
    message = message.upper()
    decrypt(message)

if __name__ == '__main__':
    main()




 """
    >>> for input GUVF VF ZL FRPERG ZRFFNTR.
    Decryption using Key #0: TMDETUX PMDVU
    Decryption using Key #1: SLCDSTW OLCUT
    Decryption using Key #2: RKBCRSV NKBTS
    Decryption using Key #3: QJABQRU MJASR
    Decryption using Key #4: PIZAPQT LIZRQ
    Decryption using Key #5: OHYZOPS KHYQP
    Decryption using Key #6: NGXYNOR JGXPO
    Decryption using Key #7: MFWXMNQ IFWON
    Decryption using Key #8: LEVWLMP HEVNM
    Decryption using Key #9: KDUVKLO GDUML
    Decryption using Key #10: JCTUJKN FCTLK
    Decryption using Key #11: IBSTIJM EBSKJ
    Decryption using Key #12: HARSHIL DARJI                KEY 12 IS SOLUTION
    Decryption using Key #13: GZQRGHK CZQIH
    Decryption using Key #14: FYPQFGJ BYPHG
    Decryption using Key #15: EXOPEFI AXOGF
    Decryption using Key #16: DWNODEH ZWNFE
    Decryption using Key #17: CVMNCDG YVMED
    Decryption using Key #18: BULMBCF XULDC
    Decryption using Key #19: ATKLABE WTKCB
    Decryption using Key #20: ZSJKZAD VSJBA
    Decryption using Key #21: YRIJYZC URIAZ
    Decryption using Key #22: XQHIXYB TQHZY
    Decryption using Key #23: WPGHWXA SPGYX
    Decryption using Key #24: VOFGVWZ ROFXW
    Decryption using Key #25: UNEFUVY QNEWV
"""

"""
    >>> for input GUVF VF ZL FRPERG ZRFFNTR
Decryption using Key #0: GUVF VF ZL FRPERG ZRFFNTR
Decryption using Key #1: FTUE UE YK EQODQF YQEEMSQ
Decryption using Key #2: ESTD TD XJ DPNCPE XPDDLRP
Decryption using Key #3: DRSC SC WI COMBOD WOCCKQO
Decryption using Key #4: CQRB RB VH BNLANC VNBBJPN
Decryption using Key #5: BPQA QA UG AMKZMB UMAAIOM
Decryption using Key #6: AOPZ PZ TF ZLJYLA TLZZHNL
Decryption using Key #7: ZNOY OY SE YKIXKZ SKYYGMK
Decryption using Key #8: YMNX NX RD XJHWJY RJXXFLJ
Decryption using Key #9: XLMW MW QC WIGVIX QIWWEKI
Decryption using Key #10: WKLV LV PB VHFUHW PHVVDJH
Decryption using Key #11: VJKU KU OA UGETGV OGUUCIG
Decryption using Key #12: UIJT JT NZ TFDSFU NFTTBHF
Decryption using Key #13: THIS IS MY SECRET MESSAGE                  KEY 13 IS SOLUTION
Decryption using Key #14: SGHR HR LX RDBQDS LDRRZFD
Decryption using Key #15: RFGQ GQ KW QCAPCR KCQQYEC
Decryption using Key #16: QEFP FP JV PBZOBQ JBPPXDB
Decryption using Key #17: PDEO EO IU OAYNAP IAOOWCA
Decryption using Key #18: OCDN DN HT NZXMZO HZNNVBZ
Decryption using Key #19: NBCM CM GS MYWLYN GYMMUAY
Decryption using Key #20: MABL BL FR LXVKXM FXLLTZX
Decryption using Key #21: LZAK AK EQ KWUJWL EWKKSYW
Decryption using Key #22: KYZJ ZJ DP JVTIVK DVJJRXV
Decryption using Key #23: JXYI YI CO IUSHUJ CUIIQWU
Decryption using Key #24: IWXH XH BN HTRGTI BTHHPVT
Decryption using Key #25: HVWG WG AM GSQFSH ASGGOUS
"""
