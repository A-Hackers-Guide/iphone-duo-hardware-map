# `BWStereoDisparityProcessorInput`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWStillImageProcessorControllerInput`
- 6 instance variables, 6 properties, 14 instance methods, 0 class methods

## Instance variables

```
@"<BWStereoDisparityProcessorInputDelegate>" _delegate;
^{opaqueCMSampleBuffer=} _referenceSbuf;
^{opaqueCMSampleBuffer=} _auxiliarySbuf;
B _equalizeTeleGainToMatchReference;
B _emitAuxiliaryInput;
@"NSSet" _expectedPortTypes;
```

## Properties

```
@property (T@"<BWStereoDisparityProcessorInputDelegate>",&,N,V_delegate) delegate;
@property (TB,N,V_equalizeTeleGainToMatchReference) equalizeTeleGainToMatchReference;
@property (TB,N,V_emitAuxiliaryInput) emitAuxiliaryInput;
@property (T@"NSSet",&,N,V_expectedPortTypes) expectedPortTypes;
@property (T^{opaqueCMSampleBuffer=},R,N,V_referenceSbuf) referenceSbuf;
@property (T^{opaqueCMSampleBuffer=},R,N,V_auxiliarySbuf) auxiliarySbuf;
```

## Instance methods

```
-[BWStereoDisparityProcessorInput setEqualizeTeleGainToMatchReference:];
-[BWStereoDisparityProcessorInput addSampleBuffer:];
-[BWStereoDisparityProcessorInput dealloc];
-[BWStereoDisparityProcessorInput setDelegate:];
-[BWStereoDisparityProcessorInput delegate];
-[BWStereoDisparityProcessorInput description];
-[BWStereoDisparityProcessorInput equalizeTeleGainToMatchReference];
-[BWStereoDisparityProcessorInput initWithSettings:portType:];
-[BWStereoDisparityProcessorInput auxiliarySbuf];
-[BWStereoDisparityProcessorInput emitAuxiliaryInput];
-[BWStereoDisparityProcessorInput expectedPortTypes];
-[BWStereoDisparityProcessorInput referenceSbuf];
-[BWStereoDisparityProcessorInput setEmitAuxiliaryInput:];
-[BWStereoDisparityProcessorInput setExpectedPortTypes:];
```
