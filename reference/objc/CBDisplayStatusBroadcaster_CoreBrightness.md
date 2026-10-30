# `CBDisplayStatusBroadcaster`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CBDisplayManagerNotificationObserver`, `CBDisplayModeObserverProtocol`
- 6 instance variables, 4 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_os_log>" _logHandle;
@"CBDisplayManager" _manager;
@"CBDarwinStateNotifier" _notifier;
@"NSMutableDictionary" _displayOnByDisplay;
Q _lastPublishedState;
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
-[CBDisplayStatusBroadcaster dealloc];
-[CBDisplayStatusBroadcaster activate];
-[CBDisplayStatusBroadcaster sendNotificationForKey:value:origin:];
-[CBDisplayStatusBroadcaster cancel];
-[CBDisplayStatusBroadcaster displayModeProvidersUpdate:];
-[CBDisplayStatusBroadcaster initWithDisplayManager:];
-[CBDisplayStatusBroadcaster reevaluateAndNotify];
```
