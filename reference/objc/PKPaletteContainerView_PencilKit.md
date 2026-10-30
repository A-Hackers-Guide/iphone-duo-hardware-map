# `PKPaletteContainerView`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `PKPaletteEdgeLocating`, `PKPaletteViewSizeScaling`
- 15 instance variables, 7 properties, 9 instance methods, 0 class methods

## Instance variables

```
Q _edgeLocation;
Q _cornerLocation;
d _scalingFactor;
@"UIView" _contentView;
@"NSLayoutConstraint" _contentViewTopConstraint;
@"NSLayoutConstraint" _contentViewBottomConstraint;
@"NSLayoutConstraint" _contentViewLeftConstraint;
@"NSLayoutConstraint" _contentViewRightConstraint;
@"PKPaletteAccessoryView" _accessoryView;
@"NSLayoutConstraint" _accessoryViewTopConstraint;
@"NSLayoutConstraint" _accessoryViewBottomConstraint;
@"NSLayoutConstraint" _accessoryViewLeftConstraint;
@"NSLayoutConstraint" _accessoryViewRightConstraint;
@"NSLayoutConstraint" _accessoryViewWidthConstraint;
@"NSLayoutConstraint" _accessoryViewHeightConstraint;
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
-[PKPaletteContainerView scalingFactor];
-[PKPaletteContainerView layoutSubviews];
-[PKPaletteContainerView hitTest:withEvent:];
-[PKPaletteContainerView setScalingFactor:];
-[PKPaletteContainerView initWithFrame:];
-[PKPaletteContainerView cornerLocation];
-[PKPaletteContainerView edgeLocation];
-[PKPaletteContainerView setCornerLocation:];
-[PKPaletteContainerView setEdgeLocation:];
```
