from google import genai
client = genai.Client(api_key="AIzaSyBTesu_2fD8vGDREdzJvtEJHbo9dgMxU4o")

print("Modelos disponíveis para a tua chave:")
for model in client.models.list():
    print(f" - {model.name}")