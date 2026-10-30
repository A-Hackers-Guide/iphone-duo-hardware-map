# `MTLGPUDebugGPULog`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `MTLFunctionLog`
- 17 instance variables, 23 properties, 40 instance methods, 0 class methods

## Instance variables

```
@"NSString" _resourceDescription;
@"MTLGPUDebugImageData" _image;
@"NSArray" _errorStackTrace;
@"NSArray" _allocationStackTraceAddresses;
@"NSArray" _allocationStackTrace;
@"NSString" _commandDescription;
Q _type;
@"NSString" _encoderLabel;
@"<MTLFunction>" _function;
Q _functionType;
@"NSString" _functionName;
@"<MTLFunctionLogDebugLocation>" _debugLocation;
@"NSString" _pipelineIdentifier;
@"<MTLComputePipelineState>" _computePipeline;
@"<MTLRenderPipelineState>" _renderPipeline;
q _metalVersion;
Q _resourceType;
```

## Properties

```
@property (T@"NSString",R,N) locationDescription;
@property (T@"NSString",R,N) functionDescription;
@property (T@"NSString",&,N,V_resourceDescription) resourceDescription;
@property (T@"MTLGPUDebugImageData",&,N,V_image) image;
@property (T@"NSArray",&,N,V_errorStackTrace) errorStackTrace;
@property (T@"NSArray",&,N,V_allocationStackTraceAddresses) allocationStackTraceAddresses;
@property (T@"NSArray",&,N,V_allocationStackTrace) allocationStackTrace;
@property (T@"NSString",&,N,V_commandDescription) commandDescription;
@property (TQ,N,V_type) type;
@property (T@"NSString",&,N,V_encoderLabel) encoderLabel;
@property (T@"<MTLFunction>",&,N,V_function) function;
@property (TQ,N,V_functionType) functionType;
@property (T@"NSString",&,N,V_functionName) functionName;
@property (T@"<MTLFunctionLogDebugLocation>",&,N,V_debugLocation) debugLocation;
@property (T@"NSString",&,N,V_pipelineIdentifier) pipelineIdentifier;
@property (T@"<MTLComputePipelineState>",&,N,V_computePipeline) computePipeline;
@property (T@"<MTLRenderPipelineState>",&,N,V_renderPipeline) renderPipeline;
@property (Tq,N,V_metalVersion) metalVersion;
@property (TQ,N,V_resourceType) resourceType;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[MTLGPUDebugGPULog functionType];
-[MTLGPUDebugGPULog setFunctionName:];
-[MTLGPUDebugGPULog functionName];
-[MTLGPUDebugGPULog function];
-[MTLGPUDebugGPULog dealloc];
-[MTLGPUDebugGPULog resourceType];
-[MTLGPUDebugGPULog setFunction:];
-[MTLGPUDebugGPULog setType:];
-[MTLGPUDebugGPULog type];
-[MTLGPUDebugGPULog setResourceType:];
-[MTLGPUDebugGPULog image];
-[MTLGPUDebugGPULog setImage:];
-[MTLGPUDebugGPULog commandDescription];
-[MTLGPUDebugGPULog renderPipeline];
-[MTLGPUDebugGPULog setRenderPipeline:];
-[MTLGPUDebugGPULog setFunctionType:];
-[MTLGPUDebugGPULog locationDescription];
-[MTLGPUDebugGPULog encoderLabel];
-[MTLGPUDebugGPULog setEncoderLabel:];
-[MTLGPUDebugGPULog setCommandDescription:];
-[MTLGPUDebugGPULog debugLocation];
-[MTLGPUDebugGPULog metalVersion];
-[MTLGPUDebugGPULog setMetalVersion:];
-[MTLGPUDebugGPULog errorStackTrace];
-[MTLGPUDebugGPULog allocationStackTraceDescription];
-[MTLGPUDebugGPULog computePipeline];
-[MTLGPUDebugGPULog allocationStackTrace];
-[MTLGPUDebugGPULog allocationStackTraceAddresses];
-[MTLGPUDebugGPULog functionDescription];
-[MTLGPUDebugGPULog pipelineIdentifier];
-[MTLGPUDebugGPULog resourceDescription];
-[MTLGPUDebugGPULog resourceDescriptionForType:resourceID:device:];
-[MTLGPUDebugGPULog setAllocationStackTrace:];
-[MTLGPUDebugGPULog setAllocationStackTraceAddresses:];
-[MTLGPUDebugGPULog setAllocationStackTraceForResourceType:resourceID:device:];
-[MTLGPUDebugGPULog setComputePipeline:];
-[MTLGPUDebugGPULog setDebugLocation:];
-[MTLGPUDebugGPULog setErrorStackTrace:];
-[MTLGPUDebugGPULog setPipelineIdentifier:];
-[MTLGPUDebugGPULog setResourceDescription:];
```
