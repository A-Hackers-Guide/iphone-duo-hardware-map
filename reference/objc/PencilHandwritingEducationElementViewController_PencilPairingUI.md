# `PencilHandwritingEducationElementViewController`

- Image: [`/System/Library/PrivateFrameworks/PencilPairingUI.framework/PencilPairingUI`](../userland/System__Library__PrivateFrameworks__PencilPairingUI.framework__PencilPairingUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `PKCanvasViewDelegate`, `UIPencilInteractionDelegate`
- 20 instance variables, 27 properties, 91 instance methods, 0 class methods

## Instance variables

```
B _didEnableAutoRefine;
B _didDisappear;
B _didRunInitialAppearActions;
@"<PencilHandwritingEducationElementViewControllerDelegate>" _delegate;
@"PencilHandwritingEducationElementData" _elementData;
@"UIStackView" _stackView;
@"UILabel" _titleLabel;
@"PKCanvasView" _canvasView;
@"AVPlayer" _player;
@"AVPlayerLayer" _playerLayer;
@"TextLineLayer" _textLineLayer;
@"CALayer" _canvasMaskLayer;
@"UIButton" _replayButton;
@"UIButton" _clearButton;
@"UIButton" _seeRefinedButton;
@"UIButton" _seeOriginalButton;
@"NSMutableSet" _nonRefinableStrokes;
@"NSMutableSet" _originalStrokes;
@"NSMutableSet" _refinedStrokes;
@"UIPencilInteraction" _pencilInteraction;
```

## Properties

```
@property (T@"PencilHandwritingEducationElementData",&,N,V_elementData) elementData;
@property (T@"UIStackView",&,N,V_stackView) stackView;
@property (T@"UILabel",&,N,V_titleLabel) titleLabel;
@property (T@"PKCanvasView",&,N,V_canvasView) canvasView;
@property (T@"AVPlayer",&,N,V_player) player;
@property (T@"AVPlayerLayer",&,N,V_playerLayer) playerLayer;
@property (T@"TextLineLayer",&,N,V_textLineLayer) textLineLayer;
@property (T@"CALayer",&,N,V_canvasMaskLayer) canvasMaskLayer;
@property (TB,N,V_didEnableAutoRefine) didEnableAutoRefine;
@property (T@"UIButton",&,N,V_replayButton) replayButton;
@property (T@"UIButton",&,N,V_clearButton) clearButton;
@property (T@"UIButton",&,N,V_seeRefinedButton) seeRefinedButton;
@property (T@"UIButton",&,N,V_seeOriginalButton) seeOriginalButton;
@property (TB,N,V_didDisappear) didDisappear;
@property (TB,N,V_didRunInitialAppearActions) didRunInitialAppearActions;
@property (T@"NSMutableSet",&,N,V_nonRefinableStrokes) nonRefinableStrokes;
@property (T@"NSMutableSet",&,N,V_originalStrokes) originalStrokes;
@property (T@"NSMutableSet",&,N,V_refinedStrokes) refinedStrokes;
@property (T@"UIPencilInteraction",&,N,V_pencilInteraction) pencilInteraction;
@property (T@"<PencilHandwritingEducationElementViewControllerDelegate>",W,N,V_delegate) delegate;
@property (TB,R,N) hasRemainingAnimation;
@property (TB,R,N) animationInProgress;
@property (Tq,R,N) type;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[PencilHandwritingEducationElementViewController player];
-[PencilHandwritingEducationElementViewController playerLayer];
-[PencilHandwritingEducationElementViewController applicationWillResignActive:];
-[PencilHandwritingEducationElementViewController setPlayerLayer:];
-[PencilHandwritingEducationElementViewController applicationDidBecomeActive:];
-[PencilHandwritingEducationElementViewController setTitleLabel:];
-[PencilHandwritingEducationElementViewController viewWillDisappear:];
-[PencilHandwritingEducationElementViewController titleLabel];
-[PencilHandwritingEducationElementViewController dealloc];
-[PencilHandwritingEducationElementViewController viewDidLoad];
-[PencilHandwritingEducationElementViewController viewDidLayoutSubviews];
-[PencilHandwritingEducationElementViewController setPlayer:];
-[PencilHandwritingEducationElementViewController viewWillAppear:];
-[PencilHandwritingEducationElementViewController pencilInteraction:didReceiveSqueeze:];
-[PencilHandwritingEducationElementViewController _canShowWhileLocked];
-[PencilHandwritingEducationElementViewController setDelegate:];
-[PencilHandwritingEducationElementViewController viewDidAppear:];
-[PencilHandwritingEducationElementViewController type];
-[PencilHandwritingEducationElementViewController setCanvasView:];
-[PencilHandwritingEducationElementViewController delegate];
-[PencilHandwritingEducationElementViewController stackView];
-[PencilHandwritingEducationElementViewController viewDidDisappear:];
-[PencilHandwritingEducationElementViewController setStackView:];
-[PencilHandwritingEducationElementViewController canvasView];
-[PencilHandwritingEducationElementViewController beginAnimation];
-[PencilHandwritingEducationElementViewController clearButton];
-[PencilHandwritingEducationElementViewController pencilInteraction];
-[PencilHandwritingEducationElementViewController setPencilInteraction:];
-[PencilHandwritingEducationElementViewController didDisappear];
-[PencilHandwritingEducationElementViewController isPlayerHidden];
-[PencilHandwritingEducationElementViewController originalStrokes];
-[PencilHandwritingEducationElementViewController canvasView:didRefineStrokes:withNewStrokes:];
-[PencilHandwritingEducationElementViewController canvasViewDidBeginUsingTool:];
-[PencilHandwritingEducationElementViewController canvasViewDrawingDidChange:];
-[PencilHandwritingEducationElementViewController refinedStrokes];
-[PencilHandwritingEducationElementViewController setClearButton:];
-[PencilHandwritingEducationElementViewController replayButton];
-[PencilHandwritingEducationElementViewController setReplayButton:];
-[PencilHandwritingEducationElementViewController clearButtonPressed:];
-[PencilHandwritingEducationElementViewController setDidDisappear:];
-[PencilHandwritingEducationElementViewController startObservingNotifications];
-[PencilHandwritingEducationElementViewController reloadStrings];
-[PencilHandwritingEducationElementViewController canvasMaskLayer];
-[PencilHandwritingEducationElementViewController setElementData:];
-[PencilHandwritingEducationElementViewController cancelAnimation];
-[PencilHandwritingEducationElementViewController initClearButton];
-[PencilHandwritingEducationElementViewController animationInProgress];
-[PencilHandwritingEducationElementViewController calculateFittingHeightByTemporarilyAdjustingFrameForWidth:];
-[PencilHandwritingEducationElementViewController cancelScheduledAnimations];
-[PencilHandwritingEducationElementViewController clearCanvas];
-[PencilHandwritingEducationElementViewController clearTrackedStrokes];
-[PencilHandwritingEducationElementViewController createElementButtonWithTitle:image:];
-[PencilHandwritingEducationElementViewController didEnableAutoRefine];
-[PencilHandwritingEducationElementViewController didRunInitialAppearActions];
-[PencilHandwritingEducationElementViewController elementData];
-[PencilHandwritingEducationElementViewController hasRemainingAnimation];
-[PencilHandwritingEducationElementViewController hidePlayer:];
-[PencilHandwritingEducationElementViewController initCanvasMaskLayer];
-[PencilHandwritingEducationElementViewController initCanvasView];
-[PencilHandwritingEducationElementViewController initPlayer];
-[PencilHandwritingEducationElementViewController initReplayButton];
-[PencilHandwritingEducationElementViewController initSeeOriginalButton];
-[PencilHandwritingEducationElementViewController initSeeRefinedButton];
-[PencilHandwritingEducationElementViewController initStackView];
-[PencilHandwritingEducationElementViewController initTextLine];
-[PencilHandwritingEducationElementViewController initTitleLabel];
-[PencilHandwritingEducationElementViewController initWithElementData:];
-[PencilHandwritingEducationElementViewController nonRefinableStrokes];
-[PencilHandwritingEducationElementViewController notNowPressed:];
-[PencilHandwritingEducationElementViewController playerItemDidFinish:];
-[PencilHandwritingEducationElementViewController processVideoRequest:];
-[PencilHandwritingEducationElementViewController replayButtonPressed:];
-[PencilHandwritingEducationElementViewController seeOriginalButton];
-[PencilHandwritingEducationElementViewController seeOriginalButtonPressed:];
-[PencilHandwritingEducationElementViewController seeRefinedButton];
-[PencilHandwritingEducationElementViewController seeRefinedButtonPressed:];
-[PencilHandwritingEducationElementViewController setButton:hidden:animated:];
-[PencilHandwritingEducationElementViewController setCanvasMaskLayer:];
-[PencilHandwritingEducationElementViewController setDidEnableAutoRefine:];
-[PencilHandwritingEducationElementViewController setDidRunInitialAppearActions:];
-[PencilHandwritingEducationElementViewController setNonRefinableStrokes:];
-[PencilHandwritingEducationElementViewController setOriginalStrokes:];
-[PencilHandwritingEducationElementViewController setRefinedStrokes:];
-[PencilHandwritingEducationElementViewController setSeeOriginalButton:];
-[PencilHandwritingEducationElementViewController setSeeRefinedButton:];
-[PencilHandwritingEducationElementViewController setTextLineLayer:];
-[PencilHandwritingEducationElementViewController showPlayer:];
-[PencilHandwritingEducationElementViewController stopPlayer];
-[PencilHandwritingEducationElementViewController textLineLayer];
-[PencilHandwritingEducationElementViewController turnOnPressed:];
-[PencilHandwritingEducationElementViewController updateButtonTray:];
```
