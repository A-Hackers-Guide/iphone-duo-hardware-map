# `PLABMClient`

- Image: [`/System/Library/PrivateFrameworks/PowerlogCore.framework/PowerlogCore`](../userland/System__Library__PrivateFrameworks__PowerlogCore.framework__PowerlogCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 1 properties, 26 instance methods, 1 class methods

## Instance variables

```
^{dispatch_queue_s=} _queue;
{shared_ptr<abm::client::Manager>="__ptr_"^{Manager}"__cntrl_"^{__shared_weak_count}} abmPLClnt;
@"<PLABMClientMessageDelegate>" _delegate;
```

## Properties

```
@property (T@"<PLABMClientMessageDelegate>",&,V_delegate) delegate;
```

## Class methods

```
+[PLABMClient sharedABMClient];
```

## Instance methods

```
-[PLABMClient init];
-[PLABMClient setDelegate:];
-[PLABMClient delegate];
-[PLABMClient startListening];
-[PLABMClient addDaleDeviceConfig];
-[PLABMClient addDaleDeviceConfigDebug];
-[PLABMClient addDeviceConfigWith:andConfigExtension:];
-[PLABMClient addICEDeviceConfig];
-[PLABMClient addICEDeviceConfigDebug];
-[PLABMClient addMavDeviceConfig];
-[PLABMClient addMavDeviceConfigDebug];
-[PLABMClient addSinopeDeviceConfig];
-[PLABMClient addSinopeDeviceConfigDebug];
-[PLABMClient getBasebandBootState];
-[PLABMClient getBasebandTimeAndLatency];
-[PLABMClient getLTESleepManagerStats];
-[PLABMClient regBBWakeListener];
-[PLABMClient regBootStateListener];
-[PLABMClient regMetricListener];
-[PLABMClient regTriggerListener];
-[PLABMClient removeDeviceConfig];
-[PLABMClient sendBootStateChangInfoToLoggerUsing:];
-[PLABMClient sendMetricToLoggerUsing:];
-[PLABMClient sendTriggerToLoggerUsing:];
-[PLABMClient sendWakeInfoToLoggerUsing:];
-[PLABMClient triggerPeriodicMetrics:andprofileId:];
```
