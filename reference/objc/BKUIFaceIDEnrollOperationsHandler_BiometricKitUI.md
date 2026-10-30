# `BKUIFaceIDEnrollOperationsHandler`

- Image: [`/System/Library/PrivateFrameworks/BiometricKitUI.framework/BiometricKitUI`](../userland/System__Library__PrivateFrameworks__BiometricKitUI.framework__BiometricKitUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BKEnrollOperationDelegate`, `BKEnrollPearlOperationDelegate`
- 26 instance variables, 25 properties, 81 instance methods, 1 class methods

## Instance variables

```
@"SFClient" _sharingclient;
@"LAContext" _authContext;
B _enrollOperationInProgress;
@"NSObject<OS_dispatch_queue>" _enrollStartStopQueue;
@"NSDate" _lastFaceFoundDate;
B _userSelectedUseAccessibilityEnrollment;
B _suspend;
B _inbuddy;
B _canStartEnrollmentOperation;
B _glassesFound;
B _glassesEnforcementError;
B _centerBinComplete;
B _supportsPeriocularEnrollment;
@"<BKUIPearlEnrollOperationsDelegate>" _operationsDelegate;
@"NSString" _credential;
@"NSMutableArray" _poseStatus;
Q _enrollmentConfiguration;
q _enrollmentType;
@"BKDevicePearl" _device;
@"BKIdentity" _identity;
@"NSData" _externalizedAuthContext;
d _bioKitCompletionPercentage;
@"BKEnrollPearlOperation" _enrollOperation;
@"BKUIMatchVerifyPearlOperation" _matchOperation;
@? _matchUserThenDoSingleEnrollmentCompletion;
@"BKUIAnalyticsManager" _analyticsManager;
```

## Properties

```
@property (T@"BKEnrollPearlOperation",&,N,V_enrollOperation) enrollOperation;
@property (T@"BKDevicePearl",&,N,V_device) device;
@property (TB,N,V_supportsPeriocularEnrollment) supportsPeriocularEnrollment;
@property (TB,N,V_glassesEnforcementError) glassesEnforcementError;
@property (Td,N,V_bioKitCompletionPercentage) bioKitCompletionPercentage;
@property (TB,N,V_canStartEnrollmentOperation) canStartEnrollmentOperation;
@property (T@"BKUIAnalyticsManager",&,V_analyticsManager) analyticsManager;
@property (T@"<BKUIPearlEnrollOperationsDelegate>",W,N,V_operationsDelegate) operationsDelegate;
@property (T@"NSString",C,N,V_credential) credential;
@property (TB,N,GisSuspended,V_suspend) suspend;
@property (TB,N,V_inbuddy) inbuddy;
@property (T@"NSMutableArray",&,N,V_poseStatus) poseStatus;
@property (TQ,N,V_enrollmentConfiguration) enrollmentConfiguration;
@property (Tq,N,V_enrollmentType) enrollmentType;
@property (T@"BKIdentity",&,N,V_identity) identity;
@property (T@"NSData",&,N,V_externalizedAuthContext) externalizedAuthContext;
@property (TB,N,V_glassesFound) glassesFound;
@property (TB,N,V_centerBinComplete) centerBinComplete;
@property (TB,N,V_userSelectedUseAccessibilityEnrollment) userSelectedUseAccessibilityEnrollment;
@property (T@"BKUIMatchVerifyPearlOperation",&,N,V_matchOperation) matchOperation;
@property (T@?,C,N,V_matchUserThenDoSingleEnrollmentCompletion) matchUserThenDoSingleEnrollmentCompletion;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BKUIFaceIDEnrollOperationsHandler handlersForEnrollmentConfiguration:inBuddy:delegate:credential:externalizedAuthContext:];
```

## Instance methods

```
-[BKUIFaceIDEnrollOperationsHandler setAnalyticsManager:];
-[BKUIFaceIDEnrollOperationsHandler credential];
-[BKUIFaceIDEnrollOperationsHandler setDevice:];
-[BKUIFaceIDEnrollOperationsHandler isSuspended];
-[BKUIFaceIDEnrollOperationsHandler device];
-[BKUIFaceIDEnrollOperationsHandler init];
-[BKUIFaceIDEnrollOperationsHandler setIdentity:];
-[BKUIFaceIDEnrollOperationsHandler identity];
-[BKUIFaceIDEnrollOperationsHandler operation:faceDetectStateChanged:];
-[BKUIFaceIDEnrollOperationsHandler isActive];
-[BKUIFaceIDEnrollOperationsHandler analyticsManager];
-[BKUIFaceIDEnrollOperationsHandler setCredential:];
-[BKUIFaceIDEnrollOperationsHandler enrollOperation:failedWithReason:];
-[BKUIFaceIDEnrollOperationsHandler enrollOperation:finishedWithEnrollResult:];
-[BKUIFaceIDEnrollOperationsHandler enrollOperation:percentCompleted:];
-[BKUIFaceIDEnrollOperationsHandler enrollOperation:progressedWithInfo:];
-[BKUIFaceIDEnrollOperationsHandler enrollmentType];
-[BKUIFaceIDEnrollOperationsHandler setEnrollmentType:];
-[BKUIFaceIDEnrollOperationsHandler retryPressed];
-[BKUIFaceIDEnrollOperationsHandler setSuspend:];
-[BKUIFaceIDEnrollOperationsHandler enrollOperation];
-[BKUIFaceIDEnrollOperationsHandler inbuddy];
-[BKUIFaceIDEnrollOperationsHandler _cleanupEnroll:];
-[BKUIFaceIDEnrollOperationsHandler _removeIdentity];
-[BKUIFaceIDEnrollOperationsHandler setCanStartEnrollmentOperation:];
-[BKUIFaceIDEnrollOperationsHandler _cleanupEnroll];
-[BKUIFaceIDEnrollOperationsHandler _completeOperationWithError:];
-[BKUIFaceIDEnrollOperationsHandler _matchOperationPreflightCheck:];
-[BKUIFaceIDEnrollOperationsHandler _startOperationWithError:];
-[BKUIFaceIDEnrollOperationsHandler _validateEnrolledPoses:];
-[BKUIFaceIDEnrollOperationsHandler advanceEnrollmentState];
-[BKUIFaceIDEnrollOperationsHandler bioKitCompletionPercentage];
-[BKUIFaceIDEnrollOperationsHandler bkIdentities];
-[BKUIFaceIDEnrollOperationsHandler canStartEnrollmentOperation];
-[BKUIFaceIDEnrollOperationsHandler cancelCurrentEnrollmentOperationIfUnfinished];
-[BKUIFaceIDEnrollOperationsHandler cancelEnroll];
-[BKUIFaceIDEnrollOperationsHandler cancelEnrollForRotation];
-[BKUIFaceIDEnrollOperationsHandler cancelEnrollPreserveIdentity];
-[BKUIFaceIDEnrollOperationsHandler centerBinComplete];
-[BKUIFaceIDEnrollOperationsHandler cleanupEnroll];
-[BKUIFaceIDEnrollOperationsHandler completeCurrentEnrollOperationWithError:];
-[BKUIFaceIDEnrollOperationsHandler enrollmentConfiguration];
-[BKUIFaceIDEnrollOperationsHandler externalizedAuthContext];
-[BKUIFaceIDEnrollOperationsHandler getAuthContextForCredentialError:];
-[BKUIFaceIDEnrollOperationsHandler getAuthContextForCredentialError:authContext:];
-[BKUIFaceIDEnrollOperationsHandler glassesEnforcementError];
-[BKUIFaceIDEnrollOperationsHandler glassesFound];
-[BKUIFaceIDEnrollOperationsHandler glassesRequirement];
-[BKUIFaceIDEnrollOperationsHandler initWithBKPearlEnrollmentType:];
-[BKUIFaceIDEnrollOperationsHandler isEnrollmentAugmentationOnly];
-[BKUIFaceIDEnrollOperationsHandler isEnrollmentOrMatchActive];
-[BKUIFaceIDEnrollOperationsHandler matchOperation];
-[BKUIFaceIDEnrollOperationsHandler matchOperation:failedToMatchWithUserPositionSubstate:operationCompleteAction:];
-[BKUIFaceIDEnrollOperationsHandler matchUserForGlassesPhaseEnrollmentWithCompletionAction:];
-[BKUIFaceIDEnrollOperationsHandler matchUserForSecondPhaseEnrollmentWithCompletionAction:];
-[BKUIFaceIDEnrollOperationsHandler matchUserThenDoSingleEnrollmentCompletion];
-[BKUIFaceIDEnrollOperationsHandler matchUserThenDoSingleEnrollmentWithExisitingEnrollmentConfigCompletionAction:];
-[BKUIFaceIDEnrollOperationsHandler needsCancellationForState:];
-[BKUIFaceIDEnrollOperationsHandler operationsDelegate];
-[BKUIFaceIDEnrollOperationsHandler poseStatus];
-[BKUIFaceIDEnrollOperationsHandler retryOperation];
-[BKUIFaceIDEnrollOperationsHandler setBioKitCompletionPercentage:];
-[BKUIFaceIDEnrollOperationsHandler setCenterBinComplete:];
-[BKUIFaceIDEnrollOperationsHandler setEnrollOperation:];
-[BKUIFaceIDEnrollOperationsHandler setEnrollmentConfiguration:];
-[BKUIFaceIDEnrollOperationsHandler setExternalizedAuthContext:];
-[BKUIFaceIDEnrollOperationsHandler setGlassesEnforcementError:];
-[BKUIFaceIDEnrollOperationsHandler setGlassesFound:];
-[BKUIFaceIDEnrollOperationsHandler setInbuddy:];
-[BKUIFaceIDEnrollOperationsHandler setMatchOperation:];
-[BKUIFaceIDEnrollOperationsHandler setMatchUserThenDoSingleEnrollmentCompletion:];
-[BKUIFaceIDEnrollOperationsHandler setOperationsDelegate:];
-[BKUIFaceIDEnrollOperationsHandler setPoseStatus:];
-[BKUIFaceIDEnrollOperationsHandler setSupportsPeriocularEnrollment:];
-[BKUIFaceIDEnrollOperationsHandler setUserSelectedUseAccessibilityEnrollment:];
-[BKUIFaceIDEnrollOperationsHandler shouldShowRetryUI];
-[BKUIFaceIDEnrollOperationsHandler showAddGlassesButton];
-[BKUIFaceIDEnrollOperationsHandler startEnroll];
-[BKUIFaceIDEnrollOperationsHandler startEnrollForEnrollmentType:glassesRequirement:identity:operationStartedActionBlock:];
-[BKUIFaceIDEnrollOperationsHandler supportsPeriocularEnrollment];
-[BKUIFaceIDEnrollOperationsHandler userSelectedUseAccessibilityEnrollment];
```
