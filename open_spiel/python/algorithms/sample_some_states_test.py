# Copyright 2019 DeepMind Technologies Ltd. All rights reserved.
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

"""Tests for open_spiel.python.algorithms.sample_some_states."""

from absl.testing import absltest

from open_spiel.python.algorithms import sample_some_states
import pyspiel


class SampleSomeStatesTest(absltest.TestCase):

  def test_sampling_in_simple_games(self):
    # The tests that have explicit time limit
    # can fail with very small probability.

    matrix_mp_num_states = 1+2+4
    game = pyspiel.load_game_as_turn_based("matrix_mp")
    for n in range(1, matrix_mp_num_states+1):
      states = sample_some_states.sample_some_states(game, max_states=n)
      self.assertLen(states, n)

    states = sample_some_states.sample_some_states(
        game, max_states=1, depth_limit=0)
    self.assertLen(states, 1)

    states = sample_some_states.sample_some_states(
        game, max_states=matrix_mp_num_states+1, time_limit=0.1)
    self.assertLen(states, matrix_mp_num_states)

    states = sample_some_states.sample_some_states(
        game, include_terminals=False,
        time_limit=0.1, max_states=matrix_mp_num_states)
    self.assertLen(states, 3)

    states = sample_some_states.sample_some_states(
        game, depth_limit=1, time_limit=0.1, max_states=matrix_mp_num_states)
    self.assertLen(states, 3)

    coordinated_mp_num_states = 1+2+4+8
    game = pyspiel.load_game_as_turn_based("coordinated_mp")
    for n in range(1, coordinated_mp_num_states+1):
      states = sample_some_states.sample_some_states(game, max_states=n)
      self.assertLen(states, n)

    states = sample_some_states.sample_some_states(
        game, max_states=coordinated_mp_num_states+1, time_limit=0.1)
    self.assertLen(states, coordinated_mp_num_states)

    states = sample_some_states.sample_some_states(
        game, max_states=coordinated_mp_num_states,
        include_chance_states=False, time_limit=0.1)
    self.assertLen(states, coordinated_mp_num_states-2)

if __name__ == "__main__":
  absltest.main()
