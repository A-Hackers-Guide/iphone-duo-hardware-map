# `BWApplySmartStyleRenderer`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BWFilterRenderer`
- 6 instance variables, 8 properties, 13 instance methods, 2 class methods

## Instance variables

```
@"<CMISmartStyleProcessor>" _smartStyleProcessor;
@"BWSmartStyleRendererConfiguration" _configuration;
# _smartStyleProcessorInputOutputClass;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _appliedCropRect;
{?="width"i"height"i} _appliedCropInputDimensions;
{?="width"i"height"i} _appliedCropOutputDimensions;
```

## Properties

```
@property (T@"NSString",R,C,N) displayName;
@property (Ts,R,N) type;
@property (TB,R,N) supportsAnimation;
@property (TB,R,N) adjustsMetadata;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BWApplySmartStyleRenderer initialize];
+[BWApplySmartStyleRenderer requiredSharedMetalAllocatorBackendSizeWithProcessorVersion:];
```

## Instance methods

```
-[BWApplySmartStyleRenderer displayName];
-[BWApplySmartStyleRenderer dealloc];
-[BWApplySmartStyleRenderer initWithConfiguration:];
-[BWApplySmartStyleRenderer type];
-[BWApplySmartStyleRenderer adjustsMetadata];
-[BWApplySmartStyleRenderer isMetalRenderer];
-[BWApplySmartStyleRenderer adjustMetadataOfSampleBuffer:];
-[BWApplySmartStyleRenderer isPassThroughRenderer];
-[BWApplySmartStyleRenderer prepareForProcessingType:];
-[BWApplySmartStyleRenderer prepareForRenderingWithParameters:inputVideoFormat:inputMediaPropertiesByAttachedMediaKey:];
-[BWApplySmartStyleRenderer renderUsingParameters:inputPixelBuffer:inputSampleBuffer:processedPixelBuffer:completionHandler:];
-[BWApplySmartStyleRenderer supportsAnimation];
-[BWApplySmartStyleRenderer waitForMetalCompletion];
```
