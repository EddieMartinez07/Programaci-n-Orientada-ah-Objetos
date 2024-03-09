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
