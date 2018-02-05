import requests
import re

def retrieve_dji_list():
    r = requests.get('http://money.cnn.com/data/dow30/')
    search_pattern = re.compile('class="wsod_symbol">(.*?)</a>.*?<span.*?">(.*?)</span>.*?\n.*?class="wsod_stream">(.*?)</span>')
    dji_list_in_text = re.findall(search_pattern, r.text)
    return dji_list_in_text

dji_list = retrieve_dji_list()
for i  in range(15):
    print('{:<8}{:8s}{:8s}'.format(i+1,dji_list[i][0],dji_list[i][2]))



'''<tr>
		<td class="wsod_firstCol"><a href="/quote/quote.html?symb=MMM" class="wsod_symbol">MMM</a>&nbsp;<span title="3M">3M</span></td>
		<td class="wsod_aRight"><span stream="last_202757" class="wsod_stream">252.36</span></td>
		<td class="wsod_aRight"><span stream="change_202757" class="wsod_stream"><span class="posData">+4.67</span></span></td>
		<td class="wsod_aRight"><span stream="changePct_202757" class="wsod_stream"><span class="posChangePct">+1.89%</span></span></td>
		<td class="wsod_aRight">3,507,873</td>
		<td class="wsod_aRight"><span class="posData">+7.22%</span></td>
	</tr>'''