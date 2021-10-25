{"filter":false,"title":"car_fleet.py","tooltip":"/Python/car_fleet.py","undoManager":{"mark":100,"position":100,"stack":[[{"start":{"row":15,"column":0},"end":{"row":15,"column":4},"action":"remove","lines":["    "],"id":34}],[{"start":{"row":15,"column":0},"end":{"row":16,"column":0},"action":"insert","lines":["",""],"id":35}],[{"start":{"row":16,"column":0},"end":{"row":16,"column":20},"action":"insert","lines":["myInventoryList = []"],"id":36}],[{"start":{"row":16,"column":20},"end":{"row":17,"column":0},"action":"insert","lines":["",""],"id":37},{"start":{"row":17,"column":0},"end":{"row":18,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":18,"column":0},"end":{"row":38,"column":42},"action":"insert","lines":["with open('car_fleet.csv') as csvFile:","    csvReader = csv.reader(csvFile, delimiter=',')  ","    lineCount = 0  ","    for row in csvReader:","        if lineCount == 0:","            print(f'Column names are: {\", \".join(row)}')  ","            lineCount += 1  ","        else:  ","            print(f'vin: {row[0]} make: {row[1]}, model: {row[2]}, year: {row[3]}, range: {row[4]}, topSpeed: {row[5]}, zeroSixty: {row[6]}, mileage: {row[7]}')  ","            currentVehicle = copy.deepcopy(myVehicle)  ","            currentVehicle[\"vin\"] = row[0]  ","            currentVehicle[\"make\"] = row[1]  ","            currentVehicle[\"model\"] = row[2]  ","            currentVehicle[\"year\"] = row[3]  ","            currentVehicle[\"range\"] = row[4]  ","            currentVehicle[\"topSpeed\"] = row[5]  ","            currentVehicle[\"zeroSixty\"] = row[6]  ","            currentVehicle[\"mileage\"] = row[7]  ","            myInventoryList.append(currentVehicle)  ","            lineCount += 1  ","    print(f'Processed {lineCount} lines.')"],"id":38}],[{"start":{"row":18,"column":38},"end":{"row":18,"column":39},"action":"insert","lines":[" "],"id":39},{"start":{"row":18,"column":39},"end":{"row":18,"column":40},"action":"insert","lines":["#"]},{"start":{"row":18,"column":40},"end":{"row":18,"column":41},"action":"insert","lines":["#"]}],[{"start":{"row":18,"column":41},"end":{"row":18,"column":42},"action":"insert","lines":[" "],"id":40}],[{"start":{"row":18,"column":41},"end":{"row":18,"column":42},"action":"remove","lines":[" "],"id":41},{"start":{"row":18,"column":40},"end":{"row":18,"column":41},"action":"remove","lines":["#"]}],[{"start":{"row":18,"column":40},"end":{"row":18,"column":41},"action":"insert","lines":[" "],"id":42}],[{"start":{"row":18,"column":41},"end":{"row":18,"column":78},"action":"insert","lines":["keeps a file open while you read data"],"id":43}],[{"start":{"row":19,"column":52},"end":{"row":19,"column":53},"action":"insert","lines":["#"],"id":44}],[{"start":{"row":19,"column":53},"end":{"row":19,"column":54},"action":"insert","lines":[" "],"id":45}],[{"start":{"row":18,"column":78},"end":{"row":18,"column":79},"action":"insert","lines":[","],"id":46}],[{"start":{"row":18,"column":79},"end":{"row":18,"column":80},"action":"insert","lines":[" "],"id":47},{"start":{"row":18,"column":80},"end":{"row":18,"column":81},"action":"insert","lines":["i"]},{"start":{"row":18,"column":81},"end":{"row":18,"column":82},"action":"insert","lines":["t"]}],[{"start":{"row":18,"column":82},"end":{"row":18,"column":83},"action":"insert","lines":[" "],"id":48},{"start":{"row":18,"column":83},"end":{"row":18,"column":84},"action":"insert","lines":["w"]},{"start":{"row":18,"column":84},"end":{"row":18,"column":85},"action":"insert","lines":["i"]},{"start":{"row":18,"column":85},"end":{"row":18,"column":86},"action":"insert","lines":["l"]},{"start":{"row":18,"column":86},"end":{"row":18,"column":87},"action":"insert","lines":["l"]}],[{"start":{"row":18,"column":87},"end":{"row":18,"column":88},"action":"insert","lines":[" "],"id":49},{"start":{"row":18,"column":88},"end":{"row":18,"column":89},"action":"insert","lines":["b"]},{"start":{"row":18,"column":89},"end":{"row":18,"column":90},"action":"insert","lines":["e"]}],[{"start":{"row":18,"column":90},"end":{"row":18,"column":91},"action":"insert","lines":[" "],"id":50},{"start":{"row":18,"column":91},"end":{"row":18,"column":92},"action":"insert","lines":["o"]},{"start":{"row":18,"column":92},"end":{"row":18,"column":93},"action":"insert","lines":["p"]},{"start":{"row":18,"column":93},"end":{"row":18,"column":94},"action":"insert","lines":["e"]},{"start":{"row":18,"column":94},"end":{"row":18,"column":95},"action":"insert","lines":["n"]}],[{"start":{"row":18,"column":95},"end":{"row":18,"column":96},"action":"insert","lines":[" "],"id":51},{"start":{"row":18,"column":96},"end":{"row":18,"column":97},"action":"insert","lines":["a"]},{"start":{"row":18,"column":97},"end":{"row":18,"column":98},"action":"insert","lines":["s"]}],[{"start":{"row":18,"column":98},"end":{"row":18,"column":99},"action":"insert","lines":[" "],"id":52},{"start":{"row":18,"column":99},"end":{"row":18,"column":100},"action":"insert","lines":["a"]}],[{"start":{"row":18,"column":100},"end":{"row":18,"column":101},"action":"insert","lines":[" "],"id":53},{"start":{"row":18,"column":101},"end":{"row":18,"column":102},"action":"insert","lines":["v"]},{"start":{"row":18,"column":102},"end":{"row":18,"column":103},"action":"insert","lines":["a"]},{"start":{"row":18,"column":103},"end":{"row":18,"column":104},"action":"insert","lines":["r"]},{"start":{"row":18,"column":104},"end":{"row":18,"column":105},"action":"insert","lines":["i"]},{"start":{"row":18,"column":105},"end":{"row":18,"column":106},"action":"insert","lines":["b"]},{"start":{"row":18,"column":106},"end":{"row":18,"column":107},"action":"insert","lines":["a"]},{"start":{"row":18,"column":107},"end":{"row":18,"column":108},"action":"insert","lines":["l"]},{"start":{"row":18,"column":108},"end":{"row":18,"column":109},"action":"insert","lines":["e"]}],[{"start":{"row":18,"column":109},"end":{"row":18,"column":110},"action":"insert","lines":[" "],"id":54},{"start":{"row":18,"column":110},"end":{"row":18,"column":111},"action":"insert","lines":["n"]},{"start":{"row":18,"column":111},"end":{"row":18,"column":112},"action":"insert","lines":["a"]},{"start":{"row":18,"column":112},"end":{"row":18,"column":113},"action":"insert","lines":["m"]},{"start":{"row":18,"column":113},"end":{"row":18,"column":114},"action":"insert","lines":["e"]}],[{"start":{"row":18,"column":114},"end":{"row":18,"column":115},"action":"insert","lines":[" "],"id":55},{"start":{"row":18,"column":115},"end":{"row":18,"column":116},"action":"insert","lines":["c"]}],[{"start":{"row":18,"column":116},"end":{"row":18,"column":117},"action":"insert","lines":["s"],"id":56},{"start":{"row":18,"column":117},"end":{"row":18,"column":118},"action":"insert","lines":["v"]},{"start":{"row":18,"column":118},"end":{"row":18,"column":119},"action":"insert","lines":["F"]}],[{"start":{"row":18,"column":119},"end":{"row":18,"column":120},"action":"insert","lines":["i"],"id":57},{"start":{"row":18,"column":120},"end":{"row":18,"column":121},"action":"insert","lines":["l"]},{"start":{"row":18,"column":121},"end":{"row":18,"column":122},"action":"insert","lines":["e"]}],[{"start":{"row":19,"column":54},"end":{"row":19,"column":55},"action":"insert","lines":["c"],"id":58},{"start":{"row":19,"column":55},"end":{"row":19,"column":56},"action":"insert","lines":["s"]},{"start":{"row":19,"column":56},"end":{"row":19,"column":57},"action":"insert","lines":["v"]}],[{"start":{"row":19,"column":57},"end":{"row":19,"column":58},"action":"insert","lines":[" "],"id":59}],[{"start":{"row":19,"column":57},"end":{"row":19,"column":58},"action":"remove","lines":[" "],"id":60}],[{"start":{"row":19,"column":57},"end":{"row":19,"column":58},"action":"insert","lines":["R"],"id":61},{"start":{"row":19,"column":58},"end":{"row":19,"column":59},"action":"insert","lines":["e"]},{"start":{"row":19,"column":59},"end":{"row":19,"column":60},"action":"insert","lines":["a"]}],[{"start":{"row":19,"column":59},"end":{"row":19,"column":60},"action":"remove","lines":["a"],"id":62},{"start":{"row":19,"column":58},"end":{"row":19,"column":59},"action":"remove","lines":["e"]},{"start":{"row":19,"column":57},"end":{"row":19,"column":58},"action":"remove","lines":["R"]},{"start":{"row":19,"column":56},"end":{"row":19,"column":57},"action":"remove","lines":["v"]},{"start":{"row":19,"column":55},"end":{"row":19,"column":56},"action":"remove","lines":["s"]}],[{"start":{"row":19,"column":54},"end":{"row":19,"column":55},"action":"remove","lines":["c"],"id":63}],[{"start":{"row":19,"column":54},"end":{"row":19,"column":55},"action":"insert","lines":["v"],"id":64},{"start":{"row":19,"column":55},"end":{"row":19,"column":56},"action":"insert","lines":["a"]},{"start":{"row":19,"column":56},"end":{"row":19,"column":57},"action":"insert","lines":["a"]}],[{"start":{"row":19,"column":56},"end":{"row":19,"column":57},"action":"remove","lines":["a"],"id":65},{"start":{"row":19,"column":55},"end":{"row":19,"column":56},"action":"remove","lines":["a"]},{"start":{"row":19,"column":54},"end":{"row":19,"column":55},"action":"remove","lines":["v"]}],[{"start":{"row":19,"column":54},"end":{"row":19,"column":55},"action":"insert","lines":["r"],"id":66},{"start":{"row":19,"column":55},"end":{"row":19,"column":56},"action":"insert","lines":["e"]},{"start":{"row":19,"column":56},"end":{"row":19,"column":57},"action":"insert","lines":["a"]},{"start":{"row":19,"column":57},"end":{"row":19,"column":58},"action":"insert","lines":["d"]},{"start":{"row":19,"column":58},"end":{"row":19,"column":59},"action":"insert","lines":["s"]}],[{"start":{"row":19,"column":59},"end":{"row":19,"column":60},"action":"insert","lines":[" "],"id":67}],[{"start":{"row":19,"column":60},"end":{"row":19,"column":61},"action":"insert","lines":["a"],"id":68}],[{"start":{"row":19,"column":61},"end":{"row":19,"column":62},"action":"insert","lines":[" "],"id":69},{"start":{"row":19,"column":62},"end":{"row":19,"column":63},"action":"insert","lines":["c"]},{"start":{"row":19,"column":63},"end":{"row":19,"column":64},"action":"insert","lines":["o"]},{"start":{"row":19,"column":64},"end":{"row":19,"column":65},"action":"insert","lines":["l"]},{"start":{"row":19,"column":65},"end":{"row":19,"column":66},"action":"insert","lines":["u"]},{"start":{"row":19,"column":66},"end":{"row":19,"column":67},"action":"insert","lines":["m"]},{"start":{"row":19,"column":67},"end":{"row":19,"column":68},"action":"insert","lines":["n"]}],[{"start":{"row":19,"column":68},"end":{"row":19,"column":69},"action":"insert","lines":[" "],"id":70},{"start":{"row":19,"column":69},"end":{"row":19,"column":70},"action":"insert","lines":["o"]},{"start":{"row":19,"column":70},"end":{"row":19,"column":71},"action":"insert","lines":["n"]},{"start":{"row":19,"column":71},"end":{"row":19,"column":72},"action":"insert","lines":["e"]}],[{"start":{"row":19,"column":72},"end":{"row":19,"column":73},"action":"insert","lines":[" "],"id":71},{"start":{"row":19,"column":73},"end":{"row":19,"column":74},"action":"insert","lines":["b"]},{"start":{"row":19,"column":74},"end":{"row":19,"column":75},"action":"insert","lines":["y"]}],[{"start":{"row":19,"column":75},"end":{"row":19,"column":76},"action":"insert","lines":[" "],"id":72},{"start":{"row":19,"column":76},"end":{"row":19,"column":77},"action":"insert","lines":["o"]},{"start":{"row":19,"column":77},"end":{"row":19,"column":78},"action":"insert","lines":["n"]},{"start":{"row":19,"column":78},"end":{"row":19,"column":79},"action":"insert","lines":["e"]}],[{"start":{"row":19,"column":79},"end":{"row":19,"column":80},"action":"insert","lines":[" "],"id":73}],[{"start":{"row":19,"column":79},"end":{"row":19,"column":80},"action":"remove","lines":[" "],"id":74}],[{"start":{"row":19,"column":79},"end":{"row":19,"column":80},"action":"insert","lines":[" "],"id":75},{"start":{"row":19,"column":80},"end":{"row":19,"column":81},"action":"insert","lines":["a"]},{"start":{"row":19,"column":81},"end":{"row":19,"column":82},"action":"insert","lines":["s"]}],[{"start":{"row":19,"column":82},"end":{"row":19,"column":83},"action":"insert","lines":[" "],"id":76},{"start":{"row":19,"column":83},"end":{"row":19,"column":84},"action":"insert","lines":["t"]},{"start":{"row":19,"column":84},"end":{"row":19,"column":85},"action":"insert","lines":["h"]},{"start":{"row":19,"column":85},"end":{"row":19,"column":86},"action":"insert","lines":["e"]}],[{"start":{"row":19,"column":86},"end":{"row":19,"column":87},"action":"insert","lines":[" "],"id":77}],[{"start":{"row":19,"column":86},"end":{"row":19,"column":87},"action":"remove","lines":[" "],"id":78},{"start":{"row":19,"column":85},"end":{"row":19,"column":86},"action":"remove","lines":["e"]},{"start":{"row":19,"column":84},"end":{"row":19,"column":85},"action":"remove","lines":["h"]},{"start":{"row":19,"column":83},"end":{"row":19,"column":84},"action":"remove","lines":["t"]},{"start":{"row":19,"column":82},"end":{"row":19,"column":83},"action":"remove","lines":[" "]},{"start":{"row":19,"column":81},"end":{"row":19,"column":82},"action":"remove","lines":["s"]},{"start":{"row":19,"column":80},"end":{"row":19,"column":81},"action":"remove","lines":["a"]},{"start":{"row":19,"column":79},"end":{"row":19,"column":80},"action":"remove","lines":[" "]}],[{"start":{"row":19,"column":79},"end":{"row":19,"column":80},"action":"insert","lines":[" "],"id":79},{"start":{"row":19,"column":80},"end":{"row":19,"column":81},"action":"insert","lines":["t"]},{"start":{"row":19,"column":81},"end":{"row":19,"column":82},"action":"insert","lines":["a"]},{"start":{"row":19,"column":82},"end":{"row":19,"column":83},"action":"insert","lines":["k"]},{"start":{"row":19,"column":83},"end":{"row":19,"column":84},"action":"insert","lines":["i"]},{"start":{"row":19,"column":84},"end":{"row":19,"column":85},"action":"insert","lines":["n"]},{"start":{"row":19,"column":85},"end":{"row":19,"column":86},"action":"insert","lines":["g"]}],[{"start":{"row":19,"column":86},"end":{"row":19,"column":87},"action":"insert","lines":[" "],"id":80},{"start":{"row":19,"column":87},"end":{"row":19,"column":88},"action":"insert","lines":["t"]},{"start":{"row":19,"column":88},"end":{"row":19,"column":89},"action":"insert","lines":["h"]},{"start":{"row":19,"column":89},"end":{"row":19,"column":90},"action":"insert","lines":["e"]}],[{"start":{"row":19,"column":90},"end":{"row":19,"column":91},"action":"insert","lines":[" "],"id":81},{"start":{"row":19,"column":91},"end":{"row":19,"column":92},"action":"insert","lines":["c"]},{"start":{"row":19,"column":92},"end":{"row":19,"column":93},"action":"insert","lines":["o"]},{"start":{"row":19,"column":93},"end":{"row":19,"column":94},"action":"insert","lines":["m"]},{"start":{"row":19,"column":94},"end":{"row":19,"column":95},"action":"insert","lines":["m"]},{"start":{"row":19,"column":95},"end":{"row":19,"column":96},"action":"insert","lines":["a"]}],[{"start":{"row":19,"column":96},"end":{"row":19,"column":97},"action":"insert","lines":[" "],"id":82},{"start":{"row":19,"column":97},"end":{"row":19,"column":98},"action":"insert","lines":["a"]}],[{"start":{"row":19,"column":98},"end":{"row":19,"column":99},"action":"insert","lines":[" "],"id":83},{"start":{"row":19,"column":99},"end":{"row":19,"column":100},"action":"insert","lines":["d"]},{"start":{"row":19,"column":100},"end":{"row":19,"column":101},"action":"insert","lines":["e"]},{"start":{"row":19,"column":101},"end":{"row":19,"column":102},"action":"insert","lines":["l"]},{"start":{"row":19,"column":102},"end":{"row":19,"column":103},"action":"insert","lines":["i"]}],[{"start":{"row":19,"column":103},"end":{"row":19,"column":104},"action":"insert","lines":["m"],"id":84},{"start":{"row":19,"column":104},"end":{"row":19,"column":105},"action":"insert","lines":["e"]},{"start":{"row":19,"column":105},"end":{"row":19,"column":106},"action":"insert","lines":["t"]},{"start":{"row":19,"column":106},"end":{"row":19,"column":107},"action":"insert","lines":["e"]},{"start":{"row":19,"column":107},"end":{"row":19,"column":108},"action":"insert","lines":["r"]}],[{"start":{"row":19,"column":108},"end":{"row":19,"column":109},"action":"insert","lines":[" "],"id":85},{"start":{"row":19,"column":109},"end":{"row":19,"column":110},"action":"insert","lines":["a"]},{"start":{"row":19,"column":110},"end":{"row":19,"column":111},"action":"insert","lines":["n"]},{"start":{"row":19,"column":111},"end":{"row":19,"column":112},"action":"insert","lines":["d"]}],[{"start":{"row":19,"column":112},"end":{"row":19,"column":113},"action":"insert","lines":[" "],"id":86},{"start":{"row":19,"column":113},"end":{"row":19,"column":114},"action":"insert","lines":["t"]},{"start":{"row":19,"column":114},"end":{"row":19,"column":115},"action":"insert","lines":["h"]},{"start":{"row":19,"column":115},"end":{"row":19,"column":116},"action":"insert","lines":["e"]}],[{"start":{"row":19,"column":116},"end":{"row":19,"column":117},"action":"insert","lines":[" "],"id":87},{"start":{"row":19,"column":117},"end":{"row":19,"column":118},"action":"insert","lines":["v"]},{"start":{"row":19,"column":118},"end":{"row":19,"column":119},"action":"insert","lines":["a"]},{"start":{"row":19,"column":119},"end":{"row":19,"column":120},"action":"insert","lines":["l"]},{"start":{"row":19,"column":120},"end":{"row":19,"column":121},"action":"insert","lines":["u"]},{"start":{"row":19,"column":121},"end":{"row":19,"column":122},"action":"insert","lines":["e"]}],[{"start":{"row":19,"column":122},"end":{"row":19,"column":123},"action":"insert","lines":[" "],"id":88},{"start":{"row":19,"column":123},"end":{"row":19,"column":124},"action":"insert","lines":["w"]},{"start":{"row":19,"column":124},"end":{"row":19,"column":125},"action":"insert","lines":["i"]},{"start":{"row":19,"column":125},"end":{"row":19,"column":126},"action":"insert","lines":["l"]},{"start":{"row":19,"column":126},"end":{"row":19,"column":127},"action":"insert","lines":["l"]}],[{"start":{"row":19,"column":127},"end":{"row":19,"column":128},"action":"insert","lines":[" "],"id":89},{"start":{"row":19,"column":128},"end":{"row":19,"column":129},"action":"insert","lines":["b"]},{"start":{"row":19,"column":129},"end":{"row":19,"column":130},"action":"insert","lines":["e"]}],[{"start":{"row":19,"column":130},"end":{"row":19,"column":131},"action":"insert","lines":[" "],"id":90},{"start":{"row":19,"column":131},"end":{"row":19,"column":132},"action":"insert","lines":["a"]},{"start":{"row":19,"column":132},"end":{"row":19,"column":133},"action":"insert","lines":["s"]},{"start":{"row":19,"column":133},"end":{"row":19,"column":134},"action":"insert","lines":["s"]},{"start":{"row":19,"column":134},"end":{"row":19,"column":135},"action":"insert","lines":["i"]},{"start":{"row":19,"column":135},"end":{"row":19,"column":136},"action":"insert","lines":["g"]},{"start":{"row":19,"column":136},"end":{"row":19,"column":137},"action":"insert","lines":["n"]},{"start":{"row":19,"column":137},"end":{"row":19,"column":138},"action":"insert","lines":["e"]}],[{"start":{"row":19,"column":138},"end":{"row":19,"column":139},"action":"insert","lines":["d"],"id":91}],[{"start":{"row":19,"column":139},"end":{"row":19,"column":140},"action":"insert","lines":[" "],"id":92},{"start":{"row":19,"column":140},"end":{"row":19,"column":141},"action":"insert","lines":["t"]},{"start":{"row":19,"column":141},"end":{"row":19,"column":142},"action":"insert","lines":["o"]}],[{"start":{"row":19,"column":142},"end":{"row":19,"column":143},"action":"insert","lines":[" "],"id":93},{"start":{"row":19,"column":143},"end":{"row":19,"column":144},"action":"insert","lines":["c"]}],[{"start":{"row":19,"column":144},"end":{"row":19,"column":145},"action":"insert","lines":["s"],"id":94},{"start":{"row":19,"column":145},"end":{"row":19,"column":146},"action":"insert","lines":["v"]},{"start":{"row":19,"column":146},"end":{"row":19,"column":147},"action":"insert","lines":["R"]}],[{"start":{"row":19,"column":147},"end":{"row":19,"column":148},"action":"insert","lines":["e"],"id":95},{"start":{"row":19,"column":148},"end":{"row":19,"column":149},"action":"insert","lines":["a"]},{"start":{"row":19,"column":149},"end":{"row":19,"column":150},"action":"insert","lines":["d"]},{"start":{"row":19,"column":150},"end":{"row":19,"column":151},"action":"insert","lines":["e"]},{"start":{"row":19,"column":151},"end":{"row":19,"column":152},"action":"insert","lines":["r"]}],[{"start":{"row":20,"column":19},"end":{"row":20,"column":20},"action":"insert","lines":["#"],"id":96}],[{"start":{"row":20,"column":20},"end":{"row":20,"column":21},"action":"insert","lines":[" "],"id":97},{"start":{"row":20,"column":21},"end":{"row":20,"column":22},"action":"insert","lines":["l"]},{"start":{"row":20,"column":22},"end":{"row":20,"column":23},"action":"insert","lines":["i"]},{"start":{"row":20,"column":23},"end":{"row":20,"column":24},"action":"insert","lines":["n"]},{"start":{"row":20,"column":24},"end":{"row":20,"column":25},"action":"insert","lines":["e"]},{"start":{"row":20,"column":25},"end":{"row":20,"column":26},"action":"insert","lines":["s"]}],[{"start":{"row":20,"column":26},"end":{"row":20,"column":27},"action":"insert","lines":[" "],"id":98},{"start":{"row":20,"column":27},"end":{"row":20,"column":28},"action":"insert","lines":["c"]},{"start":{"row":20,"column":28},"end":{"row":20,"column":29},"action":"insert","lines":["o"]},{"start":{"row":20,"column":29},"end":{"row":20,"column":30},"action":"insert","lines":["u"]},{"start":{"row":20,"column":30},"end":{"row":20,"column":31},"action":"insert","lines":["n"]},{"start":{"row":20,"column":31},"end":{"row":20,"column":32},"action":"insert","lines":["t"]},{"start":{"row":20,"column":32},"end":{"row":20,"column":33},"action":"insert","lines":["e"]},{"start":{"row":20,"column":33},"end":{"row":20,"column":34},"action":"insert","lines":["r"]}],[{"start":{"row":21,"column":25},"end":{"row":21,"column":26},"action":"insert","lines":[" "],"id":99},{"start":{"row":21,"column":26},"end":{"row":21,"column":27},"action":"insert","lines":["#"]}],[{"start":{"row":21,"column":27},"end":{"row":21,"column":28},"action":"insert","lines":[" "],"id":100},{"start":{"row":21,"column":28},"end":{"row":21,"column":29},"action":"insert","lines":["f"]},{"start":{"row":21,"column":29},"end":{"row":21,"column":30},"action":"insert","lines":["o"]},{"start":{"row":21,"column":30},"end":{"row":21,"column":31},"action":"insert","lines":["r"]}],[{"start":{"row":21,"column":31},"end":{"row":21,"column":32},"action":"insert","lines":[" "],"id":101},{"start":{"row":21,"column":32},"end":{"row":21,"column":33},"action":"insert","lines":["e"]},{"start":{"row":21,"column":33},"end":{"row":21,"column":34},"action":"insert","lines":["a"]},{"start":{"row":21,"column":34},"end":{"row":21,"column":35},"action":"insert","lines":["c"]},{"start":{"row":21,"column":35},"end":{"row":21,"column":36},"action":"insert","lines":["h"]}],[{"start":{"row":21,"column":36},"end":{"row":21,"column":37},"action":"insert","lines":[" "],"id":102},{"start":{"row":21,"column":37},"end":{"row":21,"column":38},"action":"insert","lines":["l"]},{"start":{"row":21,"column":38},"end":{"row":21,"column":39},"action":"insert","lines":["i"]},{"start":{"row":21,"column":39},"end":{"row":21,"column":40},"action":"insert","lines":["n"]},{"start":{"row":21,"column":40},"end":{"row":21,"column":41},"action":"insert","lines":["e"]}],[{"start":{"row":21,"column":41},"end":{"row":21,"column":42},"action":"insert","lines":[" "],"id":103},{"start":{"row":21,"column":42},"end":{"row":21,"column":43},"action":"insert","lines":["e"]}],[{"start":{"row":21,"column":42},"end":{"row":21,"column":43},"action":"remove","lines":["e"],"id":104}],[{"start":{"row":21,"column":42},"end":{"row":21,"column":43},"action":"insert","lines":["i"],"id":105},{"start":{"row":21,"column":43},"end":{"row":21,"column":44},"action":"insert","lines":["n"]}],[{"start":{"row":21,"column":44},"end":{"row":21,"column":45},"action":"insert","lines":[" "],"id":106},{"start":{"row":21,"column":45},"end":{"row":21,"column":46},"action":"insert","lines":["c"]}],[{"start":{"row":21,"column":46},"end":{"row":21,"column":47},"action":"insert","lines":["s"],"id":107},{"start":{"row":21,"column":47},"end":{"row":21,"column":48},"action":"insert","lines":["v"]}],[{"start":{"row":21,"column":48},"end":{"row":21,"column":49},"action":"insert","lines":["R"],"id":108},{"start":{"row":21,"column":49},"end":{"row":21,"column":50},"action":"insert","lines":["e"]},{"start":{"row":21,"column":50},"end":{"row":21,"column":51},"action":"insert","lines":["a"]},{"start":{"row":21,"column":51},"end":{"row":21,"column":52},"action":"insert","lines":["d"]},{"start":{"row":21,"column":52},"end":{"row":21,"column":53},"action":"insert","lines":["e"]},{"start":{"row":21,"column":53},"end":{"row":21,"column":54},"action":"insert","lines":["r"]}],[{"start":{"row":22,"column":26},"end":{"row":22,"column":27},"action":"insert","lines":[" "],"id":109},{"start":{"row":22,"column":27},"end":{"row":22,"column":28},"action":"insert","lines":["#"]}],[{"start":{"row":23,"column":58},"end":{"row":23,"column":59},"action":"insert","lines":["#"],"id":110}],[{"start":{"row":23,"column":59},"end":{"row":23,"column":60},"action":"insert","lines":[" "],"id":111},{"start":{"row":23,"column":60},"end":{"row":23,"column":61},"action":"insert","lines":["f"]}],[{"start":{"row":23,"column":61},"end":{"row":23,"column":62},"action":"insert","lines":[" "],"id":112},{"start":{"row":23,"column":62},"end":{"row":23,"column":63},"action":"insert","lines":["r"]},{"start":{"row":23,"column":63},"end":{"row":23,"column":64},"action":"insert","lines":["e"]},{"start":{"row":23,"column":64},"end":{"row":23,"column":65},"action":"insert","lines":["p"]},{"start":{"row":23,"column":65},"end":{"row":23,"column":66},"action":"insert","lines":["l"]},{"start":{"row":23,"column":66},"end":{"row":23,"column":67},"action":"insert","lines":["a"]},{"start":{"row":23,"column":67},"end":{"row":23,"column":68},"action":"insert","lines":["c"]},{"start":{"row":23,"column":68},"end":{"row":23,"column":69},"action":"insert","lines":["e"]},{"start":{"row":23,"column":69},"end":{"row":23,"column":70},"action":"insert","lines":["s"]}],[{"start":{"row":23,"column":70},"end":{"row":23,"column":71},"action":"insert","lines":[" "],"id":113},{"start":{"row":23,"column":71},"end":{"row":23,"column":72},"action":"insert","lines":["."]},{"start":{"row":23,"column":72},"end":{"row":23,"column":73},"action":"insert","lines":["f"]},{"start":{"row":23,"column":73},"end":{"row":23,"column":74},"action":"insert","lines":["o"]},{"start":{"row":23,"column":74},"end":{"row":23,"column":75},"action":"insert","lines":["r"]},{"start":{"row":23,"column":75},"end":{"row":23,"column":76},"action":"insert","lines":["m"]},{"start":{"row":23,"column":76},"end":{"row":23,"column":77},"action":"insert","lines":["a"]}],[{"start":{"row":23,"column":77},"end":{"row":23,"column":78},"action":"insert","lines":["t"],"id":114}],[{"start":{"row":23,"column":78},"end":{"row":23,"column":80},"action":"insert","lines":["()"],"id":115}],[{"start":{"row":25,"column":8},"end":{"row":38,"column":42},"action":"remove","lines":["else:  ","            print(f'vin: {row[0]} make: {row[1]}, model: {row[2]}, year: {row[3]}, range: {row[4]}, topSpeed: {row[5]}, zeroSixty: {row[6]}, mileage: {row[7]}')  ","            currentVehicle = copy.deepcopy(myVehicle)  ","            currentVehicle[\"vin\"] = row[0]  ","            currentVehicle[\"make\"] = row[1]  ","            currentVehicle[\"model\"] = row[2]  ","            currentVehicle[\"year\"] = row[3]  ","            currentVehicle[\"range\"] = row[4]  ","            currentVehicle[\"topSpeed\"] = row[5]  ","            currentVehicle[\"zeroSixty\"] = row[6]  ","            currentVehicle[\"mileage\"] = row[7]  ","            myInventoryList.append(currentVehicle)  ","            lineCount += 1  ","    print(f'Processed {lineCount} lines.')"],"id":116}],[{"start":{"row":25,"column":8},"end":{"row":38,"column":42},"action":"insert","lines":["else:  ","            print(f'vin: {row[0]} make: {row[1]}, model: {row[2]}, year: {row[3]}, range: {row[4]}, topSpeed: {row[5]}, zeroSixty: {row[6]}, mileage: {row[7]}')  ","            currentVehicle = copy.deepcopy(myVehicle)  ","            currentVehicle[\"vin\"] = row[0]  ","            currentVehicle[\"make\"] = row[1]  ","            currentVehicle[\"model\"] = row[2]  ","            currentVehicle[\"year\"] = row[3]  ","            currentVehicle[\"range\"] = row[4]  ","            currentVehicle[\"topSpeed\"] = row[5]  ","            currentVehicle[\"zeroSixty\"] = row[6]  ","            currentVehicle[\"mileage\"] = row[7]  ","            myInventoryList.append(currentVehicle)  ","            lineCount += 1  ","    print(f'Processed {lineCount} lines.')"],"id":117}],[{"start":{"row":38,"column":0},"end":{"row":38,"column":4},"action":"remove","lines":["    "],"id":118}],[{"start":{"row":18,"column":11},"end":{"row":18,"column":24},"action":"remove","lines":["car_fleet.csv"],"id":119},{"start":{"row":18,"column":11},"end":{"row":18,"column":23},"action":"insert","lines":["car_fleet.cs"]}],[{"start":{"row":18,"column":23},"end":{"row":18,"column":24},"action":"insert","lines":["v"],"id":120}],[{"start":{"row":18,"column":11},"end":{"row":18,"column":24},"action":"remove","lines":["car_fleet.csv"],"id":121},{"start":{"row":18,"column":11},"end":{"row":18,"column":32},"action":"insert","lines":["/Python/car_fleet.csv"]}],[{"start":{"row":18,"column":11},"end":{"row":18,"column":18},"action":"remove","lines":["/Python"],"id":122},{"start":{"row":18,"column":11},"end":{"row":18,"column":18},"action":"insert","lines":["/Python"]}],[{"start":{"row":18,"column":11},"end":{"row":18,"column":18},"action":"remove","lines":["/Python"],"id":123},{"start":{"row":18,"column":11},"end":{"row":18,"column":18},"action":"insert","lines":["/Python"]}],[{"start":{"row":18,"column":11},"end":{"row":18,"column":38},"action":"insert","lines":["/home/ec2-user/environment/"],"id":124}],[{"start":{"row":18,"column":37},"end":{"row":18,"column":38},"action":"remove","lines":["/"],"id":125}],[{"start":{"row":25,"column":7},"end":{"row":38,"column":38},"action":"remove","lines":[" else:  ","            print(f'vin: {row[0]} make: {row[1]}, model: {row[2]}, year: {row[3]}, range: {row[4]}, topSpeed: {row[5]}, zeroSixty: {row[6]}, mileage: {row[7]}')  ","            currentVehicle = copy.deepcopy(myVehicle)  ","            currentVehicle[\"vin\"] = row[0]  ","            currentVehicle[\"make\"] = row[1]  ","            currentVehicle[\"model\"] = row[2]  ","            currentVehicle[\"year\"] = row[3]  ","            currentVehicle[\"range\"] = row[4]  ","            currentVehicle[\"topSpeed\"] = row[5]  ","            currentVehicle[\"zeroSixty\"] = row[6]  ","            currentVehicle[\"mileage\"] = row[7]  ","            myInventoryList.append(currentVehicle)  ","            lineCount += 1  ","print(f'Processed {lineCount} lines.')"],"id":126}],[{"start":{"row":25,"column":7},"end":{"row":38,"column":38},"action":"insert","lines":[" else:  ","            print(f'vin: {row[0]} make: {row[1]}, model: {row[2]}, year: {row[3]}, range: {row[4]}, topSpeed: {row[5]}, zeroSixty: {row[6]}, mileage: {row[7]}')  ","            currentVehicle = copy.deepcopy(myVehicle)  ","            currentVehicle[\"vin\"] = row[0]  ","            currentVehicle[\"make\"] = row[1]  ","            currentVehicle[\"model\"] = row[2]  ","            currentVehicle[\"year\"] = row[3]  ","            currentVehicle[\"range\"] = row[4]  ","            currentVehicle[\"topSpeed\"] = row[5]  ","            currentVehicle[\"zeroSixty\"] = row[6]  ","            currentVehicle[\"mileage\"] = row[7]  ","            myInventoryList.append(currentVehicle)  ","            lineCount += 1  ","print(f'Processed {lineCount} lines.')"],"id":127}],[{"start":{"row":38,"column":38},"end":{"row":39,"column":0},"action":"insert","lines":["",""],"id":129},{"start":{"row":39,"column":0},"end":{"row":39,"column":1},"action":"insert","lines":["p"]},{"start":{"row":39,"column":1},"end":{"row":39,"column":2},"action":"insert","lines":["r"]},{"start":{"row":39,"column":2},"end":{"row":39,"column":3},"action":"insert","lines":["i"]},{"start":{"row":39,"column":3},"end":{"row":39,"column":4},"action":"insert","lines":["n"]},{"start":{"row":39,"column":4},"end":{"row":39,"column":5},"action":"insert","lines":["t"]}],[{"start":{"row":39,"column":5},"end":{"row":39,"column":6},"action":"insert","lines":[" "],"id":130}],[{"start":{"row":39,"column":5},"end":{"row":39,"column":6},"action":"remove","lines":[" "],"id":131}],[{"start":{"row":39,"column":5},"end":{"row":39,"column":7},"action":"insert","lines":["()"],"id":132}],[{"start":{"row":39,"column":6},"end":{"row":39,"column":7},"action":"insert","lines":["m"],"id":133},{"start":{"row":39,"column":7},"end":{"row":39,"column":8},"action":"insert","lines":["y"]}],[{"start":{"row":39,"column":6},"end":{"row":39,"column":8},"action":"remove","lines":["my"],"id":134},{"start":{"row":39,"column":6},"end":{"row":39,"column":15},"action":"insert","lines":["myVehicle"]}],[{"start":{"row":39,"column":6},"end":{"row":39,"column":15},"action":"remove","lines":["myVehicle"],"id":135},{"start":{"row":39,"column":6},"end":{"row":39,"column":20},"action":"insert","lines":["currentVehicle"]}]]},"ace":{"folds":[],"scrolltop":212.5,"scrollleft":0,"selection":{"start":{"row":21,"column":28},"end":{"row":21,"column":28},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":14,"state":"start","mode":"ace/mode/python"}},"timestamp":1634767030880,"hash":"5452d8eecbc5bde4d2ed50b5cb9edc0110d69a74"}