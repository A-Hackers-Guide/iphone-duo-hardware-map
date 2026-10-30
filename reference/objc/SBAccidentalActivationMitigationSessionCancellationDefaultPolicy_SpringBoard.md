# `SBAccidentalActivationMitigationSessionCancellationDefaultPolicy`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBAttentionAwarenessClientDelegate`, `SBLiftToWakeObserver`, `SBSAccidentalActivationMitigationSessionCancellationPolicy`
- 7 instance variables, 6 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"<SBSAccidentalActivationMitigationSession>" _session;
@"SBCaptureButtonSuppressionManager" _suppressionManager;
@"SBLiftToWakeController" _liftToWakeController;
@"AWAttentionAwarenessConfiguration" _idleUserIntentAwarenessConfiguration;
@"SBAttentionAwarenessClient" _idleUserIntentAwarenessClient;
q _eventType;
@"NSString" _eventReason;
```

## Properties

```
@property (Tq,R,N,V_eventType) eventType;
@property (T@"NSString",R,C,N,V_eventReason) eventReason;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBAccidentalActivationMitigationSessionCancellationDefaultPolicy clientDidResetForUserAttention:withEvent:];
-[SBAccidentalActivationMitigationSessionCancellationDefaultPolicy eventType];
-[SBAccidentalActivationMitigationSessionCancellationDefaultPolicy client:attentionLostTimeoutDidExpire:forConfigurationGeneration:withAssociatedObject:];
-[SBAccidentalActivationMitigationSessionCancellationDefaultPolicy dealloc];
-[SBAccidentalActivationMitigationSessionCancellationDefaultPolicy liftToWakeController:didObserveTransition:deviceOrientation:];
-[SBAccidentalActivationMitigationSessionCancellationDefaultPolicy initWithSession:];
-[SBAccidentalActivationMitigationSessionCancellationDefaultPolicy accidentalActivationMitigationSessionStateDidChange:];
-[SBAccidentalActivationMitigationSessionCancellationDefaultPolicy _startEvaluatingWhetherActivationWasIntentional];
-[SBAccidentalActivationMitigationSessionCancellationDefaultPolicy _stopEvaluatingWhetherActivationWasIntentional];
-[SBAccidentalActivationMitigationSessionCancellationDefaultPolicy eventReason];
-[SBAccidentalActivationMitigationSessionCancellationDefaultPolicy initWithSession:suppressionManager:liftToWakeController:];
```
