# `SRAcousticSettingsMusicEQ`

- Image: [`/System/Library/Frameworks/SensorKit.framework/SensorKit`](../userland/System__Library__Frameworks__SensorKit.framework__SensorKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SRSampling`, `NSSecureCoding`, `NSCopying`
- 2 instance variables, 6 properties, 11 instance methods, 1 class methods

## Instance variables

```
B _soundCheckEnabled;
B _lateNightModeEnabled;
```

## Properties

```
@property (TB,R,N,GisSoundCheckEnabled,V_soundCheckEnabled) soundCheckEnabled;
@property (TB,R,N,GisLateNightModeEnabled,V_lateNightModeEnabled) lateNightModeEnabled;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SRAcousticSettingsMusicEQ supportsSecureCoding];
```

## Instance methods

```
-[SRAcousticSettingsMusicEQ encodeWithCoder:];
-[SRAcousticSettingsMusicEQ hash];
-[SRAcousticSettingsMusicEQ description];
-[SRAcousticSettingsMusicEQ initWithCoder:];
-[SRAcousticSettingsMusicEQ copyWithZone:];
-[SRAcousticSettingsMusicEQ isEqual:];
-[SRAcousticSettingsMusicEQ isSoundCheckEnabled];
-[SRAcousticSettingsMusicEQ binarySampleRepresentation];
-[SRAcousticSettingsMusicEQ initWithBinarySampleRepresentation:metadata:timestamp:];
-[SRAcousticSettingsMusicEQ initWithSoundCheckEnabled:lateNightModeEnabled:];
-[SRAcousticSettingsMusicEQ isLateNightModeEnabled];
```
