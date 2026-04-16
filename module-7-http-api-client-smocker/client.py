import time

import httpx
from config import BASE_URL, MAX_RETRIES, RETRY_DELAY, TIMEOUT


class APIClient:
    def __init__(self):
        self.client = httpx.Client(base_url=BASE_URL, timeout=TIMEOUT)

    # ---------------------------
    # GET simple con manejo error
    # ---------------------------
    def get_users(self):
        try:
            response = self.client.get("/users")
            response.raise_for_status()
            return response.json()

        except httpx.RequestError as e:
            print(f"[ERROR] Conexión: {e}")

        except httpx.HTTPStatusError as e:
            print(f"[ERROR] HTTP {e.response.status_code}")

    # ---------------------------
    # GET con retries (resiliencia)
    # ---------------------------
    def get_users_with_retry(self):
        for attempt in range(1, MAX_RETRIES + 1):
            try:
                response = self.client.get("/users")
                response.raise_for_status()
                return response.json()

            except Exception as e:
                print(f"[Retry {attempt}] fallo: {e}")

                if attempt < MAX_RETRIES:
                    time.sleep(RETRY_DELAY * attempt)  # backoff simple
                else:
                    print("❌ Todos los intentos fallaron")
                    raise

    # ---------------------------
    # Streaming (descarga a disco)
    # ---------------------------
    def download_users_stream(self, output_file="users.json"):
        try:
            with self.client.stream("GET", "/users") as response:
                response.raise_for_status()

                with open(output_file, "wb") as f:
                    for chunk in response.iter_bytes():
                        f.write(chunk)

            print("✅ Archivo descargado por streaming")

        except Exception as e:
            print(f"[ERROR] Streaming: {e}")

    # ---------------------------
    # Cerrar cliente
    # ---------------------------
    def close(self):
        self.client.close()


# ---------------------------------
# ASYNC (extra / pro)
# ---------------------------------
async def get_users_async():
    async with httpx.AsyncClient(
        base_url=BASE_URL, timeout=TIMEOUT, http2=True  # http2 activado
    ) as client:
        response = await client.get("/users")
        response.raise_for_status()
        return response.json()
