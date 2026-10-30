# `_UISceneSafeAreaEdgeInsetStatusBarAxisResolver`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UISceneSafeAreaEdgeInsetResolver`
- 2 instance variables, 5 properties, 11 instance methods, 1 class methods

## Instance variables

```
horizontalResolver;
verticalResolver;
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
+[_UISceneSafeAreaEdgeInsetStatusBarAxisResolver supportsBSXPCSecureCoding];
```

## Instance methods

```
-[_UISceneSafeAreaEdgeInsetStatusBarAxisResolver containsStatusBarVisibilityDependentResolver];
-[_UISceneSafeAreaEdgeInsetStatusBarAxisResolver init];
-[_UISceneSafeAreaEdgeInsetStatusBarAxisResolver safeAreaEdgeInsetsForOrientation:statusBarHidden:statusBarAxis:];
-[_UISceneSafeAreaEdgeInsetStatusBarAxisResolver containsOrientationDependentResolver];
-[_UISceneSafeAreaEdgeInsetStatusBarAxisResolver hash];
-[_UISceneSafeAreaEdgeInsetStatusBarAxisResolver description];
-[_UISceneSafeAreaEdgeInsetStatusBarAxisResolver encodeWithBSXPCCoder:];
-[_UISceneSafeAreaEdgeInsetStatusBarAxisResolver initWithBSXPCCoder:];
-[_UISceneSafeAreaEdgeInsetStatusBarAxisResolver isEqual:];
-[_UISceneSafeAreaEdgeInsetStatusBarAxisResolver containsStatusBarAxisDependentResolver];
-[_UISceneSafeAreaEdgeInsetStatusBarAxisResolver initWithStatusBarHorizontalAxisResolver:statusBarVerticalAxisResolver:];
```
