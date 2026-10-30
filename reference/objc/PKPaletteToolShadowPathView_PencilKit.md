# `PKPaletteToolShadowPathView`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `PKPaletteEdgeLocating`, `PKPaletteViewSizeScaling`
- 5 instance variables, 7 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"UIView" _largeShadow;
@"UIView" _smallShadow;
Q _edgeLocation;
Q _cornerLocation;
d _scalingFactor;
```

## Properties

```
@property (TQ,N,V_edgeLocation) edgeLocation;
@property (TQ,N,V_cornerLocation) cornerLocation;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (Td,N,V_scalingFactor) scalingFactor;
```

## Instance methods

```
-[PKPaletteToolShadowPathView intrinsicContentSize];
-[PKPaletteToolShadowPathView scalingFactor];
-[PKPaletteToolShadowPathView layoutSubviews];
-[PKPaletteToolShadowPathView setScalingFactor:];
-[PKPaletteToolShadowPathView _updateUI];
-[PKPaletteToolShadowPathView _applyLargeShadowToLayer:];
-[PKPaletteToolShadowPathView _applySmallShadowToLayer:];
-[PKPaletteToolShadowPathView applyShadowToLayer:];
-[PKPaletteToolShadowPathView cornerLocation];
-[PKPaletteToolShadowPathView edgeLocation];
-[PKPaletteToolShadowPathView initWithToolConfiguration:];
-[PKPaletteToolShadowPathView setCornerLocation:];
-[PKPaletteToolShadowPathView setEdgeLocation:];
```
