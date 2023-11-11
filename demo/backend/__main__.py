import os
import eel
import yaml
import json
import requests

API_PREFIX = "http://82.156.154.239:30000/"

count = 0
collecting = False
total_data = [0] + [49.29, 2566.77, 3215.7, 47.24, 458.04, 38.65, 49.43, 3280.04, 47.01, 49.62, 3766.31, 50.06, 49.94, 3491.7, 51.37, 51.14, 3082.84, 39.09, 645.55, 4061.83, 3302.93, 50.98, 50.06, 778.12, 48.67, 4397.96, 51.18, 49.34, 49.73, 49.32, 50.29, 51.01, 47.15, 4566.44, 749.6, 495.23, 50.31, 653.21, 49.49, 446.33, 42.25, 1183.44, 712.32, 388.35, 403.85, 50.83, 38.62, 50.42, 50.92, 439.13, 48.59, 3301.76, 3296.42, 50.07, 3507.23, 592.61, 39.2, 49.4, 389.07, 1446.03, 49.34, 41.99, 49.57, 409.57, 47.6, 51.58, 51.95, 49.76, 3549.84, 51.75, 52.35, 48.91, 50.51, 50.76, 4203.87, 51.66, 49.44, 50.26, 408.19, 51.83, 52.53, 50.87, 50.02, 48.98, 2549.92, 713.27, 37.73, 49.12, 51.78, 50.77, 52.17, 36.18, 2507.51, 2700.17, 3705.44, 2709.57, 51.75, 49.12, 3194.99, 3497.34]

config = None
experience = None
knob_effect = None

with open("demo/backend/share/experience.json") as f:
    experience = json.load(f)
with open("demo/backend/share/perf_stat_tpcc2.json") as f:
    knob_effect = json.load(f)


@eel.expose
def load_file(yamlContent):
    global config
    
    with open("demo/backend/share/tmp.yaml", "w") as f:
        f.write(yamlContent)
    with open("demo/backend/share/tmp.yaml","r") as f:
        config = yaml.load(f)

    response = requests.post(API_PREFIX + "load_file", data={"yaml": yamlContent})
    return response.status_code == 200



@eel.expose
def data_workload_feature(key):
    response = requests.get(API_PREFIX + "workload_feature", params={"key": key})
    data = response.json()
    assert key in experience.keys()
    all_feature = data.get("all_feature", [])
    suid_feature = data.get("suid_feature", [])
    opts_feature = data.get("opts_feature", [])
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
            "data": all_feature
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
            "data": suid_feature
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
            "data": opts_feature
        }]
    }
    return json.dumps(data)


@eel.expose
def data_knob_importance(key):
    knobs = []
    importance = []
    assert key in experience.keys()
    for ele in experience[key]["importance"][:6]:
        knobs = [ele[0]] + knobs
        importance = [ele[1]] + importance
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
            "data": knobs,
        }],
        "series": [{
            "name": 'Knob Importance',
            "type": 'bar',
            "data": importance,
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
def data_knob_effect(key):
    assert key in knob_effect.keys()
    name = [key]
    try:
        int(knob_effect[key]["knob_conf"][0])
        x_data = [str(int(x)) + knob_effect[key].get("unit", "")  for x in knob_effect[key]["knob_conf"]]
    except:
        x_data = [x for x in knob_effect[key]["knob_conf"]]
    y_data = [int(y) for y in knob_effect[key]["knob_perf"]]
    data = {
        "tooltip": {
            "trigger": "item"
        },
        "legend": {
            "data": name,
        },
        "calculable":
        True,
        "xAxis": [{
            "type":
            "category",
            "boundaryGap":
            False,
            "data":
            x_data
        }],
        "yAxis": [{
            "type": "value",
            "axisLabel": {
                "formatter": "{value}"
            }
        }],
        "series": [{
            "name": name[0],
            "type": "line",
            "data": y_data,
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
                    "color": "#ff4040"
                }
            }
        }]
    }
    return json.dumps(data)


est_count = 0

@eel.expose
def data_knob_estimation():
    est_data =  [480, 312]
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
            "data": est_data,
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


@eel.expose
def start_run():
    global collecting
    print("run ok stated")
    collecting = True

@eel.expose
def get_chart_data():
    global count
    global collecting
    if count <= 100 and collecting:
        chart_data["series"][0]["data"] = total_data[(1 if count > 0 else 0):1 + count]
        # count += 1
    return json.dumps(chart_data)

@eel.expose
def get_count():
    global count
    old_count = count
    count = min(100, count + 1)
    return old_count

@eel.expose
def handleModifiedContent(modifiedContent):
    print("接收到的最终修改后的内容是：" + modifiedContent)


if __name__ == "__main__": 
    eel.init(str(os.path.split(os.path.realpath(__file__))[0]) + '/../static_web')
    eel.start('index.html', mode='chrome')
