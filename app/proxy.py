from flask import Blueprint, request, Response

proxy_bp = Blueprint('proxy', __name__)

@proxy_bp.route('/forward', methods=['POST'])
def forward_proxy():
    # Aquí podrías manejar las peticiones que se envían a WhatsApp
        data = request.get_json()
            
                # Lógica de proxy para redirigir la solicitud a otro servidor
                    # Por ejemplo, reenviar a un servidor proxy que maneje el tráfico a WhatsApp.
                        
                            return Response("Request forwarded", status=200)

                                                                                                         