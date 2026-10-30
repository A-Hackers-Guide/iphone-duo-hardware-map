# `BKMatchOperation`

- Image: [`/System/Library/PrivateFrameworks/BiometricKit.framework/BiometricKit`](../userland/System__Library__PrivateFrameworks__BiometricKit.framework__BiometricKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BKOperation`
- 8 instance variables, 9 properties, 25 instance methods, 0 class methods

## Instance variables

```
B _stopOnSuccess;
B _captureOnly;
q _purpose;
@"NSNumber" _userID;
@"NSArray" _selectedIdentities;
q _priority;
@"NSData" _credentialSet;
q _useCase;
```

## Properties

```
@property (T@"<BKMatchOperationDelegate>",W,D,N) delegate;
@property (Tq,N,V_purpose) purpose;
@property (T@"NSNumber",&,N,V_userID) userID;
@property (T@"NSArray",C,N,V_selectedIdentities) selectedIdentities;
@property (Tq,N,V_priority) priority;
@property (T@"NSData",C,N,V_credentialSet) credentialSet;
@property (Tq,N,V_useCase) useCase;
@property (TB,N,V_stopOnSuccess) stopOnSuccess;
@property (TB,N,V_captureOnly) captureOnly;
```

## Instance methods

```
-[BKMatchOperation useCase];
-[BKMatchOperation statusMessage:client:];
-[BKMatchOperation userID];
-[BKMatchOperation priority];
-[BKMatchOperation setUserID:];
-[BKMatchOperation setPurpose:];
-[BKMatchOperation initWithDevice:];
-[BKMatchOperation setCaptureOnly:];
-[BKMatchOperation setPriority:];
-[BKMatchOperation dealloc];
-[BKMatchOperation startBioOperation:reply:];
-[BKMatchOperation purpose];
-[BKMatchOperation setUseCase:];
-[BKMatchOperation matchResult:details:client:];
-[BKMatchOperation captureOnly];
-[BKMatchOperation setStopOnSuccess:];
-[BKMatchOperation setCredentialSet:];
-[BKMatchOperation credentialSet];
-[BKMatchOperation matchResultInfoWithServerIdentity:details:];
-[BKMatchOperation operationInterrupted];
-[BKMatchOperation optionsDictionaryWithError:];
-[BKMatchOperation processMatchFailReason:];
-[BKMatchOperation selectedIdentities];
-[BKMatchOperation setSelectedIdentities:];
-[BKMatchOperation stopOnSuccess];
```
