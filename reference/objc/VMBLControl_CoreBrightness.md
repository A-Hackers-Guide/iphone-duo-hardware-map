# `VMBLControl`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BLControl`
- Protocols: `VMHeadroomRequestDelegate`
- 5 instance variables, 4 properties, 19 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_os_log>" _logHandle;
@"OS_xpc_remote_connection" _listener;
@"NSMutableArray" _connections;
@"NSMutableDictionary" _displays;
@"NSMutableDictionary" _cachedHeadroomRequests;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[VMBLControl findDisplays];
-[VMBLControl handleMessage:];
-[VMBLControl addDisplayModuleForBrightnessControlProxy:];
-[VMBLControl setPropertyWithKey:property:client:];
-[VMBLControl handleCAWindowServerDisplay:];
-[VMBLControl init];
-[VMBLControl stop];
-[VMBLControl dealloc];
-[VMBLControl parseCacheKey:displayIdentifier:builtIn:];
-[VMBLControl start];
-[VMBLControl sendBrightnessTransactionRequestForDisplayUUID:builtIn:];
-[VMBLControl sendHeadroomRequestOnQueue:forDisplayUUID:builtIn:];
-[VMBLControl connectToHost];
-[VMBLControl cacheKeyForDisplayIdentifier:builtIn:];
-[VMBLControl closeHostConnections];
-[VMBLControl sendHeadroomRequest:forDisplayUUID:builtIn:];
-[VMBLControl handleBrightnessTransaction:builtIn:displayIdentifier:];
-[VMBLControl sendBrightnessTransactionRequestOnQueueForDisplayUUID:builtIn:];
-[VMBLControl copyPropertyWithKey:client:];
```
