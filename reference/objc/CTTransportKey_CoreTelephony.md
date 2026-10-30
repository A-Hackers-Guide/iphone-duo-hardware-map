# `CTTransportKey`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 5 instance variables, 5 properties, 17 instance methods, 1 class methods

## Instance variables

```
B _last_resort;
i _index;
@"NSData" _key;
@"NSData" _key_epki;
@"NSData" _retiredKey_epki;
```

## Properties

```
@property (Ti,N,V_index) index;
@property (T@"NSData",&,N,V_key) key;
@property (T@"NSData",&,N,V_key_epki) key_epki;
@property (T@"NSData",&,N,V_retiredKey_epki) retiredKey_epki;
@property (TB,N,V_last_resort) last_resort;
```

## Class methods

```
+[CTTransportKey supportsSecureCoding];
```

## Instance methods

```
-[CTTransportKey index];
-[CTTransportKey setKey:];
-[CTTransportKey setIndex:];
-[CTTransportKey encodeWithCoder:];
-[CTTransportKey description];
-[CTTransportKey initWithCoder:];
-[CTTransportKey copyWithZone:];
-[CTTransportKey key];
-[CTTransportKey setLast_resort:];
-[CTTransportKey retiredKey_epki];
-[CTTransportKey initWithKey:epki:forIdx:toReplace:epki:];
-[CTTransportKey initWithKey:epki:forIdx:toReplaceEpki:isLastResort:];
-[CTTransportKey initWithKey:forIdx:toReplace:];
-[CTTransportKey key_epki];
-[CTTransportKey last_resort];
-[CTTransportKey setKey_epki:];
-[CTTransportKey setRetiredKey_epki:];
```
