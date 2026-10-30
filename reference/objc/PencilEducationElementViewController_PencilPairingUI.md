# `PencilEducationElementViewController`

- Image: [`/System/Library/PrivateFrameworks/PencilPairingUI.framework/PencilPairingUI`](../userland/System__Library__PrivateFrameworks__PencilPairingUI.framework__PencilPairingUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `PKScribbleInteractionDelegate`
- 27 instance variables, 35 properties, 104 instance methods, 1 class methods

## Instance variables

```
B _alternateLayout;
B _disableAnimations;
B _isAnimating;
B _isRunningAnimationSequence;
B _hasPencilInteraction;
B _didDisappear;
B _didRunInitialAppearActions;
B _isTextFieldRTL;
@"<PencilEducationElementViewControllerDelegate>" _delegate;
q _deviceType;
@"PencilEducationElementData" _elementData;
@"UIStackView" _stackView;
@"UILabel" _titleLabel;
@"PencilEducationElementTextField" _textField;
@"NSString" _processedString;
@"<UITextCursorAssertion>" _cursorAssertion;
@"PKTextInputSettings" _textInputSettings;
@"NSDictionary" _localizationOffsetDictionary;
@"UIButton" _replayButton;
@"PKTextInputInteraction" _textInputInteraction;
@"PKDrawingReplayController" _drawingReplayController;
@"PKDrawingReplayController" _delayDrawingReplayController;
@"NSMutableArray" _animationQueue;
q _inProgressAnimationType;
Q _replayButtonHiddenIndex;
Q _performAnimationAsyncIndex;
@? _endWritingCompletionBlock;
```

## Properties

```
@property (TB,N,V_isAnimating) isAnimating;
@property (TB,N,V_isRunningAnimationSequence) isRunningAnimationSequence;
@property (T@"PencilEducationElementData",&,N,V_elementData) elementData;
@property (T@"UIStackView",&,N,V_stackView) stackView;
@property (T@"UILabel",W,N,V_titleLabel) titleLabel;
@property (T@"PencilEducationElementTextField",W,N,V_textField) textField;
@property (T@"NSString",&,N,V_processedString) processedString;
@property (T@"<UITextCursorAssertion>",&,N,V_cursorAssertion) cursorAssertion;
@property (T@"PKTextInputSettings",&,N,V_textInputSettings) textInputSettings;
@property (T@"NSDictionary",&,N,V_localizationOffsetDictionary) localizationOffsetDictionary;
@property (T@"UIButton",W,N,V_replayButton) replayButton;
@property (T@"PKTextInputInteraction",R,N,V_textInputInteraction) textInputInteraction;
@property (T@"PKDrawingReplayController",&,N,V_drawingReplayController) drawingReplayController;
@property (T@"PKDrawingReplayController",&,N,V_delayDrawingReplayController) delayDrawingReplayController;
@property (T@"NSMutableArray",&,N,V_animationQueue) animationQueue;
@property (Tq,N,V_inProgressAnimationType) inProgressAnimationType;
@property (TB,N,V_hasPencilInteraction) hasPencilInteraction;
@property (TQ,N,V_replayButtonHiddenIndex) replayButtonHiddenIndex;
@property (TQ,N,V_performAnimationAsyncIndex) performAnimationAsyncIndex;
@property (T@?,C,N,V_endWritingCompletionBlock) endWritingCompletionBlock;
@property (TB,N,V_didDisappear) didDisappear;
@property (TB,N,V_didRunInitialAppearActions) didRunInitialAppearActions;
@property (TB,R,N) isUIRTL;
@property (TB,N,V_isTextFieldRTL) isTextFieldRTL;
@property (T@"<PencilEducationElementViewControllerDelegate>",W,N,V_delegate) delegate;
@property (TB,R,N) hasRemainingAnimation;
@property (TB,R,N) animationInProgress;
@property (Tq,R,N) type;
@property (Tq,R,N,V_deviceType) deviceType;
@property (TB,N,V_alternateLayout) alternateLayout;
@property (TB,N,V_disableAnimations) disableAnimations;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[PencilEducationElementViewController keyPathsForValuesAffectingAnimationInProgress];
```

## Instance methods

```
-[PencilEducationElementViewController setCursorAssertion:];
-[PencilEducationElementViewController cursorAssertion];
-[PencilEducationElementViewController setTitleLabel:];
-[PencilEducationElementViewController viewWillDisappear:];
-[PencilEducationElementViewController titleLabel];
-[PencilEducationElementViewController deviceType];
-[PencilEducationElementViewController _scribbleInteraction:focusWillTransformElement:];
-[PencilEducationElementViewController textField];
-[PencilEducationElementViewController viewDidLoad];
-[PencilEducationElementViewController setIsAnimating:];
-[PencilEducationElementViewController _scribbleInteraction:didFinishWritingInElement:];
-[PencilEducationElementViewController viewWillAppear:];
-[PencilEducationElementViewController _canShowWhileLocked];
-[PencilEducationElementViewController setDelegate:];
-[PencilEducationElementViewController viewDidAppear:];
-[PencilEducationElementViewController type];
-[PencilEducationElementViewController viewWillTransitionToSize:withTransitionCoordinator:];
-[PencilEducationElementViewController setAlternateLayout:];
-[PencilEducationElementViewController delegate];
-[PencilEducationElementViewController _scribbleInteraction:willBeginWritingInElement:];
-[PencilEducationElementViewController stackView];
-[PencilEducationElementViewController viewDidDisappear:];
-[PencilEducationElementViewController setStackView:];
-[PencilEducationElementViewController isAnimating];
-[PencilEducationElementViewController alternateLayout];
-[PencilEducationElementViewController beginAnimation];
-[PencilEducationElementViewController setTextField:];
-[PencilEducationElementViewController _pkScribbleInteractionShouldDisableInputAssistant:];
-[PencilEducationElementViewController processedString];
-[PencilEducationElementViewController setProcessedString:];
-[PencilEducationElementViewController disableAnimations];
-[PencilEducationElementViewController didDisappear];
-[PencilEducationElementViewController textInputInteraction];
-[PencilEducationElementViewController replayButton];
-[PencilEducationElementViewController setReplayButton:];
-[PencilEducationElementViewController setDidDisappear:];
-[PencilEducationElementViewController reloadStrings];
-[PencilEducationElementViewController animationQueue];
-[PencilEducationElementViewController initWithElementData:deviceType:];
-[PencilEducationElementViewController isUIRTL];
-[PencilEducationElementViewController setElementData:];
-[PencilEducationElementViewController cancelAnimation];
-[PencilEducationElementViewController _alternateLayoutWriteScaleClampedForBaseScale:baseHeight:drawing:];
-[PencilEducationElementViewController _reloadAnimationQueue];
-[PencilEducationElementViewController _setUpAlternateLayoutContentViews];
-[PencilEducationElementViewController allowedCalloutActionsForType:];
-[PencilEducationElementViewController animationInProgress];
-[PencilEducationElementViewController applyLocalizationScaleOffsetsIfNecesssaryForDrawing:animationType:transform:];
-[PencilEducationElementViewController beginAnimationIfNecessary];
-[PencilEducationElementViewController calculateFittingHeightByTemporarilyAdjustingFrameForWidth:];
-[PencilEducationElementViewController cancelPendingReplayHiddenCommands];
-[PencilEducationElementViewController cancelScheduledAnimations];
-[PencilEducationElementViewController customHeightRatioForAnimationType:];
-[PencilEducationElementViewController customWidthRatioForAnimationType:];
-[PencilEducationElementViewController defaultAllowedCalloutActions];
-[PencilEducationElementViewController delayDrawingReplayController];
-[PencilEducationElementViewController didRunInitialAppearActions];
-[PencilEducationElementViewController drawingForAnimationType:];
-[PencilEducationElementViewController drawingReplayController];
-[PencilEducationElementViewController elementData];
-[PencilEducationElementViewController endWritingCompletionBlock];
-[PencilEducationElementViewController handleEndAnimation];
-[PencilEducationElementViewController hasCustomHeightRatioForAnimationType:];
-[PencilEducationElementViewController hasCustomWidthRatioForAnimationType:];
-[PencilEducationElementViewController hasPencilInteraction];
-[PencilEducationElementViewController hasRemainingAnimation];
-[PencilEducationElementViewController inProgressAnimationType];
-[PencilEducationElementViewController isRunningAnimationSequence];
-[PencilEducationElementViewController isSecondaryAnimationForType:];
-[PencilEducationElementViewController isTextAddedForAnimationType:];
-[PencilEducationElementViewController isTextFieldRTL];
-[PencilEducationElementViewController localizationOffsetDictionary];
-[PencilEducationElementViewController localizationOffsetKeyForAnimationType:];
-[PencilEducationElementViewController localizationOffsetsForAnimationType:];
-[PencilEducationElementViewController nextAnimationDelayForAnimationType:];
-[PencilEducationElementViewController offsetForAnimationType:];
-[PencilEducationElementViewController performAnimationAsyncIndex];
-[PencilEducationElementViewController reloadAnimationQueue];
-[PencilEducationElementViewController replacePlaceholdersInString:];
-[PencilEducationElementViewController replayButtonHiddenIndex];
-[PencilEducationElementViewController replayButtonPressed:];
-[PencilEducationElementViewController scaleRatioForAnimationType:];
-[PencilEducationElementViewController setAnimationQueue:];
-[PencilEducationElementViewController setDelayDrawingReplayController:];
-[PencilEducationElementViewController setDidRunInitialAppearActions:];
-[PencilEducationElementViewController setDisableAnimations:];
-[PencilEducationElementViewController setDrawingReplayController:];
-[PencilEducationElementViewController setEndWritingCompletionBlock:];
-[PencilEducationElementViewController setHasPencilInteraction:];
-[PencilEducationElementViewController setInProgressAnimationType:];
-[PencilEducationElementViewController setIsRunningAnimationSequence:];
-[PencilEducationElementViewController setIsTextFieldRTL:];
-[PencilEducationElementViewController setLocalizationOffsetDictionary:];
-[PencilEducationElementViewController setPerformAnimationAsyncIndex:];
-[PencilEducationElementViewController setReplayButtonHiddenIndex:];
-[PencilEducationElementViewController setTextInputSettings:];
-[PencilEducationElementViewController speedRatioForAnimationType:];
-[PencilEducationElementViewController textFieldBoundsForRange:];
-[PencilEducationElementViewController textInputSettings];
-[PencilEducationElementViewController textRangeForAnimationType:];
-[PencilEducationElementViewController transformDimensionAnimationType:];
-[PencilEducationElementViewController transformDrawing:toFitBounds:dimension:offset:animationType:];
-[PencilEducationElementViewController transformForAnimationType:drawing:bounds:];
-[PencilEducationElementViewController updateIsAnimatingUI];
```
