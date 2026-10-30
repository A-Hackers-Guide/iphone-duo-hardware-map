# `WFHyperlinkFooterView`

- Image: [`/System/Library/PrivateFrameworks/WiFiKit.framework/WiFiKit`](../userland/System__Library__PrivateFrameworks__WiFiKit.framework__WiFiKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `UITextViewDelegate`
- 6 instance variables, 9 properties, 18 instance methods, 0 class methods

## Instance variables

```
@"UITextView" _textView;
@"NSString" _text;
@"NSURL" _URL;
{_NSRange="location"Q"length"Q} _linkRange;
@ _target;
: _action;
```

## Properties

```
@property (T@"NSString",&) text;
@property (T{_NSRange=QQ}) linkRange;
@property (T@,W,V_target) target;
@property (T:,V_action) action;
@property (T@"NSURL",&) URL;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[WFHyperlinkFooterView text];
-[WFHyperlinkFooterView init];
-[WFHyperlinkFooterView textInsets];
-[WFHyperlinkFooterView layoutSubviews];
-[WFHyperlinkFooterView setAction:];
-[WFHyperlinkFooterView action];
-[WFHyperlinkFooterView setLinkRange:];
-[WFHyperlinkFooterView sizeThatFits:];
-[WFHyperlinkFooterView setURL:];
-[WFHyperlinkFooterView setTarget:];
-[WFHyperlinkFooterView setText:];
-[WFHyperlinkFooterView linkRange];
-[WFHyperlinkFooterView target];
-[WFHyperlinkFooterView URL];
-[WFHyperlinkFooterView textView:shouldInteractWithURL:inRange:interaction:];
-[WFHyperlinkFooterView preferredHeightForWidth:];
-[WFHyperlinkFooterView _linkify];
-[WFHyperlinkFooterView isLargeAccessibilityTextSize];
```
