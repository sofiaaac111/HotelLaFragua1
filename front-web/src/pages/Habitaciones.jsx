import { useEffect, useState } from "react";
import { getHabitaciones } from "../services/habitacionesService";

export default function Habitaciones() {
  const [habitaciones, setHabitaciones] = useState([]);

  useEffect(() => {
    getHabitaciones().then(data => setHabitaciones(data));
  }, []);

  return (
    <div className="p-10">
      <h1 className="text-3xl font-bold mb-6">Gestión de Habitaciones</h1>

      {habitaciones.length === 0 ? (
        <p>No hay habitaciones registradas.</p>
      ) : (
        <ul className="list-disc pl-5">
          {habitaciones.map(h => (
            <li key={h.id}>
              Habitación {h.numero} – {h.tipo}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}
