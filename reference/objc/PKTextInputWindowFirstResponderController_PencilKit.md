# `PKTextInputWindowFirstResponderController`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIKeyboardSceneDelegateVisibilityObserver`
- 5 instance variables, 9 properties, 21 instance methods, 0 class methods

## Instance variables

```
B _paletteFloatingMode;
@"<PKTextInputWindowFirstResponderControllerDelegate>" _delegate;
@"PKTextInputWindowFirstResponder" _firstResponder;
@"NSNotificationCenter" __notificationCenter;
@"NSNotification" __delayedNotification;
```

## Properties

```
@property (T@"NSNotificationCenter",&,N,V__notificationCenter) _notificationCenter;
@property (T@"PKTextInputWindowFirstResponder",&,N,V_firstResponder) firstResponder;
@property (T@"NSNotification",&,N,V__delayedNotification) _delayedNotification;
@property (T@"<PKTextInputWindowFirstResponderControllerDelegate>",W,N,V_delegate) delegate;
@property (TB,N,V_paletteFloatingMode) paletteFloatingMode;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[PKTextInputWindowFirstResponderController _notificationCenter];
-[PKTextInputWindowFirstResponderController init];
-[PKTextInputWindowFirstResponderController dealloc];
-[PKTextInputWindowFirstResponderController setDelegate:];
-[PKTextInputWindowFirstResponderController delegate];
-[PKTextInputWindowFirstResponderController initWithNotificationCenter:];
-[PKTextInputWindowFirstResponderController firstResponder];
-[PKTextInputWindowFirstResponderController keyboardSceneDelegate:inputViewSetVisibilityDidChange:includedReset:];
-[PKTextInputWindowFirstResponderController setFirstResponder:];
-[PKTextInputWindowFirstResponderController _delayedNotification];
-[PKTextInputWindowFirstResponderController _forceControllerToReload:];
-[PKTextInputWindowFirstResponderController _handleTextInputSourceDidChange:];
-[PKTextInputWindowFirstResponderController _isResponderEditableTextInput:];
-[PKTextInputWindowFirstResponderController _textInputResponderDidChangeNotificationHandler:];
-[PKTextInputWindowFirstResponderController _updateFirstResponder:isVisible:sendDelegateCallback:];
-[PKTextInputWindowFirstResponderController paletteFloatingMode];
-[PKTextInputWindowFirstResponderController setPaletteFloatingMode:];
-[PKTextInputWindowFirstResponderController set_delayedNotification:];
-[PKTextInputWindowFirstResponderController set_notificationCenter:];
-[PKTextInputWindowFirstResponderController textInputSourceDidChange:];
-[PKTextInputWindowFirstResponderController updateFirstResponderFromWindowScene:sendDelegateCallback:];
```
