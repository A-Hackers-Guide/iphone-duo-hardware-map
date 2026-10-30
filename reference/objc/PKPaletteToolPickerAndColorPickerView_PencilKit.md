# `PKPaletteToolPickerAndColorPickerView`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `PKPaletteEdgeLocating`, `PKPalettePopoverDismissing`, `PKPaletteViewSizeScaling`
- 33 instance variables, 37 properties, 75 instance methods, 0 class methods

## Instance variables

```
@"UIView" _lassoToolEditingViewForNilIdentifier;
@"NSMutableDictionary" _lassoToolEditingViewForIdentifierTable;
B _wantsColorPickerContainerViewInHierarchy;
B _showsPlusButton;
B _lassoToolEditingViewVisible;
B _isSmallestSupportedCompactWidth;
B _inputAssistantViewVisible;
Q _edgeLocation;
Q _cornerLocation;
d _scalingFactor;
@"PKPaletteToolPickerContainerView" _toolPickerContainerView;
@"PKPaletteColorPickerContainerView" _colorPickerContainerView;
@"PKPaletteButton" _plusButton;
@"NSString" _lassoToolEditingViewIdentifier;
@"UIView" _lassoToolEditingView;
@"PKDrawingPaletteInputAssistantView" _paletteInputAssistantView;
q _contextEditingMode;
d _compactPaletteWidth;
@"UIStackView" _stackView;
@"NSLayoutConstraint" _toolPickerContainerViewWidthConstraint;
@"NSLayoutConstraint" _toolPickerContainerViewHeightConstraint;
@"NSLayoutConstraint" _compactToolPickerContainerViewWidthConstraint;
@"NSLayoutConstraint" _compactToolPickerContainerViewHeightConstraint;
@"NSLayoutConstraint" _compactColorPickerContainerViewWidthConstraint;
@"NSLayoutConstraint" _compactColorPickerContainerViewHeightConstraint;
@"UIView" _colorPickerAndPlusView;
@"NSLayoutConstraint" _compactColorPickerAndPlusViewWidthConstraint;
@"NSLayoutConstraint" _compactColorPickerAndPlusViewHeightConstraint;
@"UIView" _lassoToolEditingContainerView;
@"NSLayoutConstraint" _lassoToolEditingContainerViewWidthConstraint;
@"NSLayoutConstraint" _lassoToolEditingContainerViewHeightConstraint;
@"NSLayoutConstraint" _lassoToolEditingContainerViewCompactWidthConstraint;
@"NSLayoutConstraint" _lassoToolEditingContainerViewCompactHeightConstraint;
```

## Properties

```
@property (T@"UIStackView",&,N,V_stackView) stackView;
@property (T@"PKPaletteToolPickerContainerView",&,N,V_toolPickerContainerView) toolPickerContainerView;
@property (T@"PKPaletteColorPickerContainerView",&,N,V_colorPickerContainerView) colorPickerContainerView;
@property (T@"NSLayoutConstraint",&,N,V_toolPickerContainerViewWidthConstraint) toolPickerContainerViewWidthConstraint;
@property (T@"NSLayoutConstraint",&,N,V_toolPickerContainerViewHeightConstraint) toolPickerContainerViewHeightConstraint;
@property (T@"NSLayoutConstraint",&,N,V_compactToolPickerContainerViewWidthConstraint) compactToolPickerContainerViewWidthConstraint;
@property (T@"NSLayoutConstraint",&,N,V_compactToolPickerContainerViewHeightConstraint) compactToolPickerContainerViewHeightConstraint;
@property (T@"NSLayoutConstraint",&,N,V_compactColorPickerContainerViewWidthConstraint) compactColorPickerContainerViewWidthConstraint;
@property (T@"NSLayoutConstraint",&,N,V_compactColorPickerContainerViewHeightConstraint) compactColorPickerContainerViewHeightConstraint;
@property (T@"UIView",&,N,V_colorPickerAndPlusView) colorPickerAndPlusView;
@property (T@"NSLayoutConstraint",&,N,V_compactColorPickerAndPlusViewWidthConstraint) compactColorPickerAndPlusViewWidthConstraint;
@property (T@"NSLayoutConstraint",&,N,V_compactColorPickerAndPlusViewHeightConstraint) compactColorPickerAndPlusViewHeightConstraint;
@property (T@"UIView",&,N,V_lassoToolEditingContainerView) lassoToolEditingContainerView;
@property (T@"NSLayoutConstraint",&,N,V_lassoToolEditingContainerViewWidthConstraint) lassoToolEditingContainerViewWidthConstraint;
@property (T@"NSLayoutConstraint",&,N,V_lassoToolEditingContainerViewHeightConstraint) lassoToolEditingContainerViewHeightConstraint;
@property (T@"NSLayoutConstraint",&,N,V_lassoToolEditingContainerViewCompactWidthConstraint) lassoToolEditingContainerViewCompactWidthConstraint;
@property (T@"NSLayoutConstraint",&,N,V_lassoToolEditingContainerViewCompactHeightConstraint) lassoToolEditingContainerViewCompactHeightConstraint;
@property (T@"PKPaletteToolPickerView",R,N) toolPickerView;
@property (T@"PKPaletteColorPickerView",R,N) colorPickerView;
@property (TB,N,V_wantsColorPickerContainerViewInHierarchy) wantsColorPickerContainerViewInHierarchy;
@property (TB,N,V_showsPlusButton) showsPlusButton;
@property (T@"PKPaletteButton",&,N,V_plusButton) plusButton;
@property (T@"NSString",C,N,V_lassoToolEditingViewIdentifier) lassoToolEditingViewIdentifier;
@property (T@"UIView",R,N,V_lassoToolEditingView) lassoToolEditingView;
@property (TB,N,GisLassoToolEditingViewVisible,V_lassoToolEditingViewVisible) lassoToolEditingViewVisible;
@property (T@"PKDrawingPaletteInputAssistantView",R,N,V_paletteInputAssistantView) paletteInputAssistantView;
@property (Tq,N,V_contextEditingMode) contextEditingMode;
@property (TB,N,V_isSmallestSupportedCompactWidth) isSmallestSupportedCompactWidth;
@property (TB,N,GisInputAssistantViewVisible,V_inputAssistantViewVisible) inputAssistantViewVisible;
@property (Td,N,V_compactPaletteWidth) compactPaletteWidth;
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
-[PKPaletteToolPickerAndColorPickerView scalingFactor];
-[PKPaletteToolPickerAndColorPickerView init];
-[PKPaletteToolPickerAndColorPickerView layoutSubviews];
-[PKPaletteToolPickerAndColorPickerView hitTest:withEvent:];
-[PKPaletteToolPickerAndColorPickerView stackView];
-[PKPaletteToolPickerAndColorPickerView setScalingFactor:];
-[PKPaletteToolPickerAndColorPickerView setStackView:];
-[PKPaletteToolPickerAndColorPickerView traitCollectionDidChange:];
-[PKPaletteToolPickerAndColorPickerView _updateUI];
-[PKPaletteToolPickerAndColorPickerView dismissPalettePopoverWithCompletion:];
-[PKPaletteToolPickerAndColorPickerView plusButton];
-[PKPaletteToolPickerAndColorPickerView setPlusButton:];
-[PKPaletteToolPickerAndColorPickerView setLassoToolEditingViewVisible:];
-[PKPaletteToolPickerAndColorPickerView showsPlusButton];
-[PKPaletteToolPickerAndColorPickerView colorPickerView];
-[PKPaletteToolPickerAndColorPickerView isSmallestSupportedCompactWidth];
-[PKPaletteToolPickerAndColorPickerView _compactToolsContainerMaximumWidth];
-[PKPaletteToolPickerAndColorPickerView _compactToolsContainerWidth];
-[PKPaletteToolPickerAndColorPickerView _hasColorPickerContainerView];
-[PKPaletteToolPickerAndColorPickerView _hasPlusButtonView];
-[PKPaletteToolPickerAndColorPickerView _stackViewSpacing];
-[PKPaletteToolPickerAndColorPickerView colorPickerAndPlusView];
-[PKPaletteToolPickerAndColorPickerView colorPickerContainerView];
-[PKPaletteToolPickerAndColorPickerView compactColorPickerAndPlusViewHeightConstraint];
-[PKPaletteToolPickerAndColorPickerView compactColorPickerAndPlusViewWidthConstraint];
-[PKPaletteToolPickerAndColorPickerView compactColorPickerContainerViewHeightConstraint];
-[PKPaletteToolPickerAndColorPickerView compactColorPickerContainerViewWidthConstraint];
-[PKPaletteToolPickerAndColorPickerView compactPaletteWidth];
-[PKPaletteToolPickerAndColorPickerView compactToolPickerContainerViewHeightConstraint];
-[PKPaletteToolPickerAndColorPickerView compactToolPickerContainerViewWidthConstraint];
-[PKPaletteToolPickerAndColorPickerView contextEditingMode];
-[PKPaletteToolPickerAndColorPickerView cornerLocation];
-[PKPaletteToolPickerAndColorPickerView edgeLocation];
-[PKPaletteToolPickerAndColorPickerView isInputAssistantViewVisible];
-[PKPaletteToolPickerAndColorPickerView isLassoToolEditingViewVisible];
-[PKPaletteToolPickerAndColorPickerView lassoToolEditingContainerView];
-[PKPaletteToolPickerAndColorPickerView lassoToolEditingContainerViewCompactHeightConstraint];
-[PKPaletteToolPickerAndColorPickerView lassoToolEditingContainerViewCompactWidthConstraint];
-[PKPaletteToolPickerAndColorPickerView lassoToolEditingContainerViewHeightConstraint];
-[PKPaletteToolPickerAndColorPickerView lassoToolEditingContainerViewWidthConstraint];
-[PKPaletteToolPickerAndColorPickerView lassoToolEditingView];
-[PKPaletteToolPickerAndColorPickerView lassoToolEditingViewIdentifier];
-[PKPaletteToolPickerAndColorPickerView paletteInputAssistantView];
-[PKPaletteToolPickerAndColorPickerView setColorPickerAndPlusView:];
-[PKPaletteToolPickerAndColorPickerView setColorPickerContainerView:];
-[PKPaletteToolPickerAndColorPickerView setCompactColorPickerAndPlusViewHeightConstraint:];
-[PKPaletteToolPickerAndColorPickerView setCompactColorPickerAndPlusViewWidthConstraint:];
-[PKPaletteToolPickerAndColorPickerView setCompactColorPickerContainerViewHeightConstraint:];
-[PKPaletteToolPickerAndColorPickerView setCompactColorPickerContainerViewWidthConstraint:];
-[PKPaletteToolPickerAndColorPickerView setCompactPaletteWidth:];
-[PKPaletteToolPickerAndColorPickerView setCompactToolPickerContainerViewHeightConstraint:];
-[PKPaletteToolPickerAndColorPickerView setCompactToolPickerContainerViewWidthConstraint:];
-[PKPaletteToolPickerAndColorPickerView setContextEditingMode:];
-[PKPaletteToolPickerAndColorPickerView setCornerLocation:];
-[PKPaletteToolPickerAndColorPickerView setEdgeLocation:];
-[PKPaletteToolPickerAndColorPickerView setInputAssistantViewVisible:];
-[PKPaletteToolPickerAndColorPickerView setIsSmallestSupportedCompactWidth:];
-[PKPaletteToolPickerAndColorPickerView setLassoToolEditingContainerView:];
-[PKPaletteToolPickerAndColorPickerView setLassoToolEditingContainerViewCompactHeightConstraint:];
-[PKPaletteToolPickerAndColorPickerView setLassoToolEditingContainerViewCompactWidthConstraint:];
-[PKPaletteToolPickerAndColorPickerView setLassoToolEditingContainerViewHeightConstraint:];
-[PKPaletteToolPickerAndColorPickerView setLassoToolEditingContainerViewWidthConstraint:];
-[PKPaletteToolPickerAndColorPickerView setLassoToolEditingViewIdentifier:];
-[PKPaletteToolPickerAndColorPickerView setShowsPlusButton:];
-[PKPaletteToolPickerAndColorPickerView setToolPickerContainerView:];
-[PKPaletteToolPickerAndColorPickerView setToolPickerContainerViewHeightConstraint:];
-[PKPaletteToolPickerAndColorPickerView setToolPickerContainerViewWidthConstraint:];
-[PKPaletteToolPickerAndColorPickerView setWantsColorPickerContainerViewInHierarchy:];
-[PKPaletteToolPickerAndColorPickerView shouldShowPlusButton];
-[PKPaletteToolPickerAndColorPickerView toolPickerContainerView];
-[PKPaletteToolPickerAndColorPickerView toolPickerContainerViewHeightConstraint];
-[PKPaletteToolPickerAndColorPickerView toolPickerContainerViewWidthConstraint];
-[PKPaletteToolPickerAndColorPickerView toolPickerView];
-[PKPaletteToolPickerAndColorPickerView updateColorPickerAndPlusView:];
-[PKPaletteToolPickerAndColorPickerView wantsColorPickerContainerViewInHierarchy];
```
