from django.db import models

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.



class Appconfiguration(models.Model):
    configname = models.CharField(max_length=100)
    configvalue = models.CharField(max_length=100)
    modifiedby = models.CharField(max_length=20)
    modifieddate = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'appconfiguration'


class Appgroup(models.Model):
    groupid = models.CharField(primary_key=True, max_length=40)
    groupname = models.CharField(max_length=50)
    readonly = models.CharField(max_length=1)
    isapps = models.CharField(max_length=1)
    createdby = models.CharField(max_length=20)
    createddate = models.CharField(max_length=16)
    modifiedby = models.CharField(max_length=20)
    modifieddate = models.CharField(max_length=16)
    deleted = models.CharField(max_length=1)
    menusid = models.CharField(max_length=500)
    # defaultmodule = models.CharField(max_length=40)
    defaultmodule = models.ForeignKey('app.Appmodule', db_column='defaultmodule', on_delete=models.CASCADE)
    dpdid = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'appgroup'


class Applang(models.Model):
    langid = models.CharField(max_length=40,primary_key=True) # tmp set as primary key
    langname = models.CharField(max_length=100)
    shortcode = models.CharField(max_length=20)
    createdby = models.CharField(max_length=20)
    createddate = models.CharField(max_length=16)
    modifiedby = models.CharField(max_length=20)
    modifieddate = models.CharField(max_length=16)
    deleted = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'applang'


class Appmenu(models.Model):
    menuid = models.AutoField(primary_key=True)
    menutext = models.CharField(max_length=40)
    menutext_id = models.CharField(max_length=20)
    menuicon = models.CharField(max_length=20)
    # moduleid = models.CharField(max_length=40, blank=True, null=True)
    menuorder = models.IntegerField()
    parentid = models.CharField(max_length=40, blank=True, null=True)
    readonly = models.CharField(max_length=1)
    createdby = models.CharField(max_length=20)
    createddate = models.CharField(max_length=16)
    modifiedby = models.CharField(max_length=20)
    modifieddate = models.CharField(max_length=16)
    deleted = models.CharField(max_length=1)
    #additional
    module = models.ForeignKey("app.Appmodule", on_delete=models.CASCADE,db_column='moduleid')
    
    class Meta:
        managed = False
        db_table = 'appmenu'


class Appmodule(models.Model):
    moduleid = models.CharField(primary_key=True, max_length=40)
    modulename = models.CharField(max_length=30)
    readonly = models.CharField(max_length=1)
    createdby = models.CharField(max_length=20)
    createddate = models.CharField(max_length=16)
    modifiedby = models.CharField(max_length=20)
    modifieddate = models.CharField(max_length=16)
    deleted = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'appmodule'


class Appnotification(models.Model):
    id = models.CharField(primary_key=True, max_length=40)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=500)
    triggerby = models.CharField(max_length=100)
    createdby = models.CharField(max_length=20)
    createddate = models.CharField(max_length=16)
    modifiedby = models.CharField(max_length=20)
    modifieddate = models.CharField(max_length=16)
    deleted = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'appnotification'


class Appnotificationuser(models.Model):
    id = models.CharField(primary_key=True, max_length=40)
    iduser = models.CharField(max_length=40)
    idnotification = models.CharField(max_length=40)
    readed = models.CharField(max_length=1)
    createdby = models.CharField(max_length=20)
    createddate = models.CharField(max_length=16)
    modifiedby = models.CharField(max_length=20)
    modifieddate = models.CharField(max_length=16)

    class Meta:
        managed = False
        db_table = 'appnotificationuser'


class Appuser(models.Model):
    userkey = models.CharField(primary_key=True, max_length=40)
    user = models.CharField(max_length=20)
    password = models.CharField(max_length=34)
    level = models.CharField(max_length=1)
    createdby = models.CharField(max_length=20)
    createddate = models.CharField(max_length=16)
    modifiedby = models.CharField(max_length=20)
    modifieddate = models.CharField(max_length=16)
    deleted = models.CharField(max_length=1)
    groupid = models.CharField(max_length=40)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    picture = models.CharField(max_length=200)
    status = models.IntegerField()
    companyid = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'appuser'


class DataTourist(models.Model):
    touristid = models.CharField(primary_key=True, max_length=40)
    # tourismid = models.CharField(max_length=100)
    bulan = models.CharField(max_length=40)
    pendapatan = models.CharField(max_length=1000)
    createdby = models.CharField(max_length=20)
    createddate = models.CharField(max_length=16)
    modifiedby = models.CharField(max_length=20)
    modifieddate = models.CharField(max_length=16)
    deleted = models.CharField(max_length=1)
    indonesia = models.CharField(max_length=1000)
    australia = models.CharField(max_length=1000)
    prancis = models.CharField(max_length=1000)
    india = models.CharField(max_length=1000)
    jepang = models.CharField(max_length=1000)
    malaysia = models.CharField(max_length=1000)
    singapore = models.CharField(max_length=1000)
    kanada = models.CharField(max_length=1000)
    brazil = models.CharField(max_length=1000)
    belanda = models.CharField(max_length=1000)
    china = models.CharField(max_length=1000)
    jerman = models.CharField(max_length=1000)
    inggris = models.CharField(max_length=1000)
    pakistan = models.CharField(max_length=1000)
    philipina = models.CharField(max_length=1000)
    thailand = models.CharField(max_length=1000)
    cili = models.CharField(max_length=1000)
    arab = models.CharField(max_length=1000)
    lainlain = models.CharField(max_length=1000)
    mancanegara = models.CharField(max_length=1000)
    date = models.DateField(null=True, blank=True)
    tourism = models.ForeignKey("app.MasterTourism",db_column='tourismid',on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'data_tourist'


class MasterCategory(models.Model):
    categoryid = models.CharField(primary_key=True, max_length=40)
    categoryname = models.CharField(max_length=100)
    categorygroup = models.CharField(max_length=20)
    createdby = models.CharField(max_length=20)
    createddate = models.CharField(max_length=16)
    modifiedby = models.CharField(max_length=20)
    modifieddate = models.CharField(max_length=16)
    deleted = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'master_category'


class MasterJenis(models.Model):
    jenisid = models.CharField(primary_key=True, max_length=40)
    jenis = models.CharField(max_length=40)
    # jenisgroup = models.CharField(max_length=100)
    createdby = models.CharField(max_length=20)
    createddate = models.CharField(max_length=16)
    modifiedby = models.CharField(max_length=20)
    modifieddate = models.CharField(max_length=16)
    deleted = models.CharField(max_length=1)
    #tambahan
    category = models.ForeignKey(MasterCategory, db_column='jenisgroup', on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'master_jenis'


class MasterKecamatan(models.Model):
    kecamatanid = models.CharField(primary_key=True, max_length=40)
    kecamatan = models.CharField(max_length=40)
    createdby = models.CharField(max_length=20)
    createddate = models.CharField(max_length=16)
    modifiedby = models.CharField(max_length=20)
    modifieddate = models.CharField(max_length=16)
    deleted = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'master_kecamatan'


class MasterLanguage(models.Model):
    languageid = models.CharField(primary_key=True, max_length=40)
    languagename = models.CharField(max_length=20)
    createdby = models.CharField(max_length=20)
    createddate = models.CharField(max_length=16)
    modifiedby = models.CharField(max_length=20)
    modifieddate = models.CharField(max_length=16)
    deleted = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'master_language'


class MasterTourism(models.Model):
    tourismid = models.CharField(primary_key=True, max_length=20)
    tourismname = models.CharField(max_length=40)
    karyawan = models.IntegerField()
    karyawati = models.IntegerField()
    categoryid = models.CharField(max_length=100)
    jenisid = models.CharField(max_length=100)
    pengelola = models.CharField(max_length=300)
    suratizin = models.CharField(max_length=40)
    tanggal_suratizin = models.CharField(max_length=40)
    masaizin = models.CharField(max_length=40)
    nosurat = models.CharField(max_length=500)
    tanggal_input = models.CharField(max_length=40)
    wilayah = models.CharField(max_length=50)
    kecamatanid = models.CharField(max_length=20)
    alamat = models.CharField(max_length=1000)
    file1 = models.CharField(max_length=50)
    file2 = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=400)
    month = models.CharField(max_length=30)
    year = models.CharField(max_length=10)
    longitude = models.CharField(max_length=500)
    latitude = models.CharField(max_length=500)
    fasilitas = models.CharField(max_length=2000)
    status = models.CharField(max_length=20)
    createdby = models.CharField(max_length=20)
    createddate = models.CharField(max_length=16)
    modifiedby = models.CharField(max_length=20)
    modifieddate = models.CharField(max_length=16)
    deleted = models.CharField(max_length=1)

    @property
    def jenis(self):
        return MasterJenis.objects.filter(jenisid=self.jenisid).first() 
    
    class Meta:
        managed = False
        db_table = 'master_tourism'

#  model baru