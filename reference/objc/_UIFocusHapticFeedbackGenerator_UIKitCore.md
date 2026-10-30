# `_UIFocusHapticFeedbackGenerator`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"CARSession" _carSession;
@"CARInputDeviceTouchpad" _currentTouchpad;
@"<_UISceneCarPlaySessionClient>" _carSessionClient;
@"_UISceneCarPlaySessionTouchpad" _currentCarTouchpad;
Q _currentSenderID;
```

## Properties

```
@property (T@"CARSession",&,N,V_carSession) carSession;
@property (T@"CARInputDeviceTouchpad",&,N,V_currentTouchpad) currentTouchpad;
@property (T@"<_UISceneCarPlaySessionClient>",&,N,V_carSessionClient) carSessionClient;
@property (T@"_UISceneCarPlaySessionTouchpad",&,N,V_currentCarTouchpad) currentCarTouchpad;
@property (TQ,N,V_currentSenderID) currentSenderID;
```

## Instance methods

```
-[_UIFocusHapticFeedbackGenerator initWithWindowScene:];
-[_UIFocusHapticFeedbackGenerator currentSenderID];
-[_UIFocusHapticFeedbackGenerator currentTouchpad];
-[_UIFocusHapticFeedbackGenerator carSession];
-[_UIFocusHapticFeedbackGenerator carSessionClient];
-[_UIFocusHapticFeedbackGenerator currentCarTouchpad];
-[_UIFocusHapticFeedbackGenerator performHapticFeedbackForFocusUpdateInContext:];
-[_UIFocusHapticFeedbackGenerator setCarSession:];
-[_UIFocusHapticFeedbackGenerator setCarSessionClient:];
-[_UIFocusHapticFeedbackGenerator setCurrentCarTouchpad:];
-[_UIFocusHapticFeedbackGenerator setCurrentSenderID:];
-[_UIFocusHapticFeedbackGenerator setCurrentTouchpad:];
```
