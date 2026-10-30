# `UIDictationPopoverController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIKeyboardPopoverController`
- Protocols: `_UIScrollViewScrollObserver`, `_UIGeometryChangeObserver`
- 18 instance variables, 4 properties, 22 instance methods, 0 class methods

## Instance variables

```
@"UIResponder<UITextInput>" _inputDelegate;
@"NSMutableArray" _scrollViews;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _initCaretRectInView;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _sourceRect;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _editMenuFrame;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _clipBounds;
@"UIView" _inputAccessoryView;
@"UIView" _dictationView;
@"NSLayoutConstraint" _dictationViewTopConstraint;
@"NSLayoutConstraint" _dictationViewBottomConstraint;
@"UILabel" _title;
@"UITextView" _textView;
@"UIView" _bottomEdgeView;
B _isVerticalText;
B _needsRestoreArrowDirction;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _popoverFrame;
d _bottomMargin;
Q _arrowDirection;
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
-[UIDictationPopoverController _observeScrollViewDidScroll:];
-[UIDictationPopoverController sourceRect];
-[UIDictationPopoverController textDidChange:];
-[UIDictationPopoverController dealloc];
-[UIDictationPopoverController viewDidLoad];
-[UIDictationPopoverController _geometryChanged:forAncestor:];
-[UIDictationPopoverController viewDidAppear:];
-[UIDictationPopoverController viewDidDisappear:];
-[UIDictationPopoverController setRemoteDictationPopover:];
-[UIDictationPopoverController overrideUserInterfaceStyle];
-[UIDictationPopoverController canPresentTip];
-[UIDictationPopoverController clipBounds];
-[UIDictationPopoverController dismissTip];
-[UIDictationPopoverController forwardRemoteDictationPopover:];
-[UIDictationPopoverController initWithContentView:contentSize:inputDelegate:];
-[UIDictationPopoverController keyboardDidChange:];
-[UIDictationPopoverController movePopoverView:];
-[UIDictationPopoverController movePopoverView:editMenuFrame:];
-[UIDictationPopoverController movePopoverViewForEditMenuFrame:];
-[UIDictationPopoverController movePopoverViewToCurrentCareLocation];
-[UIDictationPopoverController presentTip:tipDescription:];
-[UIDictationPopoverController rectInWindow:];
```
