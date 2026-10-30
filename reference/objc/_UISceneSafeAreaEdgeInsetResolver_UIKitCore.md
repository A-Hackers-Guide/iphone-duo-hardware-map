# `_UISceneSafeAreaEdgeInsetResolver`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSXPCSecureCoding`
- 0 instance variables, 3 properties, 9 instance methods, 1 class methods

## Properties

```
@property (TB,N,R) containsStatusBarAxisDependentResolver;
@property (TB,N,R) containsStatusBarVisibilityDependentResolver;
@property (TB,N,R) containsOrientationDependentResolver;
```

## Class methods

```
+[_UISceneSafeAreaEdgeInsetResolver supportsBSXPCSecureCoding];
```

## Instance methods

```
-[_UISceneSafeAreaEdgeInsetResolver containsStatusBarVisibilityDependentResolver];
-[_UISceneSafeAreaEdgeInsetResolver init];
-[_UISceneSafeAreaEdgeInsetResolver safeAreaEdgeInsetsForOrientation:];
-[_UISceneSafeAreaEdgeInsetResolver safeAreaEdgeInsetsForOrientation:statusBarHidden:statusBarAxis:];
-[_UISceneSafeAreaEdgeInsetResolver containsOrientationDependentResolver];
-[_UISceneSafeAreaEdgeInsetResolver encodeWithBSXPCCoder:];
-[_UISceneSafeAreaEdgeInsetResolver initWithBSXPCCoder:];
-[_UISceneSafeAreaEdgeInsetResolver safeAreaEdgeInsetsForOrientation:statusBarHidden:];
-[_UISceneSafeAreaEdgeInsetResolver containsStatusBarAxisDependentResolver];
```
