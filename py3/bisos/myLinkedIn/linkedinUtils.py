import csv
import logging
from pathlib import Path
import zipfile
import vobject
from typing import Optional, List, Dict



logger = logging.getLogger(__name__)

class LinkedinId:
    """
    Utility functions for handling LinkedinId
    """

    @staticmethod
    def fromUrl(url: str) -> str:
        """
        Extract the LinkedIn ID from the profile URL.
        """
        parts = url.rstrip('/').split('/')
        return parts[-1]

    @staticmethod
    def fromStr(vcard_dir: Path, uid: str) -> Optional[Path]:
        """
        Find the vCard file corresponding to the LinkedIn ID (UID) in the directory.
        """
        vcard_path = vcard_dir / f"{uid}.vcf"
        if vcard_path.exists():
            return vcard_path
        return None


    @staticmethod
    def fromPath(vcard_dir: Path, uid: str) -> Optional[Path]:
        """
        Find the vCard file corresponding to the LinkedIn ID (UID) in the directory.
        """
        vcard_path = vcard_dir / f"{uid}.vcf"
        if vcard_path.exists():
            return vcard_path
        return None


    @staticmethod
    def canonical(inStr: str) -> str:
        """
        Determine the canonical form of a LinkedIn identifier.

        This method checks the input string to determine if it is a URL, a file path,
        or a LinkedIn ID. It returns the LinkedIn ID in a canonical form based on the input type.

        - If the input is a URL, it extracts the LinkedIn ID using the fromUrl method.
        - If the input is a file path ending with '.vcf', it returns the file name without the extension.
        - If the input is a plain string, it assumes it is a LinkedIn ID and returns it as is.

        Args:
            inStr (str): The input string to be canonicalized.

        Returns:
            str: The canonical LinkedIn ID.
        """
        from urllib.parse import urlparse

        # Check if the input is a URL
        try:
            result = urlparse(inStr)
            if all([result.scheme, result.netloc]):
                return LinkedinId.fromUrl(inStr)
        except Exception:
            pass

        # Check if the input is a file path
        path = Path(inStr)
        if path.suffix == '.vcf':
            return path.stem

        # Otherwise, assume it's a LinkedIn ID
        return inStr


class VCard:
    """
    Utility functions for handling vCards and LinkedIn data files.
    """

    @staticmethod
    def get_linkedin_id(url: str) -> str:
        """
        Extract the LinkedIn ID from the profile URL.
        """
        return url.split('/')[-2]

    @staticmethod
    def read_csv(file_path: Path) -> List[Dict[str, str]]:
        """
        Read a CSV file and return the rows as a list of dictionaries.
        """
        if not file_path.exists():
            raise FileNotFoundError(f"{file_path} does not exist.")

        with file_path.open('r', encoding='utf-8') as f:
            return list(csv.DictReader(f))

    @staticmethod
    def write_vcard(vcard, vcard_path: Path) -> None:
        """
        Write the vCard object to a file.
        """
        with vcard_path.open('w', encoding='utf-8') as vcard_file:
            vcard_file.write(vcard.serialize())

    @staticmethod
    def read_vcard(vcard_path: Path):
        """
        Read a vCard from a file and return the vCard object.
        """
        with vcard_path.open('r', encoding='utf-8') as vcard_file:
            return vobject.readOne(vcard_file.read())

    @staticmethod
    def find_vcard(vcard_dir: Path, uid: str) -> Optional[Path]:
        """
        Find the vCard file corresponding to the LinkedIn ID (UID) in the directory.
        """
        vcard_path = vcard_dir / f"{uid}.vcf"
        if vcard_path.exists():
            return vcard_path
        return None

    
class Common:

    @staticmethod
    def unzip_file(zip_path: Path, extract_to: Path) -> None:
        """Unzips a .zip file to the specified directory using pathlib.
        Use it like so: unzip_file(Path("LinkedInDataExport.zip"), Path("unzipped"))
        """
        logger.info(f"Unzipping {zip_path} to {extract_to}")
        extract_to.mkdir(parents=True, exist_ok=True)
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_to)
