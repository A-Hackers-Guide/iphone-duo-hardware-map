# `CBBrightnessBroadcaster`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CBDisplayManagerNotificationObserver`, `CBDisplayModeObserverProtocol`
- 6 instance variables, 4 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_os_log>" _logHandle;
@"CBDisplayManager" _manager;
@"<CBStateNotifier>" _notifier;
@"NSMutableDictionary" _brightnessByDisplay;
Q _lastPublishedRawState;
B _hasPublished;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[CBBrightnessBroadcaster dealloc];
-[CBBrightnessBroadcaster activate];
-[CBBrightnessBroadcaster sendNotificationForKey:value:origin:];
-[CBBrightnessBroadcaster cancel];
-[CBBrightnessBroadcaster displayModeProvidersUpdate:];
-[CBBrightnessBroadcaster encodeBrightnessState:];
-[CBBrightnessBroadcaster initWithDisplayManager:];
-[CBBrightnessBroadcaster initWithDisplayManager:notifier:];
-[CBBrightnessBroadcaster reevaluateAndNotify];
```
