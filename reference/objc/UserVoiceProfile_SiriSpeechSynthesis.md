# `UserVoiceProfile`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 6 properties, 14 instance methods, 0 class methods

## Instance variables

```
f _pitch_mean;
f _pitch_std;
f _energy_mean;
f _energy_std;
f _duration_mean;
f _duration_std;
```

## Properties

```
@property (Tf,N,V_pitch_mean) pitch_mean;
@property (Tf,N,V_pitch_std) pitch_std;
@property (Tf,N,V_energy_mean) energy_mean;
@property (Tf,N,V_energy_std) energy_std;
@property (Tf,N,V_duration_mean) duration_mean;
@property (Tf,N,V_duration_std) duration_std;
```

## Instance methods

```
-[UserVoiceProfile init];
-[UserVoiceProfile setEnergy_mean:];
-[UserVoiceProfile duration_mean];
-[UserVoiceProfile duration_std];
-[UserVoiceProfile energy_mean];
-[UserVoiceProfile energy_std];
-[UserVoiceProfile pitch_mean];
-[UserVoiceProfile pitch_std];
-[UserVoiceProfile setDuration_mean:];
-[UserVoiceProfile setDuration_std:];
-[UserVoiceProfile setEnergy_std:];
-[UserVoiceProfile setPitch_mean:];
-[UserVoiceProfile setPitch_std:];
-[UserVoiceProfile initWithJson:];
```
