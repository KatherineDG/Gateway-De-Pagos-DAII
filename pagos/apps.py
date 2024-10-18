from django.apps import AppConfig
from .utils.libreria_sns_client import init_sns_client, subscribe_to_topic  
from decouple import config
import threading

class PagosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pagos'

    def ready(self):
        from .consumidor_rabbitmq import escuchar_topicos
        # Suscripción a los tópicos al iniciar la aplicación
        # Credenciales de AWS SNS
        AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
        AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')
        AWS_SESSION_TOKEN = config('AWS_SESSION_TOKEN')
        AWS_DEFAULT_REGION = config('AWS_DEFAULT_REGION', default='us-east-1')
        
        sns_client = init_sns_client(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_SESSION_TOKEN, AWS_DEFAULT_REGION)

        # Suscribirse a los tópicos de reserva y backoffice
        subscribe_to_topic(sns_client, config('TOPIC_ARN_RESERVA'), 'https', 'https://ce9e-190-174-52-206.ngrok-free.app/pagos/sns-webhook/')
        subscribe_to_topic(sns_client, config('TOPIC_ARN_BACKOFFICE'), 'https', 'https://ce9e-190-174-52-206.ngrok-free.app/pagos/sns-webhook/')

        # Comprobar si el hilo ya está activo antes de iniciarlo
        if not hasattr(threading.current_thread(), 'escuchar_thread'):
            thread = threading.Thread(target=escuchar_topicos, daemon=True)
            thread.start()
            print("Hilo iniciado para escuchar tópicos de RabbitMQ")
        else:
            print("El hilo ya está activo.")