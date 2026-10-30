# `AccelerationStructureBuilder`

- Image: [`/System/Library/Extensions/AGXMetalG19P.bundle/AGXMetalG19P`](../userland/System__Library__Extensions__AGXMetalG19P.bundle__AGXMetalG19P.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 4 properties, 22 instance methods, 1 class methods

## Instance variables

```
@"AccelerationStructureShaderCache" _shaderCache;
{unique_ptr<Pool<Builder>, std::default_delete<Pool<Builder>>>=""{?="__ptr_"^v}} _builderPool;
I _builderOptions;
C _buildAlgorithm;
B _gpuAsserts;
```

## Properties

```
@property (T@"<MTLDevice>",R) device;
@property (TB,N,V_gpuAsserts) gpuAsserts;
@property (TI,N) builderOptions;
@property (TC,N) buildAlgorithm;
```

## Class methods

```
+[AccelerationStructureBuilder backendForDevice:];
```

## Instance methods

```
-[AccelerationStructureBuilder isCompatibleWithAccelerationStructure:];
-[AccelerationStructureBuilder device];
-[AccelerationStructureBuilder dealloc];
-[AccelerationStructureBuilder checkoutBuilder];
-[AccelerationStructureBuilder checkinBuilder:];
-[AccelerationStructureBuilder buildAlgorithm];
-[AccelerationStructureBuilder builderOptions];
-[AccelerationStructureBuilder checkinRecorder:];
-[AccelerationStructureBuilder checkoutRecorder];
-[AccelerationStructureBuilder computeSizes:];
-[AccelerationStructureBuilder computeSizes:buildAlgorithm:];
-[AccelerationStructureBuilder computeSizesWithCDescriptor:];
-[AccelerationStructureBuilder computeSizesWithCDescriptor:buildAlgorithm:];
-[AccelerationStructureBuilder cpuDeserializeInstanceAccelerationStructure:fromBytes:referencedAccelerationStructures:];
-[AccelerationStructureBuilder cpuDeserializePrimitiveAccelerationStructure:fromBytes:];
-[AccelerationStructureBuilder gpuAsserts];
-[AccelerationStructureBuilder initWithDevice:shaderCache:builderConfig:];
-[AccelerationStructureBuilder resetRecorder:];
-[AccelerationStructureBuilder resetUsedResourcesOnRecorder:];
-[AccelerationStructureBuilder setBuildAlgorithm:];
-[AccelerationStructureBuilder setBuilderOptions:];
-[AccelerationStructureBuilder setGpuAsserts:];
```
