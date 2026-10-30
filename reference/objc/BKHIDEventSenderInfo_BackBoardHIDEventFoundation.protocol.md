# `BKHIDEventSenderInfo` (protocol)

- Image: [`/System/Library/PrivateFrameworks/BackBoardHIDEventFoundation.framework/BackBoardHIDEventFoundation`](../userland/System__Library__PrivateFrameworks__BackBoardHIDEventFoundation.framework__BackBoardHIDEventFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 8 properties, 9 instance methods, 0 class methods

## Properties

```
@property (T@"NSString",R,C,N) displayUUID;
@property (Ti,R,N) eventSource;
@property (TQ,R,N) senderID;
@property (TI,R,N) primaryUsagePage;
@property (TI,R,N) primaryUsage;
@property (TB,R,N,GisAuthenticated) authenticated;
@property (TB,R,N,GisBuiltIn) builtIn;
@property (T@"BKSHIDEventSenderDescriptor",R,C,N) senderDescriptor;
```

## Instance methods

```
-[BKHIDEventSenderInfo isAuthenticated];
-[BKHIDEventSenderInfo eventSource];
-[BKHIDEventSenderInfo displayUUID];
-[BKHIDEventSenderInfo senderDescriptorForEventType:];
-[BKHIDEventSenderInfo senderID];
-[BKHIDEventSenderInfo isBuiltIn];
-[BKHIDEventSenderInfo senderDescriptor];
-[BKHIDEventSenderInfo primaryUsagePage];
-[BKHIDEventSenderInfo primaryUsage];
```
