# `EGStillImageStereoPhotoSubgraph`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `EGGraph`
- 10 instance variables, 5 properties, 7 instance methods, 1 class methods

## Instance variables

```
@"EGSubgraphInput" _gatingInput;
@"EGSubgraphInput" _primarySbufInput;
@"EGSubgraphInput" _secondarySbufInput;
@"NSMutableArray" _softISPProcessingCompleteSubgraphOutputs;
@"NSMutableArray" _captureCompleteSubgraphOutputs;
@"BWStillImageSettings" _stillImageSettings;
@"BWPhotonicEngineNodeConfiguration" _nodeConfiguration;
@"BWPhotonicEngineNodeResourceCoordinator" _resourceCoordinator;
@"<BWStillImageProcessingCoordinatorDelegate>" _delegate;
@"NSMutableDictionary" _processorControllerSourceNodesByType;
```

## Properties

```
@property (T@"EGSubgraphInput",R,N,V_gatingInput) gatingInput;
@property (T@"EGSubgraphInput",R,N,V_primarySbufInput) primarySbufInput;
@property (T@"EGSubgraphInput",R,N,V_secondarySbufInput) secondarySbufInput;
@property (T@"NSArray",R,N,V_softISPProcessingCompleteSubgraphOutputs) softISPProcessingCompleteSubgraphOutputs;
@property (T@"NSArray",R,N,V_captureCompleteSubgraphOutputs) captureCompleteSubgraphOutputs;
```

## Class methods

```
+[EGStillImageStereoPhotoSubgraph initialize];
```

## Instance methods

```
-[EGStillImageStereoPhotoSubgraph dealloc];
-[EGStillImageStereoPhotoSubgraph captureCompleteSubgraphOutputs];
-[EGStillImageStereoPhotoSubgraph gatingInput];
-[EGStillImageStereoPhotoSubgraph initWithName:stillImageSettings:nodeConfiguration:resourceCoordinator:delegate:];
-[EGStillImageStereoPhotoSubgraph primarySbufInput];
-[EGStillImageStereoPhotoSubgraph secondarySbufInput];
-[EGStillImageStereoPhotoSubgraph softISPProcessingCompleteSubgraphOutputs];
```
