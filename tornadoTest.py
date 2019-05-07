import tornado.web
import tornado.ioloop
import tornado.httpserver

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("coooooooool")

if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/", IndexHandler)
    ])

    httpServer = tornado.httpserver.HTTPServer(app)
    httpServer.listen(8000)

    tornado.ioloop.IOLoop.current().start()
