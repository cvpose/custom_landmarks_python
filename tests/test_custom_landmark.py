# Copyright 2024 cvpose
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
from custom_landmarks.custom_landmark import CustomLandmark
from custom_landmarks.decorator import landmark

import mediapipe as mp 

PoseLandmark = mp.solutions.pose.PoseLandmark


class DummyCustom(CustomLandmark):
    @landmark("CENTER", connection=["NECK", PoseLandmark.RIGHT_SHOULDER])
    def center(self):
        return (0.5, 0.5, 0.0)
    
    @landmark("NECK")
    def neck(self):
         return (0.5, 0.8, 0.0)


def test_custom_landmark_registers(fake_landmarks):
    obj = DummyCustom(fake_landmarks)
    assert obj.CENTER.value == len(fake_landmarks)

    center_point = obj[obj.CENTER.value]
    assert center_point.x == 0.5
    assert center_point.y == 0.5
    assert center_point.z == 0.0
     