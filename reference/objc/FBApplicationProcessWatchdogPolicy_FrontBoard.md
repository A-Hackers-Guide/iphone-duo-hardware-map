# `FBApplicationProcessWatchdogPolicy`

- Image: [`/System/Library/PrivateFrameworks/FrontBoard.framework/FrontBoard`](../userland/System__Library__PrivateFrameworks__FrontBoard.framework__FrontBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FBProcessWatchdogProviding`
- 7 instance variables, 4 properties, 5 instance methods, 5 class methods

## Instance variables

```
d _deviceLaunchScale;
d _deviceResumeScale;
d _additionalFirstPartyScale;
B _enableThirdPartyPre9;
i _daNotificationToken;
@"NSDictionary" _watchdogPolicyExceptions;
@"NSObject<OS_dispatch_queue>" _queue;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[FBApplicationProcessWatchdogPolicy defaultPolicy];
+[FBApplicationProcessWatchdogPolicy _defaultFirstPartyAdditionalScale];
+[FBApplicationProcessWatchdogPolicy _defaultLaunchScale];
+[FBApplicationProcessWatchdogPolicy _defaultResumeScale];
+[FBApplicationProcessWatchdogPolicy _scaleForGestaltKey:];
```

## Instance methods

```
-[FBApplicationProcessWatchdogPolicy _queue_reloadDefaultSettings];
-[FBApplicationProcessWatchdogPolicy watchdogPolicyForProcess:eventContext:];
-[FBApplicationProcessWatchdogPolicy init];
-[FBApplicationProcessWatchdogPolicy dealloc];
-[FBApplicationProcessWatchdogPolicy _queue_watchdogScalingFactorForAppInfo:isResume:];
```
