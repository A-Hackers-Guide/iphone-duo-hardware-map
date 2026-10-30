# `CBAmmolitePolicy`

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
-[CBAmmolitePolicy dealloc];
-[CBAmmolitePolicy initWithParams:];
-[CBAmmolitePolicy name];
-[CBAmmolitePolicy rampUpDuration];
-[CBAmmolitePolicy rampIdentifier];
-[CBAmmolitePolicy cappedRampStartLux:];
-[CBAmmolitePolicy cappedRampTargetLux:];
-[CBAmmolitePolicy isEnabledPropertyKey];
-[CBAmmolitePolicy luxIsInActiveRange:];
-[CBAmmolitePolicy nitsAreInActiveRange:];
-[CBAmmolitePolicy rampDownDuration];
-[CBAmmolitePolicy rampDownLuxDeltaThresholdFor:];
-[CBAmmolitePolicy rampTargetLuxCap];
-[CBAmmolitePolicy rampUpLuxDeltaThresholdFor:];
-[CBAmmolitePolicy strengthForNits:andLux:];
-[CBAmmolitePolicy strengthNotification];
```
