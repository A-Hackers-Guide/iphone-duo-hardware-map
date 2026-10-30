# `UIDictationPopoverView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIDictationView`
- Protocols: `UIPointerInteractionDelegate`
- 12 instance variables, 4 properties, 16 instance methods, 1 class methods

## Instance variables

```
@"UIButton" _languageButton;
@"UIButton" _cancelButton;
@"UIButton" _centerButton;
@"UIButton" _startButton;
@"UIButton" _stopButton;
@"UIButton" _keyboardButton;
@"UIImage" _showKeyboardButtonImage;
@"UIImage" _hideKeyboardButtonImage;
@"UIImage" _stopDictationImage;
Q _popoverPage;
@"NSMutableArray" _languageButtons;
@"UIView" _languageView;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UIDictationPopoverView viewSize];
```

## Instance methods

```
-[UIDictationPopoverView setState:];
-[UIDictationPopoverView intrinsicContentSize];
-[UIDictationPopoverView pointerInteraction:styleForRegion:];
-[UIDictationPopoverView layoutSubviews];
-[UIDictationPopoverView willMoveToWindow:];
-[UIDictationPopoverView initWithFrame:];
-[UIDictationPopoverView buttonImageNamed:];
-[UIDictationPopoverView cancelButtonPressed:];
-[UIDictationPopoverView centerButtonPressed:];
-[UIDictationPopoverView clearLanguageButtons];
-[UIDictationPopoverView keyboardButtonPressed:];
-[UIDictationPopoverView languageButtonPressed:withEvent:];
-[UIDictationPopoverView languageButtons:];
-[UIDictationPopoverView returnToKeyboard];
-[UIDictationPopoverView startButtonPressed:];
-[UIDictationPopoverView stopButtonPressed:];
```
