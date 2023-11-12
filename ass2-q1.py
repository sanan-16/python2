import queue
import time


class WebServer:
    def _init_(self):
        self.request_queue = queue.Queue()

    def add_request(self, request):
        print(f"Incoming request {request['type']} with processing time {request['processing_time']} seconds.")
        self.request_queue.put(request)

    def process_requests(self):
        while not self.request_queue.empty():
            request = self.request_queue.get()
            print(f"Processing {request['type']} request...")
            time.sleep(request['processing_time'])
            print(f"{request['type']} request processed.")


web_server = WebServer()

# Simulate incoming requests
requests = [
    {'type': 'A', 'processing_time': 3},
    {'type': 'B', 'processing_time': 5},
    {'type': 'C', 'processing_time': 2},
]

for request in requests:
    web_server.add_request(request)

web_server.process_requests()