# `MLComputePlanDeviceUsage`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 5 instance methods, 0 class methods

## Instance variables

```
@"NSArray" _supportedComputeDevices;
@"<MLComputeDeviceProtocol>" _preferredComputeDevice;
@"NSArray" _deviceSupportInfoArray;
```

## Properties

```
@property (T@"NSArray",R,C,N,V_deviceSupportInfoArray) deviceSupportInfoArray;
@property (T@"NSArray",R,C,N,V_supportedComputeDevices) supportedComputeDevices;
@property (T@"<MLComputeDeviceProtocol>",R,N,V_preferredComputeDevice) preferredComputeDevice;
```

## Instance methods

```
-[MLComputePlanDeviceUsage supportedComputeDevices];
-[MLComputePlanDeviceUsage deviceSupportInfoArray];
-[MLComputePlanDeviceUsage initWithSupportedComputeDevices:preferredComputeDevice:deviceSupportInfoArray:];
-[MLComputePlanDeviceUsage preferredComputeDevice];
-[MLComputePlanDeviceUsage supportInfoForComputeDevice:];
```
