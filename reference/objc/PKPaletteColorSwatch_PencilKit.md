# `PKPaletteColorSwatch`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `UIPointerInteractionDelegate`
- 10 instance variables, 10 properties, 19 instance methods, 0 class methods

## Instance variables

```
B _selected;
B _showsSelectionHighlight;
@"PKSwatchColor" _swatchColor;
q _colorAppearance;
@"UIPointerInteraction" _pointerInteraction;
d _selectionInset;
d _bulletInset;
@"UIView" _colorBackgroundView;
@"CAShapeLayer" _selectionRingMaskLayer;
@"UIView" _colorBulletView;
```

## Properties

```
@property (T@"UIView",&,N,V_colorBackgroundView) colorBackgroundView;
@property (T@"CAShapeLayer",&,N,V_selectionRingMaskLayer) selectionRingMaskLayer;
@property (T@"UIView",&,N,V_colorBulletView) colorBulletView;
@property (T@"UIColor",R,N) presentationColor;
@property (TB,N,GisSelected,V_selected) selected;
@property (T@"PKSwatchColor",&,N,V_swatchColor) swatchColor;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[PKPaletteColorSwatch setSelected:];
-[PKPaletteColorSwatch pointerInteraction:styleForRegion:];
-[PKPaletteColorSwatch init];
-[PKPaletteColorSwatch layoutSubviews];
-[PKPaletteColorSwatch isSelected];
-[PKPaletteColorSwatch pointerInteraction:regionForRequest:defaultRegion:];
-[PKPaletteColorSwatch traitCollectionDidChange:];
-[PKPaletteColorSwatch colorBulletView];
-[PKPaletteColorSwatch setSwatchColor:];
-[PKPaletteColorSwatch colorBackgroundView];
-[PKPaletteColorSwatch newColorBackgroundView];
-[PKPaletteColorSwatch presentationColor];
-[PKPaletteColorSwatch selectionRingMaskLayer];
-[PKPaletteColorSwatch setColorBackgroundView:];
-[PKPaletteColorSwatch setColorBulletView:];
-[PKPaletteColorSwatch setSelectionRingMaskLayer:];
-[PKPaletteColorSwatch swatchColor];
-[PKPaletteColorSwatch wantsBackgroundViewColor];
-[PKPaletteColorSwatch wantsColorBulletVisible];
```
