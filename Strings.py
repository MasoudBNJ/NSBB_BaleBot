import BotConfigs

money_request_title = "کالای تستی"
money_request_description = "این یک کالای قشنگ است :)"
money_request_pan = BotConfigs.receiver_pan
receipt_success_message = "با موفقیت پرداخت شد.\n شماره پیگیری: {}"
template_message_title = "یکی از دکمه‌ها رو بفشارید :)"
template_message_buttons = ['ببر خیزان', 'اجدهای پنهان', 'پیرمرد مهربان']

reserve_place_title = "سلااااااام\nمی‌دونم حالت خییلی خوب نیست... ولی ناچاری که تو صَفِش بری که بعدا تو کَفِش نری " \
                      ":دی\nنوبت می‌گیری یا جور دیگه مشکلت رو حل می‌کنی؟؟؟ "

reserve_place_buttons = ['نوبت می‌خوام']

added_to_queue_message = 'خب ... اومدی تو صف و نفر  {}ام صف‌ای. به نظرم دم در وای‌نیسا شلوغ می‌شه. به کارت برس. ' \
                         'نوبت‌ات شد خبرت می‌کنم. '

exist_in_queue_message = 'معلومه بد تحت فشاری‌ها. الان که نوبت {}م صفی. یا جور دیگه مشکلت رو حل کن یا ۳ بار بگو *شیش ' \
                         'سیخ جیگر سیخی شیشِزار* '

# Turn arrived
turn_arrived_menu_title = 'ایول ...!\nنوبتت شد. می‌ری دیگه؟'
turn_arrived_menu_buttons = ['آره می‌رم', 'نه. حل شد!']
other_user_turn_arrived_title = 'ایول ...!\nنوبتت شد. می‌ری دیگه؟'
other_user_turn_arrived_buttons = ['آره', 'دیگه دیر شد!']

# Go inside
inside_menu_message = 'خوش اومدی... راحت باش.\n.البته حواستم به بیرونیه باشه. درم قفل کن.'
inside_menu_buttons = ['تموم شد... اومدم بیرون']

give_up_message = 'حیف شد!'

# Finish and quite message
finish_message = 'خسته نباشی دلاور...\nامیدوارم این چند دقیقه بهت خوش گذشته باشه ... راستی چند دقیقه شد حالا؟!'

# Waiting state strings
waiting_menu_buttons = ['حاجی فوریه!!!']

# How important
how_important_menu_title = 'چقدر فوریه؟؟'
how_important_menu_buttons = ['یکی جلوتر', 'سه تا جلوتر', 'پنج تا جلوتر', 'داره می‌ریزه!']
how_important_money_request_title = 'خرج داره'
how_important_money_request_description = 'بالاخره داری تو صف می‌زنی :)'


# After cheat
cheater_user_new_place_in_queue_message = 'حالا شدی نفر {}ام.'


CHEAT_AMOUNT_1 = int(1)
CHEAT_AMOUNT_2 = int(3)
CHEAT_AMOUNT_3 = int(5)
CHEAT_AMOUNT_WOW = int(50)
