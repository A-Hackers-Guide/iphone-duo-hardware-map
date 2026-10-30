# `PLAWDCamera`

- Image: [`/System/Library/PrivateFrameworks/PowerlogFullOperators.framework/PowerlogFullOperators`](../userland/System__Library__PrivateFrameworks__PowerlogFullOperators.framework__PowerlogFullOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PLAWDAuxMetrics`
- 9 instance variables, 9 properties, 29 instance methods, 3 class methods

## Instance variables

```
B _prevFrontCameraState;
B _prevBackCameraState;
B _prevTorchCameraState;
@"PLEntryNotificationOperatorComposition" _cameraEventCallback;
@"PLEntryNotificationOperatorComposition" _cameraEventCallbackTorch;
d _frontCameraTimestamp;
d _backCameraTimestamp;
d _torchCameraTimestamp;
q _cameraSubmitCnt;
```

## Properties

```
@property (T@"PLEntryNotificationOperatorComposition",&,V_cameraEventCallback) cameraEventCallback;
@property (T@"PLEntryNotificationOperatorComposition",&,V_cameraEventCallbackTorch) cameraEventCallbackTorch;
@property (TB,V_prevFrontCameraState) prevFrontCameraState;
@property (TB,V_prevBackCameraState) prevBackCameraState;
@property (TB,V_prevTorchCameraState) prevTorchCameraState;
@property (Td,V_frontCameraTimestamp) frontCameraTimestamp;
@property (Td,V_backCameraTimestamp) backCameraTimestamp;
@property (Td,V_torchCameraTimestamp) torchCameraTimestamp;
@property (Tq,V_cameraSubmitCnt) cameraSubmitCnt;
```

## Class methods

```
+[PLAWDCamera entryAggregateDefinitions];
+[PLAWDCamera entryAggregateDefinitionAwdCamera];
+[PLAWDCamera getSharedObjWithOperator:];
```

## Instance methods

```
-[PLAWDCamera cameraSubmitCnt];
-[PLAWDCamera initCameraStats];
-[PLAWDCamera addEntryToCameraTable:withValue:];
-[PLAWDCamera backCameraTimestamp];
-[PLAWDCamera cameraEventCallback];
-[PLAWDCamera cameraEventCallbackTorch];
-[PLAWDCamera frontCameraTimestamp];
-[PLAWDCamera handleBackCameraCallback:];
-[PLAWDCamera handleCameraCallback:];
-[PLAWDCamera handleFrontCameraCallback:];
-[PLAWDCamera handleTorchCameraCallback:];
-[PLAWDCamera prevBackCameraState];
-[PLAWDCamera prevFrontCameraState];
-[PLAWDCamera prevTorchCameraState];
-[PLAWDCamera reInitCameraStats];
-[PLAWDCamera resetCameraTable];
-[PLAWDCamera setBackCameraTimestamp:];
-[PLAWDCamera setCameraEventCallback:];
-[PLAWDCamera setCameraEventCallbackTorch:];
-[PLAWDCamera setCameraSubmitCnt:];
-[PLAWDCamera setFrontCameraTimestamp:];
-[PLAWDCamera setPrevBackCameraState:];
-[PLAWDCamera setPrevFrontCameraState:];
-[PLAWDCamera setPrevTorchCameraState:];
-[PLAWDCamera setTorchCameraTimestamp:];
-[PLAWDCamera startMetricCollection:];
-[PLAWDCamera stopMetricCollection:];
-[PLAWDCamera submitDataToAWDServer:withAwdConn:];
-[PLAWDCamera torchCameraTimestamp];
```
