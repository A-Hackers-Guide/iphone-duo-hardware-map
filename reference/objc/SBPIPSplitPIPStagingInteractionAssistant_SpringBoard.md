# `SBPIPSplitPIPStagingInteractionAssistant`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 9 instance variables, 3 properties, 20 instance methods, 0 class methods

## Instance variables

```
@"_UIHyperInteractor" _positionInteractor;
@"_UIHyperInteractor" _scaleInteractor;
@"SBPIPSplitPIPSettings" _settings;
@"SBPIPSplitPIPStagingPauseDetector" _pauseDetector;
B _isHoldCheckScheduled;
d _settleDeadline;
d _restoreScale;
B _staging;
@"<SBPIPSplitPIPStagingInteractionAssistantDelegate>" _delegate;
```

## Properties

```
@property (T@"<SBPIPSplitPIPStagingInteractionAssistantDelegate>",W,N,V_delegate) delegate;
@property (TB,R,N,GisStaging,V_staging) staging;
@property (TQ,R,N) panGestureLayoutReason;
```

## Instance methods

```
-[SBPIPSplitPIPStagingInteractionAssistant setDelegate:];
-[SBPIPSplitPIPStagingInteractionAssistant delegate];
-[SBPIPSplitPIPStagingInteractionAssistant _geometry];
-[SBPIPSplitPIPStagingInteractionAssistant _canStageWithGeometry:];
-[SBPIPSplitPIPStagingInteractionAssistant _cancelHoldCheck];
-[SBPIPSplitPIPStagingInteractionAssistant _checkHold];
-[SBPIPSplitPIPStagingInteractionAssistant _endStagingWithCommit:isDragging:];
-[SBPIPSplitPIPStagingInteractionAssistant _stageForReason:];
-[SBPIPSplitPIPStagingInteractionAssistant _stageOnceHeldLongEnough];
-[SBPIPSplitPIPStagingInteractionAssistant _targetRectForGeometry:];
-[SBPIPSplitPIPStagingInteractionAssistant _unconstrainedCenter];
-[SBPIPSplitPIPStagingInteractionAssistant _updateEscapeForPanSample:];
-[SBPIPSplitPIPStagingInteractionAssistant beginStaging];
-[SBPIPSplitPIPStagingInteractionAssistant dragDidEnd];
-[SBPIPSplitPIPStagingInteractionAssistant dragWillSettle];
-[SBPIPSplitPIPStagingInteractionAssistant endStagingWithCommit:];
-[SBPIPSplitPIPStagingInteractionAssistant initWithPositionInteractor:scaleInteractor:settings:pointsPerMillimeter:];
-[SBPIPSplitPIPStagingInteractionAssistant isStaging];
-[SBPIPSplitPIPStagingInteractionAssistant panGestureLayoutReason];
-[SBPIPSplitPIPStagingInteractionAssistant updateForPanSample:];
```
