# `CBUserNotificationRequest`

- Image: [`/System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth`](../userland/System__Library__Frameworks__CoreBluetooth.framework__CoreBluetooth.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CUXPCCodable`, `NSSecureCoding`, `NSCopying`
- 2 instance variables, 2 properties, 12 instance methods, 1 class methods

## Instance variables

```
I _event;
@"CBDevice" _device;
```

## Properties

```
@property (TI,N,V_event) event;
@property (T@"CBDevice",&,N,V_device) device;
```

## Class methods

```
+[CBUserNotificationRequest supportsSecureCoding];
```

## Instance methods

```
-[CBUserNotificationRequest setEvent:];
-[CBUserNotificationRequest encodeWithXPCObject:];
-[CBUserNotificationRequest initWithDictionary:error:];
-[CBUserNotificationRequest initWithXPCObject:error:];
-[CBUserNotificationRequest setDevice:];
-[CBUserNotificationRequest device];
-[CBUserNotificationRequest event];
-[CBUserNotificationRequest encodeWithCoder:];
-[CBUserNotificationRequest description];
-[CBUserNotificationRequest initWithCoder:];
-[CBUserNotificationRequest copyWithZone:];
-[CBUserNotificationRequest dictionaryRepresentation];
```
