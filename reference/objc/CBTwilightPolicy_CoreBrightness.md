# `CBTwilightPolicy`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CBChromaticCorrectionPolicy`, `CBLuxRampPolicy`
- 4 instance variables, 6 properties, 16 instance methods, 0 class methods

## Instance variables

```
@"CBChromaticCorrectionParams" _params;
^f _luxTable;
^f _nitsTable;
^f _strengthTable;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (Tf,R) rampUpDuration;
@property (Tf,R) rampDownDuration;
```

## Instance methods

```
-[CBTwilightPolicy dealloc];
-[CBTwilightPolicy initWithParams:];
-[CBTwilightPolicy name];
-[CBTwilightPolicy rampUpDuration];
-[CBTwilightPolicy rampIdentifier];
-[CBTwilightPolicy cappedRampStartLux:];
-[CBTwilightPolicy cappedRampTargetLux:];
-[CBTwilightPolicy isEnabledPropertyKey];
-[CBTwilightPolicy luxIsInActiveRange:];
-[CBTwilightPolicy nitsAreInActiveRange:];
-[CBTwilightPolicy rampDownDuration];
-[CBTwilightPolicy rampDownLuxDeltaThresholdFor:];
-[CBTwilightPolicy rampTargetLuxCap];
-[CBTwilightPolicy rampUpLuxDeltaThresholdFor:];
-[CBTwilightPolicy strengthForNits:andLux:];
-[CBTwilightPolicy strengthNotification];
```
