# `BKSHIDKeyboardDevice`

- Image: [`/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices`](../userland/System__Library__PrivateFrameworks__BackBoardServices.framework__BackBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionStreaming`, `BKSHIDKeyboardDevicePropertiesProviding`
- 4 instance variables, 16 properties, 19 instance methods, 1 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
Q _senderID;
@"BKSHIDKeyboardDeviceProperties" _lock_properties;
@"BKSHIDKeyboardService" _service;
```

## Properties

```
@property (T@"NSString",R,C,N) _serverLayout;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TQ,R,D,N) senderID;
@property (T@"NSString",R,C,D,N) transport;
@property (T@"NSString",R,C,D,N) language;
@property (T@"NSString",R,C,D,N) layout;
@property (T@"NSString",R,C,D,N) exclusivityIdentifier;
@property (T@"NSData",R,C,D,N) platformInputModeConfiguration;
@property (TC,R,D,N) countryCode;
@property (TI,R,D,N) standardType;
@property (Tq,R,D,N) subinterfaceID;
@property (TB,R,D,N) capsLockKeyHasLanguageSwitchLabel;
@property (TB,R,D,N) globeKeyLabelHasGlobeSymbol;
```

## Class methods

```
+[BKSHIDKeyboardDevice new];
```

## Instance methods

```
-[BKSHIDKeyboardDevice language];
-[BKSHIDKeyboardDevice init];
-[BKSHIDKeyboardDevice _properties];
-[BKSHIDKeyboardDevice globeKeyLabelHasGlobeSymbol];
-[BKSHIDKeyboardDevice appendDescriptionToStream:fromProxy:];
-[BKSHIDKeyboardDevice transport];
-[BKSHIDKeyboardDevice exclusivityIdentifier];
-[BKSHIDKeyboardDevice subinterfaceID];
-[BKSHIDKeyboardDevice senderID];
-[BKSHIDKeyboardDevice countryCode];
-[BKSHIDKeyboardDevice standardType];
-[BKSHIDKeyboardDevice capsLockKeyHasLanguageSwitchLabel];
-[BKSHIDKeyboardDevice _initWithProperties:service:];
-[BKSHIDKeyboardDevice description];
-[BKSHIDKeyboardDevice appendDescriptionToStream:];
-[BKSHIDKeyboardDevice layout];
-[BKSHIDKeyboardDevice platformInputModeConfiguration];
-[BKSHIDKeyboardDevice _replaceProperties:];
-[BKSHIDKeyboardDevice _serverLayout];
```
