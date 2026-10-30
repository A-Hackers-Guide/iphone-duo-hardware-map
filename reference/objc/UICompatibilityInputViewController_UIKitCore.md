# `UICompatibilityInputViewController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIInputViewController`
- Protocols: `_UIKBDelegateAwareInputController`
- 15 instance variables, 8 properties, 51 instance methods, 5 class methods

## Instance variables

```
@"UIKeyboardInputMode" _inputMode;
@"UIKeyboard" _deferredSystemView;
@"UIKeyboardInputMode" _incomingExtensionInputMode;
d _incomingExtensionInputModeTime;
d _lastSuspendedTime;
d _currentResumeTime;
B _shouldRegenerateSizingConstraints;
B _shouldSuppressRemoteInputController;
B _tearingDownInputController;
d _resetInputModeTime;
Q _latestDelayTime;
@"UILayoutGuide" _focusSafeAreaLayoutGuide;
@"UIViewController" _inputController;
@"NSArray" _internalEdgeMatchConstraints;
@"<UITextCursorAssertion>" _blinkAssertion;
```

## Properties

```
@property (T@"UIViewController",&,N,V_inputController) inputController;
@property (T@"NSArray",&,N,V_internalEdgeMatchConstraints) internalEdgeMatchConstraints;
@property (T@"<UITextCursorAssertion>",&,N,V_blinkAssertion) blinkAssertion;
@property (T@"UILayoutGuide",R,N) focusSafeAreaLayoutGuide;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UICompatibilityInputViewController deferredInputModeControllerWithKeyboard:];
+[UICompatibilityInputViewController _requiresProxyInterface];
+[UICompatibilityInputViewController inputViewControllerWithView:];
+[UICompatibilityInputViewController applicationDidReceiveMemoryWarning:];
+[UICompatibilityInputViewController inputSnapshotViewForInputMode:orientation:];
```

## Instance methods

```
-[UICompatibilityInputViewController willRotateToInterfaceOrientation:duration:];
-[UICompatibilityInputViewController willAnimateRotationToInterfaceOrientation:duration:];
-[UICompatibilityInputViewController _keyboard];
-[UICompatibilityInputViewController isHosted:];
-[UICompatibilityInputViewController setInputMode:];
-[UICompatibilityInputViewController willResume:];
-[UICompatibilityInputViewController didRotateFromInterfaceOrientation:];
-[UICompatibilityInputViewController validateInputModeIsDisplayed];
-[UICompatibilityInputViewController didFinishTranslation];
-[UICompatibilityInputViewController didSuspend:];
-[UICompatibilityInputViewController blinkAssertion];
-[UICompatibilityInputViewController viewWillDisappear:];
-[UICompatibilityInputViewController _tvUpdateAppearanceForUserInterfaceStyle];
-[UICompatibilityInputViewController _initAsDeferredController];
-[UICompatibilityInputViewController resetInputModeInMainThread];
-[UICompatibilityInputViewController childCompatibilityController];
-[UICompatibilityInputViewController dealloc];
-[UICompatibilityInputViewController setDeferredSystemView:];
-[UICompatibilityInputViewController inputController];
-[UICompatibilityInputViewController rebuildChildConstraints];
-[UICompatibilityInputViewController viewDidLayoutSubviews];
-[UICompatibilityInputViewController _compatView];
-[UICompatibilityInputViewController _systemViewControllerForInputMode:];
-[UICompatibilityInputViewController willBeginTranslation];
-[UICompatibilityInputViewController keyboardWillChangeFromDelegate:toDelegate:];
-[UICompatibilityInputViewController viewWillAppear:];
-[UICompatibilityInputViewController removeSnapshotView];
-[UICompatibilityInputViewController _canShowWhileLocked];
-[UICompatibilityInputViewController tearDownInputController];
-[UICompatibilityInputViewController setInputController:];
-[UICompatibilityInputViewController loadView];
-[UICompatibilityInputViewController addSnapshotViewForInputMode:];
-[UICompatibilityInputViewController focusSafeAreaLayoutGuide];
-[UICompatibilityInputViewController generateCompatibleSizeConstraintsIfNecessary];
-[UICompatibilityInputViewController resetInputMode];
-[UICompatibilityInputViewController shouldUpdateInputMode:];
-[UICompatibilityInputViewController killIncomingExtension];
-[UICompatibilityInputViewController setBlinkAssertion:];
-[UICompatibilityInputViewController shouldAutomaticallyForwardRotationMethods];
-[UICompatibilityInputViewController setInternalEdgeMatchConstraints:];
-[UICompatibilityInputViewController animatableElement];
-[UICompatibilityInputViewController _keyboardForThisViewController];
-[UICompatibilityInputViewController setTearingDownInputController];
-[UICompatibilityInputViewController takeSnapshotView];
-[UICompatibilityInputViewController internalEdgeMatchConstraints];
-[UICompatibilityInputViewController didMoveToParentViewController:];
-[UICompatibilityInputViewController preferredFocusedView];
-[UICompatibilityInputViewController finishSplitTransition:];
-[UICompatibilityInputViewController assertCurrentInputModeIfNecessary];
-[UICompatibilityInputViewController shouldAutomaticallyForwardAppearanceMethods];
-[UICompatibilityInputViewController _compatibilityController];
```
