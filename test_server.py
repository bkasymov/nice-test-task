import unittest
import threading
import requests
import time
import server


class TestHTTPServer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server_thread = threading.Thread(target=server.run_server)
        cls.server_thread.daemon = True
        cls.server_thread.start()
        time.sleep(1)

    def test_get_request(self):
        response = requests.get(f"http://localhost:{server.PORT}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, "Hello from PSPDFKit Engineer!")


if __name__ == "__main__":
    unittest.main()
