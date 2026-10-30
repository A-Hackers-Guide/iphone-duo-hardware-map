# `CBSoftwareUpdatePayloadInfo`

- Image: [`/System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth`](../userland/System__Library__Frameworks__CoreBluetooth.framework__CoreBluetooth.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CUXPCCodable`
- 3 instance variables, 3 properties, 9 instance methods, 0 class methods

## Instance variables

```
C _softwareUpdateActionType;
@"NSData" _softwareUpdateDataBlob;
@"NSData" _softwareUpdateDataMask;
```

## Properties

```
@property (TC,N,V_softwareUpdateActionType) softwareUpdateActionType;
@property (T@"NSData",C,N,V_softwareUpdateDataBlob) softwareUpdateDataBlob;
@property (T@"NSData",C,N,V_softwareUpdateDataMask) softwareUpdateDataMask;
```

## Instance methods

```
-[CBSoftwareUpdatePayloadInfo encodeWithXPCObject:];
-[CBSoftwareUpdatePayloadInfo initWithXPCObject:error:];
-[CBSoftwareUpdatePayloadInfo setSoftwareUpdateActionType:];
-[CBSoftwareUpdatePayloadInfo softwareUpdateActionType];
-[CBSoftwareUpdatePayloadInfo description];
-[CBSoftwareUpdatePayloadInfo setSoftwareUpdateDataBlob:];
-[CBSoftwareUpdatePayloadInfo setSoftwareUpdateDataMask:];
-[CBSoftwareUpdatePayloadInfo softwareUpdateDataBlob];
-[CBSoftwareUpdatePayloadInfo softwareUpdateDataMask];
```
