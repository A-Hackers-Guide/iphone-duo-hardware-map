# `CSConcreteUnlockRequest`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CSUnlockRequest`
- 5 instance variables, 9 properties, 10 instance methods, 0 class methods

## Instance variables

```
B wantsBiometricPresentation;
B confirmedNotInPocket;
i source;
i intent;
@"NSString" name;
```

## Properties

```
@property (T@"NSString",C,N,Vname) name;
@property (Ti,N,Vsource) source;
@property (Ti,N,Vintent) intent;
@property (TB,N,VwantsBiometricPresentation) wantsBiometricPresentation;
@property (TB,N,VconfirmedNotInPocket) confirmedNotInPocket;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[CSConcreteUnlockRequest setIntent:];
-[CSConcreteUnlockRequest intent];
-[CSConcreteUnlockRequest setConfirmedNotInPocket:];
-[CSConcreteUnlockRequest setSource:];
-[CSConcreteUnlockRequest wantsBiometricPresentation];
-[CSConcreteUnlockRequest setName:];
-[CSConcreteUnlockRequest confirmedNotInPocket];
-[CSConcreteUnlockRequest setWantsBiometricPresentation:];
-[CSConcreteUnlockRequest name];
-[CSConcreteUnlockRequest source];
```
