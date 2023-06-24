import io
import os
import pandas as pd

__version__ = "0.1.1"


def read_waypoints(file: os.PathLike):
    """
    Load waypoints from ARINC424 file
    :param file: Filesystem path
    :return: Pandas dataframe
    """

    colspecs = [(0, 1), (1, 4), (4, 5), (5, 6), (6, 10), (10, 12), (12, 13), (13, 18), (19, 21), (21, 22), (26, 29),
                (30, 31), (32, 41), (41, 51), (74, 79), (84, 87), (95, 98), (98, 123), (123, 128), (128, 132)]
    names = ['RecordType', 'CustomerAreaCode', 'SectionCode', 'SubsectionCode', 'RegionCode', 'ICAOCode', 'Subsection',
             'WaypointIdentifier', 'ICAOCode2', 'ContinuationRecordNo', 'WaypointType', 'WaypointUsage',
             'WaypointLatitude', 'WaypointLongitude', 'DynamicMagneticVariation', 'DatumCode', 'NameFormatIndicator',
             'WaypointNameDescription', 'FileRecordNo', 'CycleDate']
    try:
        temp = io.StringIO()
        with open(file, 'r') as f:
            for line in f:
                # Check if the 4th and 5th characters are 'AE' - this means line describes waypoint
                if line[3:5] == 'AE':
                    # If so, write to the temp file
                    temp.write(line)
        temp.seek(0)
        df = pd.read_fwf(temp, index_col=False, colspecs=colspecs, header=None, names=names)
        temp.close()
        return df
    except Exception as e:
        print("Exception:", e)
