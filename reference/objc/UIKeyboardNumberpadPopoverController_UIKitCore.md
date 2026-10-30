# `UIKeyboardNumberpadPopoverController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIKeyboardPopoverController`
- Protocols: `UIKeyboardLayoutStarDelegate`
- 6 instance variables, 5 properties, 10 instance methods, 1 class methods

## Instance variables

```
@"UIKeyboardLayoutStar" _layout;
@"UIKBScreenTraits" _screenTraits;
@"UITextInputTraits" _textInputTraits;
@"UIKBTree" _keyboard;
@"UIKeyboardInputMode" _keyboardInputMode;
B _shownKeyboardLayout;
```

## Properties

```
@property (T@"UIKeyboardLayoutStar",&,N,V_layout) layout;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UIKeyboardNumberpadPopoverController visualEffectGroupName];
```

## Instance methods

```
-[UIKeyboardNumberpadPopoverController setContentView:];
-[UIKeyboardNumberpadPopoverController viewDidLoad];
-[UIKeyboardNumberpadPopoverController viewDidLayoutSubviews];
-[UIKeyboardNumberpadPopoverController layout];
-[UIKeyboardNumberpadPopoverController preferredContentSize];
-[UIKeyboardNumberpadPopoverController setLayout:];
-[UIKeyboardNumberpadPopoverController initWithTextInputTraits:keyboardInputMode:];
-[UIKeyboardNumberpadPopoverController shouldDismissNotification:];
-[UIKeyboardNumberpadPopoverController showKeyboardLayout];
-[UIKeyboardNumberpadPopoverController wantsDimmingView];
```
