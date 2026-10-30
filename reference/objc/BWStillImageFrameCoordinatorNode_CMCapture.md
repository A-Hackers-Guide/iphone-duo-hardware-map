# `BWStillImageFrameCoordinatorNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWNode`
- 12 instance variables, 0 properties, 16 instance methods, 1 class methods

## Instance variables

```
@"BWStillImageNodeConfiguration" _nodeConfiguration;
@"NSDictionary" _portTypeToInput;
@"NSDictionary" _portTypeToOutput;
@"NSDictionary" _portTypeToSensorRawInput;
@"NSDictionary" _portTypeToSensorRawOutput;
@"NSMutableDictionary" _portTypeToFrameCounters;
@"BWStillImageSettings" _currentStillImageSettings;
@"NSMutableDictionary" _lockedFinalCropRectForOptimizedProcessingForZoomFOVByPortType;
@"NSMutableDictionary" _lockedNormalizedMinimumValidBufferRectForGDCForOptimizedProcessingForZoomFOVByPortType;
B _holdMessagesUntilAllInputsAreLive;
@"NSMutableArray" _queuedMessages;
@"NSMutableArray" _inputsForQueuedMessages;
```

## Class methods

```
+[BWStillImageFrameCoordinatorNode initialize];
```

## Instance methods

```
-[BWStillImageFrameCoordinatorNode initWithNodeConfiguration:inputPortTypes:sensorRawInputPortTypes:];
-[BWStillImageFrameCoordinatorNode sensorRawInputForPortType:];
-[BWStillImageFrameCoordinatorNode renderSampleBuffer:forInput:];
-[BWStillImageFrameCoordinatorNode inputForPortType:];
-[BWStillImageFrameCoordinatorNode sensorRawOutputForPortType:];
-[BWStillImageFrameCoordinatorNode dealloc];
-[BWStillImageFrameCoordinatorNode outputForPortType:];
-[BWStillImageFrameCoordinatorNode handleStillImagePrewarmWithSettings:resourceConfig:forInput:];
-[BWStillImageFrameCoordinatorNode handleDroppedSample:forInput:];
-[BWStillImageFrameCoordinatorNode didReachEndOfDataForConfigurationID:input:];
-[BWStillImageFrameCoordinatorNode nodeSubType];
-[BWStillImageFrameCoordinatorNode _handleMessage:fromInput:];
-[BWStillImageFrameCoordinatorNode didSelectFormat:forInput:];
-[BWStillImageFrameCoordinatorNode configurationWithID:updatedFormat:didBecomeLiveForInput:];
-[BWStillImageFrameCoordinatorNode handleNodeError:forInput:];
-[BWStillImageFrameCoordinatorNode nodeType];
```
