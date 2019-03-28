class NetworkRequests:
    def __init__(self, parser, tracker_list):
        self.parser = parser
        self.tracker_list = tracker_list

    def fetch_conditions(self):
        """This function fetches the predefined  conditions from config file"""
        self.EC1 = self.parser.get('Expected_network_requests', 'network_request1')
        self.EC2 = self.parser.get('Expected_network_requests', 'network_request2')
        self.EC3 = self.parser.get('Expected_network_requests', 'network_request3')

    def network_request_counter(self):
        """This function validates the expected requests against the actual requests list"""

        # Assign fail status to all expected network requests initially
        self.wikipedia_ico = "FAIL"
        self.Wikipedia_logo_v2 = "FAIL"
        self.Wikinews_logo_sister = "FAIL"

        print(self.EC1)
        print(self.EC2)
        print(self.EC3)

        for  self.tracker in self.tracker_list:
            if ( self.tracker["name"].find(self.EC1) != -1):
                print( self.tracker["name"])
                self.wikipedia_ico = "PASS"

            elif ( self.tracker["name"].find(self.EC2) != -1):
                print( self.tracker["name"])
                self.Wikipedia_logo_v2 = "PASS"

            elif ( self.tracker["name"].find(self.EC3) != -1):
                print( self.tracker["name"])
                self.Wikinews_logo_sister = "PASS"

        result = []
        result.extend((self.wikipedia_ico,self.Wikipedia_logo_v2,self.Wikinews_logo_sister))
        print(result)
        return result
