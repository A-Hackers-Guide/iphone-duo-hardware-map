# `LACEvaluationRequestDefault`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LACEvaluationRequest`
- 22 instance variables, 26 properties, 32 instance methods, 0 class methods

## Instance variables

```
B customUI;
B immediateSuccess;
B isInteractive;
B isPurposeApplePay;
B isPurposeInAppPayment;
B isPurposeUnlock;
B isRecoveringFromBiolockout;
I evaluationUserId;
I identifier;
@"NSData" acl;
@ aclOperation;
@"LACAnalyticsData" analyticsData;
@"<LACXPCClient>" client;
@"LACClientInfo" clientInfo;
@"NSUUID" contextID;
@"NSData" externalizedContext;
@"NSDictionary" options;
Q originatorId;
@"NSDictionary" payload;
q policy;
q purpose;
@"NSError" retryingForError;
```

## Properties

```
@property (Tq,R,N,Vpolicy) policy;
@property (T@"NSData",R,N,Vacl) acl;
@property (T@,R,N,VaclOperation) aclOperation;
@property (T@"NSDictionary",R,N,Voptions) options;
@property (T@"<LACXPCClient>",R,N,Vclient) client;
@property (TB,R,N,VcustomUI) customUI;
@property (T@"NSData",&,N,VexternalizedContext) externalizedContext;
@property (TI,R,N,VevaluationUserId) evaluationUserId;
@property (T@"NSDictionary",R,N,Vpayload) payload;
@property (Tq,R,N,Vpurpose) purpose;
@property (TB,R,N,VisPurposeApplePay) isPurposeApplePay;
@property (TB,R,N,VisPurposeUnlock) isPurposeUnlock;
@property (TB,R,N,VisPurposeInAppPayment) isPurposeInAppPayment;
@property (TB,R,N,VisInteractive) isInteractive;
@property (TB,N,GisImmediateSuccess,VimmediateSuccess) immediateSuccess;
@property (T@"NSError",&,N,VretryingForError) retryingForError;
@property (TB,R,N,VisRecoveringFromBiolockout) isRecoveringFromBiolockout;
@property (T@"LACAnalyticsData",&,N,VanalyticsData) analyticsData;
@property (T@"LACClientInfo",R,N,VclientInfo) clientInfo;
@property (T@"NSUUID",R,N,VcontextID) contextID;
@property (TQ,R,N,VoriginatorId) originatorId;
@property (TI,R,N,Videntifier) identifier;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[LACEvaluationRequestDefault acl];
-[LACEvaluationRequestDefault pause:event:];
-[LACEvaluationRequestDefault clientInfo];
-[LACEvaluationRequestDefault identifier];
-[LACEvaluationRequestDefault evaluationUserId];
-[LACEvaluationRequestDefault analyticsData];
-[LACEvaluationRequestDefault updateOptions:];
-[LACEvaluationRequestDefault isInteractive];
-[LACEvaluationRequestDefault isImmediateSuccess];
-[LACEvaluationRequestDefault payload];
-[LACEvaluationRequestDefault isEventPaused:];
-[LACEvaluationRequestDefault isRecoveringFromBiolockout];
-[LACEvaluationRequestDefault setImmediateSuccess:];
-[LACEvaluationRequestDefault externalizedContext];
-[LACEvaluationRequestDefault aclOperation];
-[LACEvaluationRequestDefault setAnalyticsData:];
-[LACEvaluationRequestDefault purpose];
-[LACEvaluationRequestDefault customUI];
-[LACEvaluationRequestDefault setExternalizedContext:];
-[LACEvaluationRequestDefault isPurposeInAppPayment];
-[LACEvaluationRequestDefault isPurposeUnlock];
-[LACEvaluationRequestDefault shallowCopy];
-[LACEvaluationRequestDefault options];
-[LACEvaluationRequestDefault contextID];
-[LACEvaluationRequestDefault originatorId];
-[LACEvaluationRequestDefault retryingForError];
-[LACEvaluationRequestDefault client];
-[LACEvaluationRequestDefault resetPausedEvents];
-[LACEvaluationRequestDefault updatePayload:];
-[LACEvaluationRequestDefault isPurposeApplePay];
-[LACEvaluationRequestDefault setRetryingForError:];
-[LACEvaluationRequestDefault policy];
```
