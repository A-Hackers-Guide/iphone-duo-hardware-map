# `SBFFluidBehaviorSettings`

- Image: [`/System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation`](../userland/System__Library__PrivateFrameworks__SpringBoardFoundation.framework__SpringBoardFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PTSettings`
- Protocols: `BSDescriptionProviding`, `BSXPCAutoCoding`, `UIViewSpringAnimationBehaviorDescribing`
- 17 instance variables, 21 properties, 54 instance methods, 3 class methods

## Instance variables

```
B _smoothingAndProjectionEnabled;
q _behaviorType;
@"NSString" _name;
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
@"PTFrameRateRangeSettings" _preferredFrameRateRange;
```

## Properties

```
@property (Tq,N,V_behaviorType) behaviorType;
@property (T@"NSString",C,N,V_name) name;
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
@property (T@"PTFrameRateRangeSettings",C,N,V_preferredFrameRateRange) preferredFrameRateRange;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBFFluidBehaviorSettings initialize];
+[SBFFluidBehaviorSettings settingsControllerModule];
+[SBFFluidBehaviorSettings _moduleWithSectionTitle:];
```

## Instance methods

```
-[SBFFluidBehaviorSettings inertialTargetSmoothingRatio];
-[SBFFluidBehaviorSettings setResponseSmoothing:];
-[SBFFluidBehaviorSettings retargetImpulse];
-[SBFFluidBehaviorSettings setTrackingRetargetImpulse:];
-[SBFFluidBehaviorSettings setRetargetImpulse:];
-[SBFFluidBehaviorSettings trackingDampingRatioSmoothing];
-[SBFFluidBehaviorSettings setInertialTargetSmoothingRatio:];
-[SBFFluidBehaviorSettings setInertialProjectionDeceleration:];
-[SBFFluidBehaviorSettings setTrackingDampingRatio:];
-[SBFFluidBehaviorSettings trackingResponse];
-[SBFFluidBehaviorSettings frameRateRange];
-[SBFFluidBehaviorSettings behaviorType];
-[SBFFluidBehaviorSettings setResponse:];
-[SBFFluidBehaviorSettings responseSmoothing];
-[SBFFluidBehaviorSettings trackingDampingRatio];
-[SBFFluidBehaviorSettings inertialProjectionDeceleration];
-[SBFFluidBehaviorSettings setSmoothingAndProjectionEnabled:];
-[SBFFluidBehaviorSettings smoothingAndProjectionEnabled];
-[SBFFluidBehaviorSettings succinctDescriptionBuilder];
-[SBFFluidBehaviorSettings trackingResponseSmoothing];
-[SBFFluidBehaviorSettings trackingRetargetImpulse];
-[SBFFluidBehaviorSettings setTrackingDampingRatioSmoothing:];
-[SBFFluidBehaviorSettings setTrackingResponseSmoothing:];
-[SBFFluidBehaviorSettings setDefaultCriticallyDampedValues];
-[SBFFluidBehaviorSettings parametersForTransitionFromState:toState:];
-[SBFFluidBehaviorSettings setDampingRatioSmoothing:];
-[SBFFluidBehaviorSettings setTrackingResponse:];
-[SBFFluidBehaviorSettings setDeceleration:];
-[SBFFluidBehaviorSettings setPreferredFrameRateRange:];
-[SBFFluidBehaviorSettings dampingRatioSmoothing];
-[SBFFluidBehaviorSettings setDampingRatio:];
-[SBFFluidBehaviorSettings setBehaviorType:];
-[SBFFluidBehaviorSettings deceleration];
-[SBFFluidBehaviorSettings dampingRatio];
-[SBFFluidBehaviorSettings BSAnimationSettings];
-[SBFFluidBehaviorSettings setFrameRateRange:highFrameRateReason:];
-[SBFFluidBehaviorSettings descriptionWithMultilinePrefix:];
-[SBFFluidBehaviorSettings preferredFrameRateRange];
-[SBFFluidBehaviorSettings succinctDescription];
-[SBFFluidBehaviorSettings setDefaultValues];
-[SBFFluidBehaviorSettings settlingDuration];
-[SBFFluidBehaviorSettings encodeWithCoder:];
-[SBFFluidBehaviorSettings hash];
-[SBFFluidBehaviorSettings description];
-[SBFFluidBehaviorSettings setName:];
-[SBFFluidBehaviorSettings copyWithZone:];
-[SBFFluidBehaviorSettings isEqual:];
-[SBFFluidBehaviorSettings name];
-[SBFFluidBehaviorSettings response];
-[SBFFluidBehaviorSettings descriptionBuilderWithMultilinePrefix:];
-[SBFFluidBehaviorSettings membersForCoder];
-[SBFFluidBehaviorSettings _effectiveTrackingDampingRatio];
-[SBFFluidBehaviorSettings _effectiveTrackingResponse];
-[SBFFluidBehaviorSettings _effectiveTrackingRetargetImpulse];
```
