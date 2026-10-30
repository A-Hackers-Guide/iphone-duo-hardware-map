# `MTLLegacySVImageData`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 12 instance variables, 6 properties, 14 instance methods, 0 class methods

## Instance variables

```
@"MTLLegacySVBuffer" constantDataBuffer;
@"MTLLegacySVDevice" _device;
{mutex="__m_"{_opaque_pthread_mutex_t="__sig"q"__opaque"[56c]}} _constantDataMutex;
Q _constantDataBufferIndex;
{KeyBufferPair="key"{Key="hash"{?="key"[32C]}"data"@"NSData"}"buffer"@"<MTLBuffer>"} _constantDataKeyPair;
@"NSString" _loadedImageName;
@"MTLDebugInstrumentationData" _debugInstrumentationData;
i _imageType;
Q _imageID;
Q _functionType;
@"MTLLegacySVFunction" _function;
@"MTLLegacySVDynamicLibrary" _dynamicLibrary;
```

## Properties

```
@property (T@"NSString",R,N) loadedImageName;
@property (Ti,R,N) imageType;
@property (T@"MTLDebugInstrumentationData",R,N) debugInstrumentationData;
@property (TQ,R,N) functionType;
@property (T@"MTLLegacySVFunction",R,W,N) function;
@property (T@"MTLLegacySVDynamicLibrary",R,W,N) dynamicLibrary;
```

## Instance methods

```
-[MTLLegacySVImageData functionType];
-[MTLLegacySVImageData function];
-[MTLLegacySVImageData imageType];
-[MTLLegacySVImageData dealloc];
-[MTLLegacySVImageData debugInstrumentationData];
-[MTLLegacySVImageData initWithFunction:];
-[MTLLegacySVImageData setConstantData:];
-[MTLLegacySVImageData dynamicLibrary];
-[MTLLegacySVImageData initWithDynamicLibrary:];
-[MTLLegacySVImageData loadedImageName];
-[MTLLegacySVImageData _applyConstantRelocation];
-[MTLLegacySVImageData _applyConstantRelocation:];
-[MTLLegacySVImageData _applyImageIDRelocation:];
-[MTLLegacySVImageData initWithFunction:debugInstrumentationData:];
```
