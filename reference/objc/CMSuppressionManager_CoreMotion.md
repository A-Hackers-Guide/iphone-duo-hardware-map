# `CMSuppressionManager`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `DPCWatchPresenceDelegate`
- 4 instance variables, 7 properties, 48 instance methods, 3 class methods

## Instance variables

```
@ _internal;
B _isCameraCapturePose;
q _cameraCapturePoseUIHint;
q _suppressionClientType;
```

## Properties

```
@property (TB,R,N,V_isCameraCapturePose) isCameraCapturePose;
@property (Tq,R,N,V_cameraCapturePoseUIHint) cameraCapturePoseUIHint;
@property (Tq,R,N,V_suppressionClientType) suppressionClientType;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[CMSuppressionManager isAvailable];
+[CMSuppressionManager isSourceAvailable:];
+[CMSuppressionManager isSourceAvailable:configType:];
```

## Instance methods

```
-[CMSuppressionManager connect];
-[CMSuppressionManager init];
-[CMSuppressionManager dealloc];
-[CMSuppressionManager deallocPrivate];
-[CMSuppressionManager onNotification:];
-[CMSuppressionManager didDetectSignificantUserInteraction];
-[CMSuppressionManager initWithClientType:];
-[CMSuppressionManager cameraCapturePoseUIHint];
-[CMSuppressionManager currentSuppressionEvent];
-[CMSuppressionManager feedDevicePresenceEvent:timestamp:force:];
-[CMSuppressionManager feedDeviceStateEvent:facedown:timestamp:force:];
-[CMSuppressionManager feedSmartPowerNapEvent:timestamp:force:];
-[CMSuppressionManager feedViewObstructedEvent:facedown:timeSinceLastFacedownStatic:timestamp:force:];
-[CMSuppressionManager handleDeviceStateEvent:];
-[CMSuppressionManager handleSmartPowerNapState:];
-[CMSuppressionManager initPrivateWithClientType:configType:];
-[CMSuppressionManager initWithClientType:configType:];
-[CMSuppressionManager isCameraCapturePose];
-[CMSuppressionManager managerDidDetectEvent:];
-[CMSuppressionManager managerDidFindError:];
-[CMSuppressionManager onCameraCapturePoseData:];
-[CMSuppressionManager onEclipseData:];
-[CMSuppressionManager onViewObstructedStateData:];
-[CMSuppressionManager sendServiceRequestPrivate];
-[CMSuppressionManager sendSuppressionEventToClientPrivate];
-[CMSuppressionManager sendViewObstructedRequestPrivate];
-[CMSuppressionManager sendViewObstructedStateToClientPrivate:];
-[CMSuppressionManager simulateSignificantUserInteraction];
-[CMSuppressionManager startCameraCapturePoseUpdatesPrivateToQueue:withHandler:];
-[CMSuppressionManager startCameraCapturePoseUpdatesToQueue:withHandler:];
-[CMSuppressionManager startService];
-[CMSuppressionManager startSuppressionUpdatesPrivateToQueue:withHandler:];
-[CMSuppressionManager startSuppressionUpdatesToQueue:withHandler:];
-[CMSuppressionManager startSuppressionUpdatesToQueue:withOptions:withHandler:];
-[CMSuppressionManager startViewObstructedStateUpdatesPrivateToQueue:withHandler:];
-[CMSuppressionManager startViewObstructedStateUpdatesToQueue:withHandler:];
-[CMSuppressionManager staticPoseBlocking];
-[CMSuppressionManager stopCameraCapturePoseUpdates];
-[CMSuppressionManager stopCameraCapturePoseUpdatesPrivate];
-[CMSuppressionManager stopService];
-[CMSuppressionManager stopSuppressionUpdates];
-[CMSuppressionManager stopSuppressionUpdatesPrivate];
-[CMSuppressionManager stopViewObstructedStateUpdates];
-[CMSuppressionManager stopViewObstructedStateUpdatesPrivate];
-[CMSuppressionManager suppressionClientType];
-[CMSuppressionManager updateCurrentSuppressionEvent:timestamp:reason:facedownState:timeSinceLastFacedownStatic:];
-[CMSuppressionManager updateSuppressionStateAndSendToClient];
-[CMSuppressionManager viewObstructedBlocking];
```
