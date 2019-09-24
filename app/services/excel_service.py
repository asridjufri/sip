import pandas as pd
from pandas import ExcelFile
from app.models import MasterCategory, MasterJenis, MasterTourism, DataTourist, MasterKecamatan
import datetime
import uuid
from random import randint

JAN=['jan','january','januari']
FEB=['feb','february','februari','fabruari']
MAR=['mar','march','maret', 'marc']
APR=['apr','april']
MAY=['may', 'mei']
JUN=['jun','june','juni']
JUL=['jul','july','juli']
AUG=['aug','august','agustus']
SEPT=['sept','sep','september']
OCT=['oct','october','oktober']
NOV=['nov','november']
DEC=['dec','december','desember']

def get_bulan_number(bulan_str):
    bulan_str=bulan_str.lower()
    if bulan_str in JAN:
        return 1
    if bulan_str in FEB:
        return 2
    if bulan_str in MAR:
        return 3
    if bulan_str in APR:
        return 4
    if bulan_str in MAY:
        return 5
    if bulan_str in JUN:
        return 6
    if bulan_str in JUL:
        return 7
    if bulan_str in AUG:
        return 8
    if bulan_str in SEPT:
        return 9
    if bulan_str in OCT:
        return 10
    if bulan_str in NOV:
        return 11
    if bulan_str in DEC:
        return 12

class ImportExcelService():
    @staticmethod
    def parse_data( file_name):
        df = pd.read_excel(file_name, sheet_name='Table 1',skiprows=2)
        df=df[(df.columns[0] !=df[df.columns[0]])]
        df.dropna(axis=0, how='all',inplace=True)
        
        # print(df.head(10))
        # print(df.columns)
        
        # print(df['No.'])
        # print(df['Nama Wisata'])
        # for item in df['Nama Wisata']:
        #     if type(item) == float:
        #         print("float")
        #     elif type(item) == str:
        #         print(item)
        # print(df.columns)
        idx_bulans=[6,9,12,15,18,21]
        bulan_1=''
        bulan_2=''
        bulan_3=''
        bulan_4=''
        bulan_5=''
        bulan_6=''
        cleaned_data=[]
        
        for index, row in df.iterrows():
            
            
            if type(row['Nama Wisata']) == float:
                bulan_1=''
                bulan_2=''
                bulan_3=''
                bulan_4=''
                bulan_5=''
                bulan_6=''

                bulan_1=df.columns[6]
                bulan_2=df.columns[9]
                bulan_3=df.columns[12]
                bulan_4=df.columns[15]
                bulan_5=df.columns[18]
                bulan_6=df.columns[21]
                print(bulan_1,bulan_2,bulan_3,bulan_4,bulan_5,bulan_6)
                
                
                
                
            elif type(row['Nama Wisata']) == str:
                # print(row['Nama Wisata'])
                tenaga_l=row['Tenaga']
                tenaga_p=row['Unnamed: 5']
                
                data_bulanan=[]
                for index in idx_bulans:
                    nus=row[index]
                    man=row[index+1]
                    rp=row[index+2]
                    if '.' in str(nus):
                        nus = int(nus*1000)
                    if '.' in str(man):
                        man=int(man*1000)
                    item_bulanan={'month':df.columns[index],
                                    'nus':nus,
                                    'man':man,
                                    'rp':rp
                                }
                    data_bulanan.append(item_bulanan)
                    
                # data_bulanan=[{'month':bulan_1,'nus':nus_1}]
                item={'name':row['Nama Wisata'], 'jenis_wisata':row['Jenis Wisata'],'alamat':row['Alamat Wisata'],
                    'tenaga_l':tenaga_l, 'tenaga_p':tenaga_p,'data':data_bulanan
                    }
                cleaned_data.append(item)    
            
            # print(row['Nama Wisata'])   
        return cleaned_data
    
    @staticmethod
    def save_data(year_data, category_data, data, force=False):
        print(force)
        msg=""
        if year_data < 1990 :
            raise Exception("year not valid value")
        master_category = MasterCategory.objects.filter(categoryname = category_data.lower()).first()
        now=datetime.datetime.now()
        

        if not master_category:
            raise Exception("category %s not found in database please add this category in master category" %category_data)
        for item in data:
            nama_wisata=item['name']
            jenis_wisata = item['jenis_wisata']
            alamat = item['alamat']
            tenaga_l = item['tenaga_l']
            tenaga_p = item['tenaga_p']
            for i in item['data']:
                bulan_str=i['month']
                nus=i['nus']
                man=i['man']
                rp = i['rp']
                master_jenis=None
                try:
                    master_jenis = MasterJenis.objects.filter(jenis=jenis_wisata.lower(), category=master_category.categoryid).first()
                    
                except Exception as identifier:
                    continue
                if force:
                    if master_jenis is None:
                        master_jenis = MasterJenis()
                        master_jenis.jenisid = str(uuid.uuid4())
                        master_jenis.jenis=jenis_wisata
                        master_jenis.createdby='system'
                        master_jenis.modifiedby='system'
                        master_jenis.deleted='0'
                        master_jenis.createddate = now.strftime('%Y-%m-%d %H:%M:%S')
                        master_jenis.modifieddate = now.strftime('%Y-%m-%d %H:%M:%S')
                        master_jenis.category = master_category
                        master_jenis.save()
                        print("\033[94m [MASER JENIS] create new jenis \033[0m")
                        msg+="%s\n" %("[MASER JENIS] create new jenis")

                if master_jenis:
                    print("found ",master_jenis.jenis)
                    msg="%s/n"%("found "+master_jenis.jenis)
                    master_tourism = MasterTourism.objects.filter(tourismname=nama_wisata.lower(),month=str(get_bulan_number(bulan_str)), year=str(year_data)).first()
                    if master_tourism:
                        print("[MASTER TOURISM] data was exist")
                        msg+="%s\n"%("[MASTER TOURISM] data was exist")
                    else:
                        master_tourism = MasterTourism()
                        master_tourism.tourismid = str(uuid.uuid4())
                        master_tourism.tourismname = nama_wisata
                        master_tourism.karyawan = int(tenaga_l)
                        master_tourism.karyawati = int(tenaga_p)
                        master_tourism.categoryid= master_jenis.category.categoryname
                        master_tourism.jenisid = master_jenis.jenisid
                        master_tourism.pengelola = 'Berizin'
                        master_tourism.suratizin = '-'
                        master_tourism.tanggal_suratizin = now.strftime("%Y-%m-%d")
                        master_tourism.masaizin ='-'
                        master_tourism.nosurat = '-'
                        master_tourism.tanggal_input = now.strftime("%Y-%m-%d %H:%M:%S")
                        master_tourism.wilayah = 'Kota Tangerang Selatan'
                        master_tourism.kecamatanid =  1
                        
                            
                        if '-' in alamat:
                            array_alamat = alamat.split('-')
                            kecamatan = array_alamat[1]
                            kecamatan = kecamatan.replace('Kecamatan','')
                            kecamatan = kecamatan.replace('kecamatan','')
                            kecamatan =kecamatan.strip()
                            kecamatan_db = MasterKecamatan.objects.filter(kecamatan=kecamatan.lower()).first()
                            if kecamatan_db:
                                master_tourism.kecamatanid=kecamatan_db.kecamatanid



                        master_tourism.alamat = alamat
                        master_tourism.phone = '-'
                        master_tourism.email = str('user%s@gmail.com' %(randint(1,200)))
                        # date = datetime.date(year_data, get_bulan_number(bulan_str), 1)
                        master_tourism.month = str(get_bulan_number(bulan_str))
                        master_tourism.year = str(year_data)
                        master_tourism.longitude = '106.68639259999998'
                        master_tourism.latitude = '-6.3033316'
                        master_tourism.fasilitas ='-'
                        master_tourism.status = 'Aktif'
                        master_tourism.createdby = 'system'
                        master_tourism.createddate = now.strftime("%Y-%m-%d")
                        master_tourism.modifiedby = 'system'
                        master_tourism.modifieddate = master_tourism.createddate
                        master_tourism.deleted =0
                        master_tourism.save()
                        print("\033[94m [MASER TOURISM] master tourism saved \033[0m")
                        msg+="%s\n"%("[MASER TOURISM] master tourism saved")
                    
                    date = datetime.date(year_data, get_bulan_number(bulan_str), 1)
                    data_tourist = DataTourist.objects.filter(tourismid=master_tourism.tourismid,date=date,mancanegara=man, indonesia=nus).first()
                    if data_tourist:
                        print('[DATA TOURIST] data touris was exist')
                        msg += "%s\n"%("[DATA TOURIST] data touris was exist")
                    else:
                        data_tourist = DataTourist()
                        data_tourist.touristid = str(uuid.uuid4())
                        data_tourist.tourismid = master_tourism.tourismid
                        data_tourist.bulan = str(date.strftime('%Y-%m'))
                        data_tourist.pendapatan = rp
                        data_tourist.createdby = 'system'
                        data_tourist.createddate = now.strftime('%Y-%m-%d %H:%M:%S')
                        data_tourist.modifiedby = 'system'
                        data_tourist.modifieddate = now.strftime('%Y-%m-%d %H:%M:%S')
                        data_tourist.deleted = 0
                        data_tourist.indonesia = nus
                        data_tourist.australia = 0
                        data_tourist.prancis = 0
                        data_tourist.india = 0
                        data_tourist.jepang = 0
                        data_tourist.malaysia = 0
                        data_tourist.singapore = 0
                        data_tourist.kanada = 0
                        data_tourist.brazil = 0
                        data_tourist.belanda = 0
                        data_tourist.china = 0
                        data_tourist.jerman = 0
                        data_tourist.inggris = 0
                        data_tourist.pakistan = 0
                        data_tourist.philipina = 0
                        data_tourist.thailand = 0
                        data_tourist.cili = 0
                        data_tourist.arab = 0
                        data_tourist.lainlain = 0
                        data_tourist.mancanegara = man
                        data_tourist.date = date
                        data_tourist.save()
                        print("\033[94m [DATA TOURIS]  data tourism  saved \033[0m")
                        msg += "%s\n"%("[DATA TOURIS]  data tourism  saved")

                else:
                    print("\033[93m master jenis %s notfound \033[0m"%jenis_wisata)
                    msg+="master jenis %s notfound\n"%(jenis_wisata)
        return msg
                # print("saved data for %s jenis %s"%(nama_wisata, jenis_wisata))


        