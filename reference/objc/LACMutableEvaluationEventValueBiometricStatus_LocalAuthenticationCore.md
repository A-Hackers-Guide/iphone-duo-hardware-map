# `LACMutableEvaluationEventValueBiometricStatus`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LACEvaluationEventValueBiometricStatus`, `LACEvaluationEventValue`
- 3 instance variables, 5 properties, 10 instance methods, 0 class methods

## Instance variables

```
? lockoutError;
@"NSNumber" matchingStatus;
? payload;
```

## Properties

```
@property (T@"NSError",N,C) lockoutError;
@property (T@"NSNumber",N,&,VmatchingStatus) matchingStatus;
@property (T@"NSDictionary",N,C) payload;
@property (T@"NSString",N,R) description;
@property (Tq,N,R) hash;
```

## Instance methods

```
-[LACMutableEvaluationEventValueBiometricStatus init];
-[LACMutableEvaluationEventValueBiometricStatus payload];
-[LACMutableEvaluationEventValueBiometricStatus setPayload:];
-[LACMutableEvaluationEventValueBiometricStatus hash];
-[LACMutableEvaluationEventValueBiometricStatus description];
-[LACMutableEvaluationEventValueBiometricStatus isEqual:];
-[LACMutableEvaluationEventValueBiometricStatus lockoutError];
-[LACMutableEvaluationEventValueBiometricStatus matchingStatus];
-[LACMutableEvaluationEventValueBiometricStatus setLockoutError:];
-[LACMutableEvaluationEventValueBiometricStatus setMatchingStatus:];
```
