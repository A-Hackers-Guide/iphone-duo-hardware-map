# `LACSharedMode`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 2 properties, 6 instance methods, 1 class methods

## Instance variables

```
B _active;
B _confirmed;
```

## Properties

```
@property (TB,R,N,GisActive,V_active) active;
@property (TB,R,N,GisConfirmed,V_confirmed) confirmed;
```

## Class methods

```
+[LACSharedMode defaultSharedMode];
```

## Instance methods

```
-[LACSharedMode description];
-[LACSharedMode isActive];
-[LACSharedMode isConfirmed];
-[LACSharedMode isEqual:];
-[LACSharedMode initWithActive:];
-[LACSharedMode initWithActive:confirmed:];
```
