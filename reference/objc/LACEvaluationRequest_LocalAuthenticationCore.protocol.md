# `LACEvaluationRequest` (protocol)

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `LACClientRequest`
- 0 instance variables, 18 properties, 29 instance methods, 0 class methods

## Properties

```
@property (Tq,R,N) policy;
@property (T@"NSData",R,N) acl;
@property (T@,R,N) aclOperation;
@property (T@"NSDictionary",R,N) options;
@property (T@"<LACXPCClient>",R,N) client;
@property (TB,R,N) customUI;
@property (T@"NSData",&,N) externalizedContext;
@property (TI,R,N) evaluationUserId;
@property (T@"NSDictionary",R,N) payload;
@property (Tq,R,N) purpose;
@property (TB,R,N) isPurposeApplePay;
@property (TB,R,N) isPurposeUnlock;
@property (TB,R,N) isPurposeInAppPayment;
@property (TB,R,N) isInteractive;
@property (TB,N,GisImmediateSuccess) immediateSuccess;
@property (T@"NSError",&,N) retryingForError;
@property (TB,R,N) isRecoveringFromBiolockout;
@property (T@"LACAnalyticsData",&,N) analyticsData;
```

## Instance methods

```
-[LACEvaluationRequest acl];
-[LACEvaluationRequest pause:event:];
-[LACEvaluationRequest evaluationUserId];
-[LACEvaluationRequest analyticsData];
-[LACEvaluationRequest updateOptions:];
-[LACEvaluationRequest isInteractive];
-[LACEvaluationRequest isImmediateSuccess];
-[LACEvaluationRequest payload];
-[LACEvaluationRequest isEventPaused:];
-[LACEvaluationRequest isRecoveringFromBiolockout];
-[LACEvaluationRequest setImmediateSuccess:];
-[LACEvaluationRequest externalizedContext];
-[LACEvaluationRequest aclOperation];
-[LACEvaluationRequest setAnalyticsData:];
-[LACEvaluationRequest purpose];
-[LACEvaluationRequest shallowCopyWithAdditionalOptions:];
-[LACEvaluationRequest customUI];
-[LACEvaluationRequest setExternalizedContext:];
-[LACEvaluationRequest isPurposeInAppPayment];
-[LACEvaluationRequest isPurposeUnlock];
-[LACEvaluationRequest shallowCopy];
-[LACEvaluationRequest options];
-[LACEvaluationRequest retryingForError];
-[LACEvaluationRequest client];
-[LACEvaluationRequest resetPausedEvents];
-[LACEvaluationRequest updatePayload:];
-[LACEvaluationRequest isPurposeApplePay];
-[LACEvaluationRequest setRetryingForError:];
-[LACEvaluationRequest policy];
```
