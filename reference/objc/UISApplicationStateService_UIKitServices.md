# `UISApplicationStateService`

- Image: [`/System/Library/PrivateFrameworks/UIKitServices.framework/UIKitServices`](../userland/System__Library__PrivateFrameworks__UIKitServices.framework__UIKitServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSServiceConnectionListenerDelegate`, `UISApplicationStateXPCServerInterface`
- 4 instance variables, 5 properties, 18 instance methods, 0 class methods

## Instance variables

```
@"BSServiceConnectionListener" _listener;
@"BSServiceQueue" _calloutQueue;
@"<UISApplicationStateServiceDelegate>" _delegate;
{?="delegateDataSourceForApplicationBundleIdentifier"b1} _delegateFlags;
```

## Properties

```
@property (T@"<UISApplicationStateServiceDelegate>",W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UISApplicationStateService setBadgeValue:];
-[UISApplicationStateService listener:didReceiveConnection:withContext:];
-[UISApplicationStateService init];
-[UISApplicationStateService setDelegate:];
-[UISApplicationStateService delegate];
-[UISApplicationStateService setMinimumBackgroundFetchInterval:];
-[UISApplicationStateService setNextWakeIntervalSinceReferenceDate:];
-[UISApplicationStateService setUsesBackgroundNetwork:];
-[UISApplicationStateService setBadgeString:];
-[UISApplicationStateService initWithCalloutQueue:];
-[UISApplicationStateService setBadgeNumber:];
-[UISApplicationStateService _dataSourceForApplicationBundleIdentifier:];
-[UISApplicationStateService _isCurrentConnectionAuthorizedForApplicationBundleIdentifier:description:];
-[UISApplicationStateService _isCurrentConnectionAuthorizedForApplicationBundleIdentifier:description:legacyEntitlement:];
-[UISApplicationStateService _operatingBundleIdentifier];
-[UISApplicationStateService badgeValueWithCompletion:];
-[UISApplicationStateService nextWakeIntervalSinceReferenceDateWithCompletion:];
-[UISApplicationStateService usesBackgroundNetworkWithCompletion:];
```
