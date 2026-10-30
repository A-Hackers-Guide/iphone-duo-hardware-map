# `BWSWFRProcessorController`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWStillImageProcessorController`
- Protocols: `BWSWFRProcessorControllerInputUpdatesDelegate`, `CMISoftwareFlashRenderingProcessorDelegate`
- 5 instance variables, 5 properties, 12 instance methods, 1 class methods

## Instance variables

```
i _version;
I _outputPixelFormat;
@"<CMISoftwareFlashRenderingProcessor>" _processor;
^{opaqueCMFormatDescription=} _outputFormatDescription;
^{opaqueCMFormatDescription=} _demosaicedRawFormatDescription;
```

## Properties

```
@property (TI,R,N,V_outputPixelFormat) outputPixelFormat;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BWSWFRProcessorController usesCustomProcessingFlow];
```

## Instance methods

```
-[BWSWFRProcessorController inputAddFrameFailed:];
-[BWSWFRProcessorController process];
-[BWSWFRProcessorController dealloc];
-[BWSWFRProcessorController reset];
-[BWSWFRProcessorController input:addFlashFrame:];
-[BWSWFRProcessorController initWithConfiguration:];
-[BWSWFRProcessorController prepare];
-[BWSWFRProcessorController processorNewInferences:];
-[BWSWFRProcessorController input:addAmbientFrame:];
-[BWSWFRProcessorController metalImageBufferProcessor];
-[BWSWFRProcessorController requestForInput:delegate:errOut:];
-[BWSWFRProcessorController outputPixelFormat];
```
