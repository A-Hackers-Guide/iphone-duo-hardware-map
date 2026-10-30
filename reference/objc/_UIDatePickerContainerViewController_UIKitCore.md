# `_UIDatePickerContainerViewController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `_UIPassthroughScrollInteractionDelegate`
- 2 instance variables, 7 properties, 18 instance methods, 0 class methods

## Instance variables

```
@? _pendingKeyboardAdjustment;
d _keyboardAdjustmentOffset;
```

## Properties

```
@property (T@?,C,N,V_pendingKeyboardAdjustment) pendingKeyboardAdjustment;
@property (Td,N,V_keyboardAdjustmentOffset) keyboardAdjustmentOffset;
@property (T@"_UIDatePickerOverlayPresentation",R,N) presentation;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIDatePickerContainerViewController willTransitionToTraitCollection:withTransitionCoordinator:];
-[_UIDatePickerContainerViewController presentation];
-[_UIDatePickerContainerViewController dealloc];
-[_UIDatePickerContainerViewController keyCommands];
-[_UIDatePickerContainerViewController passthroughScrollInteractionDidRecognize:atLocation:];
-[_UIDatePickerContainerViewController initWithPresentation:];
-[_UIDatePickerContainerViewController _canShowWhileLocked];
-[_UIDatePickerContainerViewController passthroughScrollInteraction:shouldInteractAtLocation:withEvent:];
-[_UIDatePickerContainerViewController viewWillTransitionToSize:withTransitionCoordinator:];
-[_UIDatePickerContainerViewController viewDidDisappear:];
-[_UIDatePickerContainerViewController _defersToPresentingViewControllerForSupportedInterfaceOrientations];
-[_UIDatePickerContainerViewController _didReceiveEscapeKey:];
-[_UIDatePickerContainerViewController didChangeKeyboardAvoidanceAdjustmentDeferral];
-[_UIDatePickerContainerViewController keyboardAdjustmentOffset];
-[_UIDatePickerContainerViewController keyboardFrameWillChange:];
-[_UIDatePickerContainerViewController pendingKeyboardAdjustment];
-[_UIDatePickerContainerViewController setKeyboardAdjustmentOffset:];
-[_UIDatePickerContainerViewController setPendingKeyboardAdjustment:];
```
