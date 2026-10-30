# `SBDeviceApplicationSystemUISceneAbstractViewProvider`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBDeviceApplicationSceneOverlayViewProvider`
- Protocols: `SBDeviceApplicationSceneHandleObserver`, `SBScenePresenting`
- 6 instance variables, 5 properties, 25 instance methods, 0 class methods

## Instance variables

```
B _isActive;
q _displayMode;
@"FBScene" _presentedScene;
@"UIViewController" _systemSceneUIViewController;
@"<BSInvalidatable>" _systemUIScenePresenterAssertion;
@"<SBScenePresentingDelegate>" _systemUIScenePresentingDelegate;
```

## Properties

```
@property (TB,R,N) isActive;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBDeviceApplicationSystemUISceneAbstractViewProvider setPresentingDelegate:];
-[SBDeviceApplicationSystemUISceneAbstractViewProvider presentingDelegate];
-[SBDeviceApplicationSystemUISceneAbstractViewProvider dismissScene:];
-[SBDeviceApplicationSystemUISceneAbstractViewProvider _realOverlayViewController];
-[SBDeviceApplicationSystemUISceneAbstractViewProvider acquireSystemUIScenePresentingAssertion];
-[SBDeviceApplicationSystemUISceneAbstractViewProvider sceneHandle:didUpdateSettingsWithDiff:previousSettings:];
-[SBDeviceApplicationSystemUISceneAbstractViewProvider viewControllerWithBuilder:];
-[SBDeviceApplicationSystemUISceneAbstractViewProvider dealloc];
-[SBDeviceApplicationSystemUISceneAbstractViewProvider presentScene:viewControllerBuilderBlock:];
-[SBDeviceApplicationSystemUISceneAbstractViewProvider initWithSceneHandle:delegate:];
-[SBDeviceApplicationSystemUISceneAbstractViewProvider _activateIfPossible];
-[SBDeviceApplicationSystemUISceneAbstractViewProvider noteDisplayModeChange:];
-[SBDeviceApplicationSystemUISceneAbstractViewProvider _deactivateIfPossible];
-[SBDeviceApplicationSystemUISceneAbstractViewProvider description];
-[SBDeviceApplicationSystemUISceneAbstractViewProvider wantsResignActiveAssertion];
-[SBDeviceApplicationSystemUISceneAbstractViewProvider _windowManagementStyleDidChange:];
-[SBDeviceApplicationSystemUISceneAbstractViewProvider isActive];
-[SBDeviceApplicationSystemUISceneAbstractViewProvider containerParticipant];
-[SBDeviceApplicationSystemUISceneAbstractViewProvider _acquireSystemUIScenePresentingAssertionIfNecessary];
-[SBDeviceApplicationSystemUISceneAbstractViewProvider _invalidateSystemUIScenePresentingAssertion];
-[SBDeviceApplicationSystemUISceneAbstractViewProvider _isUnderUILock];
-[SBDeviceApplicationSystemUISceneAbstractViewProvider affectsStatusBarPresentation];
-[SBDeviceApplicationSystemUISceneAbstractViewProvider currentDisplayIdentity];
-[SBDeviceApplicationSystemUISceneAbstractViewProvider isVisibleOnScreen];
-[SBDeviceApplicationSystemUISceneAbstractViewProvider parentSceneIdentityToken];
```
