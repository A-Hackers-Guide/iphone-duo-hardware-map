# `BWEspressoInferenceContext`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 3 properties, 11 instance methods, 1 class methods

## Instance variables

```
i _executionTarget;
^v _espressoContext;
Q _options;
B _shareIntermediateBuffer;
^v _rootIntermediateBufferPlan;
@"NSString" _sharedBufferNetworksPath;
```

## Properties

```
@property (Ti,R,N,V_executionTarget) executionTarget;
@property (T^v,R,N) espressoContext;
@property (TB,R,N,GisPrepared) prepared;
```

## Class methods

```
+[BWEspressoInferenceContext initialize];
```

## Instance methods

```
-[BWEspressoInferenceContext isPrepared];
-[BWEspressoInferenceContext dealloc];
-[BWEspressoInferenceContext executionTarget];
-[BWEspressoInferenceContext enableIntermediateBufferSharingWithNetworksLoadedFromPath:];
-[BWEspressoInferenceContext description];
-[BWEspressoInferenceContext espressoContext];
-[BWEspressoInferenceContext configureIntermediateBufferSharingForPlanPostbuild:];
-[BWEspressoInferenceContext configureIntermediateBufferSharingForPlanPrebuild:];
-[BWEspressoInferenceContext initWithExecutionTarget:];
-[BWEspressoInferenceContext initWithExecutionTarget:shareIntermediateBuffer:];
-[BWEspressoInferenceContext prepareForInference];
```
