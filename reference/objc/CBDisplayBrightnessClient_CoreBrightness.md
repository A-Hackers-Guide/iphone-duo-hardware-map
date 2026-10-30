# `CBDisplayBrightnessClient`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CBTargetedPropertyObserver`, `CBDisplayBrightnessClientProtocol`
- 7 instance variables, 8 properties, 33 instance methods, 2 class methods

## Instance variables

```
@"BrightnessSystemClient" _bsc;
@"NSObject<OS_os_log>" _logHandle;
@"CBBrightnessTransaction" _transaction;
@"NSMutableSet" _observers;
@"NSObject<OS_dispatch_queue>" _notifyQueue;
@"CBDisplayHandle" _displayHandle;
@"NSSet" _properties;
```

## Properties

```
@property (T@"NSSet",&,V_properties) properties;
@property (T@"CBDisplayHandle",R,V_displayHandle) displayHandle;
@property (T@"CBHandle",R) handle;
@property (T@"NSObject<OS_dispatch_queue>",R,V_notifyQueue) notifyQueue;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[CBDisplayBrightnessClient sanitizeBrightnessLevel:];
+[CBDisplayBrightnessClient copyNSNumberForKey:client:handle:andError:];
```

## Instance methods

```
-[CBDisplayBrightnessClient properties];
-[CBDisplayBrightnessClient dealloc];
-[CBDisplayBrightnessClient setProperties:];
-[CBDisplayBrightnessClient notifyQueue];
-[CBDisplayBrightnessClient handle];
-[CBDisplayBrightnessClient description];
-[CBDisplayBrightnessClient observeValue:forKey:andHandle:withContext:];
-[CBDisplayBrightnessClient currentSDRNitsWithError:];
-[CBDisplayBrightnessClient disableRingLightWithRampPeriod:error:];
-[CBDisplayBrightnessClient enableRingLightWithInitialMinNits:andRampPeriod:error:];
-[CBDisplayBrightnessClient isRingLightEnabledWithError:];
-[CBDisplayBrightnessClient maxSDRDisplayNitsWithError:];
-[CBDisplayBrightnessClient registerBrightnessObserver:];
-[CBDisplayBrightnessClient setRingLightMinNits:withRampPeriod:error:];
-[CBDisplayBrightnessClient unregisterBrightnessObserver:];
-[CBDisplayBrightnessClient brightnessWithError:];
-[CBDisplayBrightnessClient controlAvailableWithError:];
-[CBDisplayBrightnessClient setBrightness:error:];
-[CBDisplayBrightnessClient setAutoBrightnessEnabled:error:];
-[CBDisplayBrightnessClient _brightnessObserversProperties];
-[CBDisplayBrightnessClient _updateBrightnessObserverForKey:withValue:];
-[CBDisplayBrightnessClient brightnessCurveLevelWithError:];
-[CBDisplayBrightnessClient displayHandle];
-[CBDisplayBrightnessClient initWithClientObj:andHandle:];
-[CBDisplayBrightnessClient isAutoBrightnessAvailableWithError:];
-[CBDisplayBrightnessClient isAutobrightnessEnabledWithError:];
-[CBDisplayBrightnessClient newBrightnessAdjustmentWithError:];
-[CBDisplayBrightnessClient newBrightnessTransaction];
-[CBDisplayBrightnessClient sanitizedBrightnessWithError:];
-[CBDisplayBrightnessClient setBrightness:withCommitType:andError:];
-[CBDisplayBrightnessClient setBrightnessCurveLevel:error:];
-[CBDisplayBrightnessClient setMinimumBrightnessLevel:withDuration:error:];
-[CBDisplayBrightnessClient setPreStrobeActive:error:];
```
