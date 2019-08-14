GATEWAY_ZARINPAL = "ZP"
GATEWAY_PECCO = "PEC"

def get_gateway_map():
    gateway_map = {
        choice.GATEWAY_ZARINPAL: apps.get_model(app_label="payment", model_name="Zarinpal"),
        choice.GATEWAY_PECCO: apps.get_model(app_label="payment", model_name="Pecco"),
    }
    
    return gateway_map
