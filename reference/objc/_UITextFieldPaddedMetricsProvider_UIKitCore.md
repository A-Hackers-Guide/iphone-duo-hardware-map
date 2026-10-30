# `_UITextFieldPaddedMetricsProvider`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UITextFieldMetricsProvider`
- 3 instance variables, 9 properties, 13 instance methods, 0 class methods

## Instance variables

```
B _canIntrinsicHeightExceedContentHeight;
d _minimumIntrinsicHeight;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _padding;
```

## Properties

```
@property (Td,N,V_minimumIntrinsicHeight) minimumIntrinsicHeight;
@property (TB,N,V_canIntrinsicHeightExceedContentHeight) canIntrinsicHeightExceedContentHeight;
@property (T{UIEdgeInsets=dddd},N,V_padding) padding;
@property (Td,R,N) naturalHeight;
@property (TB,R,N) shouldExtendCaretHeight;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UITextFieldPaddedMetricsProvider padding];
-[_UITextFieldPaddedMetricsProvider naturalHeight];
-[_UITextFieldPaddedMetricsProvider init];
-[_UITextFieldPaddedMetricsProvider initWithPerEdgePadding:];
-[_UITextFieldPaddedMetricsProvider setPadding:];
-[_UITextFieldPaddedMetricsProvider setCanIntrinsicHeightExceedContentHeight:];
-[_UITextFieldPaddedMetricsProvider initWithSymmetricalPadding:];
-[_UITextFieldPaddedMetricsProvider contentFrameForBounds:];
-[_UITextFieldPaddedMetricsProvider intrinsicSizeForContentSize:];
-[_UITextFieldPaddedMetricsProvider setMinimumIntrinsicHeight:];
-[_UITextFieldPaddedMetricsProvider minimumIntrinsicHeight];
-[_UITextFieldPaddedMetricsProvider canIntrinsicHeightExceedContentHeight];
-[_UITextFieldPaddedMetricsProvider shouldExtendCaretHeight];
```
