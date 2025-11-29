export default function Hero() {
  return (
    <section className="pt-32 text-center pb-20 bg-gradient-to-r from-primary to-secondary text-white">
      <h2 className="text-4xl font-bold">Administración del Hotel</h2>
      <p className="mt-4 text-lg opacity-90 max-w-2xl mx-auto">
        Controla los clientes, habitaciones y reservas del Hotel La Fragua de manera rápida y eficiente.
      </p>

      <button className="mt-6 bg-white text-primary px-6 py-3 rounded-lg font-semibold hover:bg-gray-200">
        Comenzar ahora
      </button>
    </section>
  );
}
