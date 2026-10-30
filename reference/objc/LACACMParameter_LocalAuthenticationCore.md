# `LACACMParameter`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 2 properties, 5 instance methods, 5 class methods

## Instance variables

```
@"NSString" _description;
I _type;
@"NSData" _data;
```

## Properties

```
@property (TI,R,N,V_type) type;
@property (T@"NSData",R,N,V_data) data;
```

## Class methods

```
+[LACACMParameter acmParameterSecureIntentSupport];
+[LACACMParameter acmParameterDoNotStartDTOTimers];
+[LACACMParameter acmParameterWithMaxContinuityAge:];
+[LACACMParameter acmParameterWithTimeOffset:];
+[LACACMParameter acmParameterWithUserId:];
```

## Instance methods

```
-[LACACMParameter data];
-[LACACMParameter type];
-[LACACMParameter description];
-[LACACMParameter copyWithZone:];
-[LACACMParameter initWithACMParamType:bytes:length:description:];
```
