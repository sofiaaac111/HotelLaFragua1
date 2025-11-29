const API_URL = "http://localhost:8001/clientes";

export async function getClientes() {
  const res = await fetch(API_URL);
  return await res.json();
}
