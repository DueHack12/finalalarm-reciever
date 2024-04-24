def on_received_string(receivedString):
    basic.show_string(receivedString)
    if receivedString == "ALARM":
        music.play(music.string_playable("C5 D C5 D C5 D C5 D ", 120),
            music.PlaybackMode.LOOPING_IN_BACKGROUND)
    elif receivedString == "Alarm Cleared":
        control.reset()
radio.on_received_string(on_received_string)

radio.set_group(5)
radio.set_frequency_band(37)
basic.pause(1000)
basic.show_string("Ready to Receive")