import ftplib
import io
from typing import Dict


class FtpConn:
    
    #Imagine this being dynamic  
    FTP_HOST = "172.23.0.1:21"
    FTP_USER = "user"
    FTP_PASS = "pass"

    def upload_file_ftp(self, remote_filepath, file=None, file_path_local=None) -> bool:
        if file is None and file_path_local is None:
            return False
        if file is not None and file_path_local is not None:
            return False#some great error message that gives the user info surely
        #try catch ....
        with ftplib.FTP(self.FTP_HOST, self.FTP_USER, self.FTP_PASS) as ftp:
            if file:
                file_io = io.BytesIO()
                file_wrapper = io.TextIOWrapper(file_io, encoding='utf-8')
                file_wrapper.write(file)
                file_io.seek(0)
                ftp.storbinary(f'STOR {remote_filepath}', file_io)
            if file_path_local:
                pass
        return True
        
    def download_file_ftp(self, local_file_path, remote_file_path):
        with ftplib.FTP(self.FTP_HOST, self.FTP_USER, self.FTP_PASS) as ftp:
            with open(local_file_path, 'wb') as file:
                ftp.retrbinary(f'RETR {remote_file_path}', file.write)

    def upload_many_ftp(self, files : Dict[str, str]):
        success_dict : dict = {}
        for k, v in files.items():
            success = self.upload_file_ftp(remote_filepath=v[0], file=v[1])
            success_dict.update({k : success})
        return success_dict
            
         

    def download_many_ftp(self):
        pass
    
