# `BKExtendEnrollTouchIDOperation`

- Image: [`/System/Library/PrivateFrameworks/BiometricKit.framework/BiometricKit`](../userland/System__Library__PrivateFrameworks__BiometricKit.framework__BiometricKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BKOperation`
- 2 instance variables, 3 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"BKIdentity" _identity;
@"NSData" _credentialSet;
```

## Properties

```
@property (T@"<BKExtendEnrollTouchIDOperationDelegate>",W,D,N) delegate;
@property (T@"BKIdentity",&,N,V_identity) identity;
@property (T@"NSData",C,N,V_credentialSet) credentialSet;
```

## Instance methods

```
-[BKExtendEnrollTouchIDOperation statusMessage:client:];
-[BKExtendEnrollTouchIDOperation homeButtonPressed:];
-[BKExtendEnrollTouchIDOperation startBioOperation:reply:];
-[BKExtendEnrollTouchIDOperation setIdentity:];
-[BKExtendEnrollTouchIDOperation identity];
-[BKExtendEnrollTouchIDOperation matchResult:details:client:];
-[BKExtendEnrollTouchIDOperation setCredentialSet:];
-[BKExtendEnrollTouchIDOperation credentialSet];
```
