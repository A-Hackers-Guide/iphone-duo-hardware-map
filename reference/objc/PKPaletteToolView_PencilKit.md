# `PKPaletteToolView`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIControl`
- Protocols: `PKPaletteTool`, `PKPaletteEdgeLocating`, `PKPaletteViewSizeScaling`, `UIPointerInteractionDelegate`
- 28 instance variables, 37 properties, 82 instance methods, 1 class methods

## Instance variables

```
B _allowHDR;
B _supportsDisplayingSelectedColor;
B _selectedToolOffsetEnabled;
B _toolImageNeedsReload;
@"PKPaletteAttributeViewController" _attributeViewController;
@"NSString" _toolIdentifier;
@"NSString" _itemIdentifier;
@"NSString" _toolVariant;
Q _edgeLocation;
Q _cornerLocation;
d _scalingFactor;
@"NSDictionary" _toolProperties;
q _colorAppearance;
@"PKToolConfiguration" _configuration;
@"UIPointerInteraction" _pointerInteraction;
@"PKPaletteToolImageContentView" _imageContentView;
@"PKPaletteToolShadowPathView" _toolShadowView;
@"NSLayoutConstraint" _toolShadowViewTopAnchorConstraint;
@"NSLayoutConstraint" _toolShadowViewLeftAnchorConstraint;
@"NSLayoutConstraint" _toolShadowViewBottomAnchorConstraint;
@"NSLayoutConstraint" _toolShadowViewRightAnchorConstraint;
@"NSLayoutConstraint" _imageViewTopAnchorConstraint;
@"NSLayoutConstraint" _imageViewBottomAnchorConstraint;
@"NSLayoutConstraint" _imageViewLeftAnchorConstraint;
@"NSLayoutConstraint" _imageViewRightAnchorConstraint;
@"NSLayoutConstraint" _imageViewWidthAnchorConstraint;
@"NSLayoutConstraint" _imageViewHeightAnchorConstraint;
{CGSize="width"d"height"d} _lastRemoteEffectsBoundsSize;
```

## Properties

```
@property (T@"NSLayoutConstraint",&,N,V_toolShadowViewTopAnchorConstraint) toolShadowViewTopAnchorConstraint;
@property (T@"NSLayoutConstraint",&,N,V_toolShadowViewLeftAnchorConstraint) toolShadowViewLeftAnchorConstraint;
@property (T@"NSLayoutConstraint",&,N,V_toolShadowViewBottomAnchorConstraint) toolShadowViewBottomAnchorConstraint;
@property (T@"NSLayoutConstraint",&,N,V_toolShadowViewRightAnchorConstraint) toolShadowViewRightAnchorConstraint;
@property (T@"NSLayoutConstraint",&,N,V_imageViewTopAnchorConstraint) imageViewTopAnchorConstraint;
@property (T@"NSLayoutConstraint",&,N,V_imageViewBottomAnchorConstraint) imageViewBottomAnchorConstraint;
@property (T@"NSLayoutConstraint",&,N,V_imageViewLeftAnchorConstraint) imageViewLeftAnchorConstraint;
@property (T@"NSLayoutConstraint",&,N,V_imageViewRightAnchorConstraint) imageViewRightAnchorConstraint;
@property (T@"NSLayoutConstraint",&,N,V_imageViewWidthAnchorConstraint) imageViewWidthAnchorConstraint;
@property (T@"NSLayoutConstraint",&,N,V_imageViewHeightAnchorConstraint) imageViewHeightAnchorConstraint;
@property (T{CGSize=dd},N,V_lastRemoteEffectsBoundsSize) lastRemoteEffectsBoundsSize;
@property (T@"<PKPaletteTool>",R,N) tool;
@property (TB,N,V_allowHDR) allowHDR;
@property (T@"PKPaletteAttributeViewController",R,N,V_attributeViewController) attributeViewController;
@property (T@"NSString",R,N) toolName;
@property (T@"NSDictionary",C,N,V_toolProperties) toolProperties;
@property (Tq,N,V_colorAppearance) colorAppearance;
@property (TB,N,V_supportsDisplayingSelectedColor) supportsDisplayingSelectedColor;
@property (T@"PKToolConfiguration",C,N,V_configuration) configuration;
@property (T@"UIPointerInteraction",&,N,V_pointerInteraction) pointerInteraction;
@property (T@"PKPaletteToolImageContentView",R,N,V_imageContentView) imageContentView;
@property (T@"PKPaletteToolShadowPathView",&,N,V_toolShadowView) toolShadowView;
@property (TB,N,V_selectedToolOffsetEnabled) selectedToolOffsetEnabled;
@property (TB,R,N,V_toolImageNeedsReload) toolImageNeedsReload;
@property (T@"NSString",R,N,V_toolIdentifier) toolIdentifier;
@property (T@"NSString",R,N,V_itemIdentifier) itemIdentifier;
@property (T@"NSString",R,N,V_toolVariant) toolVariant;
@property (T@"<PKPaletteInkingTool>",R,N) inkingTool;
@property (T@"<PKPaletteErasingTool>",R,N) erasingTool;
@property (T@"<PKPaletteHandwritingTool>",R,N) handwritingTool;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TQ,N,V_edgeLocation) edgeLocation;
@property (TQ,N,V_cornerLocation) cornerLocation;
@property (Td,N,V_scalingFactor) scalingFactor;
```

## Class methods

```
+[PKPaletteToolView toolViewWithToolIdentifier:itemIdentifier:variant:configuration:];
```

## Instance methods

```
-[PKPaletteToolView setPointerInteraction:];
-[PKPaletteToolView setSelected:];
-[PKPaletteToolView intrinsicContentSize];
-[PKPaletteToolView pointerInteraction:styleForRegion:];
-[PKPaletteToolView scalingFactor];
-[PKPaletteToolView pointerInteraction:willEnterRegion:animator:];
-[PKPaletteToolView pointerInteraction:willExitRegion:animator:];
-[PKPaletteToolView setConfiguration:];
-[PKPaletteToolView layoutSubviews];
-[PKPaletteToolView setHighlighted:];
-[PKPaletteToolView configuration];
-[PKPaletteToolView pointerInteraction];
-[PKPaletteToolView pointerInteraction:regionForRequest:defaultRegion:];
-[PKPaletteToolView updateConstraints];
-[PKPaletteToolView setScalingFactor:];
-[PKPaletteToolView traitCollectionDidChange:];
-[PKPaletteToolView tool];
-[PKPaletteToolView itemIdentifier];
-[PKPaletteToolView imageContentView];
-[PKPaletteToolView toolIdentifier];
-[PKPaletteToolView baseImage];
-[PKPaletteToolView toolName];
-[PKPaletteToolView _reloadToolImageSizeConstraints];
-[PKPaletteToolView imageViewBottomAnchorConstraint];
-[PKPaletteToolView imageViewHeightAnchorConstraint];
-[PKPaletteToolView supportsDisplayingSelectedColor];
-[PKPaletteToolView colorAppearance];
-[PKPaletteToolView handwritingTool];
-[PKPaletteToolView setLastRemoteEffectsBoundsSize:];
-[PKPaletteToolView _reloadToolImage];
-[PKPaletteToolView _setToolImageNeedsReload];
-[PKPaletteToolView _toolSelectedOffset];
-[PKPaletteToolView _updateRemoteEffects];
-[PKPaletteToolView _updateToolShadowView];
-[PKPaletteToolView allowHDR];
-[PKPaletteToolView attributeViewController];
-[PKPaletteToolView cornerLocation];
-[PKPaletteToolView edgeLocation];
-[PKPaletteToolView erasingTool];
-[PKPaletteToolView imageViewLeftAnchorConstraint];
-[PKPaletteToolView imageViewRightAnchorConstraint];
-[PKPaletteToolView imageViewTopAnchorConstraint];
-[PKPaletteToolView imageViewWidthAnchorConstraint];
-[PKPaletteToolView initWithToolIdentifier:itemIdentifier:configuration:toolProperties:];
-[PKPaletteToolView initWithToolIdentifier:itemIdentifier:variant:configuration:];
-[PKPaletteToolView inkingTool];
-[PKPaletteToolView isCustomTool];
-[PKPaletteToolView isErasingTool];
-[PKPaletteToolView isGenerationTool];
-[PKPaletteToolView isHandwritingTool];
-[PKPaletteToolView isInkingTool];
-[PKPaletteToolView isLassoTool];
-[PKPaletteToolView isRulerTool];
-[PKPaletteToolView lastRemoteEffectsBoundsSize];
-[PKPaletteToolView selectedToolOffsetEnabled];
-[PKPaletteToolView setAllowHDR:];
-[PKPaletteToolView setColorAppearance:];
-[PKPaletteToolView setCornerLocation:];
-[PKPaletteToolView setEdgeLocation:];
-[PKPaletteToolView setImageViewBottomAnchorConstraint:];
-[PKPaletteToolView setImageViewHeightAnchorConstraint:];
-[PKPaletteToolView setImageViewLeftAnchorConstraint:];
-[PKPaletteToolView setImageViewRightAnchorConstraint:];
-[PKPaletteToolView setImageViewTopAnchorConstraint:];
-[PKPaletteToolView setImageViewWidthAnchorConstraint:];
-[PKPaletteToolView setSelectedToolOffsetEnabled:];
-[PKPaletteToolView setSupportsDisplayingSelectedColor:];
-[PKPaletteToolView setToolProperties:];
-[PKPaletteToolView setToolShadowView:];
-[PKPaletteToolView setToolShadowViewBottomAnchorConstraint:];
-[PKPaletteToolView setToolShadowViewLeftAnchorConstraint:];
-[PKPaletteToolView setToolShadowViewRightAnchorConstraint:];
-[PKPaletteToolView setToolShadowViewTopAnchorConstraint:];
-[PKPaletteToolView showTooltip:];
-[PKPaletteToolView toolImageNeedsReload];
-[PKPaletteToolView toolProperties];
-[PKPaletteToolView toolShadowView];
-[PKPaletteToolView toolShadowViewBottomAnchorConstraint];
-[PKPaletteToolView toolShadowViewLeftAnchorConstraint];
-[PKPaletteToolView toolShadowViewRightAnchorConstraint];
-[PKPaletteToolView toolShadowViewTopAnchorConstraint];
-[PKPaletteToolView toolVariant];
```
