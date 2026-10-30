# `MTL4PipelineOptions`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 12 instance variables, 12 properties, 28 instance methods, 0 class methods

## Instance variables

```
B _enablePerformanceStatistics;
B _enablePostVertexDump;
B _enablePostMeshDump;
B _enableAccelerationStructureViewerInstrumentation;
B _enableResourcePatchingInstrumentation;
B _enableResourceUsageInstrumentation;
q _shaderValidation;
Q _shaderReflection;
@"NSDictionary" _pluginData;
@"MTLShaderValidationConfiguration" _shaderValidationConfig;
Q _maxNumRegisters;
Q _postVertexDumpBufferIndex;
```

## Properties

```
@property (T@"NSDictionary",&,V_pluginData) pluginData;
@property (T@"MTLShaderValidationConfiguration",R,V_shaderValidationConfig) shaderValidationConfig;
@property (TB,V_enablePerformanceStatistics) enablePerformanceStatistics;
@property (TB,V_enablePostVertexDump) enablePostVertexDump;
@property (TB,V_enablePostMeshDump) enablePostMeshDump;
@property (TB,V_enableAccelerationStructureViewerInstrumentation) enableAccelerationStructureViewerInstrumentation;
@property (TB,V_enableResourcePatchingInstrumentation) enableResourcePatchingInstrumentation;
@property (TB,V_enableResourceUsageInstrumentation) enableResourceUsageInstrumentation;
@property (TQ,V_maxNumRegisters) maxNumRegisters;
@property (TQ,V_postVertexDumpBufferIndex) postVertexDumpBufferIndex;
@property (Tq,N,V_shaderValidation) shaderValidation;
@property (TQ,N,V_shaderReflection) shaderReflection;
```

## Instance methods

```
-[MTL4PipelineOptions setPluginData:];
-[MTL4PipelineOptions setPostVertexDumpBufferIndex:];
-[MTL4PipelineOptions pluginData];
-[MTL4PipelineOptions init];
-[MTL4PipelineOptions dealloc];
-[MTL4PipelineOptions shaderValidation];
-[MTL4PipelineOptions setShaderValidation:];
-[MTL4PipelineOptions hash];
-[MTL4PipelineOptions postVertexDumpBufferIndex];
-[MTL4PipelineOptions copyWithZone:];
-[MTL4PipelineOptions isEqual:];
-[MTL4PipelineOptions setEnablePerformanceStatistics:];
-[MTL4PipelineOptions maxNumRegisters];
-[MTL4PipelineOptions enableAccelerationStructureViewerInstrumentation];
-[MTL4PipelineOptions enablePerformanceStatistics];
-[MTL4PipelineOptions enablePostMeshDump];
-[MTL4PipelineOptions enablePostVertexDump];
-[MTL4PipelineOptions enableResourcePatchingInstrumentation];
-[MTL4PipelineOptions enableResourceUsageInstrumentation];
-[MTL4PipelineOptions setEnableAccelerationStructureViewerInstrumentation:];
-[MTL4PipelineOptions setEnablePostMeshDump:];
-[MTL4PipelineOptions setEnablePostVertexDump:];
-[MTL4PipelineOptions setEnableResourcePatchingInstrumentation:];
-[MTL4PipelineOptions setEnableResourceUsageInstrumentation:];
-[MTL4PipelineOptions setMaxNumRegisters:];
-[MTL4PipelineOptions setShaderReflection:];
-[MTL4PipelineOptions shaderReflection];
-[MTL4PipelineOptions shaderValidationConfig];
```
