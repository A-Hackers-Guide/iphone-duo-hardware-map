# `SRAcousticSettingsAccessibilityBackgroundSounds`

- Image: [`/System/Library/Frameworks/SensorKit.framework/SensorKit`](../userland/System__Library__Frameworks__SensorKit.framework__SensorKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SRSampling`, `NSSecureCoding`, `NSCopying`
- 6 instance variables, 10 properties, 15 instance methods, 1 class methods

## Instance variables

```
B _enabled;
B _playWithMediaEnabled;
B _stopOnLockEnabled;
q _soundName;
d _relativeVolume;
d _relativeVolumeWithMedia;
```

## Properties

```
@property (TB,R,N,GisEnabled,V_enabled) enabled;
@property (Tq,R,N,V_soundName) soundName;
@property (Td,R,N,V_relativeVolume) relativeVolume;
@property (TB,R,N,GisPlayWithMediaEnabled,V_playWithMediaEnabled) playWithMediaEnabled;
@property (Td,R,N,V_relativeVolumeWithMedia) relativeVolumeWithMedia;
@property (TB,R,N,GisStopOnLockEnabled,V_stopOnLockEnabled) stopOnLockEnabled;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SRAcousticSettingsAccessibilityBackgroundSounds supportsSecureCoding];
```

## Instance methods

```
-[SRAcousticSettingsAccessibilityBackgroundSounds isEnabled];
-[SRAcousticSettingsAccessibilityBackgroundSounds relativeVolume];
-[SRAcousticSettingsAccessibilityBackgroundSounds soundName];
-[SRAcousticSettingsAccessibilityBackgroundSounds encodeWithCoder:];
-[SRAcousticSettingsAccessibilityBackgroundSounds hash];
-[SRAcousticSettingsAccessibilityBackgroundSounds description];
-[SRAcousticSettingsAccessibilityBackgroundSounds initWithCoder:];
-[SRAcousticSettingsAccessibilityBackgroundSounds copyWithZone:];
-[SRAcousticSettingsAccessibilityBackgroundSounds isEqual:];
-[SRAcousticSettingsAccessibilityBackgroundSounds binarySampleRepresentation];
-[SRAcousticSettingsAccessibilityBackgroundSounds initWithBinarySampleRepresentation:metadata:timestamp:];
-[SRAcousticSettingsAccessibilityBackgroundSounds initWithBackgroundSoundsEnabled:soundName:relativeVolume:playWithMediaEnabled:relativeVolumeWithMedia:stopOnLockEnabled:];
-[SRAcousticSettingsAccessibilityBackgroundSounds isPlayWithMediaEnabled];
-[SRAcousticSettingsAccessibilityBackgroundSounds isStopOnLockEnabled];
-[SRAcousticSettingsAccessibilityBackgroundSounds relativeVolumeWithMedia];
```
