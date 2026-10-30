# `SBCaptureApplicationLaunchRequest`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSTransactionObserver`, `SBCaptureApplicationLaunchAssertionManagerObserver`
- 10 instance variables, 13 properties, 27 instance methods, 0 class methods

## Instance variables

```
@"SBCaptureApplicationLaunchAssertionManager" _launchAssertionManager;
B _prewarmCamera;
@"NSString" _captureApplicationBundleIdentifier;
@"NSSet" _launchActions;
@? _completionBlock;
q _transitionSource;
q _launchType;
@"BSTransaction" _launchTransaction;
@"SBWindowScene" _windowScene;
@"SBApplicationController" _applicationController;
```

## Properties

```
@property (T@"NSString",C,N,V_captureApplicationBundleIdentifier) captureApplicationBundleIdentifier;
@property (T@"BSTransaction",&,N,V_launchTransaction) launchTransaction;
@property (T@"SBWindowScene",W,N,V_windowScene) windowScene;
@property (T@"SBApplicationController",&,N,V_applicationController) applicationController;
@property (Tq,N,V_launchType) launchType;
@property (T@"NSSet",&,N,V_launchActions) launchActions;
@property (Tq,N,V_transitionSource) transitionSource;
@property (T@?,C,N,V_completionBlock) completionBlock;
@property (TB,N,V_prewarmCamera) prewarmCamera;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBCaptureApplicationLaunchRequest setWindowScene:];
-[SBCaptureApplicationLaunchRequest applicationController];
-[SBCaptureApplicationLaunchRequest setCompletionBlock:];
-[SBCaptureApplicationLaunchRequest completionBlock];
-[SBCaptureApplicationLaunchRequest transactionDidComplete:];
-[SBCaptureApplicationLaunchRequest launchType];
-[SBCaptureApplicationLaunchRequest setLaunchActions:];
-[SBCaptureApplicationLaunchRequest setApplicationController:];
-[SBCaptureApplicationLaunchRequest dealloc];
-[SBCaptureApplicationLaunchRequest launchActions];
-[SBCaptureApplicationLaunchRequest setLaunchType:];
-[SBCaptureApplicationLaunchRequest windowScene];
-[SBCaptureApplicationLaunchRequest _errorWithCode:underlyingError:];
-[SBCaptureApplicationLaunchRequest transitionSource];
-[SBCaptureApplicationLaunchRequest _cameraPrewarmer];
-[SBCaptureApplicationLaunchRequest _completeLaunchWithError:];
-[SBCaptureApplicationLaunchRequest _setupContentObserverWithSceneEntity:];
-[SBCaptureApplicationLaunchRequest captureApplicationBundleIdentifier];
-[SBCaptureApplicationLaunchRequest captureApplicationLaunchAssertionManager:didUpdateAssertionForBundleIdentifier:];
-[SBCaptureApplicationLaunchRequest initWithCaptureApplicationBundleIdentifier:windowScene:applicationController:];
-[SBCaptureApplicationLaunchRequest initiate];
-[SBCaptureApplicationLaunchRequest launchTransaction];
-[SBCaptureApplicationLaunchRequest prewarmCamera];
-[SBCaptureApplicationLaunchRequest setCaptureApplicationBundleIdentifier:];
-[SBCaptureApplicationLaunchRequest setLaunchTransaction:];
-[SBCaptureApplicationLaunchRequest setPrewarmCamera:];
-[SBCaptureApplicationLaunchRequest setTransitionSource:];
```
