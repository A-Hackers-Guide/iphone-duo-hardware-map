# `BLSHFlipbookRenderSessionTelemetryData`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 10 instance variables, 15 properties, 17 instance methods, 0 class methods

## Instance variables

```
B _didFailToRender;
I _timedOutEnvironmentCount;
d _timestamp;
@"NSArray" _environmentIdentifiers;
@"NSString" _reasonEnded;
@"BLSHFlipbookFramesHistogram" _sessionFramesHistogram;
d _totalPreparationDuration;
d _accumulatedLayoutDuration;
d _accumulatedRenderDuration;
d _preventedSleepDuration;
```

## Properties

```
@property (T@"NSString",R,N) blsh_analyticsEventName;
@property (T@"NSDictionary",R,N) blsh_analyticsPayload;
@property (Td,R,N,V_timestamp) timestamp;
@property (T@"NSArray",R,N,V_environmentIdentifiers) environmentIdentifiers;
@property (T@"NSString",R,N,V_reasonEnded) reasonEnded;
@property (T@"BLSHFlipbookFramesHistogram",R,N,V_sessionFramesHistogram) sessionFramesHistogram;
@property (Td,R,N,V_totalPreparationDuration) totalPreparationDuration;
@property (Td,R,N,V_accumulatedLayoutDuration) accumulatedLayoutDuration;
@property (Td,R,N,V_accumulatedRenderDuration) accumulatedRenderDuration;
@property (TB,R,N) preventedSleep;
@property (Td,R,N,V_preventedSleepDuration) preventedSleepDuration;
@property (TB,R,N,V_didFailToRender) didFailToRender;
@property (TI,R,N,V_timedOutEnvironmentCount) timedOutEnvironmentCount;
@property (T@"NSString",R,N) firstEnvironmentIdentifier;
@property (TI,R,N) environmentCount;
```

## Instance methods

```
-[BLSHFlipbookRenderSessionTelemetryData timestamp];
-[BLSHFlipbookRenderSessionTelemetryData description];
-[BLSHFlipbookRenderSessionTelemetryData reasonEnded];
-[BLSHFlipbookRenderSessionTelemetryData didFailToRender];
-[BLSHFlipbookRenderSessionTelemetryData accumulatedLayoutDuration];
-[BLSHFlipbookRenderSessionTelemetryData accumulatedRenderDuration];
-[BLSHFlipbookRenderSessionTelemetryData environmentIdentifiers];
-[BLSHFlipbookRenderSessionTelemetryData sessionFramesHistogram];
-[BLSHFlipbookRenderSessionTelemetryData timedOutEnvironmentCount];
-[BLSHFlipbookRenderSessionTelemetryData totalPreparationDuration];
-[BLSHFlipbookRenderSessionTelemetryData blsh_analyticsEventName];
-[BLSHFlipbookRenderSessionTelemetryData blsh_analyticsPayload];
-[BLSHFlipbookRenderSessionTelemetryData environmentCount];
-[BLSHFlipbookRenderSessionTelemetryData firstEnvironmentIdentifier];
-[BLSHFlipbookRenderSessionTelemetryData initWithTimestamp:environmentIdentifiers:reasonEnded:sessionFramesHistogram:totalPreparationDuration:accumulatedLayoutDuration:accumulatedRenderDuration:preventedSleepDuration:didFailToRender:timedOutEnvironmentCount:];
-[BLSHFlipbookRenderSessionTelemetryData preventedSleep];
-[BLSHFlipbookRenderSessionTelemetryData preventedSleepDuration];
```
