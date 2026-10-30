# `BKSHIDKeyboardDevicePropertiesProviding` (protocol)

- Image: [`/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices`](../userland/System__Library__PrivateFrameworks__BackBoardServices.framework__BackBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 11 properties, 11 instance methods, 0 class methods

## Properties

```
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

## Instance methods

```
-[BKSHIDKeyboardDevicePropertiesProviding language];
-[BKSHIDKeyboardDevicePropertiesProviding globeKeyLabelHasGlobeSymbol];
-[BKSHIDKeyboardDevicePropertiesProviding transport];
-[BKSHIDKeyboardDevicePropertiesProviding exclusivityIdentifier];
-[BKSHIDKeyboardDevicePropertiesProviding subinterfaceID];
-[BKSHIDKeyboardDevicePropertiesProviding senderID];
-[BKSHIDKeyboardDevicePropertiesProviding countryCode];
-[BKSHIDKeyboardDevicePropertiesProviding standardType];
-[BKSHIDKeyboardDevicePropertiesProviding capsLockKeyHasLanguageSwitchLabel];
-[BKSHIDKeyboardDevicePropertiesProviding layout];
-[BKSHIDKeyboardDevicePropertiesProviding platformInputModeConfiguration];
```
