# `ANHawkeyeTask`

- Image: [`/System/Library/PrivateFrameworks/AccessoryInteraction.framework/AccessoryInteraction`](../userland/System__Library__PrivateFrameworks__AccessoryInteraction.framework__AccessoryInteraction.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `ANTask`
- Protocols: `ANGATTTaskInformationProtocol`
- 4 instance variables, 13 properties, 14 instance methods, 0 class methods

## Instance variables

```
S _hawkeyeOpcode;
@"CBUUID" _serviceUUID;
@"CBUUID" _characteristicUUID;
@"NSData" _hawkeyePayload;
```

## Properties

```
@property (T@"CBUUID",&,V_serviceUUID) serviceUUID;
@property (T@"CBUUID",&,V_characteristicUUID) characteristicUUID;
@property (TS,V_hawkeyeOpcode) hawkeyeOpcode;
@property (T@"NSData",&,V_hawkeyePayload) hawkeyePayload;
@property (TB,R) isConfigurationControlPointTask;
@property (TB,R) isPairedOwnerInformationControlPointTask;
@property (TB,R) isNonOwnerControlPointTask;
@property (TB,R) isDebugControlPointTask;
@property (TB,R) isPreciseFindingControlPointTask;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[ANHawkeyeTask serviceUUID];
-[ANHawkeyeTask setServiceUUID:];
-[ANHawkeyeTask dealloc];
-[ANHawkeyeTask characteristicUUID];
-[ANHawkeyeTask isConfigurationControlPointTask];
-[ANHawkeyeTask hawkeyeOpcode];
-[ANHawkeyeTask hawkeyePayload];
-[ANHawkeyeTask isDebugControlPointTask];
-[ANHawkeyeTask isNonOwnerControlPointTask];
-[ANHawkeyeTask isPairedOwnerInformationControlPointTask];
-[ANHawkeyeTask isPreciseFindingControlPointTask];
-[ANHawkeyeTask setCharacteristicUUID:];
-[ANHawkeyeTask setHawkeyeOpcode:];
-[ANHawkeyeTask setHawkeyePayload:];
```
