input.onButtonPressed(Button.AB, function () {
    radio.sendNumber(65)
})
radio.onReceivedString(function (receivedString) {
    if (receivedString == "ALARM") {
        basic.showString(receivedString)
        music.play(music.stringPlayable("C5 D C5 D C5 D C5 D ", 120), music.PlaybackMode.LoopingInBackground)
        led2 = 1
        while (led2 == 1) {
            basic.showLeds(`
                # # # # #
                # # # # #
                # # # # #
                # # # # #
                # # # # #
                `)
            basic.showLeds(`
                . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
                `)
        }
    }
    if (receivedString == "Alarm Cleared") {
        led2 = 0
        basic.clearScreen()
        music.stopAllSounds()
        basic.showString("Cleared")
        control.reset()
    }
})
let led2 = 0
led2 = 0
radio.setGroup(5)
radio.setFrequencyBand(37)
basic.pause(1000)
basic.showString("RR")
