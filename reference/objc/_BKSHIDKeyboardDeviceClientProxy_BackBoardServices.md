# `_BKSHIDKeyboardDeviceClientProxy`

- Image: [`/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices`](../userland/System__Library__PrivateFrameworks__BackBoardServices.framework__BackBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BKSHIDKeyboardDevicePropertiesProviding`, `BSDescriptionStreaming`
- 2 instance variables, 15 properties, 19 instance methods, 0 class methods

## Instance variables

```
@"BKSHIDKeyboardDevice" _device;
@"<BSInvalidatable>" _lifetimeAssertion;
```

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
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_BKSHIDKeyboardDeviceClientProxy language];
-[_BKSHIDKeyboardDeviceClientProxy debugDescription];
-[_BKSHIDKeyboardDeviceClientProxy _properties];
-[_BKSHIDKeyboardDeviceClientProxy dealloc];
-[_BKSHIDKeyboardDeviceClientProxy globeKeyLabelHasGlobeSymbol];
-[_BKSHIDKeyboardDeviceClientProxy transport];
-[_BKSHIDKeyboardDeviceClientProxy exclusivityIdentifier];
-[_BKSHIDKeyboardDeviceClientProxy subinterfaceID];
-[_BKSHIDKeyboardDeviceClientProxy senderID];
-[_BKSHIDKeyboardDeviceClientProxy countryCode];
-[_BKSHIDKeyboardDeviceClientProxy standardType];
-[_BKSHIDKeyboardDeviceClientProxy capsLockKeyHasLanguageSwitchLabel];
-[_BKSHIDKeyboardDeviceClientProxy hash];
-[_BKSHIDKeyboardDeviceClientProxy description];
-[_BKSHIDKeyboardDeviceClientProxy appendDescriptionToStream:];
-[_BKSHIDKeyboardDeviceClientProxy layout];
-[_BKSHIDKeyboardDeviceClientProxy platformInputModeConfiguration];
-[_BKSHIDKeyboardDeviceClientProxy isEqual:];
-[_BKSHIDKeyboardDeviceClientProxy initWithDevice:lifetimeAssertion:];
```
