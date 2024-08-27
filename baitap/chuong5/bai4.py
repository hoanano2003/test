from asyncio.windows_events import NULL


class HocSinh:
    def __init__(self,ten,diaChi,chieuCao,canNang):
        self.ten = ten
        self.diaChi =  diaChi
        self.chieuCao = chieuCao
        self.canNang = canNang
        self.hocLuc = ""
    def capNhatDiaChi(self,diaChi):
        self.diaChi = diaChi
    def capNhatChieuCaoCanNang(self,chieuCao,canNang):
        self.chieuCao = chieuCao
        self.canNang = canNang
    def capNhatHocLuc(self,hocLuc):
        self.hocLuc = hocLuc