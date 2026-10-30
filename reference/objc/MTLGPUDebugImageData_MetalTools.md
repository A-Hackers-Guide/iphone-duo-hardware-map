# `MTLGPUDebugImageData`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 13 instance variables, 7 properties, 17 instance methods, 0 class methods

## Instance variables

```
@"MTLGPUDebugBuffer" constantDataBuffer;
@"MTLGPUDebugDevice" _device;
{mutex="__m_"{_opaque_pthread_mutex_t="__sig"q"__opaque"[56c]}} _constantDataMutex;
Q _constantDataBufferIndex;
{KeyBufferPair="key"{Key="hash"{?="key"[32C]}"data"@"NSData"}"buffer"@"<MTLBuffer>"} _constantDataKeyPair;
@"NSString" _loadedImageName;
@"MTLDebugInstrumentationData" _debugInstrumentationData;
i _imageType;
Q _imageID;
Q _functionType;
@"MTLGPUDebugFunction" _function;
@"MTLGPUDebugDynamicLibrary" _dynamicLibrary;
@"MTL4GPUDebugBinaryFunction" _binaryFunction;
```

## Properties

```
@property (T@"NSString",R,N) loadedImageName;
@property (Ti,R,N) imageType;
@property (T@"MTLDebugInstrumentationData",R,N) debugInstrumentationData;
@property (TQ,R,N) functionType;
@property (T@"MTL4GPUDebugBinaryFunction",R,W,N,V_binaryFunction) binaryFunction;
@property (T@"MTLGPUDebugFunction",R,W,N) function;
@property (T@"MTLGPUDebugDynamicLibrary",R,W,N) dynamicLibrary;
```

## Instance methods

```
-[MTLGPUDebugImageData functionType];
-[MTLGPUDebugImageData function];
-[MTLGPUDebugImageData imageType];
-[MTLGPUDebugImageData dealloc];
-[MTLGPUDebugImageData debugInstrumentationData];
-[MTLGPUDebugImageData initWithFunction:];
-[MTLGPUDebugImageData setConstantData:];
-[MTLGPUDebugImageData dynamicLibrary];
-[MTLGPUDebugImageData initWithDynamicLibrary:];
-[MTLGPUDebugImageData loadedImageName];
-[MTLGPUDebugImageData _applyConstantRelocation];
-[MTLGPUDebugImageData _applyConstantRelocation:];
-[MTLGPUDebugImageData _applyImageIDRelocation:];
-[MTLGPUDebugImageData binaryFunction];
-[MTLGPUDebugImageData initWithBinaryFunction:debugInstrumentationData:device:];
-[MTLGPUDebugImageData initWithFunction:debugInstrumentationData:];
-[MTLGPUDebugImageData initWithFunctionName:functionType:debugInstrumentationData:device:];
```
