radio.onReceivedString(function (receivedString) {
    basic.showString(receivedString)
    if (receivedString == "ALARM") {
        music.play(music.stringPlayable("C5 D C5 D C5 D C5 D ", 120), music.PlaybackMode.LoopingInBackground)
    } else if (receivedString == "Alarm Cleared") {
        music.stopAllSounds()
    }
})
radio.setGroup(1)
