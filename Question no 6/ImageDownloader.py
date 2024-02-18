import requests
import time
import ImageDownloader
import os
from concurrent.futures import ThreadPoolExecutor
from threading import Thread
from tkinter import *
from tkinter.ttk import Progressbar

class ImageDownloader(Tk):
    def __init__(self):
        super().__init__()
        self.executorService = ThreadPoolExecutor(max_workers=5)
        self.DOWNLOAD_DIRECTORY = "downloaded_file/"
        self.downloadTasks = []
        self.downloadInfoMap = {}
        self.initUI()

    def initUI(self):
        self.textField = Entry(self)
        self.textField.insert(0, "Enter Images Link")
        self.textField.pack()

        self.progress_bar = Progressbar(self, orient=HORIZONTAL, length=200, mode='determinate')
        self.progress_bar.pack()

        self.downloadbtn = Button(self, text="Download", command=self.downloadbtnClicked)
        self.downloadbtn.pack()

        self.cancelbtn = Button(self, text="Cancel", command=self.cancelbtnClicked)
        self.cancelbtn.pack()

        self.pausebtn = Button(self, text="Pause", command=self.pausebtnClicked)
        self.pausebtn.pack()

        self.resumebth = Button(self, text="Resume", command=self.resumebthClicked)
        self.resumebth.pack()

    def downloadbtnClicked(self):
        urlsText = self.textField.get()
        urls = urlsText.split("[,\\s]+")
        for url in urls:
            if url:
                self.downloadImage(url)

    def pausebtnClicked(self):
        self.pauseDownloads()

    def cancelbtnClicked(self):
        self.cancelDownloads()

    def resumebthClicked(self):
        self.resumeDownloads()

    def downloadImage(self, urlString):
        def downloadTask():
            downloadInfo = self.downloadInfoMap.get(Thread.current_thread())
            progress = downloadInfo.progress if downloadInfo else 0
            try:
                response = requests.get(urlString, stream=True, headers={"User-Agent": "Mozilla/5.0"})
                if response.status_code == 200 or response.status_code == 206:
                    contentLength = int(response.headers.get('content-length'))
                    fileName = "image_" + str(int(time.time())) + ".jpg"
                    fullPath = os.path.join(self.DOWNLOAD_DIRECTORY, fileName)
                    with open(fullPath, 'wb') as file:
                        for chunk in response.iter_content(chunk_size=1024):
                            file.write(chunk)
                            progress += len(chunk)
                            currentProgress = int((progress / contentLength) * 100)
                            self.progress_bar['value'] = currentProgress
                            self.update_idletasks()
                            if Thread.current_thread().is_interrupted():
                                raise Exception("Download interrupted")
                            time.sleep(0.05)
                else:
                    raise Exception("Failed to download image. Response code: " + str(response.status_code))
            except Exception as e:
                if isinstance(e, KeyboardInterrupt):
                    Thread.current_thread().interrupt()
                if not isinstance(e, KeyboardInterrupt):
                    print(e)

        task = self.executorService.submit(downloadTask)
        self.downloadTasks.append(task)
        self.downloadInfoMap[task] = downloadInfo(urlString, 0)

    def saveImage(self, imageData, fileName):
        directory = os.path.join(os.getcwd(), self.DOWNLOAD_DIRECTORY)
        if not os.path.exists(directory):
            os.makedirs(directory)
        fullPath = os.path.join(directory, fileName)
        with open(fullPath, 'wb') as file:
            file.write(imageData)

    def resumeDownloads(self):
        for task in self.downloadTasks:
            if task.cancelled():
                downloadInfo = self.downloadInfoMap.get(task)
                if downloadInfo:
                    self.downloadImage(downloadInfo.url)

    def pauseDownloads(self):
        for task in self.downloadTasks:
            if not task.done() and not task.cancelled():
                task.cancel()

    def cancelDownloads(self):
        for task in self.downloadTasks:
            task.cancel()
        self.progress_bar['value'] = 0

    class DownloadInfo:
        def __init__(self, url, progress):
            self.url = url
            self.progress = progress

if __name__ == '__main__':
    app = ImageDownloader()
    app.mainloop()


