# `PKTextInputReserveSpaceController`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `PKTextInputDebugStateReporting`
- 10 instance variables, 16 properties, 40 instance methods, 0 class methods

## Instance variables

```
B __wasAskedToReserveSpace;
B __canvasControllerIsDrawing;
@"<PKTextInputReserveSpaceControllerDelegate>" _delegate;
@"PKTextInputFeedbackController" _feedbackController;
q __reserveSpaceState;
@"PKTextInputElementContent" __targetElementContent;
q __insertionCharacterLocation;
@"PKTextInputTextPlaceholder" __textPlaceholder;
@"NSTimer" __dismissTimer;
{CGPoint="x"d"y"d} __targetPointInElement;
```

## Properties

```
@property (T@"PKTextInputFeedbackController",R,N,V_feedbackController) feedbackController;
@property (Tq,N,S_setReserveSpaceState:,V__reserveSpaceState) _reserveSpaceState;
@property (T@"PKTextInputElementContent",&,N,S_setTargetElementContent:,V__targetElementContent) _targetElementContent;
@property (T{CGPoint=dd},N,V__targetPointInElement) _targetPointInElement;
@property (Tq,N,V__insertionCharacterLocation) _insertionCharacterLocation;
@property (TB,N,V__wasAskedToReserveSpace) _wasAskedToReserveSpace;
@property (TB,N,V__canvasControllerIsDrawing) _canvasControllerIsDrawing;
@property (T@"PKTextInputTextPlaceholder",&,N,V__textPlaceholder) _textPlaceholder;
@property (T@"NSTimer",&,N,V__dismissTimer) _dismissTimer;
@property (TB,R,N) isReserveSpaceActive;
@property (TB,R,N) isReserveSpacePlaceholderVisible;
@property (T@"<PKTextInputReserveSpaceControllerDelegate>",W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[PKTextInputReserveSpaceController setDelegate:];
-[PKTextInputReserveSpaceController delegate];
-[PKTextInputReserveSpaceController feedbackController];
-[PKTextInputReserveSpaceController set_insertionCharacterLocation:];
-[PKTextInputReserveSpaceController _canvasControllerIsDrawing];
-[PKTextInputReserveSpaceController _dismissTimer];
-[PKTextInputReserveSpaceController _finishAndResetStateInsertingWhitespace:];
-[PKTextInputReserveSpaceController _handleAutodismissTimer];
-[PKTextInputReserveSpaceController _insertWhitespaceWithElement:atReferencePoint:completion:];
-[PKTextInputReserveSpaceController _insertionCharacterLocation];
-[PKTextInputReserveSpaceController _moveToContentLoadedIfReady];
-[PKTextInputReserveSpaceController _moveToInsertingPlaceholderIfReady];
-[PKTextInputReserveSpaceController _moveToShowingIntroIfReady];
-[PKTextInputReserveSpaceController _moveToShowingPlaceholderIfReady];
-[PKTextInputReserveSpaceController _preferredInsertionLocation];
-[PKTextInputReserveSpaceController _reserveSpaceState];
-[PKTextInputReserveSpaceController _setReserveSpaceState:];
-[PKTextInputReserveSpaceController _setTargetElementContent:];
-[PKTextInputReserveSpaceController _startDismissTimerWithDelay:];
-[PKTextInputReserveSpaceController _targetElementContent];
-[PKTextInputReserveSpaceController _targetPointInElement];
-[PKTextInputReserveSpaceController _textPlaceholder];
-[PKTextInputReserveSpaceController _updateReserveSpaceState];
-[PKTextInputReserveSpaceController _wasAskedToReserveSpace];
-[PKTextInputReserveSpaceController beginIfPossibleWithElement:atLocation:coordinateSpace:];
-[PKTextInputReserveSpaceController cancelReserveSpaceIntro];
-[PKTextInputReserveSpaceController finishReserveSpaceAndInsertWhitespace:];
-[PKTextInputReserveSpaceController initWithFeedbackController:];
-[PKTextInputReserveSpaceController isReserveSpaceActive];
-[PKTextInputReserveSpaceController isReserveSpacePlaceholderVisible];
-[PKTextInputReserveSpaceController placeholderFrameInCoordinateSpace:];
-[PKTextInputReserveSpaceController reportDebugStateDescription:];
-[PKTextInputReserveSpaceController reserveSpaceWhenReady];
-[PKTextInputReserveSpaceController setCanvasControllerIsDrawing:];
-[PKTextInputReserveSpaceController set_canvasControllerIsDrawing:];
-[PKTextInputReserveSpaceController set_dismissTimer:];
-[PKTextInputReserveSpaceController set_targetPointInElement:];
-[PKTextInputReserveSpaceController set_textPlaceholder:];
-[PKTextInputReserveSpaceController set_wasAskedToReserveSpace:];
-[PKTextInputReserveSpaceController tapPointIsInPlaceholder:];
```
