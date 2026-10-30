# `MPSGraphDeviceDescriptor`

- Image: [`/System/Library/Frameworks/MetalPerformanceShadersGraph.framework/MetalPerformanceShadersGraph`](../userland/System__Library__Frameworks__MetalPerformanceShadersGraph.framework__MetalPerformanceShadersGraph.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSGraphObject`
- Protocols: `NSCopying`
- 5 instance variables, 5 properties, 15 instance methods, 0 class methods

## Instance variables

```
I _type;
q _gpuCoreCount;
@"NSString" _architecture;
@"NSArray" _serializedProperties;
Q _preComputedHash;
```

## Properties

```
@property (TI,R,N,V_type) type;
@property (Tq,R,N,V_gpuCoreCount) gpuCoreCount;
@property (T@"NSString",R,N,V_architecture) architecture;
@property (T@"NSArray",R,N,V_serializedProperties) serializedProperties;
@property (TQ,R,N,V_preComputedHash) preComputedHash;
```

## Instance methods

```
-[MPSGraphDeviceDescriptor architecture];
-[MPSGraphDeviceDescriptor supportsMXU];
-[MPSGraphDeviceDescriptor debugDescription];
-[MPSGraphDeviceDescriptor hasANE];
-[MPSGraphDeviceDescriptor isEqualTo:];
-[MPSGraphDeviceDescriptor type];
-[MPSGraphDeviceDescriptor hash];
-[MPSGraphDeviceDescriptor copyWithZone:];
-[MPSGraphDeviceDescriptor isEqual:];
-[MPSGraphDeviceDescriptor gpuCoreCount];
-[MPSGraphDeviceDescriptor serializedProperties];
-[MPSGraphDeviceDescriptor preComputedHash];
-[MPSGraphDeviceDescriptor initMetalDeviceWithGPUCoreCount:architecture:];
-[MPSGraphDeviceDescriptor initWithMPSGraphDevice:];
-[MPSGraphDeviceDescriptor initWithSerializedProperties:];
```
