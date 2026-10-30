# `CBDeviceHeySiriData`

- Image: [`/System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth`](../userland/System__Library__Frameworks__CoreBluetooth.framework__CoreBluetooth.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CBDeviceDataComponent`, `CUXPCCodable`, `NSSecureCoding`, `NSCopying`
- 9 instance variables, 13 properties, 30 instance methods, 1 class methods

## Instance variables

```
C _heySiriConfidence;
C _heySiriRandom;
C _heySiriSNR;
C _heySiriDeviceGroup;
C _heySiriDeviceClass;
C _heySiriQuantizedScore;
C _heySiriIdentityFlags;
S _heySiriPerceptualHash;
@"NSData" _heySiriAuthTag;
```

## Properties

```
@property (TC,N,V_heySiriConfidence) heySiriConfidence;
@property (TS,N,V_heySiriPerceptualHash) heySiriPerceptualHash;
@property (TC,N,V_heySiriRandom) heySiriRandom;
@property (TC,N,V_heySiriSNR) heySiriSNR;
@property (TC,N,V_heySiriDeviceGroup) heySiriDeviceGroup;
@property (TC,N,V_heySiriDeviceClass) heySiriDeviceClass;
@property (TC,N,V_heySiriQuantizedScore) heySiriQuantizedScore;
@property (TC,N,V_heySiriIdentityFlags) heySiriIdentityFlags;
@property (T@"NSData",C,N,V_heySiriAuthTag) heySiriAuthTag;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[CBDeviceHeySiriData supportsSecureCoding];
```

## Instance methods

```
-[CBDeviceHeySiriData memoryFootprint];
-[CBDeviceHeySiriData encodeWithXPCObject:];
-[CBDeviceHeySiriData initWithDictionary:error:];
-[CBDeviceHeySiriData clear];
-[CBDeviceHeySiriData initWithXPCObject:error:];
-[CBDeviceHeySiriData descriptionWithLevel:];
-[CBDeviceHeySiriData heySiriQuantizedScore];
-[CBDeviceHeySiriData setHeySiriConfidence:];
-[CBDeviceHeySiriData setHeySiriRandom:];
-[CBDeviceHeySiriData setHeySiriDeviceGroup:];
-[CBDeviceHeySiriData encodeWithCoder:];
-[CBDeviceHeySiriData heySiriDeviceClass];
-[CBDeviceHeySiriData heySiriRandom];
-[CBDeviceHeySiriData description];
-[CBDeviceHeySiriData setHeySiriQuantizedScore:];
-[CBDeviceHeySiriData initWithCoder:];
-[CBDeviceHeySiriData setHeySiriDeviceClass:];
-[CBDeviceHeySiriData hasAnyData];
-[CBDeviceHeySiriData setHeySiriPerceptualHash:];
-[CBDeviceHeySiriData setHeySiriSNR:];
-[CBDeviceHeySiriData copyWithZone:];
-[CBDeviceHeySiriData heySiriSNR];
-[CBDeviceHeySiriData heySiriDeviceGroup];
-[CBDeviceHeySiriData heySiriPerceptualHash];
-[CBDeviceHeySiriData heySiriConfidence];
-[CBDeviceHeySiriData dictionaryRepresentation];
-[CBDeviceHeySiriData heySiriAuthTag];
-[CBDeviceHeySiriData heySiriIdentityFlags];
-[CBDeviceHeySiriData setHeySiriAuthTag:];
-[CBDeviceHeySiriData setHeySiriIdentityFlags:];
```
