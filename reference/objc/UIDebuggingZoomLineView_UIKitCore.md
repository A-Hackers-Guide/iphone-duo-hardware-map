# `UIDebuggingZoomLineView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 5 instance variables, 5 properties, 13 instance methods, 0 class methods

## Instance variables

```
Q _direction;
@"UILabel" _lineLabel;
{CGPoint="x"d"y"d} _start;
{CGPoint="x"d"y"d} _end;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _rect;
```

## Properties

```
@property (T@"UILabel",&,N,V_lineLabel) lineLabel;
@property (T{CGPoint=dd},N,V_start) start;
@property (T{CGPoint=dd},N,V_end) end;
@property (TQ,N,V_direction) direction;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_rect) rect;
```

## Instance methods

```
-[UIDebuggingZoomLineView drawRect:];
-[UIDebuggingZoomLineView start];
-[UIDebuggingZoomLineView setDirection:];
-[UIDebuggingZoomLineView end];
-[UIDebuggingZoomLineView direction];
-[UIDebuggingZoomLineView setEnd:];
-[UIDebuggingZoomLineView setStart:];
-[UIDebuggingZoomLineView rect];
-[UIDebuggingZoomLineView setRect:];
-[UIDebuggingZoomLineView initWithFrame:];
-[UIDebuggingZoomLineView lineLabel];
-[UIDebuggingZoomLineView setLineLabel:];
-[UIDebuggingZoomLineView updateLabelFrame];
```
