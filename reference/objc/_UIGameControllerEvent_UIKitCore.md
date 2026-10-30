# `_UIGameControllerEvent`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIEvent`
- 3 instance variables, 0 properties, 12 instance methods, 0 class methods

## Instance variables

```
{?="senderID"Q"controllerState"[16d]"normalizedLeftStickState"[4d]"normalizedRightStickState"[4d]"normalizedShoulderButtonState"[4d]} _previousState;
Q _activeComponent;
B _beginningInputStream;
```

## Instance methods

```
-[_UIGameControllerEvent subtype];
-[_UIGameControllerEvent _reset];
-[_UIGameControllerEvent _processShoulder:pressesEvent:timestamp:];
-[_UIGameControllerEvent _leftStickPosition];
-[_UIGameControllerEvent _processLeftStick:pressesEvent:timestamp:];
-[_UIGameControllerEvent _maybeConvertAndSendAsPressesEvent];
-[_UIGameControllerEvent _sendEventToResponder:];
-[_UIGameControllerEvent _processRightStick:pressesEvent:timestamp:];
-[_UIGameControllerEvent type];
-[_UIGameControllerEvent _processDPad:pressesEvent:timestamp:];
-[_UIGameControllerEvent _determineInputTypeAndProcess:pressesEvent:timestamp:];
-[_UIGameControllerEvent _processStandardButtons:pressesEvent:timestamp:];
```
