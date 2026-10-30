# `UISApplicationStateClient`

- Image: [`/System/Library/PrivateFrameworks/UIKitServices.framework/UIKitServices`](../userland/System__Library__PrivateFrameworks__UIKitServices.framework__UIKitServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSInvalidatable`
- 4 instance variables, 7 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"NSString" _bundleIdentifier;
@"NSObject<OS_dispatch_queue>" _queue;
B _queue_invalidated;
@"BSServiceConnection" _queue_connection;
```

## Properties

```
@property (T@"NSString",C,N) badgeValue;
@property (TB,N) usesBackgroundNetwork;
@property (Td,N) nextWakeIntervalSinceReferenceDate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UISApplicationStateClient badgeValue];
-[UISApplicationStateClient setBadgeValue:];
-[UISApplicationStateClient dealloc];
-[UISApplicationStateClient invalidate];
-[UISApplicationStateClient _remoteTarget];
-[UISApplicationStateClient usesBackgroundNetwork];
-[UISApplicationStateClient nextWakeIntervalSinceReferenceDate];
-[UISApplicationStateClient setMinimumBackgroundFetchInterval:];
-[UISApplicationStateClient setNextWakeIntervalSinceReferenceDate:];
-[UISApplicationStateClient initWithBundleIdentifier:];
-[UISApplicationStateClient setUsesBackgroundNetwork:];
```
