# `CEKExpandingTickMarksView`

- Image: [`/System/Library/PrivateFrameworks/CameraEditKit.framework/CameraEditKit`](../userland/System__Library__PrivateFrameworks__CameraEditKit.framework__CameraEditKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 16 instance variables, 16 properties, 41 instance methods, 0 class methods

## Instance variables

```
B _expanded;
B _expandedTicksUseMainHeight;
B _endTicksUseMainHeight;
d _minimumValue;
d _maximumValue;
q _numberOfTicks;
d _tickSpacing;
d _tickWidth;
d _mainTickHeight;
d _secondaryTickHeight;
q _mainTickStride;
@"NSArray" _tickColorGradient;
@"UIColor" _selectedTickColor;
@"NSMutableArray" __tickViews;
q _selectionStyle;
{_NSRange="location"Q"length"Q} __selectedRange;
```

## Properties

```
@property (T{_NSRange=QQ},N,V__selectedRange) _selectedRange;
@property (T@"NSMutableArray",R,N,V__tickViews) _tickViews;
@property (TB,N,V_endTicksUseMainHeight) endTicksUseMainHeight;
@property (Tq,N,V_selectionStyle) selectionStyle;
@property (Td,R,N,V_minimumValue) minimumValue;
@property (Td,R,N,V_maximumValue) maximumValue;
@property (TB,N,V_expanded) expanded;
@property (Tq,N,V_numberOfTicks) numberOfTicks;
@property (Td,N,V_tickSpacing) tickSpacing;
@property (Td,N,V_tickWidth) tickWidth;
@property (Td,N,V_mainTickHeight) mainTickHeight;
@property (Td,N,V_secondaryTickHeight) secondaryTickHeight;
@property (Tq,N,V_mainTickStride) mainTickStride;
@property (T@"NSArray",C,N,V_tickColorGradient) tickColorGradient;
@property (T@"UIColor",&,N,V_selectedTickColor) selectedTickColor;
@property (TB,N,V_expandedTicksUseMainHeight) expandedTicksUseMainHeight;
```

## Instance methods

```
-[CEKExpandingTickMarksView setExpanded:];
-[CEKExpandingTickMarksView intrinsicContentSize];
-[CEKExpandingTickMarksView setSelectionStyle:];
-[CEKExpandingTickMarksView layoutSubviews];
-[CEKExpandingTickMarksView selectionStyle];
-[CEKExpandingTickMarksView selectedTickColor];
-[CEKExpandingTickMarksView tintColorDidChange];
-[CEKExpandingTickMarksView setTickColorGradient:];
-[CEKExpandingTickMarksView _selectedRange];
-[CEKExpandingTickMarksView setSelectedTickColor:];
-[CEKExpandingTickMarksView tickColorGradient];
-[CEKExpandingTickMarksView minimumValue];
-[CEKExpandingTickMarksView initWithFrame:];
-[CEKExpandingTickMarksView setExpanded:animated:];
-[CEKExpandingTickMarksView maximumValue];
-[CEKExpandingTickMarksView expanded];
-[CEKExpandingTickMarksView set_selectedRange:];
-[CEKExpandingTickMarksView setSelectedValue:];
-[CEKExpandingTickMarksView numberOfTicks];
-[CEKExpandingTickMarksView setTickSpacing:];
-[CEKExpandingTickMarksView _baseColorForTickAtIndex:];
-[CEKExpandingTickMarksView _collapsedTickIndexForIndex:];
-[CEKExpandingTickMarksView _middleTickIndex];
-[CEKExpandingTickMarksView _rebuildTickViews];
-[CEKExpandingTickMarksView _tickViews];
-[CEKExpandingTickMarksView endTicksUseMainHeight];
-[CEKExpandingTickMarksView expandedTicksUseMainHeight];
-[CEKExpandingTickMarksView initWithMinimumValue:maximumValue:];
-[CEKExpandingTickMarksView mainTickHeight];
-[CEKExpandingTickMarksView mainTickStride];
-[CEKExpandingTickMarksView secondaryTickHeight];
-[CEKExpandingTickMarksView setEndTicksUseMainHeight:];
-[CEKExpandingTickMarksView setExpandedTicksUseMainHeight:];
-[CEKExpandingTickMarksView setMainTickHeight:];
-[CEKExpandingTickMarksView setMainTickStride:];
-[CEKExpandingTickMarksView setNumberOfTicks:];
-[CEKExpandingTickMarksView setSecondaryTickHeight:];
-[CEKExpandingTickMarksView setSelectedValue:animated:];
-[CEKExpandingTickMarksView setTickWidth:];
-[CEKExpandingTickMarksView tickSpacing];
-[CEKExpandingTickMarksView tickWidth];
```
