# `PKPaletteHandwritingToolView`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PKPaletteToolView`
- Protocols: `PKPaletteHandwritingTool`
- 6 instance variables, 17 properties, 21 instance methods, 0 class methods

## Instance variables

```
B _needsUpdateTitleLabel;
@"NSString" _localeIdentifier;
@"UILabel" _toolLabel;
@"NSLayoutConstraint" _toolLabelCenterXConstraint;
@"NSLayoutConstraint" _toolLabelCenterYConstraint;
@? __overrideLabelCenterOffsetYHandler;
```

## Properties

```
@property (T@"UILabel",&,N,V_toolLabel) toolLabel;
@property (T@"NSLayoutConstraint",&,N,V_toolLabelCenterXConstraint) toolLabelCenterXConstraint;
@property (T@"NSLayoutConstraint",&,N,V_toolLabelCenterYConstraint) toolLabelCenterYConstraint;
@property (TB,N,V_needsUpdateTitleLabel) needsUpdateTitleLabel;
@property (T@?,C,N,S_setOverrideLabelCenterOffsetYHandler:,V__overrideLabelCenterOffsetYHandler) _overrideLabelCenterOffsetYHandler;
@property (T@"NSString",C,N,V_localeIdentifier) localeIdentifier;
@property (T@"NSString",R,N) toolIdentifier;
@property (T@"NSString",R,N) itemIdentifier;
@property (T@"NSString",R,N) toolVariant;
@property (T@"PKToolConfiguration",R,N) configuration;
@property (T@"<PKPaletteInkingTool>",R,N) inkingTool;
@property (T@"<PKPaletteErasingTool>",R,N) erasingTool;
@property (T@"<PKPaletteHandwritingTool>",R,N) handwritingTool;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[PKPaletteHandwritingToolView setLocaleIdentifier:];
-[PKPaletteHandwritingToolView localeIdentifier];
-[PKPaletteHandwritingToolView init];
-[PKPaletteHandwritingToolView updateConstraints];
-[PKPaletteHandwritingToolView setScalingFactor:];
-[PKPaletteHandwritingToolView _updateUI];
-[PKPaletteHandwritingToolView _overrideLabelCenterOffsetYHandler];
-[PKPaletteHandwritingToolView _setOverrideLabelCenterOffsetYHandler:];
-[PKPaletteHandwritingToolView _toolLabelCenterOffset];
-[PKPaletteHandwritingToolView _toolLabelImageViewTransform];
-[PKPaletteHandwritingToolView _toolLabelText];
-[PKPaletteHandwritingToolView initWithToolIdentifier:itemIdentifier:variant:configuration:];
-[PKPaletteHandwritingToolView needsUpdateTitleLabel];
-[PKPaletteHandwritingToolView setEdgeLocation:];
-[PKPaletteHandwritingToolView setNeedsUpdateTitleLabel:];
-[PKPaletteHandwritingToolView setToolLabel:];
-[PKPaletteHandwritingToolView setToolLabelCenterXConstraint:];
-[PKPaletteHandwritingToolView setToolLabelCenterYConstraint:];
-[PKPaletteHandwritingToolView toolLabel];
-[PKPaletteHandwritingToolView toolLabelCenterXConstraint];
-[PKPaletteHandwritingToolView toolLabelCenterYConstraint];
```
