# `CTTransportSTK`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 3 instance variables, 3 properties, 12 instance methods, 1 class methods

## Instance variables

```
i _index;
@"NSData" _key_epki;
@"NSData" _stk;
```

## Properties

```
@property (Ti,N,V_index) index;
@property (T@"NSData",&,N,V_key_epki) key_epki;
@property (T@"NSData",&,N,V_stk) stk;
```

## Class methods

```
+[CTTransportSTK supportsSecureCoding];
```

## Instance methods

```
-[CTTransportSTK index];
-[CTTransportSTK setIndex:];
-[CTTransportSTK encodeWithCoder:];
-[CTTransportSTK description];
-[CTTransportSTK initWithCoder:];
-[CTTransportSTK copyWithZone:];
-[CTTransportSTK setStk:];
-[CTTransportSTK stk];
-[CTTransportSTK initWithSTK:forIdx:];
-[CTTransportSTK initWithSTK:forIdx:epki:];
-[CTTransportSTK key_epki];
-[CTTransportSTK setKey_epki:];
```
