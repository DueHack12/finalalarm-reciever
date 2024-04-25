def on_button_pressed_ab():
    radio.send_number(65)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_received_string(receivedString):
    global led2
    if receivedString == "ALARM":
        basic.show_string(receivedString)
        music.play(music.string_playable("C5 D C5 D C5 D C5 D ", 120),
            music.PlaybackMode.LOOPING_IN_BACKGROUND)
        led2 = 1
        while led2 == 1:
            basic.show_leds("""
                # # # # #
                # # # # #
                # # # # #
                # # # # #
                # # # # #
                """)
            basic.show_leds("""
                . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
                """)
    if receivedString == "Alarm Cleared":
        led2 = 0
        basic.clear_screen()
        music.stop_all_sounds()
        basic.show_string("Cleared")
        control.reset()
radio.on_received_string(on_received_string)

led2 = 0
led2 = 0
radio.set_group(5)
radio.set_frequency_band(37)
basic.pause(1000)
basic.show_string("RR")