import { useEffect, useState } from "react";
import { getClientes } from "../services/clientesService";

export default function Clientes() {
  const [clientes, setClientes] = useState([]);

  useEffect(() => {
    getClientes().then(data => setClientes(data));
  }, []);

  return (
    <div className="p-10">
      <h1 className="text-3xl font-bold mb-6">Gestión de Clientes</h1>

      {clientes.length === 0 ? (
        <p>No hay clientes registrados.</p>
      ) : (
        <ul className="list-disc pl-5">
          {clientes.map(c => (
            <li key={c.id}>
              {c.nombre} – {c.documento}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}
