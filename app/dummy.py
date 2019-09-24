from random import randint
import datetime
import uuid
from django.db import connection
from app.models import MasterJenis, MasterTourism, MasterKecamatan, DataTourist
class DummyService():

    
    @staticmethod
    def get_random_date():
        date = datetime.date(randint(2017,2019), randint(1,12),randint(1,28))
        return date
    
    @staticmethod
    def get_random_pendapatan():
        base_pendapatan = 100000
        return randint(1,200) *base_pendapatan

    @staticmethod
    def get_random_jenis():
        count = MasterJenis.objects.filter(deleted=0).count()
        index = randint(0, count-1)
        return MasterJenis.objects.filter(deleted=0)[index]
    
    @staticmethod 
    def get_random_kecamatan():
        count = MasterKecamatan.objects.filter(deleted=0).count()
        index = randint(0,count-1)
        return MasterKecamatan.objects.filter(deleted=0)[index]


    @staticmethod
    def generate_dummy_master_tourism(number):
        for a in range(number):
            jenis = DummyService.get_random_jenis()
            tourism = MasterTourism()
            tourism.tourismid = str(uuid.uuid4())
            tourism.tourismname = "%s %s" %(jenis.jenis, randint(1,1000))
            tourism.karyawan = randint(1,100)
            tourism.karyawati = randint(1,100)
            tourism.categoryid= jenis.category.categoryname
            tourism.jenisid = jenis.jenisid
            tourism.pengelola = 'Berizin'
            tourism.suratizin = '-'
            tourism.tanggal_suratizin =DummyService.get_random_date().strftime("%Y-%m-%d")
            tourism.masaizin =str(randint(1,5))
            tourism.nosurat = str(randint(2000,3000))
            tourism.tanggal_input = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            tourism.wilayah = 'Kota Tangerang Selatan'
            tourism.kecamatanid =  DummyService.get_random_kecamatan().kecamatanid
            tourism.alamat = 'Alamat %s' %(randint(1,1000))
            tourism.phone = '02122233%s%s%s' %(randint(1,9), randint(0,9), randint(0,9))
            tourism.email = str('user%s@gmail.com' %(randint(1,200)))
            date = DummyService.get_random_date()
            tourism.month = str(date.month)
            tourism.year = str(date.year)
            tourism.longitude = '106.68639259999998'
            tourism.latitude = '-6.3033316'
            tourism.fasilitas ='-'
            tourism.status = 'Aktif'
            tourism.createdby = 'admin'
            tourism.createddate = datetime.datetime.now().strftime("%Y-%m-%d")
            tourism.modifiedby = 'admin'
            tourism.modifieddate = tourism.createddate
            tourism.deleted =0
            tourism.save()
    
    @staticmethod
    def truncate_master_tourism():
        with connection.cursor() as cursor:
            cursor.execute("TRUNCATE TABLE master_tourism ")

    @staticmethod
    def get_random_master_tourism():
        count = MasterTourism.objects.filter(deleted=0).count()
        index = randint(0, count-1)
        return MasterTourism.objects.filter(deleted=0)[index]
    
    @staticmethod
    def generate_dummy_data_tourist(number):
        for a in range(number):
            rdatetime = DummyService.get_random_date()

            data = DataTourist()
            data.touristid = str(uuid.uuid4())
            data.tourismid = DummyService.get_random_master_tourism().tourismid
            data.bulan = str(rdatetime.strftime('%Y-%m'))
            data.pendapatan = DummyService.get_random_pendapatan()
            data.createdby = 'admin'
            data.createddate = rdatetime.strftime('%Y-%m-%d %H:%M:%S')
            data.modifiedby = 'admin'
            data.modifieddate = rdatetime.strftime('%Y-%m-%d %H:%M:%S')
            data.deleted = 0
            data.indonesia = randint(0,5000)
            data.australia = randint(0,1000)
            data.prancis = randint(0,100)
            data.india = randint(0, 788)
            data.jepang = randint(0,2000)
            data.malaysia = randint(0,5000)
            data.singapore = randint(0,4000)
            data.kanada = randint(0, 1000)
            data.brazil = randint(0, 100)
            data.belanda = randint(0, 3500)
            data.china = randint(0,10000)
            data.jerman = randint(0, 500)
            data.inggris = randint(0,2500)
            data.pakistan = randint(0,789)
            data.philipina = randint(0,3000)
            data.thailand = randint(0,7000)
            data.cili = randint(0,400)
            data.arab = randint(0,7000)
            data.lainlain = randint(0,10000)
            data.mancanegara = randint(0,1000)
            data.date = rdatetime
            
            data.save()
    
    
    @staticmethod
    def truncate_data_tourist():
        with connection.cursor() as cursor:
            cursor.execute("TRUNCATE TABLE data_tourist ")



        
    
    
    

