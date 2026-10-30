# `_UITypeSelectInteraction`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIInteraction`
- 18 instance variables, 8 properties, 40 instance methods, 1 class methods

## Instance variables

```
@"_UITypeSelectKeyPressGestureRecognizer" _keyPressGestureRecognizer;
@"_UITypeSelectTouchResetGestureRecognizer" _didRecognizeTouchResetGestureRecognizer;
@"_UITypeSelectNavigationGestureRecognizer" _navigationGestureRecognizer;
@"NSString" _programmaticInput;
d _defaultTimeout;
@"NSTimer" _timer;
B _noMatch;
@"_UITypeSelectFilterSystem" _filterSystem;
@"_UITypeSelectItem" _primaryMatch;
@"_UITypeSelectItem" _secondaryMatch;
@"_UITypeSelectKeyInput" _keyInput;
{?="updateSceneComponentStatePendingWindowMoveToScene"b1"registrationPendingDidMoveToWindow"b1} _interactionFlags;
B _enabled;
B _hasTimedOut;
@"UIView" _view;
@"<_UITypeSelectInteractionDelegate>" _delegate;
@"NSString" _currentInput;
q _inputMethod;
```

## Properties

```
@property (T@"NSString",&,N,V_currentInput) currentInput;
@property (T@"<_UITypeSelectInteractionDelegate>",R,W,N,V_delegate) delegate;
@property (TB,N,GisEnabled,V_enabled) enabled;
@property (T@"UIView",R,W,N,V_view) view;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UITypeSelectInteraction _defaultSecondaryColorTransformer];
```

## Instance methods

```
-[_UITypeSelectInteraction _windowWillMoveToScene:];
-[_UITypeSelectInteraction _willMoveFromWindow:toWindow:];
-[_UITypeSelectInteraction _isKeyInputModeEnabled];
-[_UITypeSelectInteraction _typeSelectInteractionDidReset];
-[_UITypeSelectInteraction initWithDelegate:];
-[_UITypeSelectInteraction _keyPressedGestureRecognizerInputHasChanged:];
-[_UITypeSelectInteraction _createTimerWithTimeout:];
-[_UITypeSelectInteraction _typeSelectInteractionInputHasChanged:];
-[_UITypeSelectInteraction _unregisterWindowNotificationsOnOldWindow:];
-[_UITypeSelectInteraction _registerWindowNotificationsOnNewWindow:];
-[_UITypeSelectInteraction _updateWithResult:animated:];
-[_UITypeSelectInteraction _createTimer];
-[_UITypeSelectInteraction _didMoveFromWindow:toWindow:];
-[_UITypeSelectInteraction _removeSceneComponentStateInWindow:];
-[_UITypeSelectInteraction _removeGesturesFromView:];
-[_UITypeSelectInteraction _filterResultsForTypeSelectItems:];
-[_UITypeSelectInteraction _addSceneComponentStateInScene:];
-[_UITypeSelectInteraction isEnabled];
-[_UITypeSelectInteraction currentInput];
-[_UITypeSelectInteraction view];
-[_UITypeSelectInteraction _navigationKeyPressed:];
-[_UITypeSelectInteraction _cancelTimer];
-[_UITypeSelectInteraction gestureRecognizerShouldBegin:];
-[_UITypeSelectInteraction _updateGesturesIfNeeded];
-[_UITypeSelectInteraction _addGesturesToView:];
-[_UITypeSelectInteraction _windowDidMoveToScene:];
-[_UITypeSelectInteraction setEnabled:];
-[_UITypeSelectInteraction _createNewTimer];
-[_UITypeSelectInteraction willMoveToView:];
-[_UITypeSelectInteraction gestureRecognizer:shouldRecognizeSimultaneouslyWithGestureRecognizer:];
-[_UITypeSelectInteraction delegate];
-[_UITypeSelectInteraction _hardwareKeyboardAvailabilityChanged:];
-[_UITypeSelectInteraction _touchToEnableAllOptions];
-[_UITypeSelectInteraction canBecomeFirstResponder];
-[_UITypeSelectInteraction _resetTypeSelectInput];
-[_UITypeSelectInteraction _timerHandler:];
-[_UITypeSelectInteraction didMoveToView:];
-[_UITypeSelectInteraction _updateInputStringWithNewInput:];
-[_UITypeSelectInteraction setCurrentInput:];
-[_UITypeSelectInteraction _keyInputHasChanged];
```
