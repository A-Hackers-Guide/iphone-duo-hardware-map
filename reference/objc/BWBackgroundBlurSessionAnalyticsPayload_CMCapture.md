# `BWBackgroundBlurSessionAnalyticsPayload`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BWCoreAnalyticsPayload`
- 7 instance variables, 11 properties, 19 instance methods, 0 class methods

## Instance variables

```
@"NSString" _clientApplicationID;
q _effectQuality;
d _averageProcessingTime;
d _maxProcessingTime;
q _numberOfFrames;
i _numberOfFrameDrops;
i _maxThermalSystemPressureLevel;
```

## Properties

```
@property (T@"NSString",C,N,V_clientApplicationID) clientApplicationID;
@property (Tq,N,V_effectQuality) effectQuality;
@property (Td,N,V_averageProcessingTime) averageProcessingTime;
@property (Td,N,V_maxProcessingTime) maxProcessingTime;
@property (Tq,N,V_numberOfFrames) numberOfFrames;
@property (Ti,N,V_numberOfFrameDrops) numberOfFrameDrops;
@property (Ti,N,V_maxThermalSystemPressureLevel) maxThermalSystemPressureLevel;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[BWBackgroundBlurSessionAnalyticsPayload effectQuality];
-[BWBackgroundBlurSessionAnalyticsPayload eventDictionary];
-[BWBackgroundBlurSessionAnalyticsPayload init];
-[BWBackgroundBlurSessionAnalyticsPayload dealloc];
-[BWBackgroundBlurSessionAnalyticsPayload setEffectQuality:];
-[BWBackgroundBlurSessionAnalyticsPayload reset];
-[BWBackgroundBlurSessionAnalyticsPayload setClientApplicationID:];
-[BWBackgroundBlurSessionAnalyticsPayload eventName];
-[BWBackgroundBlurSessionAnalyticsPayload numberOfFrames];
-[BWBackgroundBlurSessionAnalyticsPayload setNumberOfFrames:];
-[BWBackgroundBlurSessionAnalyticsPayload clientApplicationID];
-[BWBackgroundBlurSessionAnalyticsPayload averageProcessingTime];
-[BWBackgroundBlurSessionAnalyticsPayload maxProcessingTime];
-[BWBackgroundBlurSessionAnalyticsPayload maxThermalSystemPressureLevel];
-[BWBackgroundBlurSessionAnalyticsPayload numberOfFrameDrops];
-[BWBackgroundBlurSessionAnalyticsPayload setAverageProcessingTime:];
-[BWBackgroundBlurSessionAnalyticsPayload setMaxProcessingTime:];
-[BWBackgroundBlurSessionAnalyticsPayload setMaxThermalSystemPressureLevel:];
-[BWBackgroundBlurSessionAnalyticsPayload setNumberOfFrameDrops:];
```
