# `_UIKeyboardArbitration` (protocol)

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- 0 instance variables, 0 properties, 21 instance methods, 0 class methods

## Instance methods

```
-[_UIKeyboardArbitration setWindowHostingPID:active:];
-[_UIKeyboardArbitration focusApplicationWithProcessIdentifier:context:onCompletion:];
-[_UIKeyboardArbitration startArbitrationWithExpectedState:hostingPIDs:usingFence:withSuppression:onConnected:];
-[_UIKeyboardArbitration signalEventSourceChanged:completionHandler:];
-[_UIKeyboardArbitration startArbitrationWithExpectedState:focusContext:hostingPIDs:usingFence:withSuppression:onConnected:];
-[_UIKeyboardArbitration focusApplicationWithProcessIdentifier:context:stealingKeyboard:onCompletion:];
-[_UIKeyboardArbitration setKeyboardTotalDisable:withFence:completionHandler:];
-[_UIKeyboardArbitration setDeactivating:];
-[_UIKeyboardArbitration setWindowContextID:focusContext:windowState:withLevel:];
-[_UIKeyboardArbitration retrieveDebugInformation:];
-[_UIKeyboardArbitration signalKeyboardChangeComplete];
-[_UIKeyboardArbitration signalKeyboardChanged:onCompletion:];
-[_UIKeyboardArbitration setClientFocusContext:];
-[_UIKeyboardArbitration signalAutofillUIBringupWithCompletion:];
-[_UIKeyboardArbitration notifyIAVHeight:];
-[_UIKeyboardArbitration transition:eventStage:withInfo:];
-[_UIKeyboardArbitration applicationShouldFocusWithBundle:onCompletion:];
-[_UIKeyboardArbitration setWantsFencing:];
-[_UIKeyboardArbitration notifyHostedPIDsOfSuppression:];
-[_UIKeyboardArbitration userFirstTapOnKeyboard];
-[_UIKeyboardArbitration retrieveMoreDebugInformationWithCompletion:];
```
