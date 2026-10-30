# `CEKFluidBehaviorSettings`

- Image: [`/System/Library/PrivateFrameworks/CameraEditKit.framework/CameraEditKit`](../userland/System__Library__PrivateFrameworks__CameraEditKit.framework__CameraEditKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `UIViewSpringAnimationBehaviorDescribing`
- 18 instance variables, 16 properties, 45 instance methods, 0 class methods

## Instance variables

```
{CAFrameRateRange="minimum"f"maximum"f"preferred"f} _frameRateRange;
I _highFrameRateReason;
B _smoothingAndProjectionEnabled;
q _behaviorType;
d _deceleration;
d _dampingRatio;
d _response;
d _retargetImpulse;
d _trackingDampingRatio;
d _trackingResponse;
d _trackingRetargetImpulse;
d _dampingRatioSmoothing;
d _responseSmoothing;
d _trackingDampingRatioSmoothing;
d _trackingResponseSmoothing;
d _inertialTargetSmoothingRatio;
d _inertialProjectionDeceleration;
@"NSString" _name;
```

## Properties

```
@property (Tq,N,V_behaviorType) behaviorType;
@property (Td,N,V_deceleration) deceleration;
@property (Td,N,V_dampingRatio) dampingRatio;
@property (Td,N,V_response) response;
@property (Td,N,V_retargetImpulse) retargetImpulse;
@property (Td,N,V_trackingDampingRatio) trackingDampingRatio;
@property (Td,N,V_trackingResponse) trackingResponse;
@property (Td,N,V_trackingRetargetImpulse) trackingRetargetImpulse;
@property (TB,N,V_smoothingAndProjectionEnabled) smoothingAndProjectionEnabled;
@property (Td,N,V_dampingRatioSmoothing) dampingRatioSmoothing;
@property (Td,N,V_responseSmoothing) responseSmoothing;
@property (Td,N,V_trackingDampingRatioSmoothing) trackingDampingRatioSmoothing;
@property (Td,N,V_trackingResponseSmoothing) trackingResponseSmoothing;
@property (Td,N,V_inertialTargetSmoothingRatio) inertialTargetSmoothingRatio;
@property (Td,N,V_inertialProjectionDeceleration) inertialProjectionDeceleration;
@property (T@"NSString",C,N,V_name) name;
```

## Instance methods

```
-[CEKFluidBehaviorSettings inertialTargetSmoothingRatio];
-[CEKFluidBehaviorSettings setResponseSmoothing:];
-[CEKFluidBehaviorSettings retargetImpulse];
-[CEKFluidBehaviorSettings setTrackingRetargetImpulse:];
-[CEKFluidBehaviorSettings setRetargetImpulse:];
-[CEKFluidBehaviorSettings trackingDampingRatioSmoothing];
-[CEKFluidBehaviorSettings setInertialTargetSmoothingRatio:];
-[CEKFluidBehaviorSettings setInertialProjectionDeceleration:];
-[CEKFluidBehaviorSettings setTrackingDampingRatio:];
-[CEKFluidBehaviorSettings trackingResponse];
-[CEKFluidBehaviorSettings frameRateRange];
-[CEKFluidBehaviorSettings behaviorType];
-[CEKFluidBehaviorSettings setResponse:];
-[CEKFluidBehaviorSettings responseSmoothing];
-[CEKFluidBehaviorSettings trackingDampingRatio];
-[CEKFluidBehaviorSettings inertialProjectionDeceleration];
-[CEKFluidBehaviorSettings setSmoothingAndProjectionEnabled:];
-[CEKFluidBehaviorSettings smoothingAndProjectionEnabled];
-[CEKFluidBehaviorSettings trackingResponseSmoothing];
-[CEKFluidBehaviorSettings trackingRetargetImpulse];
-[CEKFluidBehaviorSettings setTrackingDampingRatioSmoothing:];
-[CEKFluidBehaviorSettings setTrackingResponseSmoothing:];
-[CEKFluidBehaviorSettings setDefaultCriticallyDampedValues];
-[CEKFluidBehaviorSettings parametersForTransitionFromState:toState:];
-[CEKFluidBehaviorSettings setDampingRatioSmoothing:];
-[CEKFluidBehaviorSettings setTrackingResponse:];
-[CEKFluidBehaviorSettings setDeceleration:];
-[CEKFluidBehaviorSettings dampingRatioSmoothing];
-[CEKFluidBehaviorSettings setDampingRatio:];
-[CEKFluidBehaviorSettings setBehaviorType:];
-[CEKFluidBehaviorSettings deceleration];
-[CEKFluidBehaviorSettings dampingRatio];
-[CEKFluidBehaviorSettings setFrameRateRange:highFrameRateReason:];
-[CEKFluidBehaviorSettings highFrameRateReason];
-[CEKFluidBehaviorSettings setDefaultValues];
-[CEKFluidBehaviorSettings settlingDuration];
-[CEKFluidBehaviorSettings hash];
-[CEKFluidBehaviorSettings setName:];
-[CEKFluidBehaviorSettings copyWithZone:];
-[CEKFluidBehaviorSettings isEqual:];
-[CEKFluidBehaviorSettings name];
-[CEKFluidBehaviorSettings response];
-[CEKFluidBehaviorSettings _effectiveTrackingDampingRatio];
-[CEKFluidBehaviorSettings _effectiveTrackingResponse];
-[CEKFluidBehaviorSettings _effectiveTrackingRetargetImpulse];
```
