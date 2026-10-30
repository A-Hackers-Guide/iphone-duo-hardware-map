# `EGStillImageDisparitySubgraph`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `EGGraph`
- 9 instance variables, 4 properties, 6 instance methods, 2 class methods

## Instance variables

```
@"EGSubgraphInput" _primaryReferenceFrameInput;
@"EGSubgraphInput" _secondaryReferenceFrameInput;
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
@property (T@"EGSubgraphInput",R,N,V_primaryReferenceFrameInput) primaryReferenceFrameInput;
@property (T@"EGSubgraphInput",R,N,V_secondaryReferenceFrameInput) secondaryReferenceFrameInput;
@property (T@"NSArray",R,N,V_softISPProcessingCompleteSubgraphOutputs) softISPProcessingCompleteSubgraphOutputs;
@property (T@"NSArray",R,N,V_captureCompleteSubgraphOutputs) captureCompleteSubgraphOutputs;
```

## Class methods

```
+[EGStillImageDisparitySubgraph initialize];
+[EGStillImageDisparitySubgraph isSupportedForSettings:nodeConfiguration:];
```

## Instance methods

```
-[EGStillImageDisparitySubgraph dealloc];
-[EGStillImageDisparitySubgraph captureCompleteSubgraphOutputs];
-[EGStillImageDisparitySubgraph initWithName:stillImageSettings:nodeConfiguration:resourceCoordinator:delegate:];
-[EGStillImageDisparitySubgraph primaryReferenceFrameInput];
-[EGStillImageDisparitySubgraph secondaryReferenceFrameInput];
-[EGStillImageDisparitySubgraph softISPProcessingCompleteSubgraphOutputs];
```
