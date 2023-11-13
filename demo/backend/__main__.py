import os
import eel
import yaml
import json
import requests

API_PREFIX = "http://localhost:5001/"

count = 0
collecting = False

experience = None
knob_effect = None

total_data = [0]

with open("demo/backend/share/experience.json") as f:
    experience = json.load(f)
with open("demo/backend/share/perf_stat_tpcc2.json") as f:
    knob_effect = json.load(f)


@eel.expose
def load_file(yamlContent):
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
    response = requests.get(API_PREFIX + "knob_importance", params={"key": key})
    data = response.json()
    knobs = data["knobs"]
    importance = data["importance"]
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
        x_data = [str(int(x)) + knob_effect[key].get("unit", "") for x in
                  knob_effect[key]["knob_conf"]]
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



@eel.expose
def data_knob_estimation(yamlContent):
    response = requests.post(API_PREFIX + "knob_estimation", data={"yaml": yamlContent})

    # {"estimation": [0.0, 0.0], "rules": [(rule, impact)]}
    data = response.json()
    estimation = [data["pred_old"], data["pred_new"]]
    rules = data["rules"]
    rule_impact = []
    for i in range(len(rules)):
        rule_impact.append(str(i + 1) +". " +  str(rules[i][0]) + " : " + ("Negative" if rules[i][1]<0 else "Positive"))
    rule_impact = "\n".join(rule_impact)
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
            "data": estimation,
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
        }],
        "rules": rule_impact
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
def start_run(run_value):
    global collecting
    print("run ok stated")
    collecting = True
    response = requests.post(API_PREFIX + "start_run", data={"run_value": str(run_value)})
    return response.status_code == 200
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
    return old_count



if __name__ == "__main__":
    eel.init(str(os.path.split(os.path.realpath(__file__))[0]) + '/../static_web')
    eel.start('index.html', mode='chrome')
