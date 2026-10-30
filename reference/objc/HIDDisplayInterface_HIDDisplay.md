# `HIDDisplayInterface`

- Image: [`/System/Library/PrivateFrameworks/HIDDisplay.framework/HIDDisplay`](../userland/System__Library__PrivateFrameworks__HIDDisplay.framework__HIDDisplay.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 3 properties, 17 instance methods, 0 class methods

## Instance variables

```
@"HIDManager" _manager;
@"HIDDevice" _deviceRef;
@"NSString" _containerID;
Q _registryID;
```

## Properties

```
@property (T@"NSString",R,V_containerID) containerID;
@property (TQ,R,V_registryID) registryID;
@property (T@"NSArray",R) capabilities;
```

## Instance methods

```
-[HIDDisplayInterface setDevice:];
-[HIDDisplayInterface initWithContainerID:];
-[HIDDisplayInterface device];
-[HIDDisplayInterface dealloc];
-[HIDDisplayInterface containerID];
-[HIDDisplayInterface capabilities];
-[HIDDisplayInterface description];
-[HIDDisplayInterface registryID];
-[HIDDisplayInterface initWithService:];
-[HIDDisplayInterface commit:error:];
-[HIDDisplayInterface extract:error:];
-[HIDDisplayInterface extractContainerIDFromService:];
-[HIDDisplayInterface getDeviceElements:];
-[HIDDisplayInterface getHIDDevices];
-[HIDDisplayInterface getHIDDevicesForMatching:];
-[HIDDisplayInterface hasMatchingContainerID:containerID:];
-[HIDDisplayInterface initWithMatching:];
```
