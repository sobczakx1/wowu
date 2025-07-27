from seleniumbase import SB

with SB(uc=True, test=True) as demiak:

    if True:
        url = "https://kick.com/brutalles"
        demiak.uc_open_with_reconnect(url, 5)
        demiak.uc_gui_click_captcha()
        demiak.sleep(1)
        demiak.uc_gui_handle_captcha()
        demiak.sleep(1)
        if demiak.is_element_present('button:contains("Accept")'):
            demiak.uc_click('button:contains("Accept")', reconnect_time=4)
        if demiak.is_element_visible('#injected-channel-player'):
            while demiak.is_element_visible('#injected-channel-player'):
                demiak.sleep(10)
