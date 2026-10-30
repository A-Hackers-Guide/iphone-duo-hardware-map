# `UIAutocorrectBubbleContainer`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 11 instance variables, 11 properties, 34 instance methods, 0 class methods

## Instance variables

```
@"NSString" _typedText;
@"UIAutocorrectBubble" _bubble;
@"UIView" _fakeTextSelectionHighlight;
@"UIView" _typedTextAnimationPlaceholder;
@"NSLayoutConstraint" _highlightWidthConstraint;
@"NSLayoutConstraint" _bubbleTopConstraint;
@"NSLayoutConstraint" _xConstraint;
@"NSLayoutConstraint" _yConstraint;
@"NSLayoutConstraint" _heightConstraint;
@"NSLayoutConstraint" _widthConstraint;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _referenceRect;
```

## Properties

```
@property (T@"NSString",&,N,V_typedText) typedText;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_referenceRect) referenceRect;
@property (T@"UIAutocorrectBubble",&,N,V_bubble) bubble;
@property (T@"UIView",&,N,V_fakeTextSelectionHighlight) fakeTextSelectionHighlight;
@property (T@"UIView",&,N,V_typedTextAnimationPlaceholder) typedTextAnimationPlaceholder;
@property (T@"NSLayoutConstraint",&,N,V_highlightWidthConstraint) highlightWidthConstraint;
@property (T@"NSLayoutConstraint",&,N,V_bubbleTopConstraint) bubbleTopConstraint;
@property (T@"NSLayoutConstraint",&,N,V_xConstraint) xConstraint;
@property (T@"NSLayoutConstraint",&,N,V_yConstraint) yConstraint;
@property (T@"NSLayoutConstraint",&,N,V_heightConstraint) heightConstraint;
@property (T@"NSLayoutConstraint",&,N,V_widthConstraint) widthConstraint;
```

## Instance methods

```
-[UIAutocorrectBubbleContainer setHeightConstraint:];
-[UIAutocorrectBubbleContainer heightConstraint];
-[UIAutocorrectBubbleContainer setTypedText:];
-[UIAutocorrectBubbleContainer typedText];
-[UIAutocorrectBubbleContainer init];
-[UIAutocorrectBubbleContainer reset];
-[UIAutocorrectBubbleContainer widthConstraint];
-[UIAutocorrectBubbleContainer setWidthConstraint:];
-[UIAutocorrectBubbleContainer setXConstraint:];
-[UIAutocorrectBubbleContainer setYConstraint:];
-[UIAutocorrectBubbleContainer isViewAnimating];
-[UIAutocorrectBubbleContainer animateAutocorrectionAccepted];
-[UIAutocorrectBubbleContainer bubble];
-[UIAutocorrectBubbleContainer bubbleTopConstraint];
-[UIAutocorrectBubbleContainer createTypedTextViewWithTypedText:];
-[UIAutocorrectBubbleContainer didTapAutocorrectionBubble];
-[UIAutocorrectBubbleContainer dismissAutocorrectBubble];
-[UIAutocorrectBubbleContainer fakeTextSelectionHighlight];
-[UIAutocorrectBubbleContainer highlightWidthConstraint];
-[UIAutocorrectBubbleContainer performReset];
-[UIAutocorrectBubbleContainer referenceRect];
-[UIAutocorrectBubbleContainer setBubble:];
-[UIAutocorrectBubbleContainer setBubbleTopConstraint:];
-[UIAutocorrectBubbleContainer setFakeTextSelectionHighlight:];
-[UIAutocorrectBubbleContainer setHighlightWidthConstraint:];
-[UIAutocorrectBubbleContainer setReferenceRect:];
-[UIAutocorrectBubbleContainer setTypedTextAnimationPlaceholder:];
-[UIAutocorrectBubbleContainer typedTextAnimationPlaceholder];
-[UIAutocorrectBubbleContainer updateBubbleWithAutocorrectionText:referenceRect:];
-[UIAutocorrectBubbleContainer updateFakeTextSelectionHighlightForRect:];
-[UIAutocorrectBubbleContainer updateSelfWithRect:];
-[UIAutocorrectBubbleContainer updateWithAutocorrectionText:typedText:referenceTextView:referenceRect:];
-[UIAutocorrectBubbleContainer xConstraint];
-[UIAutocorrectBubbleContainer yConstraint];
```
