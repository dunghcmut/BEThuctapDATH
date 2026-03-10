class AIModel:
    @staticmethod
    def predict(value):
        numeric_value = float(value)
        status = "WARNING" if numeric_value > 5 else "NORMAL"
        return {
            "value": AIModel._serialize_value(numeric_value),
            "status": status,
        }

    @staticmethod
    def _serialize_value(value):
        return int(value) if float(value).is_integer() else value
