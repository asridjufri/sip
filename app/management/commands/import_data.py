from django.core.management.base import BaseCommand, CommandError
# import pandas as pd
# from pandas import ExcelFile
from app.services.excel_service import ImportExcelService
import json





class Command(BaseCommand):
    help="import data from excel"
    def add_arguments(self, parser):
        parser.add_argument('--file',help='file excel')
        parser.add_argument('--category',help='kategory wisata')
        parser.add_argument('--year',help='tahun data',type=int)
        parser.add_argument('--force',help='tahun data',type=bool)
    
    def handle(self, *args, **options):
        force=False
        if 'category' not in options:
            raise Exception("please input category")
        if 'file' not in options:
            raise Exception("please input file")
        if 'year' not in options:
            raise Exception("please input tahun data")
        if 'force' not in options:
            force=False
        else:
            force = options['force']

        file_name = options['file']
        category = options['category']
        year = options['year']
        data = ImportExcelService.parse_data(file_name)
        print(data)
        ImportExcelService.save_data(year, category, data,force)
        
        
        
 