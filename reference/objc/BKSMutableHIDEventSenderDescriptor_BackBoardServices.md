# `BKSMutableHIDEventSenderDescriptor`

- Image: [`/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices`](../userland/System__Library__PrivateFrameworks__BackBoardServices.framework__BackBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BKSHIDEventSenderDescriptor`
- 0 instance variables, 5 properties, 7 instance methods, 1 class methods

## Properties

```
@property (TB,D,N,GisInverted) inverted;
@property (Tq,D,N) hardwareType;
@property (T@"BKSHIDEventDisplay",C,D,N) associatedDisplay;
@property (TB,D,N,GisAuthenticated) authenticated;
@property (TQ,D,N) senderID;
```

## Class methods

```
+[BKSMutableHIDEventSenderDescriptor new];
```

## Instance methods

```
-[BKSMutableHIDEventSenderDescriptor setAuthenticated:];
-[BKSMutableHIDEventSenderDescriptor init];
-[BKSMutableHIDEventSenderDescriptor setHardwareType:];
-[BKSMutableHIDEventSenderDescriptor setPrimaryPage:primaryUsage:];
-[BKSMutableHIDEventSenderDescriptor setAssociatedDisplay:];
-[BKSMutableHIDEventSenderDescriptor setSenderID:];
-[BKSMutableHIDEventSenderDescriptor setInverted:];
```
