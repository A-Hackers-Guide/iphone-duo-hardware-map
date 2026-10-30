# `PKPaletteInkingToolView`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PKPaletteToolView`
- Protocols: `PKInkAttributesPickerDelegate`, `PKPaletteInkingTool`
- 24 instance variables, 34 properties, 81 instance methods, 0 class methods

## Instance variables

```
@"PKPaletteAttributeViewController" _attributeViewController;
@"PKInk" _ink;
@"UIImageView" _colorIndicatorImageView;
@"UIImage" _colorIndicatorImageUp;
@"UIImage" _colorIndicatorImageRight;
@"UIImage" _colorIndicatorImageLeft;
@"UIImageView" _colorIndicatorContourImageView;
@"UIImage" _colorIndicatorContourImageUp;
@"UIImage" _colorIndicatorContourImageRight;
@"UIImage" _colorIndicatorContourImageLeft;
@"UIImageView" _tipIndicatorImageView;
@"UIImage" _toolTipImageUp;
@"UIImage" _toolTipImageRight;
@"UIImage" _toolTipImageLeft;
@"UIImageView" _tipIndicatorContourImageView;
@"UIImage" _toolTipContourImageUp;
@"UIImage" _toolTipContourImageRight;
@"UIImage" _toolTipContourImageLeft;
@"UILabel" _opacityLabel;
@"NSLayoutConstraint" _opacityLabelTopConstraint;
@"NSLayoutConstraint" _opacityLabelLeftConstraint;
@"NSLayoutConstraint" _opacityLabelRightConstraint;
@"NSLayoutConstraint" _opacityLabelCenterXConstraint;
@"NSLayoutConstraint" _opacityLabelCenterYConstraint;
```

## Properties

```
@property (T@"PKInk",&,N,V_ink) ink;
@property (T@"UIImageView",&,N,V_colorIndicatorImageView) colorIndicatorImageView;
@property (T@"UIImage",&,N,V_colorIndicatorImageUp) colorIndicatorImageUp;
@property (T@"UIImage",&,N,V_colorIndicatorImageRight) colorIndicatorImageRight;
@property (T@"UIImage",&,N,V_colorIndicatorImageLeft) colorIndicatorImageLeft;
@property (T@"UIImageView",&,N,V_colorIndicatorContourImageView) colorIndicatorContourImageView;
@property (T@"UIImage",&,N,V_colorIndicatorContourImageUp) colorIndicatorContourImageUp;
@property (T@"UIImage",&,N,V_colorIndicatorContourImageRight) colorIndicatorContourImageRight;
@property (T@"UIImage",&,N,V_colorIndicatorContourImageLeft) colorIndicatorContourImageLeft;
@property (T@"UIImageView",&,N,V_tipIndicatorImageView) tipIndicatorImageView;
@property (T@"UIImage",&,N,V_toolTipImageUp) toolTipImageUp;
@property (T@"UIImage",&,N,V_toolTipImageRight) toolTipImageRight;
@property (T@"UIImage",&,N,V_toolTipImageLeft) toolTipImageLeft;
@property (T@"UIImageView",&,N,V_tipIndicatorContourImageView) tipIndicatorContourImageView;
@property (T@"UIImage",&,N,V_toolTipContourImageUp) toolTipContourImageUp;
@property (T@"UIImage",&,N,V_toolTipContourImageRight) toolTipContourImageRight;
@property (T@"UIImage",&,N,V_toolTipContourImageLeft) toolTipContourImageLeft;
@property (T@"UILabel",&,N,V_opacityLabel) opacityLabel;
@property (T@"NSLayoutConstraint",&,N,V_opacityLabelTopConstraint) opacityLabelTopConstraint;
@property (T@"NSLayoutConstraint",&,N,V_opacityLabelLeftConstraint) opacityLabelLeftConstraint;
@property (T@"NSLayoutConstraint",&,N,V_opacityLabelRightConstraint) opacityLabelRightConstraint;
@property (T@"NSLayoutConstraint",&,N,V_opacityLabelCenterXConstraint) opacityLabelCenterXConstraint;
@property (T@"NSLayoutConstraint",&,N,V_opacityLabelCenterYConstraint) opacityLabelCenterYConstraint;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSString",R,N) toolIdentifier;
@property (T@"NSString",R,N) itemIdentifier;
@property (T@"NSString",R,N) toolVariant;
@property (T@"PKToolConfiguration",R,N) configuration;
@property (T@"<PKPaletteInkingTool>",R,N) inkingTool;
@property (T@"<PKPaletteErasingTool>",R,N) erasingTool;
@property (T@"<PKPaletteHandwritingTool>",R,N) handwritingTool;
```

## Instance methods

```
-[PKPaletteInkingToolView layoutSubviews];
-[PKPaletteInkingToolView ink];
-[PKPaletteInkingToolView updateConstraints];
-[PKPaletteInkingToolView setScalingFactor:];
-[PKPaletteInkingToolView setInk:];
-[PKPaletteInkingToolView setInkColor:];
-[PKPaletteInkingToolView baseImage];
-[PKPaletteInkingToolView colorIndicatorContourImageRight];
-[PKPaletteInkingToolView setOpacityLabelRightConstraint:];
-[PKPaletteInkingToolView _colorIndicatorImageViewFrame];
-[PKPaletteInkingToolView _displayModeForAttributeViewController];
-[PKPaletteInkingToolView _opacityLabelFont];
-[PKPaletteInkingToolView _opacityLabelTextColor];
-[PKPaletteInkingToolView _reloadToolImage];
-[PKPaletteInkingToolView _setToolProperties:toolIdentifier:];
-[PKPaletteInkingToolView _shouldHaveAttributeViewController];
-[PKPaletteInkingToolView _shouldInstallOpacityLabel];
-[PKPaletteInkingToolView _tintedImage:color:allowHDR:];
-[PKPaletteInkingToolView _toolColorIndicatorContourImageForCurrentEdgeLocation];
-[PKPaletteInkingToolView _toolColorIndicatorImageForCurrentEdgeLocation];
-[PKPaletteInkingToolView _toolTipContourImageForCurrentEdgeLocation];
-[PKPaletteInkingToolView _toolTipImageForCurrentEdgeLocation];
-[PKPaletteInkingToolView _uiColor];
-[PKPaletteInkingToolView _updateOpacityLabel];
-[PKPaletteInkingToolView _updateToolColorBandAndTipImageViews];
-[PKPaletteInkingToolView _updateWantsExtendedDynamicRange];
-[PKPaletteInkingToolView attributeViewController];
-[PKPaletteInkingToolView azimuthImageIndex];
-[PKPaletteInkingToolView colorIndicatorContourImageLeft];
-[PKPaletteInkingToolView colorIndicatorContourImageUp];
-[PKPaletteInkingToolView colorIndicatorContourImageView];
-[PKPaletteInkingToolView colorIndicatorImageLeft];
-[PKPaletteInkingToolView colorIndicatorImageRight];
-[PKPaletteInkingToolView colorIndicatorImageUp];
-[PKPaletteInkingToolView colorIndicatorImageView];
-[PKPaletteInkingToolView initWithToolIdentifier:itemIdentifier:variant:configuration:];
-[PKPaletteInkingToolView initWithToolIdentifier:itemIdentifier:variant:configuration:toolProperties:];
-[PKPaletteInkingToolView inkAttributesPickerDidChangeInkAzimuth:];
-[PKPaletteInkingToolView inkAttributesPickerDidChangeInkOpacity:];
-[PKPaletteInkingToolView inkAttributesPickerDidChangeInkThickness:];
-[PKPaletteInkingToolView opacityLabel];
-[PKPaletteInkingToolView opacityLabelCenterXConstraint];
-[PKPaletteInkingToolView opacityLabelCenterYConstraint];
-[PKPaletteInkingToolView opacityLabelLeftConstraint];
-[PKPaletteInkingToolView opacityLabelRightConstraint];
-[PKPaletteInkingToolView opacityLabelTopConstraint];
-[PKPaletteInkingToolView setAllowHDR:];
-[PKPaletteInkingToolView setColorIndicatorContourImageLeft:];
-[PKPaletteInkingToolView setColorIndicatorContourImageRight:];
-[PKPaletteInkingToolView setColorIndicatorContourImageUp:];
-[PKPaletteInkingToolView setColorIndicatorContourImageView:];
-[PKPaletteInkingToolView setColorIndicatorImageLeft:];
-[PKPaletteInkingToolView setColorIndicatorImageRight:];
-[PKPaletteInkingToolView setColorIndicatorImageUp:];
-[PKPaletteInkingToolView setColorIndicatorImageView:];
-[PKPaletteInkingToolView setEdgeLocation:];
-[PKPaletteInkingToolView setInkAzimuth:];
-[PKPaletteInkingToolView setInkWeight:];
-[PKPaletteInkingToolView setOpacityLabel:];
-[PKPaletteInkingToolView setOpacityLabelCenterXConstraint:];
-[PKPaletteInkingToolView setOpacityLabelCenterYConstraint:];
-[PKPaletteInkingToolView setOpacityLabelLeftConstraint:];
-[PKPaletteInkingToolView setOpacityLabelTopConstraint:];
-[PKPaletteInkingToolView setTipIndicatorContourImageView:];
-[PKPaletteInkingToolView setTipIndicatorImageView:];
-[PKPaletteInkingToolView setToolProperties:];
-[PKPaletteInkingToolView setToolTipContourImageLeft:];
-[PKPaletteInkingToolView setToolTipContourImageRight:];
-[PKPaletteInkingToolView setToolTipContourImageUp:];
-[PKPaletteInkingToolView setToolTipImageLeft:];
-[PKPaletteInkingToolView setToolTipImageRight:];
-[PKPaletteInkingToolView setToolTipImageUp:];
-[PKPaletteInkingToolView tipIndicatorContourImageView];
-[PKPaletteInkingToolView tipIndicatorImageView];
-[PKPaletteInkingToolView toolProperties];
-[PKPaletteInkingToolView toolTipContourImageLeft];
-[PKPaletteInkingToolView toolTipContourImageRight];
-[PKPaletteInkingToolView toolTipContourImageUp];
-[PKPaletteInkingToolView toolTipImageLeft];
-[PKPaletteInkingToolView toolTipImageRight];
-[PKPaletteInkingToolView toolTipImageUp];
```
