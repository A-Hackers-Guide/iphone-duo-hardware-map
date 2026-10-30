# `CBLEManager`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CBHIDServiceProtocol`
- 11 instance variables, 5 properties, 24 instance methods, 1 class methods

## Instance variables

```
@"NSMutableArray" _containers;
@"NSMutableArray" _hidServiceClients;
@"NSObject<OS_dispatch_queue>" _queue;
@"NSObject<OS_os_log>" _logHandle;
@"CBSystemContext" _systemContext;
^{IONotificationPort=} _ioNotificationPortBL;
I _matchingIteratorBL;
I _terminationIteratorBL;
@"NSMutableDictionary" _clientDisplayMap;
@"NSSet" _handledKeys;
@? _notificationBlock;
```

## Properties

```
@property (T@?,C,V_notificationBlock) notificationBlock;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[CBLEManager copyBacklightMatchingDictionary];
```

## Instance methods

```
-[CBLEManager start:];
-[CBLEManager handleEvent:];
-[CBLEManager registerNotificationBlock:];
-[CBLEManager addHIDServiceClient:];
-[CBLEManager removeHIDServiceClient:];
-[CBLEManager stop];
-[CBLEManager dealloc];
-[CBLEManager setNotificationBlock:];
-[CBLEManager handleNotificationForKey:withProperty:];
-[CBLEManager notificationBlock];
-[CBLEManager unregisterNotificationBlock];
-[CBLEManager _copyStatusInfo];
-[CBLEManager initWithQueue:andSystemContext:];
-[CBLEManager _addContainerForBacklight:];
-[CBLEManager _copyInternalPropertyForKey:andClient:];
-[CBLEManager _removeAllContainers];
-[CBLEManager _removeContainerForBacklight:];
-[CBLEManager _sendNotificationForKey:andValue:];
-[CBLEManager _startBacklightLookup];
-[CBLEManager _stopBacklightLookup];
-[CBLEManager clientMappedCopyKey:];
-[CBLEManager clientMappedSetKey:];
-[CBLEManager copyPropertyForKey:andClient:];
-[CBLEManager setProperty:forKey:andClient:];
```
