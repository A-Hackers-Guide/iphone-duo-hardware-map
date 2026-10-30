# `LACPreboardLauncher`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BKSAlternateSystemAppDelegate`
- 3 instance variables, 4 properties, 9 instance methods, 0 class methods

## Instance variables

```
@? _launchCompletion;
@"<LACDeviceLifecycleManaging>" _lifecycleManager;
@"NSObject<OS_dispatch_queue>" _workQueue;
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
-[LACPreboardLauncher alternateSystemApp:didExitWithStatus:];
-[LACPreboardLauncher alternateSystemApp:didFailToLaunchWithError:];
-[LACPreboardLauncher alternateSystemApp:didTerminateWithSignal:];
-[LACPreboardLauncher alternateSystemAppDidLaunch:];
-[LACPreboardLauncher _alternateSystemApp];
-[LACPreboardLauncher _finishLaunchingWithError:];
-[LACPreboardLauncher _terminateApp:];
-[LACPreboardLauncher initWithLifecycleManager:];
-[LACPreboardLauncher launchPreboardWithCompletion:];
```
