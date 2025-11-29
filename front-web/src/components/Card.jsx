export default function Card({ title, description, btnText }) {
  return (
    <div className="bg-white shadow-md rounded-xl p-6 text-center hover:shadow-lg transition">
      <h3 className="text-xl font-bold mb-2 text-primary">{title}</h3>
      <p className="text-gray-600 mb-4">{description}</p>
      <button className="bg-primary text-white px-4 py-2 rounded-lg hover:bg-blue-900">
        {btnText}
      </button>
    </div>
  );
}
