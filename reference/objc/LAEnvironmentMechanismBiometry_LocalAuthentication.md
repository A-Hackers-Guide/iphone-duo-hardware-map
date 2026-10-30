# `LAEnvironmentMechanismBiometry`

- Image: [`/System/Library/Frameworks/LocalAuthentication.framework/LocalAuthentication`](../userland/System__Library__Frameworks__LocalAuthentication.framework__LocalAuthentication.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `LAEnvironmentMechanism`
- 1 instance variables, 6 properties, 9 instance methods, 0 class methods

## Instance variables

```
q _approvalState;
```

## Properties

```
@property (Tq,N,V_approvalState) approvalState;
@property (Tq,R,N) biometryType;
@property (TB,R,N) isEnrolled;
@property (TB,R,N) isLockedOut;
@property (T@"NSData",R,N) stateHash;
@property (TB,R,N) builtInSensorInaccessible;
```

## Instance methods

```
-[LAEnvironmentMechanismBiometry stateHash];
-[LAEnvironmentMechanismBiometry biometryType];
-[LAEnvironmentMechanismBiometry approvalState];
-[LAEnvironmentMechanismBiometry isLockedOut];
-[LAEnvironmentMechanismBiometry isEnrolled];
-[LAEnvironmentMechanismBiometry builtInSensorInaccessible];
-[LAEnvironmentMechanismBiometry initWithCoreMechanism:];
-[LAEnvironmentMechanismBiometry setApprovalState:];
-[LAEnvironmentMechanismBiometry unsaltedStateHash];
```
