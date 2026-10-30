# `UIViewSpringAnimationBehaviorSettings`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PTSettings`
- Protocols: `UIViewSpringAnimationBehaviorDescribing`
- 1 instance variables, 18 properties, 42 instance methods, 2 class methods

## Instance variables

```
wrappedSettings;
```

## Properties

```
@property (Tq,N) behaviorType;
@property (T@"NSString",N,C) name;
@property (Td,N) deceleration;
@property (Td,N) dampingRatio;
@property (Td,N) response;
@property (Td,N) retargetImpulse;
@property (Td,N) trackingDampingRatio;
@property (Td,N) trackingResponse;
@property (Td,N) trackingRetargetImpulse;
@property (TB,N) smoothingAndProjectionEnabled;
@property (Td,N) dampingRatioSmoothing;
@property (Td,N) responseSmoothing;
@property (Td,N) trackingDampingRatioSmoothing;
@property (Td,N) trackingResponseSmoothing;
@property (Td,N) inertialTargetSmoothingRatio;
@property (Td,N) inertialProjectionDeceleration;
@property (T@"PTFrameRateRangeSettings",N,&) preferredFrameRateRange;
@property (T@"NSString",N,R) description;
```

## Class methods

```
+[UIViewSpringAnimationBehaviorSettings settingsControllerModule];
+[UIViewSpringAnimationBehaviorSettings _moduleWithSectionTitle:];
```

## Instance methods

```
-[UIViewSpringAnimationBehaviorSettings inertialTargetSmoothingRatio];
-[UIViewSpringAnimationBehaviorSettings setResponseSmoothing:];
-[UIViewSpringAnimationBehaviorSettings retargetImpulse];
-[UIViewSpringAnimationBehaviorSettings setTrackingRetargetImpulse:];
-[UIViewSpringAnimationBehaviorSettings setRetargetImpulse:];
-[UIViewSpringAnimationBehaviorSettings trackingDampingRatioSmoothing];
-[UIViewSpringAnimationBehaviorSettings setInertialTargetSmoothingRatio:];
-[UIViewSpringAnimationBehaviorSettings setInertialProjectionDeceleration:];
-[UIViewSpringAnimationBehaviorSettings setTrackingDampingRatio:];
-[UIViewSpringAnimationBehaviorSettings trackingResponse];
-[UIViewSpringAnimationBehaviorSettings frameRateRange];
-[UIViewSpringAnimationBehaviorSettings behaviorType];
-[UIViewSpringAnimationBehaviorSettings setResponse:];
-[UIViewSpringAnimationBehaviorSettings responseSmoothing];
-[UIViewSpringAnimationBehaviorSettings trackingDampingRatio];
-[UIViewSpringAnimationBehaviorSettings inertialProjectionDeceleration];
-[UIViewSpringAnimationBehaviorSettings setSmoothingAndProjectionEnabled:];
-[UIViewSpringAnimationBehaviorSettings smoothingAndProjectionEnabled];
-[UIViewSpringAnimationBehaviorSettings trackingResponseSmoothing];
-[UIViewSpringAnimationBehaviorSettings trackingRetargetImpulse];
-[UIViewSpringAnimationBehaviorSettings setTrackingDampingRatioSmoothing:];
-[UIViewSpringAnimationBehaviorSettings setTrackingResponseSmoothing:];
-[UIViewSpringAnimationBehaviorSettings setDefaultCriticallyDampedValues];
-[UIViewSpringAnimationBehaviorSettings parametersForTransitionFromState:toState:];
-[UIViewSpringAnimationBehaviorSettings setDampingRatioSmoothing:];
-[UIViewSpringAnimationBehaviorSettings setTrackingResponse:];
-[UIViewSpringAnimationBehaviorSettings setDeceleration:];
-[UIViewSpringAnimationBehaviorSettings setPreferredFrameRateRange:];
-[UIViewSpringAnimationBehaviorSettings dampingRatioSmoothing];
-[UIViewSpringAnimationBehaviorSettings setDampingRatio:];
-[UIViewSpringAnimationBehaviorSettings setBehaviorType:];
-[UIViewSpringAnimationBehaviorSettings deceleration];
-[UIViewSpringAnimationBehaviorSettings dampingRatio];
-[UIViewSpringAnimationBehaviorSettings BSAnimationSettings];
-[UIViewSpringAnimationBehaviorSettings setFrameRateRange:highFrameRateReason:];
-[UIViewSpringAnimationBehaviorSettings preferredFrameRateRange];
-[UIViewSpringAnimationBehaviorSettings settlingDuration];
-[UIViewSpringAnimationBehaviorSettings initWithDefaultValues];
-[UIViewSpringAnimationBehaviorSettings description];
-[UIViewSpringAnimationBehaviorSettings setName:];
-[UIViewSpringAnimationBehaviorSettings name];
-[UIViewSpringAnimationBehaviorSettings response];
```
