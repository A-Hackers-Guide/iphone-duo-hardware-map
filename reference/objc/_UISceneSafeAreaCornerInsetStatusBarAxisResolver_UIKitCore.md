# `_UISceneSafeAreaCornerInsetStatusBarAxisResolver`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UISceneSafeAreaCornerInsetResolver`
- 2 instance variables, 3 properties, 9 instance methods, 1 class methods

## Instance variables

```
horizontalResolver;
verticalResolver;
```

## Properties

```
@property (TB,N,R) containsOrientationDependentResolver;
@property (T@"NSString",N,R) description;
@property (Tq,N,R) hash;
```

## Class methods

```
+[_UISceneSafeAreaCornerInsetStatusBarAxisResolver supportsBSXPCSecureCoding];
```

## Instance methods

```
-[_UISceneSafeAreaCornerInsetStatusBarAxisResolver init];
-[_UISceneSafeAreaCornerInsetStatusBarAxisResolver safeAreaCornerInsetsForOrientation:statusBarHidden:statusBarAxis:];
-[_UISceneSafeAreaCornerInsetStatusBarAxisResolver containsOrientationDependentResolver];
-[_UISceneSafeAreaCornerInsetStatusBarAxisResolver hash];
-[_UISceneSafeAreaCornerInsetStatusBarAxisResolver description];
-[_UISceneSafeAreaCornerInsetStatusBarAxisResolver encodeWithBSXPCCoder:];
-[_UISceneSafeAreaCornerInsetStatusBarAxisResolver initWithBSXPCCoder:];
-[_UISceneSafeAreaCornerInsetStatusBarAxisResolver isEqual:];
-[_UISceneSafeAreaCornerInsetStatusBarAxisResolver initWithStatusBarHorizontalAxisResolver:statusBarVerticalAxisResolver:];
```
