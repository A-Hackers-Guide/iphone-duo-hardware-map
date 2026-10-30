# `WFCaptiveObserver`

- Image: [`/System/Library/PrivateFrameworks/WiFiKit.framework/WiFiKit`](../userland/System__Library__PrivateFrameworks__WiFiKit.framework__WiFiKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 14 instance methods, 0 class methods

## Instance variables

```
B _observing;
i _startCaptiveNotificationToken;
i _endCaptiveNotificationToken;
@? _eventHandler;
@"NSObject<OS_dispatch_queue>" _captiveNotificationQueue;
```

## Properties

```
@property (TB,N,GisObserving,V_observing) observing;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_captiveNotificationQueue) captiveNotificationQueue;
@property (Ti,N,V_startCaptiveNotificationToken) startCaptiveNotificationToken;
@property (Ti,N,V_endCaptiveNotificationToken) endCaptiveNotificationToken;
@property (T@?,C,N,V_eventHandler) eventHandler;
```

## Instance methods

```
-[WFCaptiveObserver eventHandler];
-[WFCaptiveObserver setEventHandler:];
-[WFCaptiveObserver init];
-[WFCaptiveObserver dealloc];
-[WFCaptiveObserver isObserving];
-[WFCaptiveObserver setObserving:];
-[WFCaptiveObserver startObservingEvents];
-[WFCaptiveObserver stopObservingEvents];
-[WFCaptiveObserver setEndCaptiveNotificationToken:];
-[WFCaptiveObserver captiveNotificationQueue];
-[WFCaptiveObserver endCaptiveNotificationToken];
-[WFCaptiveObserver setCaptiveNotificationQueue:];
-[WFCaptiveObserver setStartCaptiveNotificationToken:];
-[WFCaptiveObserver startCaptiveNotificationToken];
```
