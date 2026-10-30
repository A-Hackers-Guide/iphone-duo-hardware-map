# `BWJasperDisparityProcessorController`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWStillImageProcessorController`
- Protocols: `BWJasperDisparityProcessorInputDelegate`
- 9 instance variables, 4 properties, 13 instance methods, 1 class methods

## Instance variables

```
@"FigStateMachine" _stateMachine;
@"BWJasperDisparityProcessorControllerConfiguration" _configuration;
@"ADJasperColorV2Executor" _adStillImageExecutor;
@"NSMutableArray" _requestQueue;
@"BWJasperDisparityProcessorRequest" _currentRequest;
^{opaqueCMFormatDescription=} _depthFormatDescription;
{?="columns"[4]} _identityMatrix;
@"NSMutableArray" _pointClouds;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _pointCloudsLock;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BWJasperDisparityProcessorController initialize];
```

## Instance methods

```
-[BWJasperDisparityProcessorController finishProcessingCurrentInputNow];
-[BWJasperDisparityProcessorController dealloc];
-[BWJasperDisparityProcessorController initWithConfiguration:];
-[BWJasperDisparityProcessorController type];
-[BWJasperDisparityProcessorController cancelProcessing];
-[BWJasperDisparityProcessorController _execute];
-[BWJasperDisparityProcessorController jasperPointCloudForColorBuffer:];
-[BWJasperDisparityProcessorController _serviceNextRequest];
-[BWJasperDisparityProcessorController _setupJasperDisparityProcessor];
-[BWJasperDisparityProcessorController _updateStateIfNeeded];
-[BWJasperDisparityProcessorController addPointCloudToTimeMachine:];
-[BWJasperDisparityProcessorController enqueueInputForProcessing:delegate:];
-[BWJasperDisparityProcessorController inputReadyToExecute:];
```
