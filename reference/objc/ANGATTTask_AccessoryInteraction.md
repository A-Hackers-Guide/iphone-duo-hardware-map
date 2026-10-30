# `ANGATTTask`

- Image: [`/System/Library/PrivateFrameworks/AccessoryInteraction.framework/AccessoryInteraction`](../userland/System__Library__PrivateFrameworks__AccessoryInteraction.framework__AccessoryInteraction.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `ANTask`
- Protocols: `ANGATTTaskInformationProtocol`
- 4 instance variables, 8 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"NSMutableData" _payload;
@"CBUUID" _serviceUUID;
@"CBUUID" _characteristicUUID;
@"CBCharacteristic" _characteristic;
```

## Properties

```
@property (T@"CBUUID",R,V_serviceUUID) serviceUUID;
@property (T@"CBUUID",R,V_characteristicUUID) characteristicUUID;
@property (T@"NSData",R) characteristicPayload;
@property (T@"CBCharacteristic",&,V_characteristic) characteristic;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[ANGATTTask serviceUUID];
-[ANGATTTask init];
-[ANGATTTask dealloc];
-[ANGATTTask setPayloadData:];
-[ANGATTTask characteristic];
-[ANGATTTask setCharacteristic:];
-[ANGATTTask characteristicUUID];
-[ANGATTTask initWithCommand:serviceUUID:characteristicUUID:payload:context:];
-[ANGATTTask appendPayloadData:];
-[ANGATTTask characteristicPayload];
-[ANGATTTask doneSendingPayload];
-[ANGATTTask initWithCommand:serviceUUID:characteristicUUID:payload:];
-[ANGATTTask nextPacketOfMaxSize:];
```
