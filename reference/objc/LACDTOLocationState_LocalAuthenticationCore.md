# `LACDTOLocationState`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 8 instance methods, 2 class methods

## Instance variables

```
@"NSDate" _createdAt;
B _confirmed;
q _rawValue;
```

## Properties

```
@property (T@"NSDate",R,N,V_createdAt) createdAt;
@property (TB,R,N,V_confirmed) confirmed;
@property (Tq,R,N,V_rawValue) rawValue;
```

## Class methods

```
+[LACDTOLocationState nullInstance];
+[LACDTOLocationState strictLocationState];
```

## Instance methods

```
-[LACDTOLocationState confirmed];
-[LACDTOLocationState rawValue];
-[LACDTOLocationState isValid:];
-[LACDTOLocationState description];
-[LACDTOLocationState isEqual:];
-[LACDTOLocationState createdAt];
-[LACDTOLocationState initWithRawValue:confirmed:];
-[LACDTOLocationState initWithRawValue:confirmed:createdAt:];
```
