# `BWColorConstancyProcessorController`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWStillImageProcessorController`
- Protocols: `BWColorConstancyProcessorControllerInputUpdatesDelegate`, `CMIColourConstancyProcessorDelegate`
- 5 instance variables, 5 properties, 11 instance methods, 1 class methods

## Instance variables

```
i _version;
I _outputPixelFormat;
@"<CMIColourConstancyProcessorProtocol>" _processor;
^{opaqueCMFormatDescription=} _outputFormatDescription;
^{opaqueCMFormatDescription=} _confidenceMapFormatDescription;
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
+[BWColorConstancyProcessorController usesCustomProcessingFlow];
```

## Instance methods

```
-[BWColorConstancyProcessorController inputAddFrameFailed:];
-[BWColorConstancyProcessorController process];
-[BWColorConstancyProcessorController dealloc];
-[BWColorConstancyProcessorController reset];
-[BWColorConstancyProcessorController input:addFlashFrame:];
-[BWColorConstancyProcessorController initWithConfiguration:];
-[BWColorConstancyProcessorController prepare];
-[BWColorConstancyProcessorController input:addAmbientFrame:];
-[BWColorConstancyProcessorController metalImageBufferProcessor];
-[BWColorConstancyProcessorController requestForInput:delegate:errOut:];
-[BWColorConstancyProcessorController outputPixelFormat];
```
