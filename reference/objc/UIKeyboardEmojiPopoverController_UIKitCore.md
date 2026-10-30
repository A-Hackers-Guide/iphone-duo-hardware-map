# `UIKeyboardEmojiPopoverController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIKeyboardPopoverController`
- Protocols: `UIKeyboardLayoutStarDelegate`
- 10 instance variables, 5 properties, 29 instance methods, 1 class methods

## Instance variables

```
@"UIKeyboardLayoutStar" _layout;
@"UIView" _keyboardContainer;
@"UIKBScreenTraits" _screenTraits;
@"UITextInputTraits" _textInputTraits;
@"UIKeyboardTaskQueue" _taskQueue;
@"UIKBTree" _keyboard;
@"NSMutableArray" _hiddenKeys;
@"UIKBViewForResponderForwarding" _containerForActiveKeys;
B _shownKeyboardLayout;
@"TUIEmojiSearchInputViewController" _emojiSearchInputViewController;
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
+[UIKeyboardEmojiPopoverController visualEffectGroupName];
```

## Instance methods

```
-[UIKeyboardEmojiPopoverController viewIsAppearing:];
-[UIKeyboardEmojiPopoverController viewWillDisappear:];
-[UIKeyboardEmojiPopoverController dealloc];
-[UIKeyboardEmojiPopoverController viewDidLoad];
-[UIKeyboardEmojiPopoverController viewDidLayoutSubviews];
-[UIKeyboardEmojiPopoverController layout];
-[UIKeyboardEmojiPopoverController preferredContentSize];
-[UIKeyboardEmojiPopoverController isPhone];
-[UIKeyboardEmojiPopoverController setLayout:];
-[UIKeyboardEmojiPopoverController _containerForContainerWindowPortalInteraction];
-[UIKeyboardEmojiPopoverController associateEmojiSearchViewWithEmojiInputView];
-[UIKeyboardEmojiPopoverController configurePopoverPresentationController:];
-[UIKeyboardEmojiPopoverController handleHardwareKeyboardEvent:];
-[UIKeyboardEmojiPopoverController initWithTextInputTraits:];
-[UIKeyboardEmojiPopoverController initWithTextInputTraits:hasVerticalScrolling:];
-[UIKeyboardEmojiPopoverController initWithTextInputTraits:taskQueue:];
-[UIKeyboardEmojiPopoverController initWithTextInputTraits:taskQueue:scrollingDirection:];
-[UIKeyboardEmojiPopoverController initWithTextInputTraits:taskQueue:scrollingDirection:window:caretRect:];
-[UIKeyboardEmojiPopoverController initWithTextInputTraits:taskQueue:window:];
-[UIKeyboardEmojiPopoverController keyboardHeightAdjustmentForCaretRect:windowSize:];
-[UIKeyboardEmojiPopoverController keyboardLayout:containingViewForActiveKey:inKeyplaneView:];
-[UIKeyboardEmojiPopoverController keyboardLayout:didSwitchToKeyplane:];
-[UIKeyboardEmojiPopoverController keyboardLayout:willChangeRenderConfig:];
-[UIKeyboardEmojiPopoverController preferredContentSizeForPhone];
-[UIKeyboardEmojiPopoverController preferredTextFieldHeight];
-[UIKeyboardEmojiPopoverController shouldDismissNotification:];
-[UIKeyboardEmojiPopoverController showKeyboardLayout];
-[UIKeyboardEmojiPopoverController wantsDimmingView];
-[UIKeyboardEmojiPopoverController wireDynamicEmojiSearchDelegate];
```
