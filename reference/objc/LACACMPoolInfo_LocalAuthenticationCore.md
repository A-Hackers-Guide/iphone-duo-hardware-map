# `LACACMPoolInfo`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 6 properties, 8 instance methods, 0 class methods

## Instance variables

```
q _size;
q _used;
q _free;
q _freeForLA;
q _reservedForACM;
q _reservedForLA;
```

## Properties

```
@property (Tq,R,N,V_size) size;
@property (Tq,R,N,V_used) used;
@property (Tq,R,N,V_free) free;
@property (Tq,R,N,V_freeForLA) freeForLA;
@property (Tq,R,N,V_reservedForACM) reservedForACM;
@property (Tq,R,N,V_reservedForLA) reservedForLA;
```

## Instance methods

```
-[LACACMPoolInfo size];
-[LACACMPoolInfo used];
-[LACACMPoolInfo description];
-[LACACMPoolInfo free];
-[LACACMPoolInfo freeForLA];
-[LACACMPoolInfo initWithSize:used:];
-[LACACMPoolInfo reservedForACM];
-[LACACMPoolInfo reservedForLA];
```
