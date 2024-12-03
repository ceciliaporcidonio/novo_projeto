import asyncio
from django.http import JsonResponse

# View assíncrona com contador de tempo
async def async_counter(request):
    result = []
    for i in range(10):  # Contador de 0 a 9
        await asyncio.sleep(1)  # Pausa de 1 segundo
        result.append(f"Contando: {i}")
    return JsonResponse({"message": "Contador finalizado!", "steps": result})

