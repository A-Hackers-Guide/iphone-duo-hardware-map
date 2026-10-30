# `BWStillImageBravoDisparityNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWNode`
- 20 instance variables, 2 properties, 16 instance methods, 1 class methods

## Instance variables

```
@"NSDictionary" _sensorConfigurationsByPortType;
@"FigDisparityGenerator" _disparityGenerator;
@"BWNodeInput" _wideInput;
@"BWNodeInput" _telephotoInput;
Q _disparityMapWidth;
Q _disparityMapHeight;
^{opaqueCMFormatDescription=} _disparityFormatDescription;
@"BWStillImageSettings" _currentStillImageSettings;
i _expectedDisparityCount;
i _deliveredDisparityCount;
i _processingMode;
^{opaqueCMSampleBuffer=} _teleSbuf;
^{opaqueCMSampleBuffer=} _wideSbuf;
B _emitTeleFrame;
B _emitWideFrame;
@"BWNodeError" _errorForWide;
@"BWNodeError" _errorForTele;
B _shouldComputeDisparityWhenCalibrationFails;
B _disparityInputIsRaw;
@"BWStillImageNodeConfiguration" _nodeConfiguration;
```

## Properties

```
@property (T@"BWNodeInput",R,N,V_wideInput) wideInput;
@property (T@"BWNodeInput",R,N,V_telephotoInput) telephotoInput;
```

## Class methods

```
+[BWStillImageBravoDisparityNode initialize];
```

## Instance methods

```
-[BWStillImageBravoDisparityNode prepareForCurrentConfigurationToBecomeLive];
-[BWStillImageBravoDisparityNode renderSampleBuffer:forInput:];
-[BWStillImageBravoDisparityNode dealloc];
-[BWStillImageBravoDisparityNode setShouldComputeDisparityWhenCalibrationFails:];
-[BWStillImageBravoDisparityNode didSelectFormat:forInput:forAttachedMediaKey:];
-[BWStillImageBravoDisparityNode nodeSubType];
-[BWStillImageBravoDisparityNode configurationWithID:updatedFormat:didBecomeLiveForInput:];
-[BWStillImageBravoDisparityNode shouldComputeDisparityWhenCalibrationFails];
-[BWStillImageBravoDisparityNode handleNodeError:forInput:];
-[BWStillImageBravoDisparityNode nodeType];
-[BWStillImageBravoDisparityNode attachesInputBracketToOutputSampleBuffer];
-[BWStillImageBravoDisparityNode didReachEndOfDataForInput:];
-[BWStillImageBravoDisparityNode initWithNodeConfiguration:sensorConfigurationsByPortType:disparityMapWidth:disparityMapHeight:outputDisparityBufferCount:];
-[BWStillImageBravoDisparityNode setAttachesInputBracketToOutputSampleBuffer:];
-[BWStillImageBravoDisparityNode telephotoInput];
-[BWStillImageBravoDisparityNode wideInput];
```
