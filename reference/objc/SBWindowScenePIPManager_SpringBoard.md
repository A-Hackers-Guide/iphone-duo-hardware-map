# `SBWindowScenePIPManager`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBFZStackParticipantDelegate`, `SBWindowSceneAttachmentObserving`
- 10 instance variables, 8 properties, 31 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _contentTypeToStashedPadding;
@"NSMutableDictionary" _contentTypeToWindowMargins;
@"NSMutableDictionary" _contentTypeToWindowLevelOverrideAssertions;
@"NSMutableDictionary" _sourceToEdgeInsets;
@"NSMapTable" _stashAssertionsToCompoundAssertionMap;
@"SBFZStackParticipant" _zStackParticipant;
@"_SBPIPEndStashTabSuppressionGestureManager" _endStashTabSuppressionGestureManager;
@"SBSplitPIPSystemChromePresentation" _splitPIPSystemChromePresentation;
@"SBPIPControllerCoordinator" _globalCoordinator;
@"SBWindowScene" _windowScene;
```

## Properties

```
@property (T@"NSDictionary",C,N,G_sourceToEdgeInsets,V_sourceToEdgeInsets) sourceToEdgeInsets;
@property (T{UIEdgeInsets=dddd},R,N,G_minimumStashedPadding) minimumStashedPadding;
@property (T@"SBPIPControllerCoordinator",R,N,V_globalCoordinator) globalCoordinator;
@property (T@"SBWindowScene",R,W,N,V_windowScene) windowScene;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBWindowScenePIPManager _systemApertureInsetsDidChange:];
-[SBWindowScenePIPManager zStackParticipant:updatePreferences:];
-[SBWindowScenePIPManager windowSceneDidDisconnect:];
-[SBWindowScenePIPManager zStackParticipantDidChange:];
-[SBWindowScenePIPManager _windowManagementStyleDidChange:];
-[SBWindowScenePIPManager windowSceneDidConnect:];
-[SBWindowScenePIPManager windowScene];
-[SBWindowScenePIPManager _floatingDockHeightWillChange:];
-[SBWindowScenePIPManager _minimumStashedPadding];
-[SBWindowScenePIPManager _shelfHeightDidChange:];
-[SBWindowScenePIPManager _sourceToEdgeInsets];
-[SBWindowScenePIPManager _splitPIPSystemChromePresentationDidChange:reason:];
-[SBWindowScenePIPManager _splitPIPSystemChromePresentationDidInvalidate:];
-[SBWindowScenePIPManager _updateFloatingDockInsetsWithoutNotifyingControllers];
-[SBWindowScenePIPManager _windowLevelOverrideAssertionsForContentType:];
-[SBWindowScenePIPManager acquireSplitPIPSystemChromePresentationWithControlsVisible:];
-[SBWindowScenePIPManager acquireStashAssertionForReason:identifier:];
-[SBWindowScenePIPManager acquireWindowLevelOverrideAssertionForControllerWithContentType:toWindowLevel:withReason:identifier:];
-[SBWindowScenePIPManager addStashTabSuppressionTarget:action:];
-[SBWindowScenePIPManager applyPictureInPictureInsets:forSource:];
-[SBWindowScenePIPManager applyStashedPictureInPicturePadding:forPIPSource:];
-[SBWindowScenePIPManager configureInsetsForHomeScreenController:];
-[SBWindowScenePIPManager floatingDockInsets];
-[SBWindowScenePIPManager globalCoordinator];
-[SBWindowScenePIPManager initWithGlobalCoordinator:];
-[SBWindowScenePIPManager isPointWithinAnyPictureInPictureContent:];
-[SBWindowScenePIPManager isZStackForegroundActive];
-[SBWindowScenePIPManager removeStashTabSuppressionTarget:action:];
-[SBWindowScenePIPManager setNeedsUpdateZStackParticipantPreferencesWithReason:];
-[SBWindowScenePIPManager setSourceToEdgeInsets:];
-[SBWindowScenePIPManager updatePictureInPictureWindowLevels];
```
