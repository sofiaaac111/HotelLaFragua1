import { useNavigate } from "react-router-dom";

export default function Home() {
  const navigate = useNavigate();

  return (
    <div className="min-h-screen bg-gray-100 p-10">

      <h1 className="text-4xl font-bold mb-6 text-center">Hotel La Fragua</h1>

      <nav className="flex justify-center gap-10 mb-10 text-lg font-semibold">
        <button onClick={() => navigate("/")} className="hover:underline">Inicio</button>
        <button onClick={() => navigate("/clientes")} className="hover:underline">Clientes</button>
        <button onClick={() => navigate("/habitaciones")} className="hover:underline">Habitaciones</button>
        <button onClick={() => navigate("/reservas")} className="hover:underline">Reservas</button>

        <button className="bg-blue-600 text-white px-4 py-1 rounded ml-6">
          Iniciar Sesión
        </button>
      </nav>

      <h2 className="text-3xl font-semibold text-center mb-8">
        Administración del Hotel
      </h2>

      <p className="text-center mb-10 text-gray-700">
        Controla los clientes, habitaciones y reservas del Hotel La Fragua.
      </p>

      <div className="flex justify-center mb-16">
        <button
          onClick={() => navigate("/clientes")}
          className="bg-blue-700 text-white px-8 py-3 rounded-lg text-xl"
        >
          Comenzar ahora
        </button>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-10">
        <div className="bg-white p-6 rounded-lg shadow">
          <h3 className="text-2xl font-semibold mb-3">Gestión de Clientes</h3>
          <p className="mb-4">Agrega, consulta, actualiza o elimina clientes.</p>
          <button
            onClick={() => navigate("/clientes")}
            className="bg-gray-800 text-white px-4 py-2 rounded"
          >
            Ver clientes
          </button>
        </div>

        <div className="bg-white p-6 rounded-lg shadow">
          <h3 className="text-2xl font-semibold mb-3">Habitaciones</h3>
          <p className="mb-4">Consulta disponibilidad y administra habitaciones.</p>
          <button
            onClick={() => navigate("/habitaciones")}
            className="bg-gray-800 text-white px-4 py-2 rounded"
          >
            Gestionar habitaciones
          </button>
        </div>

        <div className="bg-white p-6 rounded-lg shadow">
          <h3 className="text-2xl font-semibold mb-3">Reservas</h3>
          <p className="mb-4">Control de reservas activas del hotel.</p>
          <button
            onClick={() => navigate("/reservas")}
            className="bg-gray-800 text-white px-4 py-2 rounded"
          >
            Administrar reservas
          </button>
        </div>
      </div>

    </div>
  );
}
