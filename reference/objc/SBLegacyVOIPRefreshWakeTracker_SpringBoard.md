# `SBLegacyVOIPRefreshWakeTracker`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBApplicationWakeLifecycleHandling`
- 1 instance variables, 5 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"RBSAssertion" _appKeepAliveAssertion;
```

## Properties

```
@property (T@"RBSAssertion",&,N,V_appKeepAliveAssertion) appKeepAliveAssertion;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBLegacyVOIPRefreshWakeTracker dealloc];
-[SBLegacyVOIPRefreshWakeTracker wakeDuration];
-[SBLegacyVOIPRefreshWakeTracker endWake];
-[SBLegacyVOIPRefreshWakeTracker _createAssertionForAppProcessIdentity:];
-[SBLegacyVOIPRefreshWakeTracker appKeepAliveAssertion];
-[SBLegacyVOIPRefreshWakeTracker beginWakeForApplication:];
-[SBLegacyVOIPRefreshWakeTracker setAppKeepAliveAssertion:];
```
