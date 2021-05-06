from image_match import match
import webbrowser
import time
import pyautogui
from colour_match import match_c
import operator

webbrowser.get('firefox').open_new_tab('https://www.binance.com/en')
time.sleep(20)

timeout = 2
match = match()
colour = match_c()

match.wait_for_match('./templates/trade_icon.png', 1920, 1080, move_to=True, timeout=timeout)
time.sleep(2)
match.wait_for_match('./templates/classic_icon.png', 1920, 1080, move_to=True, click_on=True, timeout=timeout)
time.sleep(2)
match.wait_for_match('./templates/settings_icon.png', 1920, 1080, move_to=True, timeout=timeout)
time.sleep(2)
match.wait_for_match('./templates/night_icon.png', 1920, 1080, move_to=True, click_on=True, timeout=timeout)
time.sleep(2)
match.wait_for_match('./templates/dropdown_icon.png', 1920, 1080, move_to=True, movement_type='left', timeout=timeout)
time.sleep(2)
match.wait_for_match('./templates/edit_icon.png', 1920, 1080, move_to=True, click_on=True, timeout=timeout)
time.sleep(2)
match.wait_for_match('./templates/month_icon.png', 1920, 1080, move_to=True, click_on=True, timeout=timeout)
time.sleep(2)
match.wait_for_match('./templates/save_icon.png', 1920, 1080, move_to=True, click_on=True, timeout=timeout)
time.sleep(2)

### compare to usdt: ###
match.wait_for_match('./templates/fiat.png', 1920, 1080, move_to=True, timeout=timeout)
match.wait_for_match('./templates/usdt.png', 1920, 1080, move_to=True, click_on=True, timeout=timeout)
with open('USD_list.txt') as f:
    lines = [line.rstrip() for line in f]
    for line in lines:
        match.wait_for_match('./templates/search.png', 1920, 1080, move_to=True, click_on=True, timeout=timeout)
        pyautogui.write(line+'/USDT', interval=0.25)
        pyautogui.press('enter')
        time.sleep(2)
        match.wait_for_match('./templates/star.png', 1920, 1080, move_to=True, movement_type='mid',
                             timeout=timeout, click_on=True)
        time.sleep(2)
        match.wait_for_match('./templates/cross.png', 1920, 1080, move_to=True, click_on=True, timeout=timeout)



        coord_list = match.get_bounding_box('./templates/top.png', './templates/bottom.png', './templates/right.png', 1920, 1080, timeout=timeout)
        time.sleep(2)
        bar_coords = colour.get_green_red(coord_list[0][0], coord_list[0][1], coord_list[2][0], coord_list[1][1])
        bar_coords = sorted(bar_coords, key=operator.itemgetter(0))

        match.wait_for_match('./templates/1w.png', 1920, 1080, move_to=True, click_on=True, timeout=timeout)
        time.sleep(1)

        ### image 1.1 at 1W
        pyautogui.moveTo(bar_coords[-2][0]+coord_list[0][1], bar_coords[-2][1]+coord_list[0][0]-20)
        time.sleep(1)
        im = pyautogui.screenshot('./outputs/'+line+'_USDT_1W_001.png')


        ### image 1.2 at 1W
        pyautogui.moveTo(bar_coords[-3][0] + coord_list[0][1], bar_coords[-3][1] + coord_list[0][0]-20)
        time.sleep(1)
        im = pyautogui.screenshot('./outputs/'+line+'_USDT_1W_002.png')
        time.sleep(1)


        match.wait_for_match('./templates/1m.png', 1920, 1080, move_to=True, click_on=True, timeout=timeout)

        bar_coords = colour.get_green_red(coord_list[0][0], coord_list[0][1], coord_list[2][0], coord_list[1][1])
        bar_coords = sorted(bar_coords, key=operator.itemgetter(0))
        time.sleep(1)

        ### image 1.3 at 1M
        pyautogui.moveTo(bar_coords[-2][0] + coord_list[0][1], bar_coords[-2][1] + coord_list[0][0] - 100)
        time.sleep(1)
        im = pyautogui.screenshot('./outputs/'+line+'_USDT_1M_001.png')


        ### image 1.4 at 1M
        pyautogui.moveTo(bar_coords[-3][0] + coord_list[0][1], bar_coords[-3][1] + coord_list[0][0] - 100)
        time.sleep(1)
        im = pyautogui.screenshot('./outputs/'+line+'_USDT_1M_002.png')



### Compare to ETH ###
match.wait_for_match('./templates/alts.png', 1920, 1080, move_to=True, timeout=timeout)
match.wait_for_match('./templates/eth.png', 1920, 1080, move_to=True, click_on=True, timeout=timeout)
with open('ETH_list.txt') as f:
    lines = [line.rstrip() for line in f]
    for line in lines:
        match.wait_for_match('./templates/search.png', 1920, 1080, move_to=True, click_on=True, timeout=timeout)
        pyautogui.write(line+'/ETH', interval=0.25)
        pyautogui.press('enter')
        time.sleep(2)
        match.wait_for_match('./templates/star.png', 1920, 1080, move_to=True, movement_type='mid',
                             timeout=timeout, click_on=True)
        time.sleep(2)
        match.wait_for_match('./templates/cross.png', 1920, 1080, move_to=True, click_on=True, timeout=timeout)



        coord_list = match.get_bounding_box('./templates/top.png', './templates/bottom.png', './templates/right.png', 1920, 1080, timeout=timeout)
        time.sleep(2)
        bar_coords = colour.get_green_red(coord_list[0][0], coord_list[0][1], coord_list[2][0], coord_list[1][1])
        bar_coords = sorted(bar_coords, key=operator.itemgetter(0))

        match.wait_for_match('./templates/1w.png', 1920, 1080, move_to=True, click_on=True, timeout=timeout)
        time.sleep(1)

        ### image 1.1 at 1W
        pyautogui.moveTo(bar_coords[-2][0]+coord_list[0][1], bar_coords[-2][1]+coord_list[0][0]-20)
        time.sleep(1)
        im = pyautogui.screenshot('./outputs/'+line+'_ETH_1W_001.png')


        ### image 1.2 at 1W
        pyautogui.moveTo(bar_coords[-3][0] + coord_list[0][1], bar_coords[-3][1] + coord_list[0][0]-20)
        time.sleep(1)
        im = pyautogui.screenshot('./outputs/'+line+'_ETH_1W_002.png')
        time.sleep(1)


        match.wait_for_match('./templates/1m.png', 1920, 1080, move_to=True, click_on=True, timeout=timeout)

        bar_coords = colour.get_green_red(coord_list[0][0], coord_list[0][1], coord_list[2][0], coord_list[1][1])
        bar_coords = sorted(bar_coords, key=operator.itemgetter(0))
        time.sleep(1)

        ### image 1.3 at 1M
        pyautogui.moveTo(bar_coords[-2][0] + coord_list[0][1], bar_coords[-2][1] + coord_list[0][0] - 100)
        time.sleep(1)
        im = pyautogui.screenshot('./outputs/'+line+'_ETH_1M_001.png')


        ### image 1.4 at 1M
        pyautogui.moveTo(bar_coords[-3][0] + coord_list[0][1], bar_coords[-3][1] + coord_list[0][0] - 100)
        time.sleep(1)
        im = pyautogui.screenshot('./outputs/'+line+'_ETH_1M_002.png')


### Compare to BTC: ###
match.wait_for_match('./templates/btc.png', 1920, 1080, move_to=True, click_on=True, timeout=timeout)
with open('BTC_list.txt') as f:
    lines = [line.rstrip() for line in f]
    for line in lines:
        match.wait_for_match('./templates/search.png', 1920, 1080, move_to=True, click_on=True, timeout=timeout)
        pyautogui.write(line+'/BTC', interval=0.25)
        pyautogui.press('enter')
        time.sleep(2)
        match.wait_for_match('./templates/star.png', 1920, 1080, move_to=True, movement_type='mid',
                             timeout=timeout, click_on=True)
        time.sleep(2)
        match.wait_for_match('./templates/cross.png', 1920, 1080, move_to=True, click_on=True, timeout=timeout)



        coord_list = match.get_bounding_box('./templates/top.png', './templates/bottom.png', './templates/right.png', 1920, 1080, timeout=timeout)
        time.sleep(2)
        bar_coords = colour.get_green_red(coord_list[0][0], coord_list[0][1], coord_list[2][0], coord_list[1][1])
        bar_coords = sorted(bar_coords, key=operator.itemgetter(0))

        match.wait_for_match('./templates/1w.png', 1920, 1080, move_to=True, click_on=True, timeout=timeout)
        time.sleep(1)

        ### image 1.1 at 1W
        pyautogui.moveTo(bar_coords[-2][0]+coord_list[0][1], bar_coords[-2][1]+coord_list[0][0]-20)
        time.sleep(1)
        im = pyautogui.screenshot('./outputs/'+line+'_BTC_1W_001.png')


        ### image 1.2 at 1W
        pyautogui.moveTo(bar_coords[-3][0] + coord_list[0][1], bar_coords[-3][1] + coord_list[0][0]-20)
        time.sleep(1)
        im = pyautogui.screenshot('./outputs/'+line+'_BTC_1W_002.png')
        time.sleep(1)


        match.wait_for_match('./templates/1m.png', 1920, 1080, move_to=True, click_on=True, timeout=timeout)

        bar_coords = colour.get_green_red(coord_list[0][0], coord_list[0][1], coord_list[2][0], coord_list[1][1])
        bar_coords = sorted(bar_coords, key=operator.itemgetter(0))
        time.sleep(1)

        ### image 1.3 at 1M
        pyautogui.moveTo(bar_coords[-2][0] + coord_list[0][1], bar_coords[-2][1] + coord_list[0][0] - 100)
        time.sleep(1)
        im = pyautogui.screenshot('./outputs/'+line+'_BTC_1M_001.png')


        ### image 1.4 at 1M
        pyautogui.moveTo(bar_coords[-3][0] + coord_list[0][1], bar_coords[-3][1] + coord_list[0][0] - 100)
        time.sleep(1)
        im = pyautogui.screenshot('./outputs/'+line+'_BTC_1M_002.png')


### Compare to BNB: ###
match.wait_for_match('./templates/bnb.png', 1920, 1080, move_to=True, click_on=True, timeout=timeout)
with open('BNB_list.txt') as f:
    lines = [line.rstrip() for line in f]
    for line in lines:
        match.wait_for_match('./templates/search.png', 1920, 1080, move_to=True, click_on=True, timeout=timeout)
        pyautogui.write(line+'/BNB', interval=0.25)
        pyautogui.press('enter')
        time.sleep(2)
        match.wait_for_match('./templates/star.png', 1920, 1080, move_to=True, movement_type='mid',
                             timeout=timeout, click_on=True)
        time.sleep(2)
        match.wait_for_match('./templates/cross.png', 1920, 1080, move_to=True, click_on=True, timeout=timeout)



        coord_list = match.get_bounding_box('./templates/top.png', './templates/bottom.png', './templates/right.png', 1920, 1080, timeout=timeout)
        time.sleep(2)
        bar_coords = colour.get_green_red(coord_list[0][0], coord_list[0][1], coord_list[2][0], coord_list[1][1])
        bar_coords = sorted(bar_coords, key=operator.itemgetter(0))

        match.wait_for_match('./templates/1w.png', 1920, 1080, move_to=True, click_on=True, timeout=timeout)
        time.sleep(1)

        ### image 1.1 at 1W
        pyautogui.moveTo(bar_coords[-2][0]+coord_list[0][1], bar_coords[-2][1]+coord_list[0][0]-20)
        time.sleep(1)
        im = pyautogui.screenshot('./outputs/'+line+'_BNB_1W_001.png')


        ### image 1.2 at 1W
        pyautogui.moveTo(bar_coords[-3][0] + coord_list[0][1], bar_coords[-3][1] + coord_list[0][0]-20)
        time.sleep(1)
        im = pyautogui.screenshot('./outputs/'+line+'_BNB_1W_002.png')
        time.sleep(1)


        match.wait_for_match('./templates/1m.png', 1920, 1080, move_to=True, click_on=True, timeout=timeout)

        bar_coords = colour.get_green_red(coord_list[0][0], coord_list[0][1], coord_list[2][0], coord_list[1][1])
        bar_coords = sorted(bar_coords, key=operator.itemgetter(0))
        time.sleep(1)

        ### image 1.3 at 1M
        pyautogui.moveTo(bar_coords[-2][0] + coord_list[0][1], bar_coords[-2][1] + coord_list[0][0] - 100)
        time.sleep(1)
        im = pyautogui.screenshot('./outputs/'+line+'_BNB_1M_001.png')


        ### image 1.4 at 1M
        pyautogui.moveTo(bar_coords[-3][0] + coord_list[0][1], bar_coords[-3][1] + coord_list[0][0] - 100)
        time.sleep(1)
        im = pyautogui.screenshot('./outputs/'+line+'_BNB_1M_002.png')