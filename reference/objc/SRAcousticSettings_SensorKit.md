# `SRAcousticSettings`

- Image: [`/System/Library/Frameworks/SensorKit.framework/SensorKit`](../userland/System__Library__Frameworks__SensorKit.framework__SensorKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SRSampling`, `NSSecureCoding`, `NSCopying`
- 5 instance variables, 9 properties, 15 instance methods, 2 class methods

## Instance variables

```
B _environmentalSoundMeasurementsEnabled;
q _audioExposureSampleLifetime;
@"NSNumber" _headphoneSafetyAudioLevel;
@"SRAcousticSettingsMusicEQ" _musicEQSettings;
@"SRAcousticSettingsAccessibility" _accessibilitySettings;
```

## Properties

```
@property (TB,R,N,GisEnvironmentalSoundMeasurementsEnabled,V_environmentalSoundMeasurementsEnabled) environmentalSoundMeasurementsEnabled;
@property (Tq,R,N,V_audioExposureSampleLifetime) audioExposureSampleLifetime;
@property (T@"NSNumber",R,N,V_headphoneSafetyAudioLevel) headphoneSafetyAudioLevel;
@property (T@"SRAcousticSettingsMusicEQ",R,N,V_musicEQSettings) musicEQSettings;
@property (T@"SRAcousticSettingsAccessibility",R,N,V_accessibilitySettings) accessibilitySettings;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SRAcousticSettings supportsSecureCoding];
+[SRAcousticSettings initialize];
```

## Instance methods

```
-[SRAcousticSettings dealloc];
-[SRAcousticSettings encodeWithCoder:];
-[SRAcousticSettings hash];
-[SRAcousticSettings description];
-[SRAcousticSettings initWithCoder:];
-[SRAcousticSettings copyWithZone:];
-[SRAcousticSettings isEqual:];
-[SRAcousticSettings binarySampleRepresentation];
-[SRAcousticSettings initWithBinarySampleRepresentation:metadata:timestamp:];
-[SRAcousticSettings musicEQSettings];
-[SRAcousticSettings accessibilitySettings];
-[SRAcousticSettings audioExposureSampleLifetime];
-[SRAcousticSettings headphoneSafetyAudioLevel];
-[SRAcousticSettings initWithEnvironmentalSoundMeasurementsEnabled:audioExposureSampleLifetime:headphoneSafetyAudioLevel:musicEQSettings:accessibilitySettings:];
-[SRAcousticSettings isEnvironmentalSoundMeasurementsEnabled];
```
