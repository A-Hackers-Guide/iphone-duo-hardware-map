# `CTLazuliMessageDispositionStatus`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 4 instance variables, 4 properties, 15 instance methods, 1 class methods

## Instance variables

```
q _deliveryType;
@"CTLazuliMessageID" _forMessageID;
@"CTLazuliDestination" _from;
@"CTLazuliGroupChatUri" _forGroupChat;
```

## Properties

```
@property (Tq,N,V_deliveryType) deliveryType;
@property (T@"CTLazuliMessageID",&,N,V_forMessageID) forMessageID;
@property (T@"CTLazuliDestination",&,N,V_from) from;
@property (T@"CTLazuliGroupChatUri",&,N,V_forGroupChat) forGroupChat;
```

## Class methods

```
+[CTLazuliMessageDispositionStatus supportsSecureCoding];
```

## Instance methods

```
-[CTLazuliMessageDispositionStatus setFrom:];
-[CTLazuliMessageDispositionStatus from];
-[CTLazuliMessageDispositionStatus deliveryType];
-[CTLazuliMessageDispositionStatus encodeWithCoder:];
-[CTLazuliMessageDispositionStatus description];
-[CTLazuliMessageDispositionStatus initWithCoder:];
-[CTLazuliMessageDispositionStatus copyWithZone:];
-[CTLazuliMessageDispositionStatus isEqual:];
-[CTLazuliMessageDispositionStatus setDeliveryType:];
-[CTLazuliMessageDispositionStatus forGroupChat];
-[CTLazuliMessageDispositionStatus forMessageID];
-[CTLazuliMessageDispositionStatus initWithReflection:];
-[CTLazuliMessageDispositionStatus isEqualToCTLazuliMessageDispositionStatus:];
-[CTLazuliMessageDispositionStatus setForGroupChat:];
-[CTLazuliMessageDispositionStatus setForMessageID:];
```
