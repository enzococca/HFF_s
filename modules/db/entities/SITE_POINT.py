'''Created on 30 05 2021@author: Enzo Cocca'''from builtins import objectclass SITE_POINT(object):    # def __init__"    def __init__(self,                 gid,                 id,                 location,                 name_f_p,                                  photo,                 photo2,                 photo3,                 photo4,                 photo5,                 photo6,                                  the_geom,                 coord                 ):        self.gid = gid  # 0        self.id=id        self.location = location # 1        self.name_f_p=name_f_p        self.photo1=photo        self.photo2=photo2        self.photo3=photo3        self.photo4=photo4        self.photo5=photo5        self.photo6=photo6                self.the_geom = the_geom  # 2        self.coord=coord    # def __repr__"    def __repr__(self):        return "<SITE_POINT('%d','%s', '%s',%s,'%s','%s', '%s', '%s', '%s','%s','%s','%s')>" % (            self.gid,            self.id,            self.location,            self.name_f_p,            self.photo,            self.photo2,            self.photo3,            self.photo4,            self.photo5,            self.photo6,                        self.the_geom,            self.coord        )