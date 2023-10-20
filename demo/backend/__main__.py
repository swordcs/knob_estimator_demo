import os
import time
import eel
import json
import threading


@eel.expose
def hello():
    print('Hello from %s' % time.time())


@eel.expose
def data_workload_feature():
    data = {
        "tooltip": {
            "trigger": "item",
            "formatter": "{a} <br/>{b} : {c} ({d}%)"
        },
        "legend": {
            "orient":
            "vertical",
            "x":
            "left",
            "data": [
                'S', 'U', 'I', 'D', 'Join', 'Hash', 'Scan', 'Hash Join',
                'Index Scan', 'Bitmap Scan', 'Other'
            ]
        },
        "calculable":
        False,
        "series": [{
            "name":
            "Source",
            "type":
            "pie",
            "selectedMode":
            "single",
            "radius": [0, 50],
            "x":
            "20%",
            "width":
            "40%",
            "funnelAlign":
            "right",
            "max":
            1548,
            "itemStyle": {
                "normal": {
                    "label": {
                        "position": "inner"
                    },
                    "labelLine": {
                        "show": False
                    }
                }
            },
            "data": [
                {
                    "value": 335,
                    "name": "S"
                },
                {
                    "value": 679,
                    "name": "U"
                },
                {
                    "value": 1548,
                    "name": "I"
                },
                {
                    "value": 335,
                    "name": "D"
                },
            ]
        }, {
            "name":
            "Source",
            "type":
            "pie",
            "radius": [80, 100],
            "x":
            "60%",
            "width":
            "35%",
            "funnelAlign":
            "left",
            "max":
            1048,
            "data": [{
                "value": 310,
                "name": "Join"
            }, {
                "value": 234,
                "name": "Scan"
            }, {
                "value": 135,
                "name": "Hash Join"
            }, {
                "value": 1048,
                "name": "Index Scan"
            }, {
                "value": 251,
                "name": "Bitmap Scan"
            }, {
                "value": 147,
                "name": "Hash"
            }, {
                "value": 102,
                "name": "Other"
            }]
        }]
    }

    return json.dumps(data)


@eel.expose
def data_knob_importance():

    data = {
        "tooltip": {
            "trigger": 'item'
        },
        "legend": {
            "data": ['Knob Importance']
        },
        "calculable":
        True,
        "grid": {
            "x": 150
        },
        "xAxis": [{
            "type": 'value',
            "boundaryGap": [0, 0.01]
        }],
        "yAxis": [{
            "type":
            'category',
            "data": [
                'shared_buffers', 'work_mem', 'plan_cache_mode', 'India',
                'China', 'World(M)'
            ]
        }],
        "series": [{
            "name": 'Knob Importance',
            "type": 'bar',
            "data": [18203, 23489, 29034, 104970, 131744, 630230],
            "itemStyle": {
                "normal": {
                    "color": '#0cc2aa'
                }
            }
        }]
    }
    return json.dumps(data)


@eel.expose
def data_experience_weight():
    data = {
        "tooltip": {
            "trigger": "item",
            "formatter": "{a}:{c}"
        },
        "calculable":
        True,
        "legend": {
            "data": ["1", "2", "3"]
        },
        "xAxis": [{
            "type": "category",
            "data": ["1", "2", "3", "4", "5"],
        }],
        "yAxis": [{
            "type": "value"
        }],
        "series": [{
            "name": "1",
            "type": "bar",
            "data": [100, 400, 700, 1000, 1300],
            "itemStyle": {
                "normal": {
                    "color": "#0cc2aa"
                }
            }
        }, {
            "name": "2",
            "type": "bar",
            "data": [200, 500, 800, 1100, 1400],
            "itemStyle": {
                "normal": {
                    "color": "#fcc100"
                }
            }
        }, {
            "name": "3",
            "type": "bar",
            "data": [300, 600, 900, 1200, 1499],
            "itemStyle": {
                "normal": {
                    "color": "#a88add"
                }
            }
        }]
    }
    return json.dumps(data)


@eel.expose
def data_knob_effect():
    data = {
        "tooltip": {
            "trigger": "item"
        },
        "legend": {
            "data": ["shared_buffers"]
        },
        "calculable":
        True,
        "xAxis": [{
            "type":
            "category",
            "boundaryGap":
            False,
            "data":
            ["32MB", "64MB", "96MB", "128MB", "160MB", "192MB", "224MB"]
        }],
        "yAxis": [{
            "type": "value",
            "axisLabel": {
                "formatter": "{value}"
            }
        }],
        "series": [{
            "name": "shared_buffers",
            "type": "line",
            "data": [20, 11, 15, 5, 12, 13, 10],
            "markPoint": {
                "data": [{
                    "type": "max",
                    "name": "Max"
                }, {
                    "type": "min",
                    "name": "Min"
                }]
            },
            "markLine": {
                "data": [{
                    "type": "average",
                    "name": "Average"
                }]
            },
            "itemStyle": {
                "normal": {
                    "color": "#fcc100"
                }
            }
        }]
    }
    return json.dumps(data)


@eel.expose
def data_knob_estimation():
    data = {
        "tooltip": {
            "trigger": "item"
        },
        "calculable":
        True,
        "xAxis": [{
            "type": "category",
            "data": ["Old", "New"]
        }],
        "yAxis": [{
            "type": "value"
        }],
        "series": [{
            "type": "bar",
            "data": [162.2, 135.6],
            "markPoint": {
                "data": [{
                    "type": "max",
                    "name": "Max"
                }, {
                    "type": "min",
                    "name": "Min"
                }]
            },
            "itemStyle": {
                "normal": {
                    "color": "#60C0DD"
                }
            },
            "markLine": {
                "data": [{
                    "type": "average",
                    "name": "Average"
                }]
            }
        }]
    }
    return json.dumps(data)


@eel.expose
def echartsdata():
    data = {
        "legend": {},
        "tooltip": {},
        "dataset": {
            "source": [['product', '2015', '2016', '2017'],
                       ['Matcha Latte', 43.3, 85.8, 93.7],
                       ['Milk Tea', 83.1, 73.4, 55.1],
                       ['Cheese Cocoa', 86.4, 65.2, 82.5],
                       ['Walnut Brownie', 72.4, 53.9, 39.1]]
        },
        "xAxis": {
            "type": 'category'
        },
        "yAxis": {},
        "series": [{
            "type": 'bar'
        }, {
            "type": 'bar'
        }, {
            "type": 'bar'
        }]
    }
    return json.dumps(data)


chart_data = {
    "series": [{
        "name": 'Performance',
        "type": 'line',
        "data": [0],
        "markPoint": {
            "data": [{
                "type": 'max',
                "name": 'Max'
            }, {
                "type": 'min',
                "name": 'Min'
            }]
        },
        "markLine": {
            "data": [{
                "type": 'average',
                "name": 'Average'
            }]
        }
    }]
}
count = 0
collecting = False

import random
total_data = [0] + [random.randint(20, 4000) for _ in range(100)]


# def update_chart_data():
#     global chart_data
#     global total_data
#     global count
#     chart_data["series"][0]["data"] = total_data[:1 + count]


# def run_update_thread():
#     global count  # 初始化计数器
#     while count < 100:  # 更新100次后结束任务
#         if not collecting:
#             eel.sleep(1)
#             continue
#         print("updating")
#         update_chart_data()
#         count += 1
#         eel.sleep(5)

@eel.expose
def start_run():
    global collecting
    print("run ok stated")
    collecting = True
    # update_thread = threading.Thread(target=run_update_thread)
    # update_thread.daemon = True
    # update_thread.start()


@eel.expose
def get_chart_data():
    global count
    global collecting
    if count < 100 and collecting:
        chart_data["series"][0]["data"] = total_data[:1 + count]
        count += 1
    return json.dumps(chart_data)


@eel.expose
def get_count():
    return count


eel.init(str(os.path.split(os.path.realpath(__file__))[0]) + '/../static_web')
eel.start('index.html', mode='chrome')
