# `LACDTOPendingPolicyEvaluationController`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LACDarwinNotificationCenterObserver`, `LACDTONotificationManagerDelegate`, `LACDTOPendingPolicyEvaluationController`, `LACDTOPolicyEvaluationControllerObserver`, `LACDTOEventHandler`
- 11 instance variables, 5 properties, 45 instance methods, 0 class methods

## Instance variables

```
@"<LACDTORatchetStateProvider>" _ratchetStateProvider;
@"<LACDTORatchetHandler>" _ratchetHandler;
@"<LACDTODeviceInfoProvider>" _device;
@"<LACDTOPolicyEvaluationIdentifierFactory>" _evaluationIdentifierFactory;
@"<LACDTOPendingPolicyEvaluationStore>" _evaluationStore;
@"<LACDTOTelemetryReporting>" _telemetry;
@"NSObject<OS_dispatch_queue>" _workQueue;
@"NSHashTable" _observers;
B _shouldPostRestartRatchetPrompt;
@"NSString" _activeEvaluationIdentifier;
@"LACDTONotificationManager" _notificationManager;
```

## Properties

```
@property (T@"LACDTONotificationManager",&,N,V_notificationManager) notificationManager;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[LACDTOPendingPolicyEvaluationController notificationManager];
-[LACDTOPendingPolicyEvaluationController removeObserver:];
-[LACDTOPendingPolicyEvaluationController dealloc];
-[LACDTOPendingPolicyEvaluationController setNotificationManager:];
-[LACDTOPendingPolicyEvaluationController addObserver:];
-[LACDTOPendingPolicyEvaluationController _rescheduleNotifications];
-[LACDTOPendingPolicyEvaluationController startController];
-[LACDTOPendingPolicyEvaluationController _forEachObserver:];
-[LACDTOPendingPolicyEvaluationController _scheduleNotificationForPendingEvaluationRecord:after:validity:];
-[LACDTOPendingPolicyEvaluationController _addPendingEvaluationRecord:currentState:];
-[LACDTOPendingPolicyEvaluationController _addPendingEvaluationRecordForRequest:currentState:];
-[LACDTOPendingPolicyEvaluationController _canFinishPendingEvaluationsForRatchetState:];
-[LACDTOPendingPolicyEvaluationController _cancelPreviousNotificationForPendingEvaluationRecord:scheduledOnly:];
-[LACDTOPendingPolicyEvaluationController _cancelPreviousNotificationForRatchetRestartWithRatchetState:];
-[LACDTOPendingPolicyEvaluationController _checkIsRatchetStateIn:completion:];
-[LACDTOPendingPolicyEvaluationController _checkShouldAddPendingEvaluationRecordForRequest:completion:];
-[LACDTOPendingPolicyEvaluationController _checkShouldKeepPendingEvaluationRecordForResult:completion:];
-[LACDTOPendingPolicyEvaluationController _coolOffStartedTimestampForIdentifier:currentState:];
-[LACDTOPendingPolicyEvaluationController _handleRatchetStateChanged:];
-[LACDTOPendingPolicyEvaluationController _handleSwitchToCoolOffState:];
-[LACDTOPendingPolicyEvaluationController _handleSwitchToFinalState:];
-[LACDTOPendingPolicyEvaluationController _hasPendingEvaluationRecordForRequest:];
-[LACDTOPendingPolicyEvaluationController _isRatchetRestartRequest:];
-[LACDTOPendingPolicyEvaluationController _loadPendingEvaluations];
-[LACDTOPendingPolicyEvaluationController _postNotificationForRatchetRestartIfNeeded];
-[LACDTOPendingPolicyEvaluationController _pruneInvalidatedEvaluations];
-[LACDTOPendingPolicyEvaluationController _prunePendingEvaluationsWithUUID:];
-[LACDTOPendingPolicyEvaluationController _registerNotificationObservers];
-[LACDTOPendingPolicyEvaluationController _removePendingEvaluationRecordForRequest:completion:];
-[LACDTOPendingPolicyEvaluationController _removePendingEvaluationRecordWithIdentifier:completion:];
-[LACDTOPendingPolicyEvaluationController _reportRatchetCompletionAttemptIfNeeded:];
-[LACDTOPendingPolicyEvaluationController _resetRatchetWithReason:completion:];
-[LACDTOPendingPolicyEvaluationController _restartRatchetForInvalidatedEvaluations];
-[LACDTOPendingPolicyEvaluationController _scheduleNotificationForRatchetRestart];
-[LACDTOPendingPolicyEvaluationController _shouldPrunePendingEvaluation:uuid:];
-[LACDTOPendingPolicyEvaluationController _updatePendingEvaluationsWithBlock:];
-[LACDTOPendingPolicyEvaluationController _updatePendingEvaluationsWithUpdateBlock:observerFilter:];
-[LACDTOPendingPolicyEvaluationController cancelPendingEvaluationForClient:ratchetIdentifier:reason:completion:];
-[LACDTOPendingPolicyEvaluationController handleEvent:sender:];
-[LACDTOPendingPolicyEvaluationController initWithRatchetStateProvider:ratchetHandler:device:evaluationIdentifierFactory:persistentStore:telemetry:workQueue:];
-[LACDTOPendingPolicyEvaluationController notificationCenter:didReceiveNotification:];
-[LACDTOPendingPolicyEvaluationController notificationManager:didRespondToNewSecurityDelayRequiredNotification:action:completionHandler:];
-[LACDTOPendingPolicyEvaluationController notificationManager:didRespondToSecurityDelayEndedNotification:action:completionHandler:];
-[LACDTOPendingPolicyEvaluationController policyController:didFinishPolicyEvaluation:result:];
-[LACDTOPendingPolicyEvaluationController policyController:willStartPolicyEvaluation:];
```
