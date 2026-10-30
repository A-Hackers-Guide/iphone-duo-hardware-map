# `PLCameraAgent`

- Image: [`/System/Library/PrivateFrameworks/PowerlogHelperdOperators.framework/PowerlogHelperdOperators`](../userland/System__Library__PrivateFrameworks__PowerlogHelperdOperators.framework__PowerlogHelperdOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PLAgent`
- 11 instance variables, 12 properties, 32 instance methods, 15 class methods

## Instance variables

```
B _frontCameraIsOn;
B _backCameraIsOn;
@"NSMutableDictionary" _cameraState;
@"PLXPCListenerOperatorComposition" _cameraNotification;
@"PLXPCListenerOperatorComposition" _torchNotification;
@"PLXPCListenerOperatorComposition" _smartCamDetectionNotification;
@"PLNSNotificationOperatorComposition" _thermalMonitorListener;
@"NSMutableDictionary" _backgroundBlurState;
d _currentTorchLevel;
@"NSString" _currentTorchBundleId;
@"NSDictionary" _torchPowerModel;
```

## Properties

```
@property (T@"NSMutableDictionary",&,V_cameraState) cameraState;
@property (T@"PLXPCListenerOperatorComposition",R,V_cameraNotification) cameraNotification;
@property (T@"PLXPCListenerOperatorComposition",R,V_torchNotification) torchNotification;
@property (T@"PLXPCListenerOperatorComposition",R,V_smartCamDetectionNotification) smartCamDetectionNotification;
@property (T@"PLNSNotificationOperatorComposition",&,V_thermalMonitorListener) thermalMonitorListener;
@property (TB,V_frontCameraIsOn) frontCameraIsOn;
@property (TB,V_backCameraIsOn) backCameraIsOn;
@property (T@"NSMutableDictionary",&,V_backgroundBlurState) backgroundBlurState;
@property (TB,R,N) allCamerasAreOff;
@property (Td,V_currentTorchLevel) currentTorchLevel;
@property (T@"NSString",&,V_currentTorchBundleId) currentTorchBundleId;
@property (T@"NSDictionary",R,V_torchPowerModel) torchPowerModel;
```

## Class methods

```
+[PLCameraAgent entryEventIntervalDefinitions];
+[PLCameraAgent entryEventPointDefinitions];
+[PLCameraAgent entryEventForwardDefinitions];
+[PLCameraAgent entryEventBackwardDefinitions];
+[PLCameraAgent entryEventNoneDefinitions];
+[PLCameraAgent load];
+[PLCameraAgent defaults];
+[PLCameraAgent isEnabled];
+[PLCameraAgent checkCameraType:];
+[PLCameraAgent distributionFromCameraType:];
+[PLCameraAgent entryEventForwardDefinitionCamera];
+[PLCameraAgent entryEventForwardDefinitionTorch];
+[PLCameraAgent entryEventIntervalDefinitionSmartCamDetection];
+[PLCameraAgent isBackFacingCamera:];
+[PLCameraAgent isFrontFacingCamera:];
```

## Instance methods

```
-[PLCameraAgent cameraState];
-[PLCameraAgent init];
-[PLCameraAgent initOperatorDependancies];
-[PLCameraAgent setCameraState:];
-[PLCameraAgent setThermalMonitorListener:];
-[PLCameraAgent log];
-[PLCameraAgent thermalMonitorListener];
-[PLCameraAgent frontCameraIsOn];
-[PLCameraAgent torchPowerModel];
-[PLCameraAgent getCameraPower:];
-[PLCameraAgent handleCameraEvent:withEntryKey:];
-[PLCameraAgent modelFrontCameraPowerWithEntry:];
-[PLCameraAgent allCamerasAreOff];
-[PLCameraAgent backCameraIsOn];
-[PLCameraAgent backgroundBlurState];
-[PLCameraAgent cameraNotification];
-[PLCameraAgent closeBackCameraAtDate:];
-[PLCameraAgent closeFrontCameraAtDate:];
-[PLCameraAgent closeOpenCameraEventsAtDate:withEntryKey:];
-[PLCameraAgent currentTorchBundleId];
-[PLCameraAgent currentTorchLevel];
-[PLCameraAgent handleTorchEvent:withEntryKey:];
-[PLCameraAgent logEventIntervalSmartCamDetection:];
-[PLCameraAgent modelBackCameraPowerWithEntry:];
-[PLCameraAgent modelTorchPowerWithEntry:];
-[PLCameraAgent setBackCameraIsOn:];
-[PLCameraAgent setBackgroundBlurState:];
-[PLCameraAgent setCurrentTorchBundleId:];
-[PLCameraAgent setCurrentTorchLevel:];
-[PLCameraAgent setFrontCameraIsOn:];
-[PLCameraAgent smartCamDetectionNotification];
-[PLCameraAgent torchNotification];
```
