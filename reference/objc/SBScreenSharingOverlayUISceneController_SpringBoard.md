# `SBScreenSharingOverlayUISceneController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBSystemUISceneController`
- Protocols: `FBSceneObserver`
- 4 instance variables, 7 properties, 18 instance methods, 5 class methods

## Instance variables

```
@"<BSInvalidatable>" _requireSystemGesturesShouldIgnoreHIDEdgeFlagsAssertion;
B _active;
{CGAffineTransform="a"d"b"d"c"d"d"d"tx"d"ty"d} _appliedRootWindowTransform;
{CGAffineTransform="a"d"b"d"c"d"d"d"tx"d"ty"d} _clientPreferredRootWindowTransform;
```

## Properties

```
@property (TB,N,GisActive,V_active) active;
@property (T{CGAffineTransform=dddddd},N,V_appliedRootWindowTransform) appliedRootWindowTransform;
@property (T{CGAffineTransform=dddddd},N,G_clientPreferredRootWindowTransform,S_setClientPreferredRootWindowTransform:,V_clientPreferredRootWindowTransform) clientPreferredRootWindowTransform;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBScreenSharingOverlayUISceneController _ignoredWindows];
+[SBScreenSharingOverlayUISceneController _isEssoniteFeatureEnabled];
+[SBScreenSharingOverlayUISceneController _setupInfo];
+[SBScreenSharingOverlayUISceneController ignoreWindowForScreenSharingTransform:];
+[SBScreenSharingOverlayUISceneController stopIgnoringWindowForScreenSharingTransform:];
```

## Instance methods

```
-[SBScreenSharingOverlayUISceneController _windowScene];
-[SBScreenSharingOverlayUISceneController _systemGestureManager];
-[SBScreenSharingOverlayUISceneController init];
-[SBScreenSharingOverlayUISceneController scenePresenter:willDismissScene:];
-[SBScreenSharingOverlayUISceneController setActive:];
-[SBScreenSharingOverlayUISceneController scenePresenter:didPresentScene:];
-[SBScreenSharingOverlayUISceneController _isDefaultPresenterDelegate];
-[SBScreenSharingOverlayUISceneController _displayConfiguration];
-[SBScreenSharingOverlayUISceneController isActive];
-[SBScreenSharingOverlayUISceneController scene:didUpdateClientSettings:];
-[SBScreenSharingOverlayUISceneController _applyRootWindowTransform];
-[SBScreenSharingOverlayUISceneController _clientPreferredRootWindowTransform];
-[SBScreenSharingOverlayUISceneController _convertTransformToReferenceSpace:];
-[SBScreenSharingOverlayUISceneController _modifyDefaultPresentationContextHostTransformForWindow:fromTransform:toTransform:];
-[SBScreenSharingOverlayUISceneController _setClientPreferredRootWindowTransform:];
-[SBScreenSharingOverlayUISceneController _systemGestureWindow];
-[SBScreenSharingOverlayUISceneController appliedRootWindowTransform];
-[SBScreenSharingOverlayUISceneController setAppliedRootWindowTransform:];
```
