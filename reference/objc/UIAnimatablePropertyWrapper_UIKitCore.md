# `UIAnimatablePropertyWrapper`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIAnimatablePropertyBase`
- 1 instance variables, 4 properties, 11 instance methods, 2 class methods

## Instance variables

```
@"<UIBridgedAnimatableProperty>" _animatableProperty;
```

## Properties

```
@property (T@"<UIBridgedAnimatableProperty>",R,N,V_animatableProperty) animatableProperty;
@property (T@"UIView",W,N) view;
@property (TB,R,N,GisInvalidated) invalidated;
@property (TB,N,GisVelocityUsableForVFD) velocityUsableForVFD;
```

## Class methods

```
+[UIAnimatablePropertyWrapper makeSwiftFloatAnimatablePropertyWithView:useMainScreenFallbackAnimationManager:];
+[UIAnimatablePropertyWrapper makeSwiftVectorAnimatablePropertyWithView:useMainScreenFallbackAnimationManager:];
```

## Instance methods

```
-[UIAnimatablePropertyWrapper dealloc];
-[UIAnimatablePropertyWrapper setView:];
-[UIAnimatablePropertyWrapper isInvalidated];
-[UIAnimatablePropertyWrapper invalidate];
-[UIAnimatablePropertyWrapper view];
-[UIAnimatablePropertyWrapper __swiftTransformer];
-[UIAnimatablePropertyWrapper animatableProperty];
-[UIAnimatablePropertyWrapper initWithAnimatableProperty:];
-[UIAnimatablePropertyWrapper isVelocityUsableForVFD];
-[UIAnimatablePropertyWrapper setVelocityUsableForVFD:];
-[UIAnimatablePropertyWrapper set__swiftTransformer:];
```
