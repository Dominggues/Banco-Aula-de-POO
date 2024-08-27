import sqlite3

class BancoDeDados:
	"""Classe que representa o banco de dados (database) da aplicação"""

	def __init__(self, nome='banco.db'):
		self.nome, self.conexao = nome, None

	def conecta(self):
		"""Conecta passando o nome do arquivo"""
		self.conexao = sqlite3.connect(self.nome)

	def desconecta(self):
		"""Desconecta do banco"""
		try:
			self.conexao.close()
		except AttributeError:
			pass

	def criar_tabelas(self):
		try:
			cursor = self.conexao.cursor()

			cursor.execute("""
			CREATE TABLE IF NOT EXISTS clientes (
				id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
				nome TEXT NOT NULL,
				senha VARCHAR(20) NOT NULL,
				cpf VARCHAR(11) UNIQUE NOT NULL,
				email TEXT NOT NULL
			);
			""")

		except AttributeError:
			print("Faca a conexão do banco antes de criar as tabelas")


	def inserir_cliente(self, nome, senha, cpf, email):
		"""Insere cliente no banco"""
		try:
			cursor = self.conexao.cursor()

			try:
				cursor.execute("""
					INSERT INTO clientes (nome, senha, cpf, email) VALUES (?,?,?,?)
				""",(nome, senha, cpf, email))
			except sqlite3.IntegrityError:
				print("O cpf %s já existe" % cpf)

			self.conexao.commit()

		except AttributeError:
			print("Faça a conexão com banco antes de inserir clientes")


	def buscar_cliente(self, cpf):
		"""Busca um cliente pelo cpf"""
		try:
			cursor = self.conexao.cursor()

			#obtém todos os dados
			cursor.execute("SELECT * FROM clientes WHERE cpf=?", [(cpf)])

			#print(cursor.fetchone())
			cliente = cursor.fetchone()

			if cliente:
				print("Cliente %s encontrado" % cliente[1])
				return True
			else: 
       			 print("cliente não encontrado")
			"""
				for linha in cursor.fetchall():
				if linha[2] == cpf:
					print("Cliente %s encontrado" % linha[1])
					break
			"""
		except AttributeError:
			print("Faça a conexão do banco antes de buscar clintes")

	def buscar_email(self, email):
		try:
			cursor = self.conexao.cursor()

			# obtém todos os dados
			cursor.execute("""SELECT * FROM clientes;""")

			for linha in cursor.fetchall():
				if linha[4] == email:
					print("Email %s encontrado" % linha[4])
					break
		except AttributeError:
			print("Faça a conexão do banco antes de buscar clintes")

	def login(self, username, senha):
		try:
			cursor = self.conexao.cursor()
			sql = "SELECT * FROM clientes WHERE nome=? and senha=?"
			cliente = cursor.execute(sql, [username, senha]).fetchone()
			if cliente:
				return True
			return False
		except AttributeError:
			print("Faça a nonexão coom o banco")

	def remover_cliente(self, cpf):
		try:
			cursor = self.conexao.cursor()

			# exclui todos os dados
			cursor.execute("""DELETE FROM clientes
				WHERE cpf = ?
				""", (cpf,))

		except AttributeError:
			print("Faça a conexão do banco antes de buscar clintes")


		self.conexao.commit()