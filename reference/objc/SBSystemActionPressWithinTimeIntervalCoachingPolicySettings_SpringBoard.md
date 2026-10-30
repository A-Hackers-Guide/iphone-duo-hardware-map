# `SBSystemActionPressWithinTimeIntervalCoachingPolicySettings`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PTSettings`
- 3 instance variables, 3 properties, 7 instance methods, 1 class methods

## Instance variables

```
Q _presentationThresholdForActionsWithStatefulPreviews;
Q _presentationThresholdForActionsWithStatelessPreviews;
d _timeInterval;
```

## Properties

```
@property (TQ,N,V_presentationThresholdForActionsWithStatefulPreviews) presentationThresholdForActionsWithStatefulPreviews;
@property (TQ,N,V_presentationThresholdForActionsWithStatelessPreviews) presentationThresholdForActionsWithStatelessPreviews;
@property (Td,N,V_timeInterval) timeInterval;
```

## Class methods

```
+[SBSystemActionPressWithinTimeIntervalCoachingPolicySettings settingsControllerModule];
```

## Instance methods

```
-[SBSystemActionPressWithinTimeIntervalCoachingPolicySettings timeInterval];
-[SBSystemActionPressWithinTimeIntervalCoachingPolicySettings setDefaultValues];
-[SBSystemActionPressWithinTimeIntervalCoachingPolicySettings setTimeInterval:];
-[SBSystemActionPressWithinTimeIntervalCoachingPolicySettings presentationThresholdForActionsWithStatefulPreviews];
-[SBSystemActionPressWithinTimeIntervalCoachingPolicySettings presentationThresholdForActionsWithStatelessPreviews];
-[SBSystemActionPressWithinTimeIntervalCoachingPolicySettings setPresentationThresholdForActionsWithStatefulPreviews:];
-[SBSystemActionPressWithinTimeIntervalCoachingPolicySettings setPresentationThresholdForActionsWithStatelessPreviews:];
```
