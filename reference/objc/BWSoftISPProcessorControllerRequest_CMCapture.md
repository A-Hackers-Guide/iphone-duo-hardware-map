# `BWSoftISPProcessorControllerRequest`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWStillImageProcessorControllerRequest`
- 2 instance variables, 2 properties, 8 instance methods, 0 class methods

## Instance variables

```
Q _uniqueID;
^{opaqueCMSampleBuffer=} _outputFrame;
```

## Properties

```
@property (TQ,R,N,V_uniqueID) uniqueID;
@property (T^{opaqueCMSampleBuffer=},&,N,V_outputFrame) outputFrame;
```

## Instance methods

```
-[BWSoftISPProcessorControllerRequest dealloc];
-[BWSoftISPProcessorControllerRequest outputType];
-[BWSoftISPProcessorControllerRequest uniqueID];
-[BWSoftISPProcessorControllerRequest description];
-[BWSoftISPProcessorControllerRequest setOutputFrame:];
-[BWSoftISPProcessorControllerRequest initWithInput:delegate:];
-[BWSoftISPProcessorControllerRequest outputFrame];
-[BWSoftISPProcessorControllerRequest readyForProcessing];
```
