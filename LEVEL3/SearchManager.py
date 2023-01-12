from FileSearcher import FileSearcher
from threading import Thread
class SearchManager:
    def __init__(self):
        pass
    def search(self,file_name,drives):
        print("This is a search method of search manager")
        search_thread=[]
        file_searchers=[]
        for drive in drives:
            print(drive)
            file_searcher = FileSearcher()
            file_searcher.search_for_file(drive, file_name)
            search_threads = Thread()
            search_threads.start()
            file_searchers.append(file_searcher)
            search_thread.append(search_thread)
            # 5. Iterate through all the threads and join the threads

        for search_thread in search_thread:
            search_threads.join()
        # 6. Iterate through the file searchers and get the results
        search_results = []
        for file_searcher in file_searchers:
            search_results.append(file_searcher.file_name)
        return search_results
if __name__=='__main__':
    obj=SearchManager()
    print(obj.search("program1.txt","c"))
