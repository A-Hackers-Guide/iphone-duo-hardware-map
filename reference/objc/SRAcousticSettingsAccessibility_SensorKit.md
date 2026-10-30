# `SRAcousticSettingsAccessibility`

- Image: [`/System/Library/Frameworks/SensorKit.framework/SensorKit`](../userland/System__Library__Frameworks__SensorKit.framework__SensorKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SRSampling`, `NSSecureCoding`, `NSCopying`
- 4 instance variables, 8 properties, 14 instance methods, 1 class methods

## Instance variables

```
B _monoAudioEnabled;
d _leftRightBalance;
@"SRAcousticSettingsAccessibilityBackgroundSounds" _backgroundSounds;
@"SRAcousticSettingsAccessibilityHeadphoneAccommodations" _headphoneAccommodations;
```

## Properties

```
@property (Td,R,N,V_leftRightBalance) leftRightBalance;
@property (TB,R,N,GisMonoAudioEnabled,V_monoAudioEnabled) monoAudioEnabled;
@property (T@"SRAcousticSettingsAccessibilityBackgroundSounds",R,N,V_backgroundSounds) backgroundSounds;
@property (T@"SRAcousticSettingsAccessibilityHeadphoneAccommodations",R,N,V_headphoneAccommodations) headphoneAccommodations;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SRAcousticSettingsAccessibility supportsSecureCoding];
```

## Instance methods

```
-[SRAcousticSettingsAccessibility dealloc];
-[SRAcousticSettingsAccessibility encodeWithCoder:];
-[SRAcousticSettingsAccessibility hash];
-[SRAcousticSettingsAccessibility description];
-[SRAcousticSettingsAccessibility initWithCoder:];
-[SRAcousticSettingsAccessibility copyWithZone:];
-[SRAcousticSettingsAccessibility isEqual:];
-[SRAcousticSettingsAccessibility binarySampleRepresentation];
-[SRAcousticSettingsAccessibility initWithBinarySampleRepresentation:metadata:timestamp:];
-[SRAcousticSettingsAccessibility isMonoAudioEnabled];
-[SRAcousticSettingsAccessibility backgroundSounds];
-[SRAcousticSettingsAccessibility headphoneAccommodations];
-[SRAcousticSettingsAccessibility initWithLeftRightBalance:monoAudioEnabled:backgroundSounds:headphoneAccommodations:];
-[SRAcousticSettingsAccessibility leftRightBalance];
```
