# `LACBiomeEvaluationEvent`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 7 properties, 9 instance methods, 0 class methods

## Instance variables

```
q _policy;
q _errorCode;
@"LACBiomeEvaluationMechanismState" _biometry;
@"LACBiomeEvaluationMechanismState" _passcode;
q _dtoState;
q _ratchetState;
@"NSString" _callerBundleId;
```

## Properties

```
@property (Tq,R,N,V_policy) policy;
@property (Tq,R,N,V_errorCode) errorCode;
@property (T@"LACBiomeEvaluationMechanismState",R,N,V_biometry) biometry;
@property (T@"LACBiomeEvaluationMechanismState",R,N,V_passcode) passcode;
@property (Tq,R,N,V_dtoState) dtoState;
@property (Tq,R,N,V_ratchetState) ratchetState;
@property (T@"NSString",R,N,V_callerBundleId) callerBundleId;
```

## Instance methods

```
-[LACBiomeEvaluationEvent dtoState];
-[LACBiomeEvaluationEvent biometry];
-[LACBiomeEvaluationEvent initWithPolicy:errorCode:biometry:passcode:dtoState:ratchetState:callerBundleID:];
-[LACBiomeEvaluationEvent errorCode];
-[LACBiomeEvaluationEvent passcode];
-[LACBiomeEvaluationEvent callerBundleId];
-[LACBiomeEvaluationEvent description];
-[LACBiomeEvaluationEvent ratchetState];
-[LACBiomeEvaluationEvent policy];
```
