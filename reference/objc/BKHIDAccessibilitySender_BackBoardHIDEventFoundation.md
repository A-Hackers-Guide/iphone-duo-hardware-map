# `BKHIDAccessibilitySender`

- Image: [`/System/Library/PrivateFrameworks/BackBoardHIDEventFoundation.framework/BackBoardHIDEventFoundation`](../userland/System__Library__PrivateFrameworks__BackBoardHIDEventFoundation.framework__BackBoardHIDEventFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BKHIDEventSenderInfo`
- 8 instance variables, 13 properties, 19 instance methods, 1 class methods

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
@property (TB,R,N) isPencilDigitizer;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BKHIDAccessibilitySender accessibilityHIDServices];
```

## Instance methods

```
-[BKHIDAccessibilitySender isAuthenticated];
-[BKHIDAccessibilitySender setAuthenticated:];
-[BKHIDAccessibilitySender eventSource];
-[BKHIDAccessibilitySender setEventSource:];
-[BKHIDAccessibilitySender displayUUID];
-[BKHIDAccessibilitySender senderDescriptorForEventType:];
-[BKHIDAccessibilitySender senderID];
-[BKHIDAccessibilitySender setSenderDescriptor:];
-[BKHIDAccessibilitySender setDisplayUUID:];
-[BKHIDAccessibilitySender setBuiltIn:];
-[BKHIDAccessibilitySender isBuiltIn];
-[BKHIDAccessibilitySender senderDescriptor];
-[BKHIDAccessibilitySender primaryUsagePage];
-[BKHIDAccessibilitySender setSenderID:];
-[BKHIDAccessibilitySender setPrimaryUsagePage:];
-[BKHIDAccessibilitySender primaryUsage];
-[BKHIDAccessibilitySender setPrimaryUsage:];
-[BKHIDAccessibilitySender initWithSenderID:];
-[BKHIDAccessibilitySender isPencilDigitizer];
```
