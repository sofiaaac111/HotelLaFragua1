import Navbar from "./components/Navbar";
import Hero from "./components/Hero";
import Card from "./components/Card";

export default function App() {
  return (
    <>
      <Navbar />
      <Hero />

      <div className="max-w-6xl mx-auto py-10 grid grid-cols-1 md:grid-cols-3 gap-8 px-6">
        
        <Card
          title="Gestión de Clientes"
          description="Agrega, consulta, actualiza o elimina clientes del sistema."
          btnText="Ver clientes"
        />

        <Card
          title="Habitaciones"
          description="Revisa disponibilidad y administra las habitaciones del hotel."
          btnText="Gestionar habitaciones"
        />

        <Card
          title="Reservas"
          description="Control de reservas activas y próximas estadías."
          btnText="Administrar reservas"
        />

      </div>
    </>
  );
}
