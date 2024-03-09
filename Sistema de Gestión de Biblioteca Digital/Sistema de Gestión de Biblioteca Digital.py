class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.titulo_autor = (titulo, autor)
        self.categoria = categoria
        self.isbn = isbn

class Usuario:
    def __init__(self, nombre, usuario_id):
        self.nombre = nombre
        self.usuario_id = usuario_id
        self.libros_prestados = []

class Biblioteca:
    def __init__(self):
        self.libros_disponibles = {}
        self.usuarios_registrados = set()

    def agregar_libro(self, libro):
        self.libros_disponibles[libro.isbn] = libro

    def quitar_libro(self, isbn):
        if isbn in self.libros_disponibles:
            del self.libros_disponibles[isbn]

    def registrar_usuario(self, usuario):
        self.usuarios_registrados.add(usuario.usuario_id)

    def dar_de_baja_usuario(self, usuario_id):
        if usuario_id in self.usuarios_registrados:
            self.usuarios_registrados.remove(usuario_id)

    def prestar_libro(self, usuario_id, isbn):
        if usuario_id in self.usuarios_registrados and isbn in self.libros_disponibles:
            libro = self.libros_disponibles[isbn]
            usuario = next((u for u in self.usuarios_registrados if u.usuario_id == usuario_id), None)
            if usuario:
                usuario.libros_prestados.append(libro)
                del self.libros_disponibles[isbn]
                print(f"El libro '{libro.titulo_autor[0]}' ha sido prestado a {usuario.nombre}.")
            else:
                print("Usuario no encontrado.")
        else:
            print("Usuario o libro no encontrados.")

    def devolver_libro(self, usuario_id, isbn):
        usuario = next((u for u in self.usuarios_registrados if u.usuario_id == usuario_id), None)
        if usuario:
            for libro in usuario.libros_prestados:
                if libro.isbn == isbn:
                    self.libros_disponibles[isbn] = libro
                    usuario.libros_prestados.remove(libro)
                    print(f"El libro '{libro.titulo_autor[0]}' ha sido devuelto por {usuario.nombre}.")
                    return
            print("Libro no encontrado en los préstamos del usuario.")
        else:
            print("Usuario no encontrado.")

    def buscar_libro_por_titulo(self, titulo):
        libros_encontrados = [libro for libro in self.libros_disponibles.values() if libro.titulo_autor[0].lower() == titulo.lower()]
        return libros_encontrados

    def buscar_libro_por_autor(self, autor):
        libros_encontrados = [libro for libro in self.libros_disponibles.values() if libro.titulo_autor[1].lower() == autor.lower()]
        return libros_encontrados

    def buscar_libro_por_categoria(self, categoria):
        libros_encontrados = [libro for libro in self.libros_disponibles.values() if libro.categoria.lower() == categoria.lower()]
        return libros_encontrados

    def listar_libros_prestados_a_usuario(self, usuario_id):
        usuario = next((u for u in self.usuarios_registrados if u.usuario_id == usuario_id), None)
        if usuario:
            if usuario.libros_prestados:
                print(f"Libros prestados a {usuario.nombre}:")
                for libro in usuario.libros_prestados:
                    print(f"- '{libro.titulo_autor[0]}' por {libro.titulo_autor[1]}")
            else:
                print(f"No hay libros prestados a {usuario.nombre}.")
        else:
            print("Usuario no encontrado.")
# Crear instancia de la biblioteca
biblioteca = Biblioteca()

# Crear algunos libros y usuarios
libro1 = Libro("Python Programming", "John Smith", "Programming", "123456789")
libro2 = Libro("The Great Gatsby", "F. Scott Fitzgerald", "Fiction", "987654321")
usuario1 = Usuario("Alice", 1)
usuario2 = Usuario("Bob", 2)

# Agregar libros a la biblioteca
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)

# Registrar usuarios
biblioteca.registrar_usuario(usuario1)
biblioteca.registrar_usuario(usuario2)

# Prestar un libro a un usuario
biblioteca.prestar_libro(1, "123456789")

# Devolver un libro
biblioteca.devolver_libro(1, "123456789")

# Buscar libros por título
libros_encontrados = biblioteca.buscar_libro_por_titulo("Python Programming")
for libro in libros_encontrados:
    print(libro.titulo_autor[0])

# Listar libros prestados a un usuario
biblioteca.listar_libros_prestados_a_usuario(1)