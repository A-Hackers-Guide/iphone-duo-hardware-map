# `CBDeviceRequest`

- Image: [`/System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth`](../userland/System__Library__Frameworks__CoreBluetooth.framework__CoreBluetooth.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CUXPCCodable`
- 2 instance variables, 2 properties, 7 instance methods, 0 class methods

## Instance variables

```
I _requestFlags;
d _timeoutSeconds;
```

## Properties

```
@property (TI,N,V_requestFlags) requestFlags;
@property (Td,N,V_timeoutSeconds) timeoutSeconds;
```

## Instance methods

```
-[CBDeviceRequest encodeWithXPCObject:];
-[CBDeviceRequest initWithXPCObject:error:];
-[CBDeviceRequest description];
-[CBDeviceRequest timeoutSeconds];
-[CBDeviceRequest setTimeoutSeconds:];
-[CBDeviceRequest requestFlags];
-[CBDeviceRequest setRequestFlags:];
```
