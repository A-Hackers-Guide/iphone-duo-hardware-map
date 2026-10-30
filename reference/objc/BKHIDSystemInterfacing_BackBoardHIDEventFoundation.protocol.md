# `BKHIDSystemInterfacing` (protocol)

- Image: [`/System/Library/PrivateFrameworks/BackBoardHIDEventFoundation.framework/BackBoardHIDEventFoundation`](../userland/System__Library__PrivateFrameworks__BackBoardHIDEventFoundation.framework__BackBoardHIDEventFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `BKIOHIDServiceMatcherDataProviding`, `BKHIDEventDeliveryManagerProviding`
- 0 instance variables, 2 properties, 7 instance methods, 0 class methods

## Properties

```
@property (T@"BKHIDEventSenderCache",R) senderCache;
@property (T@"BKHIDClientConnectionManager",R) clientConnectionManager;
```

## Instance methods

```
-[BKHIDSystemInterfacing systemPropertyForKey:];
-[BKHIDSystemInterfacing clientConnectionManager];
-[BKHIDSystemInterfacing injectHIDEvent:];
-[BKHIDSystemInterfacing injectGSEvent:];
-[BKHIDSystemInterfacing senderCache];
-[BKHIDSystemInterfacing setSystemProperty:forKey:];
-[BKHIDSystemInterfacing systemEventOfType:matchingEvent:options:];
```
