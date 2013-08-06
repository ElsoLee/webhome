#!/usr/bin/env python
#
#Copyright 2013 Fivelint
#
#changhong software contest
#

import os.path
import torndb
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.autoreload

from tornado.options import define, options

define("port", default=8000, help="run on the given port", type=int)
define("mysql_host", default="127.0.0.1:3306", help="webhome database host")
define("mysql_database", default="webhome", help="webhome database name")
define("mysql_user", default="webhome", help="webhome database user")
define("mysql_password", default="webhome", help="webhome database password")



class BaseHandler(tornado.web.RequestHandler):
	@property
	def db(self):
		return self.application.db
	
	def get_current_user(self):
		user_id = self.get_secure_cookie("id")

class MainHandler(BaseHandler):
	#@tornado.web.authenticated
	def get(self):
		if not self.current_user:
			self.redirect("/login")
			return
		self.render("/register")

class LoginHandler(BaseHandler):
	def get(self):
		self.render("login.html")
	
	def post(self):
		email = self.get_argument("email")
		password = self.get_argument("password")
		user = self.db.get("SELECT * FROM users WHERE email = %s", email)
		if not user:
			self.redirect("/register")
		if user.password == password:
			self.set_secure_cookie("id",user.id)
			self.redirect("/")
		else:
			self.redirect("/login")

class LogoutHandler(BaseHandler):
	def post(self):
		self.clear_cookie("id");
		self.redirect("/login")


class RegisterHandler(BaseHandler):
	def get(self):
		self.render("register.html")



class Application(tornado.web.Application):
	def __init__(self):
		handlers = [
				(r"/", MainHandler),
				(r"/login", LoginHandler),
				(r"/logout", LogoutHandler),
				(r"/register", RegisterHandler),
		]
		settings = dict(
			template_path=os.path.join(os.path.dirname(__file__), "templates"),
			static_path=os.path.join(os.path.dirname(__file__), "static"),
			cookie_secret="k3GVtZasSKyMgy8iRgrxmU+KhncLxEcykqy3EcGJ7So=",
			login_url="/login",
			debug=True,
		)
		tornado.web.Application.__init__(self, handlers, **settings)

		#Have one global connection to webhome DB all handlers
		self.db = torndb.Connection(
			host=options.mysql_host, database=options.mysql_database,
			user=options.mysql_user, password=options.mysql_password)



def main():
	tornado.options.parse_command_line()
	http_server = tornado.httpserver.HTTPServer(Application())
	http_server.listen(options.port)
	tornado.ioloop.IOLoop.instance().start()



if __name__ == "__main__":
	main()
