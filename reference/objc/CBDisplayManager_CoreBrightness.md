# `CBDisplayManager`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CBDisplayPropertyPolicyDelegate`
- 6 instance variables, 6 properties, 26 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_os_log>" _logHandle;
@"NSObject<OS_dispatch_queue>" _queue;
@"NSMutableArray" _delegates;
@"NSMutableDictionary" _containers;
@"NSMutableArray" _displayModeObservers;
@"<CBDisplayPropertyPolicy>" _propertyPolicy;
```

## Properties

```
@property (T@"NSArray",R) containers;
@property (T@"<CBDisplayPropertyPolicy>",&,V_propertyPolicy) propertyPolicy;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[CBDisplayManager removeDelegate:];
-[CBDisplayManager copyPropertyForKey:];
-[CBDisplayManager copyDisplayInfo];
-[CBDisplayManager setProperty:forKey:];
-[CBDisplayManager copyDisplayList];
-[CBDisplayManager initWithQueue:];
-[CBDisplayManager addDelegate:];
-[CBDisplayManager observeValueForKeyPath:ofObject:change:context:];
-[CBDisplayManager dealloc];
-[CBDisplayManager activate];
-[CBDisplayManager sendNotificationForKey:value:origin:];
-[CBDisplayManager containers];
-[CBDisplayManager cancel];
-[CBDisplayManager addContainer:];
-[CBDisplayManager addDisplayModeObserver:];
-[CBDisplayManager containerForHandle:];
-[CBDisplayManager copyDisplayStatusInfo];
-[CBDisplayManager copyPropertyForKey:forHandle:error:];
-[CBDisplayManager notifyDisplayModeObserver:];
-[CBDisplayManager notifyDisplayModeObservers];
-[CBDisplayManager propertyPolicy];
-[CBDisplayManager registerNotificationBlockOnContainer:];
-[CBDisplayManager removeContainerForDisplayID:];
-[CBDisplayManager removeDisplayModeObserver:];
-[CBDisplayManager setProperty:forKey:forHandle:error:];
-[CBDisplayManager setPropertyPolicy:];
```
