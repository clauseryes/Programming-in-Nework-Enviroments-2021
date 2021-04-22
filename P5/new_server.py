import http.server
import socketserver
import termcolor
import pathlib
import jinja2

def read_html_file(filename):
    content = pathlib.Path(filename).read_text()
    return content

def read_template_html_file(filename):
    content = jinja2.Template(pathlib.Path(filename).read_text())
    return content

PORT = 8080

BASES_INFORMATION = {
    "A": {"link": "https://en.wikipedia.org/wiki/Adenine",
          "formula": "C5H5N5",
          "name": "ADENINE",
          "color": "lightgreen"
    },
    "C": {"link": "https://en.wikipedia.org/wiki/Cytosine",
          "formula": "C4H5N3O",
          "name": "CYTOSINE",
          "color": "yellow"
          },
    "G": {"link": "https://en.wikipedia.org/wiki/Guanine",
          "formula": "C5H5N5O",
          "name": "GUANINE",
          "color": "lightskyblue"
          },
    "T": {"link": "https://en.wikipedia.org/wiki/Thymine",
          "formula": "C5H6N2O2",
          "name": "THYMINE",
          "color": "lightpink"
          }
}

class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

        termcolor.cprint(self.requestline, 'green')
        termcolor.cprint(self.path, 'blue')

        if self.path == "/":
            contents = read_html_file('./html/index.html')
        elif '/info/' in self.path:
            base = self.path.split('/')[-1]
            context = BASES_INFORMATION[base]
            context["letter"] = base
            contents = read_template_html_file('./html/info/general.html').render(base_information=context)
        elif self.path.endswith('.html'):
            try:
                contents = read_html_file("./html" + self.path)
            except FileNotFoundError:
                contents = read_html_file('./html/error.html')
        else:
            contents = read_html_file('./html/error.html')

        self.send_response(200)

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(contents.encode()))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(contents.encode())

        return


Handler = TestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()