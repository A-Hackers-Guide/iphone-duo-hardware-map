# `CBHIDEvent`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CBHIDEventProtocol`
- 4 instance variables, 10 properties, 12 instance methods, 1 class methods

## Instance variables

```
@"NSObject<OS_os_log>" _logHandle;
@"NSNumber" _serviceRegistryID;
^{__IOHIDEvent=} _event;
^{__IOHIDServiceClient=} _service;
```

## Properties

```
@property (T^{__IOHIDEvent=},R,N,V_event) event;
@property (T^{__IOHIDServiceClient=},R,N,V_service) service;
@property (Td,R,N) timestamp;
@property (TI,R,N) eventType;
@property (T@"NSArray",R,N) copyChildren;
@property (T@"NSNumber",R,N,V_serviceRegistryID) serviceRegistryID;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[CBHIDEvent newEvent:andService:];
```

## Instance methods

```
-[CBHIDEvent eventType];
-[CBHIDEvent initWithHIDEvent:andService:];
-[CBHIDEvent dealloc];
-[CBHIDEvent timestamp];
-[CBHIDEvent event];
-[CBHIDEvent conformsToEvent:];
-[CBHIDEvent service];
-[CBHIDEvent floatValueForKey:];
-[CBHIDEvent integerValueForKey:];
-[CBHIDEvent asHidEvent];
-[CBHIDEvent copyChildren];
-[CBHIDEvent serviceRegistryID];
```
