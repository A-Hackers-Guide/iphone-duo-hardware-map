# `BKHIDUnknownSender`

- Image: [`/System/Library/PrivateFrameworks/BackBoardHIDEventFoundation.framework/BackBoardHIDEventFoundation`](../userland/System__Library__PrivateFrameworks__BackBoardHIDEventFoundation.framework__BackBoardHIDEventFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BKHIDEventSenderInfo`
- 8 instance variables, 12 properties, 18 instance methods, 1 class methods

## Instance variables

```
B _authenticated;
B _builtIn;
i _eventSource;
I _primaryUsagePage;
I _primaryUsage;
@"NSString" _displayUUID;
Q _senderID;
@"BKSHIDEventSenderDescriptor" _senderDescriptor;
```

## Properties

```
@property (T@"NSString",C,N,V_displayUUID) displayUUID;
@property (Ti,N,V_eventSource) eventSource;
@property (TQ,N,V_senderID) senderID;
@property (TI,N,V_primaryUsagePage) primaryUsagePage;
@property (TI,N,V_primaryUsage) primaryUsage;
@property (TB,N,GisAuthenticated,V_authenticated) authenticated;
@property (TB,N,GisBuiltIn,V_builtIn) builtIn;
@property (T@"BKSHIDEventSenderDescriptor",C,N,V_senderDescriptor) senderDescriptor;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BKHIDUnknownSender unknownSenderInfo];
```

## Instance methods

```
-[BKHIDUnknownSender isAuthenticated];
-[BKHIDUnknownSender setAuthenticated:];
-[BKHIDUnknownSender eventSource];
-[BKHIDUnknownSender init];
-[BKHIDUnknownSender setEventSource:];
-[BKHIDUnknownSender displayUUID];
-[BKHIDUnknownSender senderDescriptorForEventType:];
-[BKHIDUnknownSender senderID];
-[BKHIDUnknownSender setSenderDescriptor:];
-[BKHIDUnknownSender setDisplayUUID:];
-[BKHIDUnknownSender setBuiltIn:];
-[BKHIDUnknownSender isBuiltIn];
-[BKHIDUnknownSender senderDescriptor];
-[BKHIDUnknownSender primaryUsagePage];
-[BKHIDUnknownSender setSenderID:];
-[BKHIDUnknownSender setPrimaryUsagePage:];
-[BKHIDUnknownSender primaryUsage];
-[BKHIDUnknownSender setPrimaryUsage:];
```
