# `CBHIDService`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CBEventServiceProtocol`
- 6 instance variables, 9 properties, 16 instance methods, 3 class methods

## Instance variables

```
@"NSObject<OS_os_log>" _logHandle;
^{__IOHIDServiceClient=} _service;
Q _serviceID;
I _ioService;
^{__IOHIDEvent=} _event;
B _builtIn;
```

## Properties

```
@property (T^{__IOHIDEvent=}) event;
@property (TQ,R,N,V_serviceID) serviceID;
@property (T^{__IOHIDServiceClient=},R,N,V_service) service;
@property (TI,R,N,V_ioService) ioService;
@property (TB,R,N,V_builtIn) builtIn;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[CBHIDService matchesService:];
+[CBHIDService nodeForService:];
+[CBHIDService matchingCriteria];
```

## Instance methods

```
-[CBHIDService setEvent:];
-[CBHIDService copyPropertyForKey:];
-[CBHIDService serviceID];
-[CBHIDService init];
-[CBHIDService dealloc];
-[CBHIDService event];
-[CBHIDService service];
-[CBHIDService hash];
-[CBHIDService builtIn];
-[CBHIDService isEqual:];
-[CBHIDService updateEventData];
-[CBHIDService conformsToHIDService:];
-[CBHIDService conformsToUsagePage:andUsage:];
-[CBHIDService initWithHIDServiceClient:andIdentifier:];
-[CBHIDService ioService];
-[CBHIDService setPropertyForKey:withValue:];
```
