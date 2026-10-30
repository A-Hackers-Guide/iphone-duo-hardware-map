# `LACBackgroundTaskResult`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 2 properties, 7 instance methods, 2 class methods

## Instance variables

```
@ _value;
@"NSError" _error;
```

## Properties

```
@property (T@,R,N,V_value) value;
@property (T@"NSError",R,N,V_error) error;
```

## Class methods

```
+[LACBackgroundTaskResult busyResultWithIdentifier:];
+[LACBackgroundTaskResult timeoutResultWithIdentifier:timeout:];
```

## Instance methods

```
-[LACBackgroundTaskResult value];
-[LACBackgroundTaskResult initWithError:];
-[LACBackgroundTaskResult error];
-[LACBackgroundTaskResult initWithValue:];
-[LACBackgroundTaskResult initWithValue:error:];
-[LACBackgroundTaskResult description];
-[LACBackgroundTaskResult isEqual:];
```
