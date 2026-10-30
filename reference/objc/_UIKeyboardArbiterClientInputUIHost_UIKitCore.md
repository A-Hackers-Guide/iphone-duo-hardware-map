# `_UIKeyboardArbiterClientInputUIHost`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIKeyboardArbiterClient`
- Protocols: `UIKeyboardScenePresentationModeManagerDelegate`
- 4 instance variables, 4 properties, 30 instance methods, 0 class methods

## Instance variables

```
B _showing;
B _inputDestinationInWindowedMode;
@"UIKeyboardScenePresentationModeManager" _presentationModeManager;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _keyboardFrameIncludingRemoteIAV;
```

## Properties

```
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_keyboardFrameIncludingRemoteIAV) keyboardFrameIncludingRemoteIAV;
@property (TB,N,V_showing) showing;
@property (T@"UIKeyboardScenePresentationModeManager",R,N,V_presentationModeManager) presentationModeManager;
@property (TB,N,V_inputDestinationInWindowedMode) inputDestinationInWindowedMode;
```

## Instance methods

```
-[_UIKeyboardArbiterClientInputUIHost presentationModeManager];
-[_UIKeyboardArbiterClientInputUIHost allowedToShowKeyboard];
-[_UIKeyboardArbiterClientInputUIHost setKeyboardSceneIdentifierEnteringForegroundForScene:];
-[_UIKeyboardArbiterClientInputUIHost _updateKeyboardUIScenePresentationMode];
-[_UIKeyboardArbiterClientInputUIHost init];
-[_UIKeyboardArbiterClientInputUIHost signalKeyboardUIDidChange:onCompletion:];
-[_UIKeyboardArbiterClientInputUIHost resetSnapshotWithWindowCheck:];
-[_UIKeyboardArbiterClientInputUIHost configureArbiterCommunication:];
-[_UIKeyboardArbiterClientInputUIHost arbiterProxy];
-[_UIKeyboardArbiterClientInputUIHost shouldSnapshot];
-[_UIKeyboardArbiterClientInputUIHost currentHostedPIDs];
-[_UIKeyboardArbiterClientInputUIHost completeKeyboardChange];
-[_UIKeyboardArbiterClientInputUIHost remoteKeyboardUndocked:];
-[_UIKeyboardArbiterClientInputUIHost isCurrentInputDestination];
-[_UIKeyboardArbiterClientInputUIHost setInputDestinationInWindowedMode:];
-[_UIKeyboardArbiterClientInputUIHost _layoutKeyboardViews:];
-[_UIKeyboardArbiterClientInputUIHost keyboardFrameIncludingRemoteIAV];
-[_UIKeyboardArbiterClientInputUIHost setShowing:];
-[_UIKeyboardArbiterClientInputUIHost inputSessionDidEndUnexpectedly];
-[_UIKeyboardArbiterClientInputUIHost scenePresentationModeManager:didChangeToMode:];
-[_UIKeyboardArbiterClientInputUIHost isWritingToolsHostingViewService];
-[_UIKeyboardArbiterClientInputUIHost applicationKeyWindowWillChange:];
-[_UIKeyboardArbiterClientInputUIHost isSpotlight:];
-[_UIKeyboardArbiterClientInputUIHost queue_sceneBecameFocused:withCompletion:];
-[_UIKeyboardArbiterClientInputUIHost showing];
-[_UIKeyboardArbiterClientInputUIHost inputDestinationInWindowedMode];
-[_UIKeyboardArbiterClientInputUIHost keyboardSendNotification:withInfo:isStart:];
-[_UIKeyboardArbiterClientInputUIHost setCurrentUIState:];
-[_UIKeyboardArbiterClientInputUIHost keyboardVisibilityDidChangeWithFrame:visible:tracking:];
-[_UIKeyboardArbiterClientInputUIHost snapsShotKeyboard];
```
