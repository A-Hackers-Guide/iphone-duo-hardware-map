# `BWStillImageMultiCameraDoserNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWNode`
- 4 instance variables, 0 properties, 10 instance methods, 1 class methods

## Instance variables

```
@"NSArray" _portTypes;
q _currentSettingsID;
@"NSMutableArray" _inputIndicesForWhichDosingIsPerformed;
@"NSMutableArray" _stashedObjectsByInputIndex;
```

## Class methods

```
+[BWStillImageMultiCameraDoserNode initialize];
```

## Instance methods

```
-[BWStillImageMultiCameraDoserNode renderSampleBuffer:forInput:];
-[BWStillImageMultiCameraDoserNode dealloc];
-[BWStillImageMultiCameraDoserNode initWithPortTypes:];
-[BWStillImageMultiCameraDoserNode nodeSubType];
-[BWStillImageMultiCameraDoserNode didSelectFormat:forInput:];
-[BWStillImageMultiCameraDoserNode configurationWithID:updatedFormat:didBecomeLiveForInput:];
-[BWStillImageMultiCameraDoserNode handleNodeError:forInput:];
-[BWStillImageMultiCameraDoserNode nodeType];
-[BWStillImageMultiCameraDoserNode didReachEndOfDataForInput:];
-[BWStillImageMultiCameraDoserNode outputIndexForPortType:];
```
