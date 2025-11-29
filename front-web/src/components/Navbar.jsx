export default function Navbar() {
  return (
    <nav className="bg-white shadow-md fixed w-full top-0 z-50">
      <div className="max-w-6xl mx-auto px-6 py-4 flex justify-between items-center">
        <h1 className="text-xl font-bold text-primary">Hotel La Fragua</h1>

        <div className="space-x-6 hidden md:flex">
          <a href="#" className="text-gray-700 hover:text-primary">Inicio</a>
          <a href="#" className="text-gray-700 hover:text-primary">Clientes</a>
          <a href="#" className="text-gray-700 hover:text-primary">Habitaciones</a>
        </div>

        <button className="bg-primary text-white px-4 py-2 rounded-lg hover:bg-blue-900">
          Iniciar Sesión
        </button>
      </div>
    </nav>
  );
}
