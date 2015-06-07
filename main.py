#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

# *** Unable to import libraries that are needed

import webapp2


current_flow = 100

class MainHandler(webapp2.RequestHandler):
    
    def get(self):
        self.response.write('Boise River Surf Conditions')
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('\n')
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('\n')
        self.response.write('The current flow is ')
        self.response.write(current_flow)
        self.response.write(' cfs')
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('\n')

        if current_flow <= 100 :
            self.response.write('Flow is Low')
            self.response.headers['Content-Type'] = 'text/plain'
            self.response.write('\n')
        else :
            self.response.write('Flow is High')
            self.response.headers['Content-Type'] = 'text/plain'
            self.response.write('\n')

        if current_flow <= 250 :
            self.response.write('Surfable feature is unlikely')
            self.response.headers['Content-Type'] = 'text/plain'
            self.response.write('\n')
            self.response.write('Better luck next time!')
        elif current_flow <= 650 :
            self.response.write('Waveshaper 1: Hole feature is likely')
        elif current_flow <= 1200 :
            self.response.write('Waveshaper 1: Wave feature is likely')
        elif current_flow <= 1500 :
            self.response.write('Waveshaper 1: Hole feature is likely')
            self.response.headers['Content-Type'] = 'text/plain'
            self.response.write('\n')
            self.response.write('Waveshaper 2: Wave feature is likely')
        elif current_flow <= 1800 :
            self.response.write('Waveshaper 1: Hole/Wave feature is likely')
            self.response.headers['Content-Type'] = 'text/plain'
            self.response.write('\n')
            self.response.write('Waveshaper 2: Wave feature is likely')
        elif current_flow <= 2500 :
            self.response.write('Waveshaper 1: Hole feature is likely')
            self.response.headers['Content-Type'] = 'text/plain'
            self.response.write('\n')
            self.response.write('Waveshaper 2: Hole feature is likely')
        elif current_flow <= 3000 :
            self.response.write('Waveshaper 1: Wide wave feature is likely')
            self.response.headers['Content-Type'] = 'text/plain'
            self.response.write('\n')
            self.response.write('Waveshaper 2: Hole feature is likely')
        else :
            self.response.write('Features are unpredictable, holes and waves are possible, use caution')


app = webapp2.WSGIApplication([
                               ('/', MainHandler)
                               ], debug=True)




def main():
    from paste import httpserver
    httpserver.serve(app, host='127.0.0.1', port='8080')

if __name__ == '__main__':
    main()
