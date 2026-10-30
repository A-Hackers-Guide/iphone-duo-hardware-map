# `BKEnrollOperation`

- Image: [`/System/Library/PrivateFrameworks/BiometricKit.framework/BiometricKit`](../userland/System__Library__PrivateFrameworks__BiometricKit.framework__BiometricKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BKOperation`
- 3 instance variables, 4 properties, 17 instance methods, 0 class methods

## Instance variables

```
I _userID;
@"NSData" _credentialSet;
@"BKAccessoryGroup" _accessoryGroup;
```

## Properties

```
@property (T@"<BKEnrollOperationDelegate>",W,D,N) delegate;
@property (TI,N,V_userID) userID;
@property (T@"NSData",C,N,V_credentialSet) credentialSet;
@property (T@"BKAccessoryGroup",&,N,V_accessoryGroup) accessoryGroup;
```

## Instance methods

```
-[BKEnrollOperation statusMessage:client:];
-[BKEnrollOperation userID];
-[BKEnrollOperation setUserID:];
-[BKEnrollOperation initWithDevice:];
-[BKEnrollOperation statusMessage:details:client:];
-[BKEnrollOperation enrollUpdate:client:];
-[BKEnrollOperation startBioOperation:reply:];
-[BKEnrollOperation enrollResult:details:client:];
-[BKEnrollOperation enrollFeedback:client:];
-[BKEnrollOperation setCredentialSet:];
-[BKEnrollOperation accessoryGroup];
-[BKEnrollOperation credentialSet];
-[BKEnrollOperation enrollResultInfoWithServerIdentity:details:];
-[BKEnrollOperation operationInterrupted];
-[BKEnrollOperation optionsDictionaryWithError:];
-[BKEnrollOperation processEnrollFailReason:];
-[BKEnrollOperation setAccessoryGroup:];
```
