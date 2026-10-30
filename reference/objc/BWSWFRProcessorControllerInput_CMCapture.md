# `BWSWFRProcessorControllerInput`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWStillImageProcessorControllerInput`
- 3 instance variables, 3 properties, 5 instance methods, 0 class methods

## Instance variables

```
^{opaqueCMSampleBuffer=} _flashFrame;
^{opaqueCMSampleBuffer=} _ambientFrame;
B _addFrameFailed;
```

## Properties

```
@property (T^{opaqueCMSampleBuffer=},R,N,V_flashFrame) flashFrame;
@property (T^{opaqueCMSampleBuffer=},R,N,V_ambientFrame) ambientFrame;
@property (TB,R,N,V_addFrameFailed) addFrameFailed;
```

## Instance methods

```
-[BWSWFRProcessorControllerInput dealloc];
-[BWSWFRProcessorControllerInput addFrame:];
-[BWSWFRProcessorControllerInput addFrameFailed];
-[BWSWFRProcessorControllerInput ambientFrame];
-[BWSWFRProcessorControllerInput flashFrame];
```
