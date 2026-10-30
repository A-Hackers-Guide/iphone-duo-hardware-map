# `BKSHIDKeyboardDeviceProperties`

- Image: [`/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices`](../userland/System__Library__PrivateFrameworks__BackBoardServices.framework__BackBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSMutableCopying`, `NSSecureCoding`, `BSDescriptionStreamable`, `BSProtobufSerializable`, `BKSHIDKeyboardDevicePropertiesProviding`
- 11 instance variables, 15 properties, 21 instance methods, 4 class methods

## Instance variables

```
Q _senderID;
@"NSString" _transport;
@"NSString" _language;
@"NSString" _layout;
@"NSString" _exclusivityIdentifier;
@"NSData" _platformInputModeConfiguration;
I _standardType;
q _subinterfaceID;
C _countryCode;
B _capsLockKeyHasLanguageSwitchLabel;
B _globeKeyLabelHasGlobeSymbol;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TQ,R,N) senderID;
@property (T@"NSString",R,C,N) transport;
@property (T@"NSString",R,C,N) language;
@property (T@"NSString",R,C,N) layout;
@property (T@"NSString",R,C,N) exclusivityIdentifier;
@property (T@"NSData",R,C,N) platformInputModeConfiguration;
@property (TC,R,N) countryCode;
@property (TI,R,N) standardType;
@property (Tq,R,N) subinterfaceID;
@property (TB,R,N) capsLockKeyHasLanguageSwitchLabel;
@property (TB,R,N) globeKeyLabelHasGlobeSymbol;
```

## Class methods

```
+[BKSHIDKeyboardDeviceProperties build:];
+[BKSHIDKeyboardDeviceProperties supportsSecureCoding];
+[BKSHIDKeyboardDeviceProperties protobufSchema];
+[BKSHIDKeyboardDeviceProperties new];
```

## Instance methods

```
-[BKSHIDKeyboardDeviceProperties language];
-[BKSHIDKeyboardDeviceProperties mutableCopyWithZone:];
-[BKSHIDKeyboardDeviceProperties initForProtobufDecoding];
-[BKSHIDKeyboardDeviceProperties init];
-[BKSHIDKeyboardDeviceProperties appendDescriptionToFormatter:];
-[BKSHIDKeyboardDeviceProperties globeKeyLabelHasGlobeSymbol];
-[BKSHIDKeyboardDeviceProperties transport];
-[BKSHIDKeyboardDeviceProperties exclusivityIdentifier];
-[BKSHIDKeyboardDeviceProperties subinterfaceID];
-[BKSHIDKeyboardDeviceProperties senderID];
-[BKSHIDKeyboardDeviceProperties countryCode];
-[BKSHIDKeyboardDeviceProperties standardType];
-[BKSHIDKeyboardDeviceProperties capsLockKeyHasLanguageSwitchLabel];
-[BKSHIDKeyboardDeviceProperties encodeWithCoder:];
-[BKSHIDKeyboardDeviceProperties hash];
-[BKSHIDKeyboardDeviceProperties description];
-[BKSHIDKeyboardDeviceProperties initWithCoder:];
-[BKSHIDKeyboardDeviceProperties layout];
-[BKSHIDKeyboardDeviceProperties platformInputModeConfiguration];
-[BKSHIDKeyboardDeviceProperties copyWithZone:];
-[BKSHIDKeyboardDeviceProperties isEqual:];
```
