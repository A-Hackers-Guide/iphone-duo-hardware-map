# `AVAudioDeviceTestSequenceTone`

- Image: [`/System/Library/Frameworks/AVFAudio.framework/AVFAudio`](../userland/System__Library__Frameworks__AVFAudio.framework__AVFAudio.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVAudioDeviceTestSequence`
- 9 instance variables, 9 properties, 21 instance methods, 1 class methods

## Instance variables

```
i _numberOfPulses;
d _frequency;
d _amplitude;
d _soundLevel;
d _pulseDuration;
d _pauseDuration;
d _rampDuration;
d _startDelay;
d _duration;
```

## Properties

```
@property (Td,N,V_frequency) frequency;
@property (Td,N,V_amplitude) amplitude;
@property (Td,N,V_soundLevel) soundLevel;
@property (Ti,N,V_numberOfPulses) numberOfPulses;
@property (Td,N,V_pulseDuration) pulseDuration;
@property (Td,N,V_pauseDuration) pauseDuration;
@property (Td,N,V_rampDuration) rampDuration;
@property (Td,N,V_startDelay) startDelay;
@property (Td,N,V_duration) duration;
```

## Class methods

```
+[AVAudioDeviceTestSequenceTone supportsSecureCoding];
```

## Instance methods

```
-[AVAudioDeviceTestSequenceTone frequency];
-[AVAudioDeviceTestSequenceTone init];
-[AVAudioDeviceTestSequenceTone duration];
-[AVAudioDeviceTestSequenceTone setFrequency:];
-[AVAudioDeviceTestSequenceTone encodeWithCoder:];
-[AVAudioDeviceTestSequenceTone initWithCoder:];
-[AVAudioDeviceTestSequenceTone setDuration:];
-[AVAudioDeviceTestSequenceTone pulseDuration];
-[AVAudioDeviceTestSequenceTone setPulseDuration:];
-[AVAudioDeviceTestSequenceTone pauseDuration];
-[AVAudioDeviceTestSequenceTone setPauseDuration:];
-[AVAudioDeviceTestSequenceTone startDelay];
-[AVAudioDeviceTestSequenceTone amplitude];
-[AVAudioDeviceTestSequenceTone numberOfPulses];
-[AVAudioDeviceTestSequenceTone rampDuration];
-[AVAudioDeviceTestSequenceTone setAmplitude:];
-[AVAudioDeviceTestSequenceTone setNumberOfPulses:];
-[AVAudioDeviceTestSequenceTone setRampDuration:];
-[AVAudioDeviceTestSequenceTone setSoundLevel:];
-[AVAudioDeviceTestSequenceTone setStartDelay:];
-[AVAudioDeviceTestSequenceTone soundLevel];
```
