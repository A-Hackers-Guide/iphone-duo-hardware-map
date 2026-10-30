# `SBContinuitySessionLaunchEventExecutor`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 1 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"SBApplicationController" _applicationController;
@"SBContinuitySessionManager" _continuitySessionManager;
```

## Properties

```
@property (T@"SBContinuitySessionManager",R,N,V_continuitySessionManager) continuitySessionManager;
```

## Instance methods

```
-[SBContinuitySessionLaunchEventExecutor _executeAppLaunchEvent:animatedly:completion:];
-[SBContinuitySessionLaunchEventExecutor _executeDebugLaunchEvent:animatedly:completion:];
-[SBContinuitySessionLaunchEventExecutor _executeNotificationLaunchEvent:animatedly:completion:];
-[SBContinuitySessionLaunchEventExecutor _executeWidgetLaunchEvent:animatedly:completion:];
-[SBContinuitySessionLaunchEventExecutor continuitySessionManager];
-[SBContinuitySessionLaunchEventExecutor executeLaunchEvent:animatedly:completion:];
-[SBContinuitySessionLaunchEventExecutor initWithContinuitySessionManager:applicationController:];
```
