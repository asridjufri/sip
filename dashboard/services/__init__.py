from app import repository
from app.models import MasterKecamatan
BULAN={1:'Jan',2:'Feb',3:'Mar',4:'Apr',5:'Mei',6:'Jun',7:'Jul', 8:'Aug', 9:'Sep', 10:'Oct', 11:'Nov',12:'Dec' }

class ChartService(object):
    # categoryid ('MICE','spa','hiburan dan rekreasi','jasa perjalanan','akomodasi', 'jasa makanan dan minuman')
    @staticmethod
    def get_kecamatan_by_name(name_kecamatan):
        if name_kecamatan:
            kecamatan=MasterKecamatan.objects.filter(kecamatan=name_kecamatan.lower()).first()
            return kecamatan
        return None
    
    @staticmethod
    def get_kecamatan_by_id(idkecamatan):
        if idkecamatan:
            kecamatan=MasterKecamatan.objects.filter(kecamatanid=idkecamatan).first()
            return kecamatan
        return None

    @staticmethod
    def get_chart_number_tourism_per_category_per_year(categoryid):
        d = repository.get_number_tourism_per_category_per_year(categoryid)
        
        categories={'indonesia':[],'australia':[],'prancis':[],'india':[],'jepang':[],'malaysia':[],'singapore':[],'kanada':[],'brazil':[],'belanda':[],'china':[],'jerman':[],'inggris':[],'pakistan':[],'philipina':[],'thailand':[],'cili':[],}
        m_categories =[]
        for i in d:
            for c in categories:
                found=False
                for ic in categories[c]:
                    if i['year'] in ic:
                        found=True
                        ic[i['year']]=ic[i['year']]+i[c]
 
                if not found :
                    categories[c].append({i['year']:i[c]})
        for k in categories:
            m_categories.append(k)
        years={2017:[],2018:[],2019:[]}
        for y in years:
            for cat in categories:
                # print(categories[cat])
                for item in categories[cat]:
                    if y in item:
                        years[y].append(item[y])
        series=[]
        for i in years:
            series.append({'name':'Tahun %s'%i,'data':years[i]})
        data ={'title':"Jumlah wistawan category %s per tahun"%categoryid, "categories":m_categories, 'series':series}
            
        return data

    @staticmethod
    def get_chart_number_tourism_per_category_per_month(categoryid, year):
        d = repository.get_number_tourism_percategory_per_month(categoryid,year)
        categories={'indonesia':[],'australia':[],'prancis':[],'india':[],'jepang':[],'malaysia':[],'singapore':[],'kanada':[],'brazil':[],'belanda':[],'china':[],'jerman':[],'inggris':[],'pakistan':[],'philipina':[],'thailand':[],'cili':[],}
        
        m_categories =[]
        for i in d:
            for c in categories:
                found=False
                for ic in categories[c]:
                    if i['month'] in ic:
                        found=True
                        ic[i['month']]=ic[i['month']]+i[c]
 
                if not found :
                    categories[c].append({i['month']:i[c]})
        
        for k in categories:
            m_categories.append(k)
        months={1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[],10:[],11:[],12:[]}
        for y in months:
            for cat in categories:
                # print(categories[cat])
                for item in categories[cat]:
                    if y in item:
                        months[y].append(item[y])
        series=[]
        for i in months:
            series.append({'name':'Bulan %s'%i,'data':months[i]})
        data ={'title':"Jumlah tourism category %s per bulan tahun %s"%(categoryid,year) ,"categories":m_categories, 'series':series}
        return data
    
    @staticmethod
    def get_chart_number_tourism_per_category_per_year_domestic_mancanegara(categoryid):
        d = repository.get_number_tourism_per_category_per_year_domestic_mancanegara(categoryid)
        categories={'domestic':[],'mancanegara':[]}
        m_categories =[]
        for i in d:
            for c in categories:
                found=False
                for ic in categories[c]:
                    if i['year'] in ic:
                        found=True
                        ic[i['year']]=ic[i['year']]+i[c]
 
                if not found :
                    categories[c].append({i['year']:i[c]})
        for k in categories:
            m_categories.append(k)
        years={2017:[],2018:[],2019:[]}
        for y in years:
            for cat in categories:
                # print(categories[cat])
                for item in categories[cat]:
                    if y in item:
                        years[y].append(item[y])
        series=[]
        for i in years:
            series.append({'name':'Tahun %s'%i,'data':years[i]})
        data ={'title':"Jumlah wistawan domestic dan mancanegara category %s per tahun"%categoryid, "categories":m_categories, 'series':series}
            
        return data

    @staticmethod
    def get_number_domestic_mancanegara_at_year(ayear, idkecamatan=None):
        d = repository.get_number_domestic_mancanegara_at_year(ayear, idkecamatan)
        kecamatan = ChartService.get_kecamatan_by_id(idkecamatan)
        data=[{'name':'domestic', 'y':0}, {'name':'mancanegara', 'y':0}]
        for item in d:
            for i in data:
                if i['name']== 'domestic':
                    i['y']=i['y']+item['domestic']
                if i['name']== 'mancanegara':
                    i['y']=i['y']+item['mancanegara']
        title='Jumlah wisatawan domestik dan mancanegara pada tahun %s ' %(ayear)
        if kecamatan:
            title='Jumlah wisatawan domestik dan mancanegara pada tahun %s - %s ' %(ayear, kecamatan.kecamatan.upper())
        result ={'title':title,'data':data, 'name':'jumlah wisman'}
        return result
    
    @staticmethod
    def get_number_tourist_per_categories_at_year(ayear, idkecamatan=None):
        d = repository.get_number_tourist_per_categories_at_year(ayear, idkecamatan)
        kecamatan = ChartService.get_kecamatan_by_id(idkecamatan)
        data=[]
        for item in d:
            data.append({'name':item['categoryid'],'y':item['tourist']})
        title='jumlah wisatawan per kategori pada tahun %s'%ayear
        if kecamatan:
            title = 'jumlah wisatawan per kategori pada tahun %s - %s'%(ayear, kecamatan.kecamatan.upper())
        result={'title': title, 'data':data, 'name':'jumlah wisatawan'}
        return result


                
    @staticmethod
    def get_number_tourism_per_category_per_month_domestic_mancanegara(ayear, idkecamatan=None):
        d = repository.get_number_tourism_per_category_per_month_domestic_mancanegara(ayear,idkecamatan)
        kecamatan = ChartService.get_kecamatan_by_id(idkecamatan)
        # categories={1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[],10:[],11:[],12:[]}
        
        m_categories={'domestic':[], 'mancanegara':[]}
        categories =[]
        for i in range(12):
            categories.append(BULAN[i+1])
            for item in d:
                
                if i+1 == int(item['month']):   
                    print('match ',i+1)
                    m_categories['domestic'].append(item['domestic'])
                    m_categories['mancanegara'].append(item['mancanegara'])
                    break

        
        print(m_categories)
        series=[]
        series=[{'name':'domestic', 'data':m_categories['domestic']},{'name':'mancanegara', 'data':m_categories['mancanegara']}]
            
        title = "Jumlah wisatawan per kategori per bulan tahun %s "%(ayear)
        if kecamatan:
            title = "Jumlah wisatawan per kategori per bulan tahun %s - %s "%(ayear, kecamatan.kecamatan.upper())        
        data ={'title':title ,"categories":categories, 'series':series}
        return data

    @staticmethod
    def get_number_tourism_per_categories_per_month_domestic(year, idkecamatan=None):
        d = repository.get_number_tourism_per_category_per_month_domestic_mancanegara(year, idkecamatan)
        kecamatan = ChartService.get_kecamatan_by_id(idkecamatan)
        categories={1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[],10:[],11:[],12:[]}
        m_categories =[]
        for c in categories:
            for i in d:
                if c==int(i['month']):
                    categories[c].append({i['categoryid']:i['domestic']})
        for k in categories:
            m_categories.append(BULAN[k])

        series=[{'name':'Akomodasi','data':[]},{'name':'Hiburan dan Rekreasi', 'data':[]},
                 {'name':'Jasa Makanan dan Minuman', 'data':[]}, {'name':'Jasa Perjalanan ', 'data':[]},
                 {'name':'MICE', 'data':[]},{'name':'Spa', 'data':[]}
                ]
        for i in series:
            for bulan in categories:
                for item in categories[bulan]:
                    if i['name'] in item:
                        i['data'].append(item[i['name']])
        
        title = "Jumlah wisatawan domestik per kategori  per bulan tahun %s"%(year)
        if kecamatan:
            title = "Jumlah wisatawan domestik per kategori  per bulan tahun %s - %s"%(year, kecamatan.kecamatan.upper())
        data ={'title':title ,"categories":m_categories, 'series':series}
        return data
    
    @staticmethod
    def get_number_tourism_per_categories_per_month_mancanegara(year, idkecamatan=None):
        d = repository.get_number_tourism_per_category_per_month_domestic_mancanegara(year, idkecamatan)
        kecamatan = ChartService.get_kecamatan_by_id(idkecamatan)
        categories={1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[],10:[],11:[],12:[]}
        m_categories =[]
        for c in categories:
            for i in d:
                if c==int(i['month']):
                    categories[c].append({i['categoryid']:i['mancanegara']})
        for k in categories:
            m_categories.append(BULAN[k])

        series=[{'name':'Akomodasi','data':[]},{'name':'Hiburan dan Rekreasi', 'data':[]},
                 {'name':'Jasa Makanan dan Minuman', 'data':[]}, {'name':'Jasa Perjalanan ', 'data':[]},
                 {'name':'MICE', 'data':[]},{'name':'Spa', 'data':[]}
                ]
        for i in series:
            for bulan in categories:
                for item in categories[bulan]:
                    if i['name'] in item:
                        i['data'].append(item[i['name']])
        title = "Jumlah wisatawan mancanegara per kategori  per bulan tahun %s"%(year)
        if kecamatan:
            title = "Jumlah wisatawan mancanegara per kategori  per bulan tahun %s - %s"%(year, kecamatan.kecamatan.upper())
        data ={'title':title ,"categories":m_categories, 'series':series}
        return data
            
            

    # @staticmethod
    # def get_number_tourism_percategories_at_year_domestic_mancanegara(categories, ayear):
    #     d = repository.get_number_tourism_percategories_at_year_domestic_mancanegara(categories, ayear)
    



                
