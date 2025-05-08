user_states = {}


ACCOMMODATION = [
    {
        "id": 1,
        "name": "Hotel Playa Bonita",
        "city": "Cartagena",
    },
    {
        "id": 2,
        "name": "Glamping Montaña Mágica",
        "city": "Medellín",
    },
    {
        "id": 3,
        "name": "Camping Aventura Verde",
        "city": "Cali",
    },
]


def proccess_message(text: str, phone: str) -> str:
    print("PROCESS MESSAGE")
    user_state = user_states.get(phone, {})

    if "step" not in user_state:
        user_state["step"] = 1
        user_states[phone] = user_state
        return "Hola para ayudarte con tu reserva, dime ¿a qué ciudad deseas viajar?"
    elif user_state["step"] == 1:
        user_state["destino"] = text
        user_state["step"] = 2
        return "Perfecto, ¿Para qué fechas estás buscando alojamiento?"
    elif user_state["step"] == 2:
        user_state["fechas"] = text
        user_state["step"] = 3
        return "¿Cuántas personas viajarán?"

    return "No entendí. Por favor intenta de nuevo."
