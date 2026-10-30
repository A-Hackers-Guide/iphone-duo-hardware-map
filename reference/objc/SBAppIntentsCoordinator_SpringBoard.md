# `SBAppIntentsCoordinator`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBINAppIntentsCoordinatorDelegate`, `SBSystemActionPreviewProviding`, `SBSystemActionDataSourceOverriding`
- 6 instance variables, 4 properties, 5 instance methods, 0 class methods

## Instance variables

```
@"NSArray" _allPreviewingActionIdentifiers;
@"SBINAppIntentsCoordinator" _clientCoordinator;
@"SBCameraActivationManager" _cameraActivationManager;
@"SBFlashlightActivityManager" _flashlightActivityManager;
@"SBFocusActivityManager" _focusActivityManager;
@"SBRingerControl" _ringerControl;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBAppIntentsCoordinator appIntentsCoordinator:performAppIntent:withCompletion:];
-[SBAppIntentsCoordinator providesPreviewForActionWithIdentifier:];
-[SBAppIntentsCoordinator showPreviewForAction:withContext:];
-[SBAppIntentsCoordinator soundForPerformingActionWithIdentifier:];
-[SBAppIntentsCoordinator systemActionDataSource:overrideActionForAction:];
```
