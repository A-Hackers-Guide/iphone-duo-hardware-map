# `BWStillImageFilterNodeRenderContext`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 11 properties, 20 instance methods, 0 class methods

## Instance variables

```
@"BWStillImageSettings" _stillImageSettings;
@"NSMutableDictionary" _metadata;
I _inputProcessingFlags;
B _applyPortraitFilters;
i _adjustedImageError;
B _requiresDepthSync;
B _smartStyleApplyInFilterList;
@"BWStillImageFilterNodeCaptureState" _captureState;
```

## Properties

```
@property (T@"BWStillImageSettings",R,N,V_stillImageSettings) stillImageSettings;
@property (T@"NSMutableDictionary",R,N,V_metadata) metadata;
@property (TI,R,N,V_inputProcessingFlags) inputProcessingFlags;
@property (TB,R,N) isHDR;
@property (TB,R,N) portraitFiltersRequested;
@property (T@"NSArray",R,N) requestedFilters;
@property (TB,N,V_applyPortraitFilters) applyPortraitFilters;
@property (Ti,N,V_adjustedImageError) adjustedImageError;
@property (TB,N,V_requiresDepthSync) requiresDepthSync;
@property (TB,N,V_smartStyleApplyInFilterList) smartStyleApplyInFilterList;
@property (T@"BWStillImageFilterNodeCaptureState",&,N,V_captureState) captureState;
```

## Instance methods

```
-[BWStillImageFilterNodeRenderContext stillImageSettings];
-[BWStillImageFilterNodeRenderContext captureState];
-[BWStillImageFilterNodeRenderContext isHDR];
-[BWStillImageFilterNodeRenderContext dealloc];
-[BWStillImageFilterNodeRenderContext smartStyleApplyInFilterList];
-[BWStillImageFilterNodeRenderContext initWithSampleBuffer:];
-[BWStillImageFilterNodeRenderContext applyPortraitFilters];
-[BWStillImageFilterNodeRenderContext metadata];
-[BWStillImageFilterNodeRenderContext setApplyPortraitFilters:];
-[BWStillImageFilterNodeRenderContext setCaptureState:];
-[BWStillImageFilterNodeRenderContext setSmartStyleApplyInFilterList:];
-[BWStillImageFilterNodeRenderContext requestedFilters];
-[BWStillImageFilterNodeRenderContext deliverFilteredImageWithSmartStylesInFilterNode:];
-[BWStillImageFilterNodeRenderContext description];
-[BWStillImageFilterNodeRenderContext requiresDepthSync];
-[BWStillImageFilterNodeRenderContext setAdjustedImageError:];
-[BWStillImageFilterNodeRenderContext inputProcessingFlags];
-[BWStillImageFilterNodeRenderContext setRequiresDepthSync:];
-[BWStillImageFilterNodeRenderContext portraitFiltersRequested];
-[BWStillImageFilterNodeRenderContext adjustedImageError];
```
