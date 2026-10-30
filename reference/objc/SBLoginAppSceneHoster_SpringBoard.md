# `SBLoginAppSceneHoster`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FBSceneObserver`, `SBLoginAppSceneHoster`
- 9 instance variables, 10 properties, 16 instance methods, 0 class methods

## Instance variables

```
@"FBScene" _scene;
@"<UIScenePresenter>" _scenePresenter;
@"SBDeviceApplicationSceneHandle" _sceneHandle;
@"<BSInvalidatable>" _keyboardFocusRedirectAssertion;
@"<BSInvalidatable>" _suspensionUnderLockExemption;
B _deferHIDEvents;
B _hidEventDeferralsInstalled;
@"SBApplicationController" _applicationController;
@"<SBLoginAppSceneHosterDelegate>" _delegate;
```

## Properties

```
@property (T@"<SBLoginAppSceneHosterDelegate>",W,N,V_delegate) delegate;
@property (T@"UIView",R,N) contentView;
@property (T@"NSString",R,N) hostedAppBundleID;
@property (T@"NSString",R,N) hostedSceneIdentifier;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"SBApplication",R,D,N) hostedApp;
@property (TB,N,V_deferHIDEvents) deferHIDEvents;
```

## Instance methods

```
-[SBLoginAppSceneHoster sceneDidInvalidate:withContext:];
-[SBLoginAppSceneHoster initWithApplicationController:];
-[SBLoginAppSceneHoster dealloc];
-[SBLoginAppSceneHoster setDelegate:];
-[SBLoginAppSceneHoster contentView];
-[SBLoginAppSceneHoster delegate];
-[SBLoginAppSceneHoster scene:didUpdateClientSettings:];
-[SBLoginAppSceneHoster updateSettingsWithTransitionBlock:];
-[SBLoginAppSceneHoster _updateHIDEventDeferringIfNecessary];
-[SBLoginAppSceneHoster deferHIDEvents];
-[SBLoginAppSceneHoster hostedApp];
-[SBLoginAppSceneHoster hostedAppBundleID];
-[SBLoginAppSceneHoster hostedSceneIdentifier];
-[SBLoginAppSceneHoster killLoginApp];
-[SBLoginAppSceneHoster launchLoginAppWithInitialOrientation:completion:];
-[SBLoginAppSceneHoster setDeferHIDEvents:];
```
