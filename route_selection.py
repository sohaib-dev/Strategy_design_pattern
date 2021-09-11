from transport import *


class RouteSelection:

    def __init__(self, transport):
        """self._transport references the objects of other transport classes. Its called composition."""
        self._transport = transport

    def time_estimation(self, distance):
        """Call the operation's function from referenced instance variable."""
        return self._transport.operation(distance)


if __name__ == '__main__':

    public_transport = PublicTransport()
    route_selection = RouteSelection(public_transport)
    print('Estimated time to reach destination: ', route_selection.time_estimation(60))

    car = Car()
    route_selection = RouteSelection(car)
    print('Estimated time to reach destination: ', route_selection.time_estimation(60))

    bike = Bike()
    route_selection = RouteSelection(bike)
    print('Estimated time to reach destination: ', route_selection.time_estimation(60))

