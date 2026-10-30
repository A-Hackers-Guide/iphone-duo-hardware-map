# `LACPasscode`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 1 instance variables, 5 properties, 12 instance methods, 7 class methods

## Instance variables

```
q _type;
```

## Properties

```
@property (Tq,R,N,V_type) type;
@property (TB,R,N) isComplex;
@property (Tq,R,N) length;
@property (TB,R,N) hasFixedLength;
@property (Tq,R,N) complexityRating;
```

## Class methods

```
+[LACPasscode currentPasscode];
+[LACPasscode alphanumericType];
+[LACPasscode noneType];
+[LACPasscode numericCustomDigitsType];
+[LACPasscode numericFourDigitsType];
+[LACPasscode numericSixDigitsType];
+[LACPasscode typeAllowingString:];
```

## Instance methods

```
-[LACPasscode initWithType:];
-[LACPasscode length];
-[LACPasscode type];
-[LACPasscode hash];
-[LACPasscode description];
-[LACPasscode copyWithZone:];
-[LACPasscode isEqual:];
-[LACPasscode allowsLength:];
-[LACPasscode allowsString:];
-[LACPasscode complexityRating];
-[LACPasscode hasFixedLength];
-[LACPasscode isComplex];
```
