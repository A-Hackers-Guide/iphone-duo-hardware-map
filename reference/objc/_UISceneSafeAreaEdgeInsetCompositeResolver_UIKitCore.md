# `_UISceneSafeAreaEdgeInsetCompositeResolver`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UISceneSafeAreaEdgeInsetResolver`
- 1 instance variables, 5 properties, 11 instance methods, 1 class methods

## Instance variables

```
resolvers;
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
+[_UISceneSafeAreaEdgeInsetCompositeResolver supportsBSXPCSecureCoding];
```

## Instance methods

```
-[_UISceneSafeAreaEdgeInsetCompositeResolver containsStatusBarVisibilityDependentResolver];
-[_UISceneSafeAreaEdgeInsetCompositeResolver init];
-[_UISceneSafeAreaEdgeInsetCompositeResolver safeAreaEdgeInsetsForOrientation:statusBarHidden:statusBarAxis:];
-[_UISceneSafeAreaEdgeInsetCompositeResolver containsOrientationDependentResolver];
-[_UISceneSafeAreaEdgeInsetCompositeResolver initWithResolvers:];
-[_UISceneSafeAreaEdgeInsetCompositeResolver hash];
-[_UISceneSafeAreaEdgeInsetCompositeResolver description];
-[_UISceneSafeAreaEdgeInsetCompositeResolver encodeWithBSXPCCoder:];
-[_UISceneSafeAreaEdgeInsetCompositeResolver initWithBSXPCCoder:];
-[_UISceneSafeAreaEdgeInsetCompositeResolver isEqual:];
-[_UISceneSafeAreaEdgeInsetCompositeResolver containsStatusBarAxisDependentResolver];
```
