from engine.IEngine import IEngine


class SternmanEngine(IEngine):

    def __init__(self, last_service_date, warning_light_on):
        super().__init__(last_service_date)
        self.warning_light_on = warning_light_on

    def needs_service(self):
        if type(self.warning_light_on) != bool:
            raise ValueError('Warning light on should be a boolean')
        return self.warning_light_on
