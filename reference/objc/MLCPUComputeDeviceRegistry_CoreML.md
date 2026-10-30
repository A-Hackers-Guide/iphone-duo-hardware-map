# `MLCPUComputeDeviceRegistry`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `MLComputeDeviceRegistryProtocol`
- 1 instance variables, 6 properties, 3 instance methods, 1 class methods

## Instance variables

```
@"MLCPUComputeDevice" _cpuDevice;
```

## Properties

```
@property (T@"MLCPUComputeDevice",R,N,V_cpuDevice) cpuDevice;
@property (T@"NSArray",R,C,N) registeredComputeDevices;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[MLCPUComputeDeviceRegistry sharedRegistry];
```

## Instance methods

```
-[MLCPUComputeDeviceRegistry registeredComputeDevices];
-[MLCPUComputeDeviceRegistry cpuDevice];
-[MLCPUComputeDeviceRegistry initWithCpuDevice:];
```
