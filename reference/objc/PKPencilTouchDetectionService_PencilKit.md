# `PKPencilTouchDetectionService`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSXPCListenerDelegate`, `_PKTouchDetectionProtocol`, `PKPencilTouchDetectionGestureRecognizerDelegate`
- 9 instance variables, 13 properties, 33 instance methods, 2 class methods

## Instance variables

```
B _isListening;
B _wereFrontBoardOverlaysEnabled;
@"NSXPCListener" _listener;
@"FBSDisplayLayoutMonitor" _displayLayoutMonitor;
@"PKPencilTouchDetectionGestureRecognizer" _detectionGesture;
@"NSUserDefaults" _pencilDefaults;
@"NSMutableDictionary" _timestamps;
@"NSDictionary" _userInfoForNotification;
d _activePencilUsageTimestamp;
```

## Properties

```
@property (T@"NSXPCListener",&,N,V_listener) listener;
@property (TB,N,V_isListening) isListening;
@property (T@"FBSDisplayLayoutMonitor",&,N,V_displayLayoutMonitor) displayLayoutMonitor;
@property (TB,N,V_wereFrontBoardOverlaysEnabled) wereFrontBoardOverlaysEnabled;
@property (T@"PKPencilTouchDetectionGestureRecognizer",&,N,V_detectionGesture) detectionGesture;
@property (T@"NSUserDefaults",&,N,V_pencilDefaults) pencilDefaults;
@property (T@"NSMutableDictionary",&,N,V_timestamps) timestamps;
@property (T@"NSDictionary",&,N,V_userInfoForNotification) userInfoForNotification;
@property (Td,N,V_activePencilUsageTimestamp) activePencilUsageTimestamp;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[PKPencilTouchDetectionService sharedInstance];
+[PKPencilTouchDetectionService beginObservingTouchesForDetection];
```

## Instance methods

```
-[PKPencilTouchDetectionService reset:];
-[PKPencilTouchDetectionService timestamps];
-[PKPencilTouchDetectionService listener:shouldAcceptNewConnection:];
-[PKPencilTouchDetectionService init];
-[PKPencilTouchDetectionService dealloc];
-[PKPencilTouchDetectionService setListener:];
-[PKPencilTouchDetectionService isListening];
-[PKPencilTouchDetectionService setTimestamps:];
-[PKPencilTouchDetectionService listener];
-[PKPencilTouchDetectionService pencilDefaults];
-[PKPencilTouchDetectionService setDisplayLayoutMonitor:];
-[PKPencilTouchDetectionService displayLayoutMonitor];
-[PKPencilTouchDetectionService setIsListening:];
-[PKPencilTouchDetectionService _nop:];
-[PKPencilTouchDetectionService userInfoForNotification];
-[PKPencilTouchDetectionService _updateActivePencilUsageForTouchType:];
-[PKPencilTouchDetectionService activePencilUsageTimestamp];
-[PKPencilTouchDetectionService detectionGesture];
-[PKPencilTouchDetectionService loadDefaultsIfNecessary];
-[PKPencilTouchDetectionService loadTimestampsIfNecessary];
-[PKPencilTouchDetectionService pencilType:hasRecentlyBeenUsedWithCompletionHandler:];
-[PKPencilTouchDetectionService persistTimestamps];
-[PKPencilTouchDetectionService postUpdateNotificationIfNecessary];
-[PKPencilTouchDetectionService resumeConnectionIfIdle];
-[PKPencilTouchDetectionService setActivePencilUsageTimestamp:];
-[PKPencilTouchDetectionService setDetectionGesture:];
-[PKPencilTouchDetectionService setPencilDefaults:];
-[PKPencilTouchDetectionService setUserInfoForNotification:];
-[PKPencilTouchDetectionService setWereFrontBoardOverlaysEnabled:];
-[PKPencilTouchDetectionService stringForTouchDetectionPencilType:];
-[PKPencilTouchDetectionService timestampIndicatesRecentUsage:];
-[PKPencilTouchDetectionService updateTimestampForType:];
-[PKPencilTouchDetectionService wereFrontBoardOverlaysEnabled];
```
