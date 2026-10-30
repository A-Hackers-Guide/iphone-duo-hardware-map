# `CTLazuliOperationResult`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 4 instance variables, 4 properties, 15 instance methods, 1 class methods

## Instance variables

```
B _didSucceed;
@"NSError" _error;
@"CTLazuliOperationID" _operation;
@"CTLazuliOperationError" _errorParameter;
```

## Properties

```
@property (TB,N,V_didSucceed) didSucceed;
@property (T@"NSError",C,N,V_error) error;
@property (T@"CTLazuliOperationID",C,N,V_operation) operation;
@property (T@"CTLazuliOperationError",C,N,V_errorParameter) errorParameter;
```

## Class methods

```
+[CTLazuliOperationResult supportsSecureCoding];
```

## Instance methods

```
-[CTLazuliOperationResult setOperation:];
-[CTLazuliOperationResult setError:];
-[CTLazuliOperationResult operation];
-[CTLazuliOperationResult error];
-[CTLazuliOperationResult encodeWithCoder:];
-[CTLazuliOperationResult description];
-[CTLazuliOperationResult initWithCoder:];
-[CTLazuliOperationResult copyWithZone:];
-[CTLazuliOperationResult isEqual:];
-[CTLazuliOperationResult didSucceed];
-[CTLazuliOperationResult setDidSucceed:];
-[CTLazuliOperationResult errorParameter];
-[CTLazuliOperationResult initWithReflection:];
-[CTLazuliOperationResult isEqualToCTLazuliOperationResult:];
-[CTLazuliOperationResult setErrorParameter:];
```
