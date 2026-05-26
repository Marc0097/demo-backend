# 🎬 Guion de Grabación de la Demo del Agente de IA

¡Bienvenido de nuevo! Todo el entorno está preparado y congelado en el tiempo para que grabes tu demostración a la perfección.

## 🛠️ 1. Preparación de Pantallas
Divide tu pantalla en dos mitades:
- **Mitad izquierda:** Una terminal de PowerShell (o CMD) abierta en esta misma carpeta (`C:\Users\marcn\DEMO\DEMO`).
- **Mitad derecha:** Tu navegador web de confianza vacío.

## 🎥 2. ¡Acción! Empieza el vídeo mostrando el "Bug"
1. En tu terminal, arranca el servidor local escribiendo el siguiente comando y pulsando Enter:
   ```powershell
   uvicorn main:app --reload
   ```
2. Vete a tu navegador y pega esta URL para hacer una petición a la API:
   `http://127.0.0.1:8000/api/reservas?estado=activa`
3. **Explica a tu audiencia el problema:** *"Fijaos en esto, he pedido solo las reservas 'activas' pero el sistema me devuelve una lista kilométrica que incluye reservas canceladas. Además, los ingresos totales están completamente disparados porque suma todo. Hay un fallo grave de filtrado en el código."*

## 🤖 3. Llama a la Inteligencia Artificial al rescate
1. **Sin cerrar la terminal del servidor**, abre una **nueva pestaña** o una **nueva ventana** de PowerShell y vete a esta misma carpeta (`cd C:\Users\marcn\DEMO\DEMO`).
2. **Explica a la cámara:** *"En vez de meterme yo a rebuscar y arreglar el código a mano, le voy a pasar este archivo de texto (issue.txt) con las instrucciones a nuestro Agente Inteligente, para que él mismo detecte el fallo, lo programe y lo suba a GitHub sin mi ayuda."*
3. Pega este comando en la nueva terminal y dale a Enter:
   ```powershell
   mini -c windows.yaml -m "github/gpt-4o-mini" -t (Get-Content "issue.txt" -Raw) -y
   ```
4. Deja que la cámara grabe la "magia". Verás a la IA pensando, leyendo los archivos, modificando el código de `main.py` y haciendo los comandos de git para subirlo a producción. Comenta lo que ves en pantalla para rellenar los 30 segunditos que suele tardar.

## ✨ 4. El "Efecto WOW" (La Solución)
1. Cuando la terminal de la IA termine por completo (pondrá `COMPLETE_TASK_AND_SUBMIT_FINAL_OUTPUT` y volverá a salir la ruta normal de Windows), vete corriendo a tu navegador.
2. **Dile a tu audiencia:** *"Como el servidor detecta los cambios en el código al instante gracias al flag --reload, vamos a ver si la IA lo ha conseguido arreglar en vivo."*
3. **Pulsa F5** o el botón de refrescar página en el navegador.
4. **¡BUM!** Verás que la lista kilométrica se encoge de repente mostrando **solo** las reservas "activas" y los ingresos totales se habrán recalculado a la perfección.
5. Cierra tu vídeo: *"¡Bug arreglado en el código y subido automáticamente a producción por una IA autónoma en un abrir y cerrar de ojos!"*

---
### 🔄 ¿Qué pasa si quiero repetir la toma y volver a grabarlo?
Si te has equivocado grabando y quieres volver a empezar el vídeo, no pasa nada. Solo tienes que resetear el repositorio para que el bug y los archivos vuelvan al estado original inicial que tenemos ahora mismo.
Para resetear, abre una terminal en esta carpeta y lanza estos comandos, uno a uno:

```powershell
git fetch origin
git reset --hard origin/main
```
Esto descargará la versión original y borrará las correcciones que haya hecho la IA. ¡Listo para volver a grabar la Toma 2!
