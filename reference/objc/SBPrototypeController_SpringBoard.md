# `SBPrototypeController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `PTUIClient`
- 7 instance variables, 6 properties, 22 instance methods, 1 class methods

## Instance variables

```
@"NSXPCConnection" _prototypingUIServerConnection;
@"<BSInvalidatable>" _routingKeysAssertion;
@"SBPrototypeDumpingGround" _dumpingGround;
@"SBRootSettings" _rootSettings;
@"SBSBackgroundActivityAssertion" _remotePrototypingAssertion;
@"SBRestartManager" _restartManager;
@"SBWindowScene" _windowScene;
```

## Properties

```
@property (T@"SBRestartManager",W,N,V_restartManager) restartManager;
@property (T@"SBWindowScene",W,N,V_windowScene) windowScene;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBPrototypeController sharedInstance];
```

## Instance methods

```
-[SBPrototypeController setWindowScene:];
-[SBPrototypeController rootSettings];
-[SBPrototypeController init];
-[SBPrototypeController _sendEvent:];
-[SBPrototypeController _createConnection];
-[SBPrototypeController handleKeyHIDEvent:];
-[SBPrototypeController windowScene];
-[SBPrototypeController killSpringBoard];
-[SBPrototypeController _acquireRemotePrototypingAssertion];
-[SBPrototypeController _handleKeyHIDEvent:];
-[SBPrototypeController _handlePrototypingEvent:];
-[SBPrototypeController _invalidateRemotePrototypingAssertion];
-[SBPrototypeController _shouldSendEvent:];
-[SBPrototypeController _updateKeyHIDEventRouters];
-[SBPrototypeController _updateRemoteEditingState];
-[SBPrototypeController handleRingerButtonEvent];
-[SBPrototypeController handleRingerSwitchEvent];
-[SBPrototypeController handleVolumeDecreaseEvent];
-[SBPrototypeController handleVolumeIncreaseEvent];
-[SBPrototypeController restartManager];
-[SBPrototypeController restartSpringBoard];
-[SBPrototypeController setRestartManager:];
```
