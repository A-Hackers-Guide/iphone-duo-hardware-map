# `BKUIMatchVerifyPearlOperation`

- Image: [`/System/Library/PrivateFrameworks/BiometricKitUI.framework/BiometricKitUI`](../userland/System__Library__PrivateFrameworks__BiometricKitUI.framework__BiometricKitUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BKMatchPearlOperationDelegate`
- 16 instance variables, 20 properties, 45 instance methods, 0 class methods

## Instance variables

```
B _delegateUIAtNeedsPosition;
B _faceDetected;
B _matchFailed;
i _lastErrorousSubState;
i _substate;
i _currentUIDelegateDisplaySubState;
@? _matchOperationDidMatch;
@"BKMatchPearlOperation" _matchOperation;
@"BKUIFaceIDEnrollOperationsHandler" _weakHandler;
@"<BKUIPearlEnrollOperationsDelegate>" _operationsDelegate;
q _failReason;
@"BKIdentity" _identity;
@"BKDevicePearl" _device;
@"BKIdentity" _matchedIdentity;
@"NSData" _credentialSet;
Q _enrollmentConfiguration;
```

## Properties

```
@property (T@?,C,N,V_matchOperationDidMatch) matchOperationDidMatch;
@property (T@"BKMatchPearlOperation",&,N,V_matchOperation) matchOperation;
@property (T@"BKUIFaceIDEnrollOperationsHandler",W,N,V_weakHandler) weakHandler;
@property (T@"<BKUIPearlEnrollOperationsDelegate>",W,N,V_operationsDelegate) operationsDelegate;
@property (Ti,N,V_lastErrorousSubState) lastErrorousSubState;
@property (Ti,N,V_substate) substate;
@property (Ti,N,V_currentUIDelegateDisplaySubState) currentUIDelegateDisplaySubState;
@property (Tq,N,V_failReason) failReason;
@property (T@"BKIdentity",&,N,V_identity) identity;
@property (T@"BKDevicePearl",&,N,V_device) device;
@property (T@"BKIdentity",&,N,V_matchedIdentity) matchedIdentity;
@property (T@"NSData",&,N,V_credentialSet) credentialSet;
@property (TQ,N,V_enrollmentConfiguration) enrollmentConfiguration;
@property (TB,N,V_delegateUIAtNeedsPosition) delegateUIAtNeedsPosition;
@property (TB,N,V_faceDetected) faceDetected;
@property (TB,N,V_matchFailed) matchFailed;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[BKUIMatchVerifyPearlOperation setDevice:];
-[BKUIMatchVerifyPearlOperation device];
-[BKUIMatchVerifyPearlOperation init];
-[BKUIMatchVerifyPearlOperation substate];
-[BKUIMatchVerifyPearlOperation isInProgress];
-[BKUIMatchVerifyPearlOperation setIdentity:];
-[BKUIMatchVerifyPearlOperation identity];
-[BKUIMatchVerifyPearlOperation operation:faceDetectStateChanged:];
-[BKUIMatchVerifyPearlOperation matchOperation:failedWithReason:];
-[BKUIMatchVerifyPearlOperation matchOperation:matchedWithResult:];
-[BKUIMatchVerifyPearlOperation matchOperation:presenceDetectedInLockout:];
-[BKUIMatchVerifyPearlOperation operation:stateChanged:];
-[BKUIMatchVerifyPearlOperation failReason];
-[BKUIMatchVerifyPearlOperation matchOperation:providedFeedback:];
-[BKUIMatchVerifyPearlOperation setCredentialSet:];
-[BKUIMatchVerifyPearlOperation faceDetected];
-[BKUIMatchVerifyPearlOperation matchedIdentity];
-[BKUIMatchVerifyPearlOperation credentialSet];
-[BKUIMatchVerifyPearlOperation setFaceDetected:];
-[BKUIMatchVerifyPearlOperation setMatchedIdentity:];
-[BKUIMatchVerifyPearlOperation setSubstate:];
-[BKUIMatchVerifyPearlOperation setMatchFailed:];
-[BKUIMatchVerifyPearlOperation setWeakHandler:];
-[BKUIMatchVerifyPearlOperation cancelMatchOperation];
-[BKUIMatchVerifyPearlOperation currentUIDelegateDisplaySubState];
-[BKUIMatchVerifyPearlOperation delegateUIAtNeedsPosition];
-[BKUIMatchVerifyPearlOperation enrollmentConfiguration];
-[BKUIMatchVerifyPearlOperation lastErrorousSubState];
-[BKUIMatchVerifyPearlOperation matchFailed];
-[BKUIMatchVerifyPearlOperation matchOperation];
-[BKUIMatchVerifyPearlOperation matchOperationDidMatch];
-[BKUIMatchVerifyPearlOperation moveEnrollStateToNeedsPositioning:];
-[BKUIMatchVerifyPearlOperation operationsDelegate];
-[BKUIMatchVerifyPearlOperation retryMatchOperation];
-[BKUIMatchVerifyPearlOperation setCurrentUIDelegateDisplaySubState:];
-[BKUIMatchVerifyPearlOperation setDelegateUIAtNeedsPosition:];
-[BKUIMatchVerifyPearlOperation setEnrollmentConfiguration:];
-[BKUIMatchVerifyPearlOperation setFailReason:];
-[BKUIMatchVerifyPearlOperation setLastErrorousSubState:];
-[BKUIMatchVerifyPearlOperation setMatchOperation:];
-[BKUIMatchVerifyPearlOperation setMatchOperationDidMatch:];
-[BKUIMatchVerifyPearlOperation setOperationsDelegate:];
-[BKUIMatchVerifyPearlOperation startMatchOperationWithDevice:identity:credential:withConfiguration:matchOperationActionBlock:];
-[BKUIMatchVerifyPearlOperation substateForFaceDetectionFeedBack:];
-[BKUIMatchVerifyPearlOperation weakHandler];
```
