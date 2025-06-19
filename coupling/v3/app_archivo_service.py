from datetime import datetime, timedelta
from datetime import timedelta
import secrets
from fastapi import Request, File
from src.models.archivo.archivo_model import ArchivoModel
from src.repositories.archivo.archivo_sql_repository import ArchivoSqlRepository
from src.models.archivo.archivo_mapper import ArchivoMapper
from src.entry_points.S3FilesEntrypoint import S3FilesEntrypoint
import json
import logging

logging.basicConfig(level=logging.INFO, format="[%(asctime)s] [%(process)d] [%(levelname)s] %(message)s", datefmt="%Y-%m-%d %H:%M:%S %z")
class AppArchivoService:
    def __init__(self, request:Request = None):
        self.archivo_sql_repository = ArchivoSqlRepository(request=request)
        self.archivo_mapper: ArchivoMapper = ArchivoMapper()
        self.entrypoint: S3FilesEntrypoint = S3FilesEntrypoint() # Now we can pass arguments

    async def create(self, archivo_data: str, archivo: File):
        # Guardar archivo en S3
        data = json.loads(archivo_data)
        if isinstance(data.get("tags_archivo"), str):
            data["tags_archivo"] = json.loads(data["tags_archivo"])
        model = ArchivoModel(**data)
        try:
            with archivo.file as fichero:
                objeto_key = f"files{model.url}"
                await self.entrypoint.upload_files_to_s3(fichero,objeto_key)
        except Exception as e:
            print(e)
            return None
        # Guardar archivo en base de datos
        try:
            return await self.archivo_sql_repository.create(self.archivo_mapper.application_to_sql(model))
        except Exception as e:
            print(e)
            await self.entrypoint.delete_file_from_s3(objeto_key)
            return None
    
    async def create_tmp_factura(self, archivo: File):
        # Guardar archivo en S3; no guarda en base de datos
        try:
            with archivo.file as fichero:
                nombre_token = secrets.token_hex(15)
                nombre_archivo = archivo.filename
                if (not nombre_archivo.lower().endswith('.pdf') or not self._is_pdf(fichero)):
                    raise Exception("error", "El archivo no es un PDF")
                
                objeto_key = f"tmp-factura/{nombre_token}"
                await self.entrypoint.upload_files_to_s3(fichero,objeto_key)
                logging.info(f"Archivo subido a s3 correctamente: {objeto_key}")
                return objeto_key
        except Exception as e:
            print(e)
            return None
        
        
    def _is_pdf(self, fichero):
        first_bytes = fichero.read(4)
        fichero.seek(0)
        return first_bytes == b'%PDF'