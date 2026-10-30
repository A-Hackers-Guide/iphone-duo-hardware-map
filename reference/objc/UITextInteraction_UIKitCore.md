# `UITextInteraction`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIGestureRecognizerDelegate`, `UIInteraction`
- 15 instance variables, 23 properties, 83 instance methods, 3 class methods

## Instance variables

```
@"UITextInteraction" _parent;
@"NSMutableArray" _children;
@"NSMutableArray" _gestures;
@"NSMutableDictionary" _gestureMap;
B _viewOverridesInteractivityState;
B _inGesture;
B _allowsSelectionCommands;
q _textInteractionMode;
@"UILongPressGestureRecognizer" _customHighlighterGesture;
@"_UIStatesFeedbackGenerator" _feedbackBehaviour;
@"<UITextInteractionDelegate>" _delegate;
@"UIResponder<UITextInput>" _textInput;
@"UIView" _view;
@"UITextInteractionInputDelegate" _interactionInputDelegate;
@"<UITextInteraction_AssistantDelegate>" _assistantDelegate;
```

## Properties

```
@property (T@"UIView",W,N,V_view) view;
@property (T@"UITextInteractionInputDelegate",&,N,V_interactionInputDelegate) interactionInputDelegate;
@property (T@"<UITextInteraction_AssistantDelegate>",W,N,V_assistantDelegate) assistantDelegate;
@property (T@"UITextInteraction",R,W) parent;
@property (T@"UITextInteraction",R,W) root;
@property (T@"UIView",R,N) gestureRecognizerHostView;
@property (T@"NSArray",R,N,V_children) children;
@property (T@"NSArray",R,N,V_gestures) gestures;
@property (T@"NSDictionary",R,N,V_gestureMap) gestureMap;
@property (TB,N,SsetInGesture:,V_inGesture) inGesture;
@property (T@"_UIStatesFeedbackGenerator",&,N,V_feedbackBehaviour) feedbackBehaviour;
@property (Tq,R,N) textInteractionSet;
@property (T@"UITextCursorAssertionController",R,N) _assertionController;
@property (T@"UILongPressGestureRecognizer",&,N,V_customHighlighterGesture) _customHighlighterGesture;
@property (TB,N,S_setAllowsSelectionCommands:,V_allowsSelectionCommands) _allowsSelectionCommands;
@property (T@"<UITextInteractionDelegate>",W,N,V_delegate) delegate;
@property (T@"UIResponder<UITextInput>",W,N,V_textInput) textInput;
@property (Tq,R,N,V_textInteractionMode) textInteractionMode;
@property (T@"NSArray",R,N) gesturesForFailureRequirements;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UITextInteraction _maximumBeamSnappingLength];
+[UITextInteraction textInteractionForMode:];
+[UITextInteraction textInteractionsForSet:];
```

## Instance methods

```
-[UITextInteraction root];
-[UITextInteraction finishSetup];
-[UITextInteraction gesturesForFailureRequirements];
-[UITextInteraction shouldAllowWithTouchTypes:atPoint:toBegin:];
-[UITextInteraction gestureRecognizer:shouldReceiveTouch:];
-[UITextInteraction init];
-[UITextInteraction _assertionController];
-[UITextInteraction feedbackBehaviour];
-[UITextInteraction setView:];
-[UITextInteraction doesControlDelegate];
-[UITextInteraction _shouldAllowEnforcedTouchTypeForTouch:forGestureRecognizer:];
-[UITextInteraction _performGestureType:state:location:locationOfFirstTouch:forTouchType:];
-[UITextInteraction setFeedbackBehaviour:];
-[UITextInteraction view];
-[UITextInteraction parent];
-[UITextInteraction setDelegate:];
-[UITextInteraction gestureRecognizerShouldBegin:];
-[UITextInteraction children];
-[UITextInteraction willMoveToView:];
-[UITextInteraction gestureRecognizerHostView];
-[UITextInteraction interaction_gestureRecognizer:shouldReceiveTouch:];
-[UITextInteraction gestureRecognizer:shouldRecognizeSimultaneouslyWithGestureRecognizer:];
-[UITextInteraction delegate];
-[UITextInteraction gestures];
-[UITextInteraction rangeWithTextAlternatives:atPosition:];
-[UITextInteraction addChild:];
-[UITextInteraction _applyTransientState:];
-[UITextInteraction didMoveToView:];
-[UITextInteraction _transientState];
-[UITextInteraction interaction_gestureRecognizerShouldBegin:];
-[UITextInteraction removeChild:];
-[UITextInteraction defaultTapRecognizerWithAction:];
-[UITextInteraction _allowsSelectionCommands];
-[UITextInteraction _beginSelectionChange];
-[UITextInteraction _callDelegateWillMoveTextRangeExtentAtPoint:];
-[UITextInteraction _cancelRecognizerWithName:];
-[UITextInteraction _cleanUpFeedbackForGesture];
-[UITextInteraction _createFeedbackIfNecessary];
-[UITextInteraction _customHighlighterGesture];
-[UITextInteraction _endSelectionChange];
-[UITextInteraction _performGestureType:state:location:];
-[UITextInteraction _performGestureType:state:location:locationOfFirstTouch:];
-[UITextInteraction _performPreemtiveLayoutToEnsureNoMoreLayoutWhileSelecting:];
-[UITextInteraction _playFeedbackForCursorMovement];
-[UITextInteraction _prepareFeedbackForGesture];
-[UITextInteraction _presentTextEditMenuWithOverrideMenu:];
-[UITextInteraction _setAllowsSelectionCommands:];
-[UITextInteraction _setLinkInteractionSession:];
-[UITextInteraction _shouldObscureTextInput];
-[UITextInteraction _shouldReceiveTouchesInDescendantViews];
-[UITextInteraction _textInput];
-[UITextInteraction _textInputIsInteractive];
-[UITextInteraction _textInputLivesInKeyWindow];
-[UITextInteraction _updatedAccessibilityTextMenuWithMenuElements:];
-[UITextInteraction addGestureRecognizer:withName:];
-[UITextInteraction addIndirectChild:];
-[UITextInteraction assistantDelegate];
-[UITextInteraction cancelLinkInteractionSession];
-[UITextInteraction containerChangesSelectionOnOneFingerTap];
-[UITextInteraction currentSelectionContainsPoint:];
-[UITextInteraction defaultDoubleTapRecognizerWithAction:];
-[UITextInteraction defaultTripleTapRecognizerWithAction:];
-[UITextInteraction disableClearsOnInsertion];
-[UITextInteraction distanceBetweenPoint:andRects:];
-[UITextInteraction gestureMap];
-[UITextInteraction inGesture];
-[UITextInteraction interactionInputDelegate];
-[UITextInteraction interactionWithClass:];
-[UITextInteraction interactionWithGestureForName:];
-[UITextInteraction linkInteractionSession];
-[UITextInteraction recognizerForName:];
-[UITextInteraction removeGestureRecognizerWithName:];
-[UITextInteraction selection:containsPoint:];
-[UITextInteraction setAssistantDelegate:];
-[UITextInteraction setInGesture:];
-[UITextInteraction setInteractionInputDelegate:];
-[UITextInteraction setTextInput:];
-[UITextInteraction set_customHighlighterGesture:];
-[UITextInteraction shouldHandleFormGestureAtLocation:];
-[UITextInteraction textInput];
-[UITextInteraction textInteractionMode];
-[UITextInteraction textInteractionSet];
-[UITextInteraction updateTextInputSourceForScribbleGesture:];
```
