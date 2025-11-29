const API_URL = "http://localhost:8002/habitaciones";

export async function getHabitaciones() {
  const res = await fetch(API_URL);
  return await res.json();
}
