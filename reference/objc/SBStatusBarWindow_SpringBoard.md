# `SBStatusBarWindow`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIWindow`
- Protocols: `STUIStatusBarWindow`, `SBWindowSceneAttachmentObserving`
- 3 instance variables, 6 properties, 21 instance methods, 3 class methods

## Instance variables

```
@"_SBStatusBarWindowRootViewController" _statusBarWindowRootViewController;
@"STUIStatusBar_Wrapper" _statusBar;
q _orientation;
```

## Properties

```
@property (T@"STUIStatusBar_Wrapper",&,N,V_statusBar) statusBar;
@property (Tq,N,V_orientation) orientation;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBStatusBarWindow _isSystemWindow];
+[SBStatusBarWindow _isSecure];
+[SBStatusBarWindow _defaultStatusBarSceneReferenceBounds];
```

## Instance methods

```
-[SBStatusBarWindow setOrientation:];
-[SBStatusBarWindow statusBar];
-[SBStatusBarWindow safeAreaInsets];
-[SBStatusBarWindow setStatusBar:];
-[SBStatusBarWindow _isStatusBarWindow];
-[SBStatusBarWindow windowSceneDidDisconnect:];
-[SBStatusBarWindow orientation];
-[SBStatusBarWindow _statusBarWindowBoundsForOrientation:];
-[SBStatusBarWindow hitTest:withEvent:];
-[SBStatusBarWindow _sbStatusBarWindowShouldRotate];
-[SBStatusBarWindow _rotate];
-[SBStatusBarWindow _statusBarWindowFrame];
-[SBStatusBarWindow _shouldForceTraitPropagationThroughHierarchy];
-[SBStatusBarWindow _canActAsKeyWindowForScreen:];
-[SBStatusBarWindow _setStatusBarWindowOrientation:];
-[SBStatusBarWindow setOrientation:animationParameters:];
-[SBStatusBarWindow windowSceneDidConnect:];
-[SBStatusBarWindow _shouldAdjustSizeClassesAndResizeWindow];
-[SBStatusBarWindow initWithFrame:];
-[SBStatusBarWindow _sbStatusBarWindowSupportedOrientations];
-[SBStatusBarWindow _initWithOrientation:];
```
