# `PKSqueezePaletteView`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 24 instance variables, 0 properties, 3 instance methods, 0 class methods

## Instance variables

```
@"PKSqueezePaletteViewResizeHandle" _resizeHandle;
@"CAShapeLayer" _largeShadow;
@"CAShapeLayer" _smallShadow;
@"CAShapeLayer" _baseShapeLayer;
@"CAShapeLayer" _contentClippingShapeMask;
@"CAShapeLayer" _toolsContentClippingShapeMask;
^{CGPath=} _baseShapeLayerPathForHitTesting;
{CGPoint="x"d"y"d} _viewCenter;
B _clockwise;
@"<PKSqueezePaletteViewDelegate>" _delegate;
d _radius;
d _contentHeight;
d _startAngle;
d _endAngle;
d _azimuth;
@"PKSqueezePaletteGlassBackgroundView" _backgroundView;
@"UIView" _toolsContentView;
@"UIView" _contentView;
@"PKSqueezePaletteViewLayoutFactory" _layoutFactory;
@"<PKSqueezePaletteViewLayout>" _currentLayout;
@"PKSqueezePaletteViewContext" _context;
q _colorAppearance;
@? _layoutSubviewsHandler;
@? __extendedColorPickerColorSelectionHandler;
```

## Instance methods

```
-[PKSqueezePaletteView dealloc];
-[PKSqueezePaletteView layoutSubviews];
-[PKSqueezePaletteView hitTest:withEvent:];
```
