"""A small script that downloads the satellite imagery for the city of
Zurich from the canton of Zurich online storage. The data is freely
available under http://maps.zh.ch/s/wl6xjys5

The data is licensed under a `Creative Commons (CC) BY 4.0 Lizenz` by @GIS-ZH.
"""

import json
import os
import urllib.request
import sys
import time


def report_hook(count, block_size, total_size):
    global start_time
    if count == 0:
        start_time = time.time()
        return
    duration = time.time() - start_time
    progress_size = int(count * block_size)
    speed = int(progress_size / (1024 * duration))
    percent = int(count * block_size * 100 / total_size)
    sys.stdout.write("\r  %d%%, %d MB, %d KB/s, %d seconds passed" %
                     (percent, progress_size / (1024 * 1024), speed, duration))
    sys.stdout.flush()


if __name__ == "__main__":
    file_dir = os.path.dirname(os.path.abspath(__file__))

    url_data_file_path = os.path.join(
        file_dir, "zurich_ortho_photos_raw_data_urls.json")

    with open(url_data_file_path, "r") as f:
        data_path = json.load(f)

    for url in data_path["urls"]:
        name = os.path.basename(url)
        print(name)
        urllib.request.urlretrieve(url, name, report_hook)
        print("--------------------------")
