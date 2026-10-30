# `BWStillImageTimeMachineFrameCoordinatorNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWNode`
- 4 instance variables, 0 properties, 12 instance methods, 1 class methods

## Instance variables

```
@"NSDictionary" _portTypeToInput;
@"NSDictionary" _portTypeToOutput;
@"NSMutableDictionary" _portTypeToFrameCounts;
@"BWStillImageCaptureSettings" _currentResolvedStillImageCaptureSettings;
```

## Class methods

```
+[BWStillImageTimeMachineFrameCoordinatorNode initialize];
```

## Instance methods

```
-[BWStillImageTimeMachineFrameCoordinatorNode renderSampleBuffer:forInput:];
-[BWStillImageTimeMachineFrameCoordinatorNode inputForPortType:];
-[BWStillImageTimeMachineFrameCoordinatorNode dealloc];
-[BWStillImageTimeMachineFrameCoordinatorNode outputForPortType:];
-[BWStillImageTimeMachineFrameCoordinatorNode handleDroppedSample:forInput:];
-[BWStillImageTimeMachineFrameCoordinatorNode initWithPortTypes:];
-[BWStillImageTimeMachineFrameCoordinatorNode nodeSubType];
-[BWStillImageTimeMachineFrameCoordinatorNode didSelectFormat:forInput:];
-[BWStillImageTimeMachineFrameCoordinatorNode configurationWithID:updatedFormat:didBecomeLiveForInput:];
-[BWStillImageTimeMachineFrameCoordinatorNode handleNodeError:forInput:];
-[BWStillImageTimeMachineFrameCoordinatorNode nodeType];
-[BWStillImageTimeMachineFrameCoordinatorNode didReachEndOfDataForInput:];
```
