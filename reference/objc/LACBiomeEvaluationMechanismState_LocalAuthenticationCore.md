# `LACBiomeEvaluationMechanismState`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 7 instance methods, 0 class methods

## Instance variables

```
B _available;
B _started;
B _success;
B _lockout;
I _generation;
```

## Properties

```
@property (TB,R,N,V_available) available;
@property (TB,R,N,V_started) started;
@property (TB,R,N,V_success) success;
@property (TB,R,N,V_lockout) lockout;
@property (TI,R,N,V_generation) generation;
```

## Instance methods

```
-[LACBiomeEvaluationMechanismState success];
-[LACBiomeEvaluationMechanismState started];
-[LACBiomeEvaluationMechanismState available];
-[LACBiomeEvaluationMechanismState generation];
-[LACBiomeEvaluationMechanismState description];
-[LACBiomeEvaluationMechanismState lockout];
-[LACBiomeEvaluationMechanismState initAvailable:started:success:lockout:generation:];
```
