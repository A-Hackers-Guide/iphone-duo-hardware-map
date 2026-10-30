# `CLGatheringBleAdvertisement`

- Image: [`/System/Library/Frameworks/CoreLocation.framework/CoreLocation`](../userland/System__Library__Frameworks__CoreLocation.framework__CoreLocation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 9 instance variables, 9 properties, 23 instance methods, 1 class methods

## Instance variables

```
@"NSData" _address;
@"NSString" _contactId;
q _flags;
q _eFlags;
@"NSData" _authTag;
@"NSData" _iTag;
q _rssi;
q _count;
d _unixTime;
```

## Properties

```
@property (T@"NSData",R,C,N,V_address) address;
@property (T@"NSString",R,C,N,V_contactId) contactId;
@property (Tq,R,N,V_flags) flags;
@property (Tq,R,N,V_eFlags) eFlags;
@property (T@"NSData",R,C,N,V_authTag) authTag;
@property (T@"NSData",R,C,N,V_iTag) iTag;
@property (Tq,R,N,V_rssi) rssi;
@property (Tq,R,N,V_count) count;
@property (Td,R,N,V_unixTime) unixTime;
```

## Class methods

```
+[CLGatheringBleAdvertisement supportsSecureCoding];
```

## Instance methods

```
-[CLGatheringBleAdvertisement rssi];
-[CLGatheringBleAdvertisement address];
-[CLGatheringBleAdvertisement flags];
-[CLGatheringBleAdvertisement dealloc];
-[CLGatheringBleAdvertisement count];
-[CLGatheringBleAdvertisement encodeWithCoder:];
-[CLGatheringBleAdvertisement hash];
-[CLGatheringBleAdvertisement description];
-[CLGatheringBleAdvertisement initWithCoder:];
-[CLGatheringBleAdvertisement initWithData:];
-[CLGatheringBleAdvertisement copyWithZone:];
-[CLGatheringBleAdvertisement isEqual:];
-[CLGatheringBleAdvertisement contactId];
-[CLGatheringBleAdvertisement authTag];
-[CLGatheringBleAdvertisement eFlags];
-[CLGatheringBleAdvertisement encodedBytes];
-[CLGatheringBleAdvertisement getDateString:];
-[CLGatheringBleAdvertisement hexString:];
-[CLGatheringBleAdvertisement iTag];
-[CLGatheringBleAdvertisement initWithAddress:contactId:flags:eFlags:authTag:iTag:rssi:count:unixTime:];
-[CLGatheringBleAdvertisement initWithAddress:withAuthTag:withRssi:withCount:withTime:];
-[CLGatheringBleAdvertisement initWithPersistenceBytes:];
-[CLGatheringBleAdvertisement unixTime];
```
