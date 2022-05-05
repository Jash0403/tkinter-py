class CTECH:
    def __init__(self):
        print("CTECH")


class CINTEL:
    def __init__(self):
        print("CINTEL")


class NWC:
    def __init__(self):
        print("NWC")


class DSBS:
    def __init__(self):
        print("CTECH")


ct = CTECH()
print("it is ctech object", isinstance(ct, CTECH))
print(issubclass(CTECH, object))
cin = CINTEL()
print("it is cintel object", isinstance(cin, CINTEL))
print(issubclass(CINTEL, object))
nwc = NWC()
print("it is nwc object", isinstance(nwc, NWC))
print(issubclass(NWC, object))
dsbs = DSBS()
print("it is dsbs object", isinstance(dsbs, DSBS))
print(issubclass(DSBS, object))