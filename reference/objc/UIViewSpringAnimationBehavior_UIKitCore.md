# `UIViewSpringAnimationBehavior`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIViewSpringAnimationBehaviorDescribing`
- 1 instance variables, 4 properties, 14 instance methods, 1 class methods

## Instance variables

```
wrappedBehavior;
```

## Properties

```
@property (Td,N) dampingRatio;
@property (Td,N) response;
@property (Td,N) inertialTargetSmoothing;
@property (Td,N) inertialProjectionDeceleration;
```

## Class methods

```
+[UIViewSpringAnimationBehavior behaviorWithDampingRatio:response:];
```

## Instance methods

```
-[UIViewSpringAnimationBehavior initWithDampingRatio:response:];
-[UIViewSpringAnimationBehavior setInertialProjectionDeceleration:];
-[UIViewSpringAnimationBehavior setTrackingDampingRatio:response:dampingRatioSmoothing:responseSmoothing:];
-[UIViewSpringAnimationBehavior setResponse:];
-[UIViewSpringAnimationBehavior inertialProjectionDeceleration];
-[UIViewSpringAnimationBehavior init];
-[UIViewSpringAnimationBehavior setDampingRatio:response:];
-[UIViewSpringAnimationBehavior parametersForTransitionFromState:toState:];
-[UIViewSpringAnimationBehavior setDampingRatio:];
-[UIViewSpringAnimationBehavior dampingRatio];
-[UIViewSpringAnimationBehavior setInertialTargetSmoothing:];
-[UIViewSpringAnimationBehavior setDefaultValues];
-[UIViewSpringAnimationBehavior inertialTargetSmoothing];
-[UIViewSpringAnimationBehavior response];
```
