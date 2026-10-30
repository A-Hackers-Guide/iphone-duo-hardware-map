# `_UISceneSafeAreaClientComponent`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `FBSSceneComponent`
- 2 instance variables, 5 properties, 10 instance methods, 0 class methods

## Instance variables

```
{?="hasStatusBarAxisDependentSafeAreaEdgeInsets"b1"hasStatusBarVisibilityDependentSafeAreaEdgeInsets"b1"hasOrientationDependentSafeAreaEdgeInsets"b1"hasOrientationDependentSafeAreaCornerInsets"b1} _flags;
B _safeAreaEdgeInsetsPopulated;
```

## Properties

```
@property (TB,R,N,V_safeAreaEdgeInsetsPopulated) safeAreaEdgeInsetsPopulated;
@property (TB,R,N) hasStatusBarAxisDependentSafeAreaEdgeInsets;
@property (TB,R,N) hasStatusBarVisibilityDependentSafeAreaEdgeInsets;
@property (TB,R,N) hasOrientationDependentSafeAreaEdgeInsets;
@property (TB,R,N) hasOrientationDependentSafeAreaCornerInsets;
```

## Instance methods

```
-[_UISceneSafeAreaClientComponent hasOrientationDependentSafeAreaCornerInsets];
-[_UISceneSafeAreaClientComponent hasStatusBarAxisDependentSafeAreaEdgeInsets];
-[_UISceneSafeAreaClientComponent scene:didUpdateSettings:];
-[_UISceneSafeAreaClientComponent settings];
-[_UISceneSafeAreaClientComponent safeAreaCornerInsetsForOrientation:statusBarHidden:statusBarAxis:];
-[_UISceneSafeAreaClientComponent safeAreaEdgeInsetsForOrientation:statusBarHidden:statusBarAxis:];
-[_UISceneSafeAreaClientComponent hasOrientationDependentSafeAreaEdgeInsets];
-[_UISceneSafeAreaClientComponent hasStatusBarVisibilityDependentSafeAreaEdgeInsets];
-[_UISceneSafeAreaClientComponent safeAreaEdgeInsetsPopulated];
-[_UISceneSafeAreaClientComponent updateSettings:];
```
