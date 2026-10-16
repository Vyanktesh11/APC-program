from abc import ABC, abstractmethod

class CloudStorage(ABC):
    @abstractmethod
    def upload_file(self, filename):
        pass

    @abstractmethod
    def download_file(self, filename):
        pass

    @abstractmethod
    def delete_file(self, filename):
        pass

class GoogleDrive(CloudStorage):
    def upload_file(self, filename):
        print("Uploaded to Google Drive:", filename)
    def download_file(self, filename):
        print("Downloaded from Google Drive:", filename)
    def delete_file(self, filename):
        print("Deleted from Google Drive:", filename)

class OneDrive(CloudStorage):
    def upload_file(self, filename):
        print("Uploaded to OneDrive:", filename)
    def download_file(self, filename):
        print("Downloaded from OneDrive:", filename)
    def delete_file(self, filename):
        print("Deleted from OneDrive:", filename)

storage = GoogleDrive()
storage.upload_file("notes.pdf")
storage.download_file("notes.pdf")
storage.delete_file("notes.pdf")
