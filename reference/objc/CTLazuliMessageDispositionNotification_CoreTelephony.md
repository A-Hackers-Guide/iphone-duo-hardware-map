# `CTLazuliMessageDispositionNotification`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 2 instance variables, 2 properties, 11 instance methods, 1 class methods

## Instance variables

```
q _deliveryType;
@"CTLazuliMessageID" _messageID;
```

## Properties

```
@property (Tq,N,V_deliveryType) deliveryType;
@property (T@"CTLazuliMessageID",&,N,V_messageID) messageID;
```

## Class methods

```
+[CTLazuliMessageDispositionNotification supportsSecureCoding];
```

## Instance methods

```
-[CTLazuliMessageDispositionNotification deliveryType];
-[CTLazuliMessageDispositionNotification messageID];
-[CTLazuliMessageDispositionNotification encodeWithCoder:];
-[CTLazuliMessageDispositionNotification setMessageID:];
-[CTLazuliMessageDispositionNotification description];
-[CTLazuliMessageDispositionNotification initWithCoder:];
-[CTLazuliMessageDispositionNotification copyWithZone:];
-[CTLazuliMessageDispositionNotification isEqual:];
-[CTLazuliMessageDispositionNotification setDeliveryType:];
-[CTLazuliMessageDispositionNotification initWithReflection:];
-[CTLazuliMessageDispositionNotification isEqualToCTLazuliMessageDispositionNotification:];
```
