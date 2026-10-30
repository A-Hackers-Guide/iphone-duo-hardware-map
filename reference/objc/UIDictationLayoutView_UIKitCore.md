# `UIDictationLayoutView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIDictationView`
- Protocols: `UIPointerInteractionDelegate`
- 7 instance variables, 4 properties, 13 instance methods, 0 class methods

## Instance variables

```
B _hideSwitcher;
@"UIButton" _globeButton;
@"UIButton" _keyboardButton;
@"UILabel" _languageLabel;
@"NSString" _currentDictationLanguage;
@"UIView" _waveTapEndpointButtonView;
B _blackTextColor;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UIDictationLayoutView setState:];
-[UIDictationLayoutView setRenderConfig:];
-[UIDictationLayoutView pointerInteraction:styleForRegion:];
-[UIDictationLayoutView layoutSubviews];
-[UIDictationLayoutView initWithFrame:];
-[UIDictationLayoutView darkGrayColor];
-[UIDictationLayoutView finishReturnToKeyboard];
-[UIDictationLayoutView globeButtonPressed:withEvent:];
-[UIDictationLayoutView globeButtonPressed:withEvent:location:];
-[UIDictationLayoutView isShowing];
-[UIDictationLayoutView keyboardButtonPressed:];
-[UIDictationLayoutView returnToKeyboard];
-[UIDictationLayoutView updateLanguageLabel];
```
