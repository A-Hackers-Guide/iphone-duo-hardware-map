# `CSUnlockRequest` (protocol)

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 5 properties, 10 instance methods, 0 class methods

## Properties

```
@property (T@"NSString",C,N) name;
@property (Ti,N) source;
@property (Ti,N) intent;
@property (TB,N) wantsBiometricPresentation;
@property (TB,N) confirmedNotInPocket;
```

## Instance methods

```
-[CSUnlockRequest setIntent:];
-[CSUnlockRequest intent];
-[CSUnlockRequest setConfirmedNotInPocket:];
-[CSUnlockRequest setSource:];
-[CSUnlockRequest wantsBiometricPresentation];
-[CSUnlockRequest setName:];
-[CSUnlockRequest confirmedNotInPocket];
-[CSUnlockRequest setWantsBiometricPresentation:];
-[CSUnlockRequest name];
-[CSUnlockRequest source];
```
