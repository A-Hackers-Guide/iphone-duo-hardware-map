# `MTLTensorDescriptor`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 8 instance variables, 11 properties, 35 instance methods, 0 class methods

## Instance variables

```
B _forceResourceIndex;
@"MTLTensorExtents" _dimensions;
@"MTLTensorExtents" _strides;
q _dataType;
Q _usage;
@"MTLTensorAuxiliaryPlaneDescriptorMap" _auxiliaryPlanes;
Q _resourceOptions;
Q _resourceIndex;
```

## Properties

```
@property (TB,N,V_forceResourceIndex) forceResourceIndex;
@property (TQ,N,V_resourceIndex) resourceIndex;
@property (T@"MTLTensorExtents",C,N,V_dimensions) dimensions;
@property (T@"MTLTensorExtents",C,N,V_strides) strides;
@property (Tq,N,V_dataType) dataType;
@property (TQ,N,V_usage) usage;
@property (T@"MTLTensorAuxiliaryPlaneDescriptorMap",&,N,V_auxiliaryPlanes) auxiliaryPlanes;
@property (TQ,N,V_resourceOptions) resourceOptions;
@property (TQ,D,N) cpuCacheMode;
@property (TQ,D,N) storageMode;
@property (TQ,D,N) hazardTrackingMode;
```

## Instance methods

```
-[MTLTensorDescriptor resourceOptions];
-[MTLTensorDescriptor setCpuCacheMode:];
-[MTLTensorDescriptor usage];
-[MTLTensorDescriptor setDimensions:];
-[MTLTensorDescriptor setResourceIndex:];
-[MTLTensorDescriptor resourceIndex];
-[MTLTensorDescriptor setForceResourceIndex:];
-[MTLTensorDescriptor forceResourceIndex];
-[MTLTensorDescriptor hazardTrackingMode];
-[MTLTensorDescriptor setStorageMode:];
-[MTLTensorDescriptor dimensions];
-[MTLTensorDescriptor setResourceOptions:];
-[MTLTensorDescriptor cpuCacheMode];
-[MTLTensorDescriptor setHazardTrackingMode:];
-[MTLTensorDescriptor storageMode];
-[MTLTensorDescriptor setDataType:];
-[MTLTensorDescriptor validateWithDevice:error:];
-[MTLTensorDescriptor init];
-[MTLTensorDescriptor dealloc];
-[MTLTensorDescriptor strides];
-[MTLTensorDescriptor hash];
-[MTLTensorDescriptor dataType];
-[MTLTensorDescriptor setUsage:];
-[MTLTensorDescriptor copyWithZone:];
-[MTLTensorDescriptor isEqual:];
-[MTLTensorDescriptor setStrides:];
-[MTLTensorDescriptor auxiliaryPlanes];
-[MTLTensorDescriptor _validateBuffer:offset:planeType:context:];
-[MTLTensorDescriptor _validateBufferAttachment:planeType:context:];
-[MTLTensorDescriptor _validateDataPlaneDataType:context:];
-[MTLTensorDescriptor _validateDataPlaneDescriptorWithContext:];
-[MTLTensorDescriptor _validateScalesPlaneDescriptor:context:];
-[MTLTensorDescriptor setAuxiliaryPlanes:];
-[MTLTensorDescriptor validateWithBuffer:offset:error:];
-[MTLTensorDescriptor validateWithDevice:attachments:error:];
```
