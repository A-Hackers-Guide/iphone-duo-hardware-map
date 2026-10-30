# `_UISceneSafeAreaCornerInsetStatusBarVisibilityResolver`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UISceneSafeAreaCornerInsetResolver`
- 2 instance variables, 3 properties, 9 instance methods, 1 class methods

## Instance variables

```
visibleResolver;
hiddenResolver;
```

## Properties

```
@property (TB,N,R) containsOrientationDependentResolver;
@property (T@"NSString",N,R) description;
@property (Tq,N,R) hash;
```

## Class methods

```
+[_UISceneSafeAreaCornerInsetStatusBarVisibilityResolver supportsBSXPCSecureCoding];
```

## Instance methods

```
-[_UISceneSafeAreaCornerInsetStatusBarVisibilityResolver init];
-[_UISceneSafeAreaCornerInsetStatusBarVisibilityResolver safeAreaCornerInsetsForOrientation:statusBarHidden:statusBarAxis:];
-[_UISceneSafeAreaCornerInsetStatusBarVisibilityResolver containsOrientationDependentResolver];
-[_UISceneSafeAreaCornerInsetStatusBarVisibilityResolver hash];
-[_UISceneSafeAreaCornerInsetStatusBarVisibilityResolver description];
-[_UISceneSafeAreaCornerInsetStatusBarVisibilityResolver encodeWithBSXPCCoder:];
-[_UISceneSafeAreaCornerInsetStatusBarVisibilityResolver initWithBSXPCCoder:];
-[_UISceneSafeAreaCornerInsetStatusBarVisibilityResolver isEqual:];
-[_UISceneSafeAreaCornerInsetStatusBarVisibilityResolver initWithStatusBarVisibleResolver:statusBarHiddenResolver:];
```
