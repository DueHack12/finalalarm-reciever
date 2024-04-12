def on_received_string(receivedString):
    basic.show_string(receivedString)
    if receivedString == "ALARM":
        pass
radio.on_received_string(on_received_string)

radio.set_group(1)

music.play(music.string_playable("C5 D C5 D C5 D C5 D ", 120),
            music.PlaybackMode.LOOPING_IN_BACKGROUND)