# `SBFDIDeviceControlCoordinator`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBSFDIDeviceControlCoordinating`
- 3 instance variables, 4 properties, 6 instance methods, 3 class methods

## Instance variables

```
@"NSMutableArray" _disableLiftToWakeAssertions;
@"NSMutableArray" _disableTapToWakeAssertions;
@"<BSInvalidatable>" _disableInnerDisplayAssertion;
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
+[SBFDIDeviceControlCoordinator _scene:hasEntitlement:];
+[SBFDIDeviceControlCoordinator addSceneExtensionToScene:];
+[SBFDIDeviceControlCoordinator removeSceneExtensionIfNotNeededForConnectedScene:];
```

## Instance methods

```
-[SBFDIDeviceControlCoordinator init];
-[SBFDIDeviceControlCoordinator invalidate];
-[SBFDIDeviceControlCoordinator applyFDIDeviceControlClientSettings:];
-[SBFDIDeviceControlCoordinator _updateInnerDisplayRestricted:];
-[SBFDIDeviceControlCoordinator _updateLiftToWakeForWindowScenes:wantsSuppression:];
-[SBFDIDeviceControlCoordinator _updateTapToWakeForWindowScenes:wantsSuppression:];
```
