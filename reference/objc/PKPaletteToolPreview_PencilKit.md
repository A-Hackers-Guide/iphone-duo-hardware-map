# `PKPaletteToolPreview`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `UIPopoverPresentationControllerDelegate`, `PKPaletteColorPickerControllerDelegate`, `PKPaletteEdgeLocating`, `PKPalettePopoverDismissing`, `PKPaletteViewSizeScaling`
- 17 instance variables, 23 properties, 55 instance methods, 0 class methods

## Instance variables

```
B _allowHDR;
B _toolViewVisible;
Q _edgeLocation;
Q _cornerLocation;
d _scalingFactor;
@"<PKPalettePopoverPresenting><PKPaletteToolPreviewDelegate>" _delegate;
q _colorAppearance;
@"NSString" _localeIdentifier;
@"PKPaletteToolView" _toolView;
@"<PKPaletteColorPickerController>" _colorPickerController;
@"NSLayoutConstraint" _toolViewTopAnchor;
@"NSLayoutConstraint" _toolViewHeightAnchor;
@"UILayoutGuide" _layoutGuide;
@"NSLayoutConstraint" _layoutGuideTopConstraint;
@"NSLayoutConstraint" _layoutGuideWidthConstraint;
@"NSLayoutConstraint" _layoutGuideHeightConstraint;
@"NSLayoutConstraint" _layoutGuideCenterXConstraint;
```

## Properties

```
@property (T@"PKPaletteToolView",&,N,V_toolView) toolView;
@property (T@"<PKPaletteColorPickerController>",&,N,V_colorPickerController) colorPickerController;
@property (T@"NSLayoutConstraint",&,N,V_toolViewTopAnchor) toolViewTopAnchor;
@property (T@"NSLayoutConstraint",&,N,V_toolViewHeightAnchor) toolViewHeightAnchor;
@property (T@"UILayoutGuide",&,N,V_layoutGuide) layoutGuide;
@property (T@"NSLayoutConstraint",&,N,V_layoutGuideTopConstraint) layoutGuideTopConstraint;
@property (T@"NSLayoutConstraint",&,N,V_layoutGuideWidthConstraint) layoutGuideWidthConstraint;
@property (T@"NSLayoutConstraint",&,N,V_layoutGuideHeightConstraint) layoutGuideHeightConstraint;
@property (T@"NSLayoutConstraint",&,N,V_layoutGuideCenterXConstraint) layoutGuideCenterXConstraint;
@property (TB,N,GisToolViewVisible,V_toolViewVisible) toolViewVisible;
@property (T@"<PKPalettePopoverPresenting><PKPaletteToolPreviewDelegate>",W,N,V_delegate) delegate;
@property (Tq,N,V_colorAppearance) colorAppearance;
@property (T@"NSString",C,N,V_localeIdentifier) localeIdentifier;
@property (T@"NSString",R,N) itemIdentifier;
@property (T@"UIColor",R,N) toolColor;
@property (TB,N,V_allowHDR) allowHDR;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TQ,N,V_edgeLocation) edgeLocation;
@property (TQ,N,V_cornerLocation) cornerLocation;
@property (Td,N,V_scalingFactor) scalingFactor;
```

## Instance methods

```
-[PKPaletteToolPreview setLocaleIdentifier:];
-[PKPaletteToolPreview adaptivePresentationStyleForPresentationController:traitCollection:];
-[PKPaletteToolPreview adaptivePresentationStyleForPresentationController:];
-[PKPaletteToolPreview setLayoutGuide:];
-[PKPaletteToolPreview localeIdentifier];
-[PKPaletteToolPreview layoutGuide];
-[PKPaletteToolPreview scalingFactor];
-[PKPaletteToolPreview setDelegate:];
-[PKPaletteToolPreview delegate];
-[PKPaletteToolPreview updateConstraints];
-[PKPaletteToolPreview setScalingFactor:];
-[PKPaletteToolPreview _updateLayoutGuideConstraints];
-[PKPaletteToolPreview _updateUI];
-[PKPaletteToolPreview itemIdentifier];
-[PKPaletteToolPreview initWithFrame:];
-[PKPaletteToolPreview dismissPalettePopoverWithCompletion:];
-[PKPaletteToolPreview colorPickerController];
-[PKPaletteToolPreview setColorPickerController:];
-[PKPaletteToolPreview colorAppearance];
-[PKPaletteToolPreview setLayoutGuideHeightConstraint:];
-[PKPaletteToolPreview _animateToolViewToVisible:completion:];
-[PKPaletteToolPreview _popoverPresentingSourceRect];
-[PKPaletteToolPreview _popoverPresentingSourceView];
-[PKPaletteToolPreview _replaceCurrentToolWithTool:];
-[PKPaletteToolPreview _showColorSelectionPopover];
-[PKPaletteToolPreview _toolViewTopSpacing];
-[PKPaletteToolPreview _updateToolViewInkingToolAttributesFromTool:];
-[PKPaletteToolPreview allowHDR];
-[PKPaletteToolPreview colorPickerControllerDidChangeSelectedColor:isContinuousColorSelection:];
-[PKPaletteToolPreview cornerLocation];
-[PKPaletteToolPreview edgeLocation];
-[PKPaletteToolPreview flashAlternatePreviewView:];
-[PKPaletteToolPreview isToolViewVisible];
-[PKPaletteToolPreview layoutGuideCenterXConstraint];
-[PKPaletteToolPreview layoutGuideHeightConstraint];
-[PKPaletteToolPreview layoutGuideTopConstraint];
-[PKPaletteToolPreview layoutGuideWidthConstraint];
-[PKPaletteToolPreview setAllowHDR:];
-[PKPaletteToolPreview setColorAppearance:];
-[PKPaletteToolPreview setCornerLocation:];
-[PKPaletteToolPreview setEdgeLocation:];
-[PKPaletteToolPreview setLayoutGuideCenterXConstraint:];
-[PKPaletteToolPreview setLayoutGuideTopConstraint:];
-[PKPaletteToolPreview setLayoutGuideWidthConstraint:];
-[PKPaletteToolPreview setToolImageNeedsReload];
-[PKPaletteToolPreview setToolView:];
-[PKPaletteToolPreview setToolViewHeightAnchor:];
-[PKPaletteToolPreview setToolViewTopAnchor:];
-[PKPaletteToolPreview setToolViewVisible:];
-[PKPaletteToolPreview showPreviewForTool:animated:];
-[PKPaletteToolPreview toggleColorSelectionPopover];
-[PKPaletteToolPreview toolColor];
-[PKPaletteToolPreview toolView];
-[PKPaletteToolPreview toolViewHeightAnchor];
-[PKPaletteToolPreview toolViewTopAnchor];
```
