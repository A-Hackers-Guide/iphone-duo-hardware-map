# `SRAcousticSettingsAccessibilityHeadphoneAccommodations`

- Image: [`/System/Library/Frameworks/SensorKit.framework/SensorKit`](../userland/System__Library__Frameworks__SensorKit.framework__SensorKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SRSampling`, `NSSecureCoding`, `NSCopying`
- 4 instance variables, 8 properties, 13 instance methods, 1 class methods

## Instance variables

```
B _enabled;
q _mediaEnhanceTuning;
q _mediaEnhanceBoosting;
q _mediaEnhanceApplication;
```

## Properties

```
@property (TB,R,N,GisEnabled,V_enabled) enabled;
@property (Tq,R,N,V_mediaEnhanceTuning) mediaEnhanceTuning;
@property (Tq,R,N,V_mediaEnhanceBoosting) mediaEnhanceBoosting;
@property (Tq,R,N,V_mediaEnhanceApplication) mediaEnhanceApplication;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SRAcousticSettingsAccessibilityHeadphoneAccommodations supportsSecureCoding];
```

## Instance methods

```
-[SRAcousticSettingsAccessibilityHeadphoneAccommodations isEnabled];
-[SRAcousticSettingsAccessibilityHeadphoneAccommodations encodeWithCoder:];
-[SRAcousticSettingsAccessibilityHeadphoneAccommodations hash];
-[SRAcousticSettingsAccessibilityHeadphoneAccommodations description];
-[SRAcousticSettingsAccessibilityHeadphoneAccommodations initWithCoder:];
-[SRAcousticSettingsAccessibilityHeadphoneAccommodations copyWithZone:];
-[SRAcousticSettingsAccessibilityHeadphoneAccommodations isEqual:];
-[SRAcousticSettingsAccessibilityHeadphoneAccommodations binarySampleRepresentation];
-[SRAcousticSettingsAccessibilityHeadphoneAccommodations initWithBinarySampleRepresentation:metadata:timestamp:];
-[SRAcousticSettingsAccessibilityHeadphoneAccommodations initWithHeadphoneAccommodationsEnabled:mediaEnhanceTuning:mediaEnhanceBoosting:mediaEnhanceApplication:];
-[SRAcousticSettingsAccessibilityHeadphoneAccommodations mediaEnhanceApplication];
-[SRAcousticSettingsAccessibilityHeadphoneAccommodations mediaEnhanceBoosting];
-[SRAcousticSettingsAccessibilityHeadphoneAccommodations mediaEnhanceTuning];
```
