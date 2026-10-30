# `SBSystemApertureContinuityDelayedUIWindowSceneDelegate`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBContinuitySessionSceneDelegate`, `SBContinuitySessionStateObserver`, `UIWindowSceneDelegate`
- 8 instance variables, 6 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"SBSystemApertureContinuityWindowScene" _systemApertureContinuityWindowScene;
@"SBSystemApertureContinuityCurtainWindowScene" _systemApertureContinuityCurtainWindowScene;
@"UIWindowScene" _windowScene;
B _initializedUI;
B _invalidated;
@"SBContinuitySession" _continuitySession;
@"<BSInvalidatable>" _continuitySessionManagerRegistration;
@"NSString" _debugName;
```

## Properties

```
@property (T@"SBContinuitySession",R,N) connectedSession;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"UIWindow",?,&,N) window;
```

## Instance methods

```
-[SBSystemApertureContinuityDelayedUIWindowSceneDelegate sceneDidDisconnect:];
-[SBSystemApertureContinuityDelayedUIWindowSceneDelegate scene:willConnectToSession:options:];
-[SBSystemApertureContinuityDelayedUIWindowSceneDelegate _initializeUIIfNecessaryForReason:];
-[SBSystemApertureContinuityDelayedUIWindowSceneDelegate _tearDownUIAndInvalidateIfNecessaryForReason:];
-[SBSystemApertureContinuityDelayedUIWindowSceneDelegate conformsToContinuitySessionSceneDelegate];
-[SBSystemApertureContinuityDelayedUIWindowSceneDelegate connectedSession];
-[SBSystemApertureContinuityDelayedUIWindowSceneDelegate continuitySessionDidUpdateState:];
-[SBSystemApertureContinuityDelayedUIWindowSceneDelegate didConnectToSession:];
```
