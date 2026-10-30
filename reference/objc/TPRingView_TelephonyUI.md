# `TPRingView`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUI.framework/TelephonyUI`](../userland/System__Library__PrivateFrameworks__TelephonyUI.framework__TelephonyUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 5 instance variables, 5 properties, 15 instance methods, 8 class methods

## Instance variables

```
@"CALayer" _luminanceRingLayer;
@"CALayer" _dodgeRingLayer;
@"CALayer" _highlightDodgeLayer;
@"CALayer" _highlightLuminanceLayer;
@"CALayer" _selectionLayer;
```

## Properties

```
@property (T@"CALayer",&,V_luminanceRingLayer) luminanceRingLayer;
@property (T@"CALayer",&,V_dodgeRingLayer) dodgeRingLayer;
@property (T@"CALayer",&,V_highlightDodgeLayer) highlightDodgeLayer;
@property (T@"CALayer",&,V_highlightLuminanceLayer) highlightLuminanceLayer;
@property (T@"CALayer",&,V_selectionLayer) selectionLayer;
```

## Class methods

```
+[TPRingView ringSize];
+[TPRingView colorForDodge];
+[TPRingView colorForLuminance];
+[TPRingView createRingImageWithSize:strokeWidth:color:];
+[TPRingView ringCornerRadius];
+[TPRingView ringImageForDodge];
+[TPRingView ringImageForLuminance];
+[TPRingView ringStroke];
```

## Instance methods

```
-[TPRingView setSelected:];
-[TPRingView intrinsicContentSize];
-[TPRingView setHighlighted:];
-[TPRingView setEnabled:];
-[TPRingView initWithFrame:];
-[TPRingView selectionLayer];
-[TPRingView setSelectionLayer:];
-[TPRingView dodgeRingLayer];
-[TPRingView highlightDodgeLayer];
-[TPRingView highlightLuminanceLayer];
-[TPRingView luminanceRingLayer];
-[TPRingView setDodgeRingLayer:];
-[TPRingView setHighlightDodgeLayer:];
-[TPRingView setHighlightLuminanceLayer:];
-[TPRingView setLuminanceRingLayer:];
```
