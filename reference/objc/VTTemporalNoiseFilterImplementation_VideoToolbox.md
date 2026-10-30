# `VTTemporalNoiseFilterImplementation`

- Image: [`/System/Library/Frameworks/VideoToolbox.framework/VideoToolbox`](../userland/System__Library__Frameworks__VideoToolbox.framework__VideoToolbox.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `VTFrameProcessorImplementationPrivate`
- 2 instance variables, 6 properties, 21 instance methods, 0 class methods

## Instance variables

```
^{OpaqueVTTemporalNoiseFilterInternal=^{OpaqueVTTemporalFilterSession}^{OpaqueVTPixelTransferSession}@@@{pendingFrameList=^{PendingFrameItem}}^{OpaqueFigSimpleMutex}{?=qiIq}{?=qiIq}iBB} filterInternal;
@"VTTemporalNoiseFilterConfiguration" _configuration;
```

## Properties

```
@property (T@"VTTemporalNoiseFilterConfiguration",R,N,V_configuration) configuration;
@property (Tq,?,R,N) modelID;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[VTTemporalNoiseFilterImplementation finishProcessing];
-[VTTemporalNoiseFilterImplementation init];
-[VTTemporalNoiseFilterImplementation dealloc];
-[VTTemporalNoiseFilterImplementation configuration];
-[VTTemporalNoiseFilterImplementation _completeFrames];
-[VTTemporalNoiseFilterImplementation _completeFrame:];
-[VTTemporalNoiseFilterImplementation _createPendingFrame:inputFrame:];
-[VTTemporalNoiseFilterImplementation _checkForDiscontinuity:];
-[VTTemporalNoiseFilterImplementation _clearStaledPendingFramesFromQueue];
-[VTTemporalNoiseFilterImplementation _filterStrengthValue:];
-[VTTemporalNoiseFilterImplementation _findFrameInQueue:];
-[VTTemporalNoiseFilterImplementation _freePendingFrame:];
-[VTTemporalNoiseFilterImplementation _processFrame:outputFrame:useClientProvidedOutputFrame:];
-[VTTemporalNoiseFilterImplementation _processReferenceFrameIfNotProcessed:];
-[VTTemporalNoiseFilterImplementation _processSourceFrameIfNotProcessed:completionHandler:];
-[VTTemporalNoiseFilterImplementation _setFilterStrength:];
-[VTTemporalNoiseFilterImplementation _validateParameters:];
-[VTTemporalNoiseFilterImplementation handleEmittedFrame:presentationTimestamp:status:infoFlags:];
-[VTTemporalNoiseFilterImplementation processWithParams:completionHandler:error:];
-[VTTemporalNoiseFilterImplementation processWithParams:error:];
-[VTTemporalNoiseFilterImplementation startSessionWithConfiguration:error:];
```
