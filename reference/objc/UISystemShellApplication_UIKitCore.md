# `UISystemShellApplication`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIApplication`
- 4 instance variables, 0 properties, 17 instance methods, 2 class methods

## Instance variables

```
@"FBDisplayLayoutTransition" _interfaceOrientationTransition;
q _lastPublishedInterfaceOrientation;
@"FBSDisplayIdentity" _lastPublishedDisplayIdentity;
@ _didFinishLaunchingObserver;
```

## Class methods

```
+[UISystemShellApplication registerAsSystemApp];
+[UISystemShellApplication rendersLocally];
```

## Instance methods

```
-[UISystemShellApplication isSuspended];
-[UISystemShellApplication init];
-[UISystemShellApplication canOpenURL:];
-[UISystemShellApplication isFrontBoard];
-[UISystemShellApplication _openURL:];
-[UISystemShellApplication _interfaceOrientationRotationDirectionFromOrientation:toOrientation:];
-[UISystemShellApplication _saveSnapshotWithName:];
-[UISystemShellApplication handleDoubleHeightStatusBarTapWithStyleOverride:];
-[UISystemShellApplication handleStatusBarHoverActionForRegion:];
-[UISystemShellApplication isSuspendedEventsOnly];
-[UISystemShellApplication isSuspendedUnderLock];
-[UISystemShellApplication noteActiveInterfaceOrientationDidChangeToOrientation:willAnimateWithSettings:fromOrientation:];
-[UISystemShellApplication noteActiveInterfaceOrientationDidChangeToOrientation:willAnimateWithSettings:fromOrientation:screen:];
-[UISystemShellApplication noteActiveInterfaceOrientationWillChangeToOrientation:];
-[UISystemShellApplication noteActiveInterfaceOrientationWillChangeToOrientation:screen:];
-[UISystemShellApplication resetIdleTimerAndUndim];
-[UISystemShellApplication startupInterfaceOrientation];
```
