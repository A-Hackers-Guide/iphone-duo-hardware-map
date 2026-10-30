# `BWSoftISPProcessorControllerInput`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWStillImageProcessorControllerInput`
- 4 instance variables, 4 properties, 11 instance methods, 0 class methods

## Instance variables

```
^{opaqueCMSampleBuffer=} _frame;
i _processingMode;
i _resolutionFlavor;
B _gdcEnabled;
```

## Properties

```
@property (T^{opaqueCMSampleBuffer=},&,N,V_frame) frame;
@property (Ti,R,N,V_resolutionFlavor) resolutionFlavor;
@property (Ti,R,N,V_processingMode) processingMode;
@property (TB,R,N,V_gdcEnabled) gdcEnabled;
```

## Instance methods

```
-[BWSoftISPProcessorControllerInput processingMode];
-[BWSoftISPProcessorControllerInput dealloc];
-[BWSoftISPProcessorControllerInput gdcEnabled];
-[BWSoftISPProcessorControllerInput initWithSettings:portType:resolutionFlavor:];
-[BWSoftISPProcessorControllerInput setFrame:];
-[BWSoftISPProcessorControllerInput resolutionFlavor];
-[BWSoftISPProcessorControllerInput addFrame:processingMode:];
-[BWSoftISPProcessorControllerInput description];
-[BWSoftISPProcessorControllerInput addFrame:processingMode:transferOwnership:];
-[BWSoftISPProcessorControllerInput initWithSettings:portType:resolutionFlavor:gdcEnabled:];
-[BWSoftISPProcessorControllerInput frame];
```
