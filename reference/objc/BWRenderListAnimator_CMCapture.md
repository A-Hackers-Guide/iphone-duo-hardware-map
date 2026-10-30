# `BWRenderListAnimator`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 9 instance variables, 8 properties, 13 instance methods, 1 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _preparationMutexQueue;
B _preparationMutexQueuePrepared;
@"BWRenderList" _interpolatingRenderList;
@"BWRenderListParameters" _interpolatingParameters;
@"BWSpringSimulation" _springSimulation;
@"BWRenderList" _initialRenderList;
@"BWRenderListParameters" _initialParameters;
@"BWRenderList" _finalRenderList;
@"BWRenderListParameters" _finalParameters;
```

## Properties

```
@property (T@"BWRenderList",R,&,N,V_interpolatingRenderList) renderList;
@property (T@"BWRenderListParameters",R,&,N,V_interpolatingParameters) parameters;
@property (T@"BWRenderList",R,&,N,V_initialRenderList) initialRenderList;
@property (T@"BWRenderListParameters",R,&,N,V_initialParameters) initialParameters;
@property (T@"BWRenderList",R,&,N,V_finalRenderList) finalRenderList;
@property (T@"BWRenderListParameters",R,&,N,V_finalParameters) finalParameters;
@property (TB,R,N,GisPrepared) prepared;
@property (TB,R,N,GisCompleted) completed;
```

## Class methods

```
+[BWRenderListAnimator initialize];
```

## Instance methods

```
-[BWRenderListAnimator isPrepared];
-[BWRenderListAnimator parameters];
-[BWRenderListAnimator isCompleted];
-[BWRenderListAnimator dealloc];
-[BWRenderListAnimator description];
-[BWRenderListAnimator finalRenderList];
-[BWRenderListAnimator finalParameters];
-[BWRenderListAnimator initWithInitialParameters:initialRenderList:finalParameters:finalRenderList:animation:];
-[BWRenderListAnimator initialParameters];
-[BWRenderListAnimator initialRenderList];
-[BWRenderListAnimator interpolateParameters];
-[BWRenderListAnimator prepareWithInputVideoFormat:inputMediaPropertiesByAttachedMediaKey:];
-[BWRenderListAnimator renderList];
```
