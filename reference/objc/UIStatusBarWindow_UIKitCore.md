# `UIStatusBarWindow`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIWindow`
- 2 instance variables, 0 properties, 15 instance methods, 5 class methods

## Instance variables

```
@"UIStatusBar" _statusBar;
q _orientation;
```

## Class methods

```
+[UIStatusBarWindow _isSystemWindow];
+[UIStatusBarWindow statusBarWindowFrame];
+[UIStatusBarWindow _convertRect:fromSceneReferenceSpaceToSceneSpaceWithOrientation:];
+[UIStatusBarWindow _defaultStatusBarSceneReferenceBounds];
+[UIStatusBarWindow _defaultStatusBarSceneReferenceBoundsForOrientation:];
```

## Instance methods

```
-[UIStatusBarWindow safeAreaInsets];
-[UIStatusBarWindow setStatusBar:];
-[UIStatusBarWindow _isStatusBarWindow];
-[UIStatusBarWindow orientation];
-[UIStatusBarWindow hitTest:withEvent:];
-[UIStatusBarWindow _statusBarFrameForOrientation:];
-[UIStatusBarWindow statusBarWindowFrame];
-[UIStatusBarWindow _rotate];
-[UIStatusBarWindow _shouldForceTraitPropagationThroughHierarchy];
-[UIStatusBarWindow _canActAsKeyWindowForScreen:];
-[UIStatusBarWindow setOrientation:animationParameters:];
-[UIStatusBarWindow _shouldAdjustSizeClassesAndResizeWindow];
-[UIStatusBarWindow initWithFrame:];
-[UIStatusBarWindow _defaultStatusBarSceneBoundsForOrientation:];
-[UIStatusBarWindow _didMoveFromScene:toScene:];
```
