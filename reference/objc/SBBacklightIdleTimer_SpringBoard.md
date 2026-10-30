# `SBBacklightIdleTimer`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBIdleTimerBase`
- Protocols: `ITIdleTimerDelegate`, `BSDescriptionProviding`
- 5 instance variables, 8 properties, 30 instance methods, 0 class methods

## Instance variables

```
@"ITAttentionAwareIdleTimer" _attentionAwareTimer;
B _requiresManualReset;
@"SBIdleTimerDescriptor" _descriptor;
d _timeMultiplier;
Q _expectation;
```

## Properties

```
@property (Td,N,V_timeMultiplier) timeMultiplier;
@property (TQ,N,V_expectation) expectation;
@property (TB,N,V_requiresManualReset) requiresManualReset;
@property (T@"SBIdleTimerDescriptor",C,N,V_descriptor) descriptor;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBBacklightIdleTimer setDescriptor:];
-[SBBacklightIdleTimer isActivated];
-[SBBacklightIdleTimer setExpectation:];
-[SBBacklightIdleTimer _initWithAttentionAwareTimer:];
-[SBBacklightIdleTimer descriptor];
-[SBBacklightIdleTimer setActivated:];
-[SBBacklightIdleTimer succinctDescriptionBuilder];
-[SBBacklightIdleTimer _effectiveWarnTimeoutDuration];
-[SBBacklightIdleTimer init];
-[SBBacklightIdleTimer setTimeMultiplier:];
-[SBBacklightIdleTimer reset];
-[SBBacklightIdleTimer descriptionWithMultilinePrefix:];
-[SBBacklightIdleTimer idleTimerDidReset:forUserAttention:at:];
-[SBBacklightIdleTimer initWithConfigurationIdentifier:];
-[SBBacklightIdleTimer isDisabled];
-[SBBacklightIdleTimer succinctDescription];
-[SBBacklightIdleTimer _effectiveExpireTimeoutDuration];
-[SBBacklightIdleTimer timeMultiplier];
-[SBBacklightIdleTimer _stopIfManual];
-[SBBacklightIdleTimer requiresManualReset];
-[SBBacklightIdleTimer _reconfigureAttentionClientAndReset:];
-[SBBacklightIdleTimer idleTimer:attentionLostTimeoutDidExpire:];
-[SBBacklightIdleTimer description];
-[SBBacklightIdleTimer stateCaptureDescriptionWithMultilinePrefix:];
-[SBBacklightIdleTimer _resetExpectation];
-[SBBacklightIdleTimer setRequiresManualReset:];
-[SBBacklightIdleTimer _effectiveTimeoutForBaseTimeout:];
-[SBBacklightIdleTimer expectation];
-[SBBacklightIdleTimer _effectiveQuickUnwarnTimeoutDurationForWarnTimeout:];
-[SBBacklightIdleTimer descriptionBuilderWithMultilinePrefix:];
```
