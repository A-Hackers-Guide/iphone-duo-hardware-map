# `_UISceneSafeAreaCornerInsetCompositeResolver`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UISceneSafeAreaCornerInsetResolver`
- 1 instance variables, 3 properties, 9 instance methods, 1 class methods

## Instance variables

```
resolvers;
```

## Properties

```
@property (TB,N,R) containsOrientationDependentResolver;
@property (T@"NSString",N,R) description;
@property (Tq,N,R) hash;
```

## Class methods

```
+[_UISceneSafeAreaCornerInsetCompositeResolver supportsBSXPCSecureCoding];
```

## Instance methods

```
-[_UISceneSafeAreaCornerInsetCompositeResolver init];
-[_UISceneSafeAreaCornerInsetCompositeResolver safeAreaCornerInsetsForOrientation:statusBarHidden:statusBarAxis:];
-[_UISceneSafeAreaCornerInsetCompositeResolver containsOrientationDependentResolver];
-[_UISceneSafeAreaCornerInsetCompositeResolver initWithResolvers:];
-[_UISceneSafeAreaCornerInsetCompositeResolver hash];
-[_UISceneSafeAreaCornerInsetCompositeResolver description];
-[_UISceneSafeAreaCornerInsetCompositeResolver encodeWithBSXPCCoder:];
-[_UISceneSafeAreaCornerInsetCompositeResolver initWithBSXPCCoder:];
-[_UISceneSafeAreaCornerInsetCompositeResolver isEqual:];
```
