# `CBAdaptationClient`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 1 properties, 19 instance methods, 1 class methods

## Instance variables

```
@"BrightnessSystemClient" bsc;
B ownsClient;
i _mode;
B _modeSet;
@? _notificationBlock;
@"NSObject<OS_dispatch_queue>" _notificationQueue;
@"NSObject<OS_os_log>" _logHandle;
B _supported;
```

## Properties

```
@property (TB,V_supported) supported;
```

## Class methods

```
+[CBAdaptationClient supportsAdaptation];
```

## Instance methods

```
-[CBAdaptationClient supported];
-[CBAdaptationClient setSupported:];
-[CBAdaptationClient init];
-[CBAdaptationClient dealloc];
-[CBAdaptationClient available];
-[CBAdaptationClient setEnabled:];
-[CBAdaptationClient getEnabled];
-[CBAdaptationClient animateFromWeakestAdaptationModeInArray:withLength:toWeakestInArray:withLength:withProgress:andPeriod:];
-[CBAdaptationClient getAdaptationMode];
-[CBAdaptationClient getStrengths:nStrengths:];
-[CBAdaptationClient overrideStrengths:forModes:nModes:];
-[CBAdaptationClient setAdaptationMode:withPeriod:];
-[CBAdaptationClient setWeakestAdaptationModeFromArray:withLength:andPeriod:];
-[CBAdaptationClient handleBrightnessSystemNotificationForKey:withValue:];
-[CBAdaptationClient initWithClientObj:];
-[CBAdaptationClient registerNotificationCallbackBlock:withQueue:];
-[CBAdaptationClient registerNotificationForType:];
-[CBAdaptationClient unregisterNotificationCallbackBlock];
-[CBAdaptationClient unregisterNotificationForType:];
```
