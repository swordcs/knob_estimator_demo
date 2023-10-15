import os
import time
import eel
import json


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
            "trigger": 'axis'
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
                    "color": '#F08080'
                }
            }
        }]
    }
    return json.dumps(data)


@eel.expose
def data_experience_weight():
    data = {
        "data": [{
            "data": [[1, 2], [2, 4], [3, 5], [4, 7], [5, 6], [6, 4], [7, 5],
                     [8, 4]]
        }, {
            "data": [[1, 3], [2, 4], [3, 3], [4, 6], [5, 5], [6, 4], [7, 5],
                     [8, 3]]
        }],
        "bars": {
            "show": True,
            "fill": True,
            "barWidth": 0.3,
            "lineWidth": 1,
            "order": 1,
            "fillColor": {
                "colors": [{
                    "opacity": 0.5
                }, {
                    "opacity": 0.9
                }]
            },
            "align": "center"
        },
        "colors": ["#0cc2aa", "#fcc100"],
        "series": {
            "shadowSize": 3
        },
        "xaxis": {
            "show": True,
            "font": {
                "color": "#ccc"
            },
            "position": "bottom"
        },
        "yaxis": {
            "show": True,
            "font": {
                "color": "#ccc"
            }
        },
        "grid": {
            "hoverable": True,
            "clickable": True,
            "borderWidth": 0,
            "color": "rgba(120,120,120,0.5)"
        },
        "tooltip":
        True,
        "tooltipOpts": {
            "content": "%x.0 is %y.4",
            "defaultTheme": False,
            "shifts": {
                "x": 0,
                "y": -40
            }
        }
    }
    return json.dumps(data)


@eel.expose
def data_knob_effect():
    data = {
        "tooltip": {
            "trigger": "axis"
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
                    "color": "#F08080"
                }
            }
        }]
    }
    return json.dumps(data)


@eel.expose
def data_knob_estimation():
    data = {
        "tooltip": {
            "trigger": "axis"
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


eel.init(str(os.path.split(os.path.realpath(__file__))[0]) + '/../static_web')
eel.start('index.html', mode='chrome')
