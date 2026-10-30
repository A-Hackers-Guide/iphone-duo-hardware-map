# `LACEvaluationResult`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 7 instance methods, 4 class methods

## Instance variables

```
q _rawValue;
@"NSDictionary" _value;
@"NSError" _error;
@"<LACEvaluationRequest>" _request;
```

## Properties

```
@property (Tq,R,N,V_rawValue) rawValue;
@property (T@"NSDictionary",R,N,V_value) value;
@property (T@"NSError",R,N,V_error) error;
@property (T@"<LACEvaluationRequest>",R,N,V_request) request;
```

## Class methods

```
+[LACEvaluationResult resultWithNext:];
+[LACEvaluationResult resultWithFailure:];
+[LACEvaluationResult resultWithRetry:error:];
+[LACEvaluationResult resultWithSuccess:];
```

## Instance methods

```
-[LACEvaluationResult rawValue];
-[LACEvaluationResult value];
-[LACEvaluationResult error];
-[LACEvaluationResult request];
-[LACEvaluationResult description];
-[LACEvaluationResult isEqual:];
-[LACEvaluationResult initWithValue:error:request:];
```
