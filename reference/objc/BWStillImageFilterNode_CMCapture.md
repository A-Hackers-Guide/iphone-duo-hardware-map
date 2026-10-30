# `BWStillImageFilterNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWNode`
- 4 instance variables, 0 properties, 13 instance methods, 1 class methods

## Instance variables

```
@"BWStillImageFilterNodeConfiguration" _nodeConfiguration;
@"<BWStillImageFilterStatusDelegate>" _statusDelegate;
@"BWStillImageFilterNodeResourceCoordinator" _resourceCoordinator;
@"NSMutableDictionary" _captureStateByCaptureIdentifier;
```

## Class methods

```
+[BWStillImageFilterNode initialize];
```

## Instance methods

```
-[BWStillImageFilterNode prepareForCurrentConfigurationToBecomeLive];
-[BWStillImageFilterNode injectRendererProvider:];
-[BWStillImageFilterNode sharePhotoEncoderControllerForPiecemealEncoding:];
-[BWStillImageFilterNode renderSampleBuffer:forInput:];
-[BWStillImageFilterNode dealloc];
-[BWStillImageFilterNode handleStillImagePrewarmWithSettings:resourceConfig:forInput:];
-[BWStillImageFilterNode initWithNodeConfiguration:statusDelegate:];
-[BWStillImageFilterNode didSelectFormat:forInput:forAttachedMediaKey:];
-[BWStillImageFilterNode didReachEndOfDataForConfigurationID:input:];
-[BWStillImageFilterNode nodeSubType];
-[BWStillImageFilterNode configurationWithID:updatedFormat:didBecomeLiveForInput:];
-[BWStillImageFilterNode handleNodeError:forInput:];
-[BWStillImageFilterNode nodeType];
```
