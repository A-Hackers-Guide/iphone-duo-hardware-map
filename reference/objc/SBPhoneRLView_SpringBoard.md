# `SBPhoneRLView`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 5 instance variables, 1 properties, 17 instance methods, 0 class methods

## Instance variables

```
d _phoneRLWidth;
^{CGColor=} _phoneRLColor;
B _minimized;
@"NSTimer" _minimizeTimer;
@"SBPhoneRLShapeLayer" _phoneRLLayer;
```

## Properties

```
@property (T@"SBPhoneRLShapeLayer",&,N,V_phoneRLLayer) phoneRLLayer;
```

## Instance methods

```
-[SBPhoneRLView _handleTap:];
-[SBPhoneRLView dealloc];
-[SBPhoneRLView layoutSubviews];
-[SBPhoneRLView _setupGestures];
-[SBPhoneRLView pointInside:withEvent:];
-[SBPhoneRLView _setupLayers];
-[SBPhoneRLView initWithFrame:];
-[SBPhoneRLView _updateColor];
-[SBPhoneRLView _currentWidth];
-[SBPhoneRLView _handleMinimizeTimer:];
-[SBPhoneRLView _handleOutwardSwipe:];
-[SBPhoneRLView _updatePhoneRLWidthAnimated:];
-[SBPhoneRLView phoneRLLayer];
-[SBPhoneRLView setApertureFrame:];
-[SBPhoneRLView setPhoneRLColor:];
-[SBPhoneRLView setPhoneRLLayer:];
-[SBPhoneRLView setPhoneRLWidth:animated:];
```
