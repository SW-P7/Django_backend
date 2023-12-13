import ftplib
import io
from typing import Dict
import logging

logger = logging.getLogger(__name__)
 


class FtpConn:
    FTP_HOST = "172.23.0.1"
    FTP_PORT = 21  # Default FTP port
    FTP_USER = "user"
    FTP_PASS = "pass"

    def upload_file_ftp(self, remote_filepath, file=None, file_path_local=None) -> bool:
        if file is None and file_path_local is None:
            logger.debug("No file or filepath provided")
            return False
        if file is not None and file_path_local is not None:
            logger.debug("Both file and filepath provided")
            return False
        try:
            logger.debug(remote_filepath)
            with ftplib.FTP(self.FTP_HOST, self.FTP_USER, self.FTP_PASS) as ftp:
                logger.info("Succesfully connected to FTP server")
                self.ensure_dir(ftp, remote_filepath)
                if file:
                    file_io = io.BytesIO(file.encode('utf-8') if isinstance(file, str) else file)
                    ftp.storbinary(f'STOR {remote_filepath}', file_io)
                elif file_path_local:
                    with open(file_path_local, 'rb') as file_local:
                        ftp.storbinary(f'STOR {remote_filepath}', file_local)
        except Exception as e:
            logger.debug(f"upload_file_ftp error: {str(e)}")
            return False
        logger.debug("Successfully stored file on FTP server")
        return True       
    def download_file_ftp(self, local_file_path, remote_file_path): 
        with ftplib.FTP(self.FTP_HOST, self.FTP_USER, self.FTP_PASS) as ftp:
            with open(local_file_path, 'wb') as file:
                ftp.retrbinary(f'RETR {remote_file_path}', file.write)

    def ensure_dir(self, ftp, file_path):
        """Ensure all directories in the file_path exist on the FTP server."""
        directories = file_path.split('/')
        for i in range(1, len(directories)):
            dir = '/'.join(directories[:i])
            if not dir: continue
            try:
                ftp.cwd(dir)
                logger.debug(f"Found dir {dir}")
            except ftplib.error_perm:
                ftp.mkd(dir)
                ftp.cwd(dir)
                logger.debug(f"Created dir {dir}")


    def upload_many_ftp(self, files : Dict[str, str]):
        success_dict : dict = {}
        for k, v in files.items():
            success = self.upload_file_ftp(remote_filepath=v[0], file=v[1])
            success_dict.update({k : success})
        return success_dict
            
         

    def download_many_ftp(self):
        pass
    
