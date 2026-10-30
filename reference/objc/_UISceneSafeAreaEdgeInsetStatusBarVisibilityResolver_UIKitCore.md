# `_UISceneSafeAreaEdgeInsetStatusBarVisibilityResolver`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UISceneSafeAreaEdgeInsetResolver`
- 2 instance variables, 5 properties, 11 instance methods, 1 class methods

## Instance variables

```
visibleResolver;
hiddenResolver;
```

## Properties

```
@property (TB,N,R) containsStatusBarAxisDependentResolver;
@property (TB,N,R) containsStatusBarVisibilityDependentResolver;
@property (TB,N,R) containsOrientationDependentResolver;
@property (T@"NSString",N,R) description;
@property (Tq,N,R) hash;
```

## Class methods

```
+[_UISceneSafeAreaEdgeInsetStatusBarVisibilityResolver supportsBSXPCSecureCoding];
```

## Instance methods

```
-[_UISceneSafeAreaEdgeInsetStatusBarVisibilityResolver containsStatusBarVisibilityDependentResolver];
-[_UISceneSafeAreaEdgeInsetStatusBarVisibilityResolver init];
-[_UISceneSafeAreaEdgeInsetStatusBarVisibilityResolver safeAreaEdgeInsetsForOrientation:statusBarHidden:statusBarAxis:];
-[_UISceneSafeAreaEdgeInsetStatusBarVisibilityResolver containsOrientationDependentResolver];
-[_UISceneSafeAreaEdgeInsetStatusBarVisibilityResolver hash];
-[_UISceneSafeAreaEdgeInsetStatusBarVisibilityResolver description];
-[_UISceneSafeAreaEdgeInsetStatusBarVisibilityResolver encodeWithBSXPCCoder:];
-[_UISceneSafeAreaEdgeInsetStatusBarVisibilityResolver initWithBSXPCCoder:];
-[_UISceneSafeAreaEdgeInsetStatusBarVisibilityResolver isEqual:];
-[_UISceneSafeAreaEdgeInsetStatusBarVisibilityResolver containsStatusBarAxisDependentResolver];
-[_UISceneSafeAreaEdgeInsetStatusBarVisibilityResolver initWithStatusBarVisibleResolver:statusBarHiddenResolver:];
```
