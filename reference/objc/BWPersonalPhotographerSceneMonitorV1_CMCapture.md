# `BWPersonalPhotographerSceneMonitorV1`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BWPersonalPhotographerSceneMonitor`
- 10 instance variables, 4 properties, 3 instance methods, 1 class methods

## Instance variables

```
@"NSDictionary" _tuningParametersByPortType;
B _sceneTooDarkMonitoringEnabled;
I _storageSpaceThresholdCheckRateSeconds;
I _lowStorageSpaceThresholdCheckRateSeconds;
i _maxThermalPressureLevel;
i _maxPeakPowerPressureLevel;
B _sceneIsTooDark;
B _storageSpaceIsTooLow;
@"NSObject<OS_dispatch_source>" _storageCheckTimer;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _storageCheckLock;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BWPersonalPhotographerSceneMonitorV1 initialize];
```

## Instance methods

```
-[BWPersonalPhotographerSceneMonitorV1 dealloc];
-[BWPersonalPhotographerSceneMonitorV1 initWithTuningParametersByPortType:];
-[BWPersonalPhotographerSceneMonitorV1 resolvePersonalPhotographerStatusWithSampleBuffer:frameStatisticsByPortType:thermalPressureLevel:peakPowerPressureLevel:subjectDetected:personalPhotographerStatus:];
```
