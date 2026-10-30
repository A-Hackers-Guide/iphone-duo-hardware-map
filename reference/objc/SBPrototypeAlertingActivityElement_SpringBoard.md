# `SBPrototypeAlertingActivityElement`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBSystemApertureElement`, `SAActivityBehavior`
- 5 instance variables, 9 properties, 14 instance methods, 0 class methods

## Instance variables

```
@"NSMapTable" _viewProvidersByToken;
@"<SAAutomaticallyInvalidatable>" _alertingAssertion;
@"<SAElementHosting>" _elementHost;
@"<SAActivityHosting>" _activityHost;
@"<SBSystemAperturePlatformElementHosting>" _platformElementHost;
```

## Properties

```
@property (T@"<SBSystemAperturePlatformElementHosting>",?,W,N,V_platformElementHost) platformElementHost;
@property (T@"<SAElementHosting>",?,W,N,V_elementHost) elementHost;
@property (T@"NSString",R,C,N) clientIdentifier;
@property (T@"NSString",R,C,N) elementIdentifier;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"<SAActivityHosting>",?,W,N,V_activityHost) activityHost;
```

## Instance methods

```
-[SBPrototypeAlertingActivityElement isAlerting];
-[SBPrototypeAlertingActivityElement clientIdentifier];
-[SBPrototypeAlertingActivityElement elementIdentifier];
-[SBPrototypeAlertingActivityElement init];
-[SBPrototypeAlertingActivityElement setPlatformElementHost:];
-[SBPrototypeAlertingActivityElement activityHost];
-[SBPrototypeAlertingActivityElement elementHost];
-[SBPrototypeAlertingActivityElement hasActivityBehavior];
-[SBPrototypeAlertingActivityElement setActivityHost:];
-[SBPrototypeAlertingActivityElement setElementHost:];
-[SBPrototypeAlertingActivityElement platformElementHost];
-[SBPrototypeAlertingActivityElement dropAlertingAssertion];
-[SBPrototypeAlertingActivityElement takeAlertingAssertion];
-[SBPrototypeAlertingActivityElement viewProviderForDestinationToken:];
```
