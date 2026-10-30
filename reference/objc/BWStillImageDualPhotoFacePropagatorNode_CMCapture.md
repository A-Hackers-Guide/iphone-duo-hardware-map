# `BWStillImageDualPhotoFacePropagatorNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWNode`
- 10 instance variables, 0 properties, 9 instance methods, 1 class methods

## Instance variables

```
q _currentSettingsID;
@"NSArray" _baseZoomFactors;
^{opaqueCMSampleBuffer=} _widerFOVBuffer;
^{opaqueCMSampleBuffer=} _narrowerFOVBuffer;
@"BWNodeError" _widerFOVError;
@"BWNodeError" _narrowerFOVError;
@"BWNodeInput" _widerFOVInput;
@"BWNodeInput" _narrowerFOVInput;
@"BWNodeOutput" _widerFOVOutput;
@"BWNodeOutput" _narrowerFOVOutput;
```

## Class methods

```
+[BWStillImageDualPhotoFacePropagatorNode initialize];
```

## Instance methods

```
-[BWStillImageDualPhotoFacePropagatorNode renderSampleBuffer:forInput:];
-[BWStillImageDualPhotoFacePropagatorNode dealloc];
-[BWStillImageDualPhotoFacePropagatorNode nodeSubType];
-[BWStillImageDualPhotoFacePropagatorNode didSelectFormat:forInput:];
-[BWStillImageDualPhotoFacePropagatorNode configurationWithID:updatedFormat:didBecomeLiveForInput:];
-[BWStillImageDualPhotoFacePropagatorNode handleNodeError:forInput:];
-[BWStillImageDualPhotoFacePropagatorNode nodeType];
-[BWStillImageDualPhotoFacePropagatorNode didReachEndOfDataForInput:];
-[BWStillImageDualPhotoFacePropagatorNode initWithBaseZoomFactors:];
```
