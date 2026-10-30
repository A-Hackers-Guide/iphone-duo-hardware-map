# `BWRenderList`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BWRenderListParameterListProvider`
- 8 instance variables, 12 properties, 16 instance methods, 2 class methods

## Instance variables

```
{BWRenderListRendererList="slh_first"^{BWRenderListRendererNode}} _rendererList;
{BWRenderListParameterList="slh_first"^{BWRenderListParameterNode}} _parameterList;
B _affectsMetadata;
B _supportsAnimation;
@"NSSet" _processedFilterNames;
B _isolationQueuePrepared;
@"NSObject<OS_dispatch_queue>" _preparationIsolationQueue;
B _shouldWaitForLastMetalRendererToComplete;
```

## Properties

```
@property (TB,N,GisPrepared) prepared;
@property (T^{BWRenderListRendererList=^{BWRenderListRendererNode}},R,N) rendererList;
@property (TB,R,N,V_supportsAnimation) supportsAnimation;
@property (TB,R,N,V_affectsMetadata) affectsMetadata;
@property (T@"NSSet",R,N,V_processedFilterNames) processedFilterNames;
@property (TB,R,N) hasMetalColorCubeRenderer;
@property (TB,N,V_shouldWaitForLastMetalRendererToComplete) shouldWaitForLastMetalRendererToComplete;
@property (T^{BWRenderListParameterList=^{BWRenderListParameterNode}},R,N) parameterList;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BWRenderList initialize];
+[BWRenderList shallowDepthOfFieldFilterName];
```

## Instance methods

```
-[BWRenderList isPrepared];
-[BWRenderList dealloc];
-[BWRenderList description];
-[BWRenderList setPrepared:];
-[BWRenderList affectsMetadata];
-[BWRenderList hasMetalColorCubeRenderer];
-[BWRenderList initWithAnimationSupported:affectsMetadata:];
-[BWRenderList initWithResourceProvider:processedFilters:optimizationStrategy:stillImageSettings:];
-[BWRenderList parameterList];
-[BWRenderList prepareWithParameters:forInputVideoFormat:inputMediaPropertiesByAttachedMediaKey:];
-[BWRenderList processedFilterNames];
-[BWRenderList rendererList];
-[BWRenderList setShouldWaitForLastMetalRendererToComplete:];
-[BWRenderList shouldWaitForLastMetalRendererToComplete];
-[BWRenderList supportsAnimation];
-[BWRenderList waitForLastMetalRendererToComplete];
```
