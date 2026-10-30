# `SBDeviceApplicationAppProtectionSceneOverlayViewProvider`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBDeviceApplicationSceneOverlayViewProvider`
- Protocols: `SBApplicationAppProtectionAssistantObserver`, `SBDeviceApplicationSceneHandleObserver`
- 5 instance variables, 9 properties, 30 instance methods, 0 class methods

## Instance variables

```
B _deallocating;
@"UIViewController" _shieldViewController;
@"<BSInvalidatable>" _visibilityAssertion;
@"<BSInvalidatable>" _keyboardFocusPreventionAssertion;
@"NSString" _sceneIdentifier;
```

## Properties

```
@property (T@"UIViewController",&,N,V_shieldViewController) shieldViewController;
@property (TB,N,GisDeallocating,V_deallocating) deallocating;
@property (T@"<BSInvalidatable>",&,N,V_visibilityAssertion) visibilityAssertion;
@property (T@"<BSInvalidatable>",&,N,V_keyboardFocusPreventionAssertion) keyboardFocusPreventionAssertion;
@property (T@"NSString",C,N,V_sceneIdentifier) sceneIdentifier;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBDeviceApplicationAppProtectionSceneOverlayViewProvider sceneHandle:didDestroyScene:];
-[SBDeviceApplicationAppProtectionSceneOverlayViewProvider sceneHandle:didCreateScene:];
-[SBDeviceApplicationAppProtectionSceneOverlayViewProvider priority];
-[SBDeviceApplicationAppProtectionSceneOverlayViewProvider sceneHandle:didChangeEffectiveForegroundness:];
-[SBDeviceApplicationAppProtectionSceneOverlayViewProvider setVisibilityAssertion:];
-[SBDeviceApplicationAppProtectionSceneOverlayViewProvider _realOverlayViewController];
-[SBDeviceApplicationAppProtectionSceneOverlayViewProvider hideContentWithAnimation:completionHandler:];
-[SBDeviceApplicationAppProtectionSceneOverlayViewProvider contentWantsSimplifiedOrientationBehavior];
-[SBDeviceApplicationAppProtectionSceneOverlayViewProvider dealloc];
-[SBDeviceApplicationAppProtectionSceneOverlayViewProvider _acquireVisibilityAssertionIfNeeded];
-[SBDeviceApplicationAppProtectionSceneOverlayViewProvider initWithSceneHandle:delegate:];
-[SBDeviceApplicationAppProtectionSceneOverlayViewProvider setSceneIdentifier:];
-[SBDeviceApplicationAppProtectionSceneOverlayViewProvider _activateIfPossible];
-[SBDeviceApplicationAppProtectionSceneOverlayViewProvider _acquireKeyboardFocusPreventionAssertionIfNeeded];
-[SBDeviceApplicationAppProtectionSceneOverlayViewProvider sceneIdentifier];
-[SBDeviceApplicationAppProtectionSceneOverlayViewProvider invalidate];
-[SBDeviceApplicationAppProtectionSceneOverlayViewProvider showContentWithAnimation:completionHandler:];
-[SBDeviceApplicationAppProtectionSceneOverlayViewProvider isDeallocating];
-[SBDeviceApplicationAppProtectionSceneOverlayViewProvider setShieldViewController:];
-[SBDeviceApplicationAppProtectionSceneOverlayViewProvider appProtectionAssistantShouldShieldDidChange:];
-[SBDeviceApplicationAppProtectionSceneOverlayViewProvider _invalidateVisibilityAssertion];
-[SBDeviceApplicationAppProtectionSceneOverlayViewProvider _deactivateIfPossible];
-[SBDeviceApplicationAppProtectionSceneOverlayViewProvider prepareForContainingSceneMovingToWindowScene:];
-[SBDeviceApplicationAppProtectionSceneOverlayViewProvider _appProtectionAssistant];
-[SBDeviceApplicationAppProtectionSceneOverlayViewProvider setDeallocating:];
-[SBDeviceApplicationAppProtectionSceneOverlayViewProvider setKeyboardFocusPreventionAssertion:];
-[SBDeviceApplicationAppProtectionSceneOverlayViewProvider _invalidateKeyboardFocusPreventionAssertion];
-[SBDeviceApplicationAppProtectionSceneOverlayViewProvider keyboardFocusPreventionAssertion];
-[SBDeviceApplicationAppProtectionSceneOverlayViewProvider shieldViewController];
-[SBDeviceApplicationAppProtectionSceneOverlayViewProvider visibilityAssertion];
```
