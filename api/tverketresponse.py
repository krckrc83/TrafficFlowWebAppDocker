""" This Class will help with a parser frame and sql pre formatted queries """


class TrafficFlowResponse:

    sql = "INSERT INTO trafficflow (flow, speed, time) VALUES (%s, %s, %s)"
    sql_duplicate = 'DELETE t1 FROM trafficflow t1 INNER JOIN trafficflow t2 WHERE t1.id < t2.id AND t1.time = t2.time'

    def __init__(self, json_response):
        self.flow = json_response['RESPONSE']['RESULT'][0]['TrafficFlow'][0]['VehicleFlowRate']
        self.speed = json_response['RESPONSE']['RESULT'][0]['TrafficFlow'][0]['AverageVehicleSpeed']
        self.time = json_response['RESPONSE']['RESULT'][0]['TrafficFlow'][0]['MeasurementTime']
        self.values = (self.flow, self.speed, self.time)
