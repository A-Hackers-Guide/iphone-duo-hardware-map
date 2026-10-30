# `PKPaletteToolPickerContainerView`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `PKPaletteEdgeLocating`, `PKPaletteViewSizeScaling`
- 10 instance variables, 14 properties, 23 instance methods, 0 class methods

## Instance variables

```
Q _edgeLocation;
Q _cornerLocation;
d _scalingFactor;
@"PKPaletteToolPickerView" _toolPickerView;
@"NSLayoutConstraint" _toolPickerViewTopConstraint;
@"NSLayoutConstraint" _toolPickerViewBottomConstraint;
@"NSLayoutConstraint" _toolPickerViewLeftConstraint;
@"NSLayoutConstraint" _toolPickerViewRightConstraint;
@"NSLayoutConstraint" _toolPickerViewCenterXConstraint;
@"NSLayoutConstraint" _toolPickerViewCenterYConstraint;
```

## Properties

```
@property (T@"NSLayoutConstraint",&,N,V_toolPickerViewTopConstraint) toolPickerViewTopConstraint;
@property (T@"NSLayoutConstraint",&,N,V_toolPickerViewBottomConstraint) toolPickerViewBottomConstraint;
@property (T@"NSLayoutConstraint",&,N,V_toolPickerViewLeftConstraint) toolPickerViewLeftConstraint;
@property (T@"NSLayoutConstraint",&,N,V_toolPickerViewRightConstraint) toolPickerViewRightConstraint;
@property (T@"NSLayoutConstraint",&,N,V_toolPickerViewCenterXConstraint) toolPickerViewCenterXConstraint;
@property (T@"NSLayoutConstraint",&,N,V_toolPickerViewCenterYConstraint) toolPickerViewCenterYConstraint;
@property (T@"PKPaletteToolPickerView",R,N,V_toolPickerView) toolPickerView;
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
-[PKPaletteToolPickerContainerView scalingFactor];
-[PKPaletteToolPickerContainerView init];
-[PKPaletteToolPickerContainerView hitTest:withEvent:];
-[PKPaletteToolPickerContainerView setScalingFactor:];
-[PKPaletteToolPickerContainerView traitCollectionDidChange:];
-[PKPaletteToolPickerContainerView _updateUI];
-[PKPaletteToolPickerContainerView toolPickerViewCenterYConstraint];
-[PKPaletteToolPickerContainerView setToolPickerViewTopConstraint:];
-[PKPaletteToolPickerContainerView toolPickerViewCenterXConstraint];
-[PKPaletteToolPickerContainerView cornerLocation];
-[PKPaletteToolPickerContainerView edgeLocation];
-[PKPaletteToolPickerContainerView setCornerLocation:];
-[PKPaletteToolPickerContainerView setEdgeLocation:];
-[PKPaletteToolPickerContainerView setToolPickerViewBottomConstraint:];
-[PKPaletteToolPickerContainerView setToolPickerViewCenterXConstraint:];
-[PKPaletteToolPickerContainerView setToolPickerViewCenterYConstraint:];
-[PKPaletteToolPickerContainerView setToolPickerViewLeftConstraint:];
-[PKPaletteToolPickerContainerView setToolPickerViewRightConstraint:];
-[PKPaletteToolPickerContainerView toolPickerView];
-[PKPaletteToolPickerContainerView toolPickerViewBottomConstraint];
-[PKPaletteToolPickerContainerView toolPickerViewLeftConstraint];
-[PKPaletteToolPickerContainerView toolPickerViewRightConstraint];
-[PKPaletteToolPickerContainerView toolPickerViewTopConstraint];
```
