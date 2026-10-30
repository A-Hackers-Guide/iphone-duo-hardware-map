# `BKMatchResultInfo`

- Image: [`/System/Library/PrivateFrameworks/BiometricKit.framework/BiometricKit`](../userland/System__Library__PrivateFrameworks__BiometricKit.framework__BiometricKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 10 instance methods, 0 class methods

## Instance variables

```
B _unlocked;
B _credentialAdded;
B _resultIgnored;
@"BKIdentity" _identity;
q _lockoutState;
```

## Properties

```
@property (T@"BKIdentity",&,N,V_identity) identity;
@property (Tq,N,V_lockoutState) lockoutState;
@property (TB,N,V_unlocked) unlocked;
@property (TB,N,V_credentialAdded) credentialAdded;
@property (TB,R,N,V_resultIgnored) resultIgnored;
```

## Instance methods

```
-[BKMatchResultInfo setIdentity:];
-[BKMatchResultInfo identity];
-[BKMatchResultInfo lockoutState];
-[BKMatchResultInfo setLockoutState:];
-[BKMatchResultInfo credentialAdded];
-[BKMatchResultInfo initWithServerIdentity:details:device:];
-[BKMatchResultInfo resultIgnored];
-[BKMatchResultInfo setCredentialAdded:];
-[BKMatchResultInfo setUnlocked:];
-[BKMatchResultInfo unlocked];
```
