"""
    Ingress Checkpoint Calculator
    Copyright (C) 2014  John D. Lewis

    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License along
    with this program; if not, write to the Free Software Foundation, Inc.,
    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
"""

from datetime import datetime, timedelta
from time import mktime


def main():
    # time zero, a reference point for a cycle's beginning
    t0 = datetime.strptime('2014-07-09 11', '%Y-%m-%d %H')
    hours_per_cycle = 175

    while True:
        prompt = 'Enter time, or `now` for the current cycle. [MM/DD/YY H]: '
        stamp = raw_input(prompt)
        if stamp == 'now':
            t = datetime.now()
            break
        try:
            t = datetime.strptime(stamp, '%m/%d/%y %H')
            break
        except ValueError:
            print 'Invalid date. (CTL-C to quit)'

    seconds = mktime(t.timetuple()) - mktime(t0.timetuple())
    cycles = seconds // (3600 * hours_per_cycle)
    start = t0 + timedelta(hours=cycles * hours_per_cycle)
    checkpoints = map(lambda x: start + timedelta(hours=x),
                      range(0, hours_per_cycle, 5))

    print 'Date:', t
    print

    for num, checkpoint in enumerate(checkpoints):
        if checkpoint > t:
            break
        print '%02d %s' % (num, checkpoint)


if __name__ == '__main__':
    main()
