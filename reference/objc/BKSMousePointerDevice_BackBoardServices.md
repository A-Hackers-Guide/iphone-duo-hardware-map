# `BKSMousePointerDevice`

- Image: [`/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices`](../userland/System__Library__PrivateFrameworks__BackBoardServices.framework__BackBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSProtobufSerializable`, `NSSecureCoding`, `NSCopying`
- 8 instance variables, 12 properties, 26 instance methods, 2 class methods

## Instance variables

```
B _hasVirtualMouseButtons;
B _supportsDragLock;
B _supportsLightClick;
B _supportsSystemHaptics;
@"BKSHIDEventSenderDescriptor" _senderDescriptor;
@"NSString" _productName;
@"NSString" _manufacturerName;
@"NSString" _preferenceKey;
```

## Properties

```
@property (T@"NSString",C,N,V_preferenceKey) preferenceKey;
@property (T@"NSString",C,N,V_productName) productName;
@property (T@"NSString",C,N,V_manufacturerName) manufacturerName;
@property (TB,N,V_hasVirtualMouseButtons) hasVirtualMouseButtons;
@property (TB,N,V_supportsDragLock) supportsDragLock;
@property (TB,N,V_supportsLightClick) supportsLightClick;
@property (TB,N,V_supportsSystemHaptics) supportsSystemHaptics;
@property (T@"BKSHIDEventSenderDescriptor",R,C,N,V_senderDescriptor) senderDescriptor;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BKSMousePointerDevice supportsSecureCoding];
+[BKSMousePointerDevice protobufSchema];
```

## Instance methods

```
-[BKSMousePointerDevice setProductName:];
-[BKSMousePointerDevice initForProtobufDecoding];
-[BKSMousePointerDevice setPreferences:];
-[BKSMousePointerDevice init];
-[BKSMousePointerDevice productName];
-[BKSMousePointerDevice preferences];
-[BKSMousePointerDevice manufacturerName];
-[BKSMousePointerDevice encodeWithCoder:];
-[BKSMousePointerDevice setManufacturerName:];
-[BKSMousePointerDevice senderDescriptor];
-[BKSMousePointerDevice hash];
-[BKSMousePointerDevice description];
-[BKSMousePointerDevice initWithCoder:];
-[BKSMousePointerDevice copyWithZone:];
-[BKSMousePointerDevice isEqual:];
-[BKSMousePointerDevice supportsDragLock];
-[BKSMousePointerDevice hasVirtualMouseButtons];
-[BKSMousePointerDevice initWithSenderDescriptor:];
-[BKSMousePointerDevice preferenceKey];
-[BKSMousePointerDevice setHasVirtualMouseButtons:];
-[BKSMousePointerDevice setPreferenceKey:];
-[BKSMousePointerDevice setSupportsDragLock:];
-[BKSMousePointerDevice setSupportsLightClick:];
-[BKSMousePointerDevice setSupportsSystemHaptics:];
-[BKSMousePointerDevice supportsLightClick];
-[BKSMousePointerDevice supportsSystemHaptics];
```
