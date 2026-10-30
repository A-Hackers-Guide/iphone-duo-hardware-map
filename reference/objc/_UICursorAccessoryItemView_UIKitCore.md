# `_UICursorAccessoryItemView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIControl`
- 8 instance variables, 7 properties, 19 instance methods, 2 class methods

## Instance variables

```
@"UILabel" _labelView;
@"UIImageView" _imageView;
@"_UIShapeView" _backgroundView;
B _highlighted;
B _collapsed;
Q _style;
Q _roundedEdges;
{?="label"@"NSString""identifier"@"NSString""image"@"UIImage""type"Q} _content;
```

## Properties

```
@property (TQ,N,V_style) style;
@property (TB,R,N,GisActive) active;
@property (Td,R,N) horizontalPadding;
@property (TB,N,GisHighlighted,V_highlighted) highlighted;
@property (TQ,N,V_roundedEdges) roundedEdges;
@property (TB,N,V_collapsed) collapsed;
@property (T{?=@@@Q},N,V_content) content;
```

## Class methods

```
+[_UICursorAccessoryItemView _makeImageView];
+[_UICursorAccessoryItemView _makeLabelView];
```

## Instance methods

```
-[_UICursorAccessoryItemView setCollapsed:];
-[_UICursorAccessoryItemView setContent:];
-[_UICursorAccessoryItemView horizontalPadding];
-[_UICursorAccessoryItemView content];
-[_UICursorAccessoryItemView isHighlighted];
-[_UICursorAccessoryItemView cancelTrackingWithEvent:];
-[_UICursorAccessoryItemView endTrackingWithTouch:withEvent:];
-[_UICursorAccessoryItemView layoutSubviews];
-[_UICursorAccessoryItemView style];
-[_UICursorAccessoryItemView beginTrackingWithTouch:withEvent:];
-[_UICursorAccessoryItemView setStyle:];
-[_UICursorAccessoryItemView sizeThatFits:];
-[_UICursorAccessoryItemView setHighlighted:];
-[_UICursorAccessoryItemView isActive];
-[_UICursorAccessoryItemView initWithFrame:];
-[_UICursorAccessoryItemView _recomputeColors];
-[_UICursorAccessoryItemView collapsed];
-[_UICursorAccessoryItemView roundedEdges];
-[_UICursorAccessoryItemView setRoundedEdges:];
```
