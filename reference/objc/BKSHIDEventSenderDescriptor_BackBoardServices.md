# `BKSHIDEventSenderDescriptor`

- Image: [`/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices`](../userland/System__Library__PrivateFrameworks__BackBoardServices.framework__BackBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSProtobufSerializable`, `BSDescriptionStreamable`, `NSCopying`, `NSMutableCopying`, `NSSecureCoding`
- 7 instance variables, 11 properties, 22 instance methods, 7 class methods

## Instance variables

```
q _hardwareType;
@"BKSHIDEventDisplay" _associatedDisplay;
B _authenticated;
I _primaryPage;
I _primaryUsage;
Q _senderID;
B _inverted;
```

## Properties

```
@property (TB,R,N,GisInverted,V_inverted) inverted;
@property (Tq,R,N,V_hardwareType) hardwareType;
@property (T@"BKSHIDEventDisplay",R,N,V_associatedDisplay) associatedDisplay;
@property (TB,R,N,GisAuthenticated,V_authenticated) authenticated;
@property (TI,R,N,V_primaryPage) primaryPage;
@property (TI,R,N,V_primaryUsage) primaryUsage;
@property (TQ,R,N,V_senderID) senderID;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BKSHIDEventSenderDescriptor build:];
+[BKSHIDEventSenderDescriptor supportsSecureCoding];
+[BKSHIDEventSenderDescriptor protobufSchema];
+[BKSHIDEventSenderDescriptor anyBuiltinTouchscreenDigitizer];
+[BKSHIDEventSenderDescriptor anyDigitizer];
+[BKSHIDEventSenderDescriptor stylusOpaqueTouchDigitizer];
+[BKSHIDEventSenderDescriptor wildcard];
```

## Instance methods

```
-[BKSHIDEventSenderDescriptor isAuthenticated];
-[BKSHIDEventSenderDescriptor matchesDescriptor:failureReason:];
-[BKSHIDEventSenderDescriptor isInverted];
-[BKSHIDEventSenderDescriptor primaryPage];
-[BKSHIDEventSenderDescriptor associatedDisplay];
-[BKSHIDEventSenderDescriptor mutableCopyWithZone:];
-[BKSHIDEventSenderDescriptor initForProtobufDecoding];
-[BKSHIDEventSenderDescriptor hardwareType];
-[BKSHIDEventSenderDescriptor init];
-[BKSHIDEventSenderDescriptor appendDescriptionToFormatter:];
-[BKSHIDEventSenderDescriptor propertyListEncoded];
-[BKSHIDEventSenderDescriptor initFromPropertyList:];
-[BKSHIDEventSenderDescriptor _initWithHardwareType:associatedDisplay:authenticated:primaryPage:primaryUsage:senderID:inverted:];
-[BKSHIDEventSenderDescriptor senderID];
-[BKSHIDEventSenderDescriptor encodeWithCoder:];
-[BKSHIDEventSenderDescriptor hash];
-[BKSHIDEventSenderDescriptor description];
-[BKSHIDEventSenderDescriptor initWithCoder:];
-[BKSHIDEventSenderDescriptor invertedDescriptor];
-[BKSHIDEventSenderDescriptor primaryUsage];
-[BKSHIDEventSenderDescriptor copyWithZone:];
-[BKSHIDEventSenderDescriptor isEqual:];
```
