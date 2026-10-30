# `CMAnomalyManager`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 1 properties, 12 instance methods, 2 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" fPrivateQueue;
@"NSObject<OS_dispatch_queue>" fAppQueue;
^v fLocationdConnection;
@"CMAnomalyEvent" fLastReceivedEvent;
@"CMAnomalyEvent" fLastDispatchedEvent;
B fRegisteredForNotification;
@"<CMAnomalyDelegate>" _delegate;
```

## Properties

```
@property (T@"<CMAnomalyDelegate>",N,V_delegate) delegate;
```

## Class methods

```
+[CMAnomalyManager getAnomalyFeatureEnablingStrategyForUserAge:];
+[CMAnomalyManager isAnomalyDetectionAvailable];
```

## Instance methods

```
-[CMAnomalyManager init];
-[CMAnomalyManager dealloc];
-[CMAnomalyManager setDelegate:];
-[CMAnomalyManager delegate];
-[CMAnomalyManager ackAnomalyEvent:withResolution:];
-[CMAnomalyManager _registerForAnomalyDetection:];
-[CMAnomalyManager _sendRegistrationForAnomalyEvent:];
-[CMAnomalyManager resolveAnomalyEvent:withResolution:];
-[CMAnomalyManager respondToAnomalyEvent:withResponse:];
-[CMAnomalyManager startAnomalyDetection];
-[CMAnomalyManager stopAnomalyDetection];
-[CMAnomalyManager updateAnomalyEventSOSCallState:withSOSSCallState:];
```
