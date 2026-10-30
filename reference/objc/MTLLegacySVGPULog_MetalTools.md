# `MTLLegacySVGPULog`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `MTLFunctionLog`
- 8 instance variables, 13 properties, 18 instance methods, 0 class methods

## Instance variables

```
@"MTLLegacySVImageData" _image;
@"NSArray" _errorStackTrace;
Q _callIndex;
Q _type;
@"NSString" _encoderLabel;
@"<MTLFunction>" _function;
@"<MTLFunctionLogDebugLocation>" _debugLocation;
@"NSString" _pipelineIdentifier;
```

## Properties

```
@property (T@"NSString",R,N) locationDescription;
@property (T@"MTLLegacySVImageData",&,N,V_image) image;
@property (T@"NSArray",&,N,V_errorStackTrace) errorStackTrace;
@property (TQ,N,V_callIndex) callIndex;
@property (TQ,N,V_type) type;
@property (T@"NSString",&,N,V_encoderLabel) encoderLabel;
@property (T@"<MTLFunction>",&,N,V_function) function;
@property (T@"<MTLFunctionLogDebugLocation>",&,N,V_debugLocation) debugLocation;
@property (T@"NSString",&,N,V_pipelineIdentifier) pipelineIdentifier;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[MTLLegacySVGPULog function];
-[MTLLegacySVGPULog dealloc];
-[MTLLegacySVGPULog setFunction:];
-[MTLLegacySVGPULog setType:];
-[MTLLegacySVGPULog type];
-[MTLLegacySVGPULog image];
-[MTLLegacySVGPULog setImage:];
-[MTLLegacySVGPULog locationDescription];
-[MTLLegacySVGPULog encoderLabel];
-[MTLLegacySVGPULog setEncoderLabel:];
-[MTLLegacySVGPULog debugLocation];
-[MTLLegacySVGPULog errorStackTrace];
-[MTLLegacySVGPULog callIndex];
-[MTLLegacySVGPULog pipelineIdentifier];
-[MTLLegacySVGPULog setCallIndex:];
-[MTLLegacySVGPULog setDebugLocation:];
-[MTLLegacySVGPULog setErrorStackTrace:];
-[MTLLegacySVGPULog setPipelineIdentifier:];
```
