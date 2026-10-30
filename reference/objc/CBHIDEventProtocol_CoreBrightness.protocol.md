# `CBHIDEventProtocol` (protocol)

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `CBEventProtocol`
- 0 instance variables, 6 properties, 9 instance methods, 0 class methods

## Properties

```
@property (T^{__IOHIDEvent=},R,N) event;
@property (T^{__IOHIDServiceClient=},R,N) service;
@property (Td,R,N) timestamp;
@property (TI,R,N) eventType;
@property (T@"NSArray",R,N) copyChildren;
@property (T@"NSNumber",R,N) serviceRegistryID;
```

## Instance methods

```
-[CBHIDEventProtocol eventType];
-[CBHIDEventProtocol timestamp];
-[CBHIDEventProtocol event];
-[CBHIDEventProtocol service];
-[CBHIDEventProtocol floatValueForKey:];
-[CBHIDEventProtocol integerValueForKey:];
-[CBHIDEventProtocol asHidEvent];
-[CBHIDEventProtocol copyChildren];
-[CBHIDEventProtocol serviceRegistryID];
```
