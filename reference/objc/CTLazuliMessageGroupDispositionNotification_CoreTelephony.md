# `CTLazuliMessageGroupDispositionNotification`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 3 instance variables, 3 properties, 13 instance methods, 1 class methods

## Instance variables

```
@"CTLazuliGroupChatInformation" _chatInformation;
q _deliveryType;
@"CTLazuliMessageID" _messageID;
```

## Properties

```
@property (Tq,N,V_deliveryType) deliveryType;
@property (T@"CTLazuliMessageID",&,N,V_messageID) messageID;
@property (T@"CTLazuliGroupChatInformation",&,N,V_chatInformation) chatInformation;
```

## Class methods

```
+[CTLazuliMessageGroupDispositionNotification supportsSecureCoding];
```

## Instance methods

```
-[CTLazuliMessageGroupDispositionNotification deliveryType];
-[CTLazuliMessageGroupDispositionNotification messageID];
-[CTLazuliMessageGroupDispositionNotification encodeWithCoder:];
-[CTLazuliMessageGroupDispositionNotification setMessageID:];
-[CTLazuliMessageGroupDispositionNotification description];
-[CTLazuliMessageGroupDispositionNotification initWithCoder:];
-[CTLazuliMessageGroupDispositionNotification copyWithZone:];
-[CTLazuliMessageGroupDispositionNotification isEqual:];
-[CTLazuliMessageGroupDispositionNotification setDeliveryType:];
-[CTLazuliMessageGroupDispositionNotification chatInformation];
-[CTLazuliMessageGroupDispositionNotification initWithReflection:];
-[CTLazuliMessageGroupDispositionNotification isEqualToCTLazuliMessageGroupDispositionNotification:];
-[CTLazuliMessageGroupDispositionNotification setChatInformation:];
```
