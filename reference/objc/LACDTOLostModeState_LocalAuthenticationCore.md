# `LACDTOLostModeState`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 9 instance methods, 1 class methods

## Instance variables

```
B _isInLostMode;
B _confirmed;
@"NSDate" _createdAt;
```

## Properties

```
@property (TB,R,N,V_isInLostMode) isInLostMode;
@property (T@"NSDate",R,N,V_createdAt) createdAt;
@property (TB,R,N,V_confirmed) confirmed;
```

## Class methods

```
+[LACDTOLostModeState nullInstance];
```

## Instance methods

```
-[LACDTOLostModeState confirmed];
-[LACDTOLostModeState isInLostMode];
-[LACDTOLostModeState isValid:];
-[LACDTOLostModeState description];
-[LACDTOLostModeState isEqual:];
-[LACDTOLostModeState createdAt];
-[LACDTOLostModeState initWithIsInLostMode:confirmed:];
-[LACDTOLostModeState initWithIsInLostMode:];
-[LACDTOLostModeState initWithIsInLostMode:confirmed:createdAt:];
```
