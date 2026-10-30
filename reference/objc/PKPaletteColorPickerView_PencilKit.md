# `PKPaletteColorPickerView`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `UICollectionViewDataSource`, `UICollectionViewDelegateFlowLayout`, `UICollectionViewDelegate`, `UIPopoverPresentationControllerDelegate`, `UIGestureRecognizerDelegate`, `PKPaletteColorPickerControllerDelegate`, `PKPaletteEdgeLocating`, `PKPaletteQuickColorPicking`, `PKPalettePopoverUpdating`, `PKPalettePopoverDismissing`, `PKPaletteViewSizeScaling`, `UIPointerInteractionDelegate`
- 17 instance variables, 23 properties, 74 instance methods, 1 class methods

## Instance variables

```
B _supportsAlpha;
Q _edgeLocation;
Q _cornerLocation;
d _scalingFactor;
@"<PKPalettePopoverPresenting><PKPaletteColorPickerViewDelegate>" _delegate;
q _colorAppearance;
@"PKPaletteMulticolorSwatch" _multicolorSwatch;
q _colorPickerMode;
d _colorMaximumLinearExposure;
@"UICollectionView" _collectionView;
@"NSArray" _swatches;
@"NSArray" _swatchColors;
@"UILongPressGestureRecognizer" _longPressGestureRecognizer;
@"<PKPaletteColorPickerController>" _colorPickerController;
@"UIColor" _analyticsInitialColor;
q _analyticsColorChangeCount;
d _selectedColorAlpha;
```

## Properties

```
@property (T@"UICollectionView",&,N,V_collectionView) collectionView;
@property (T@"NSArray",&,N,V_swatches) swatches;
@property (T@"PKPaletteMulticolorSwatch",&,N,V_multicolorSwatch) multicolorSwatch;
@property (T@"NSArray",&,N,V_swatchColors) swatchColors;
@property (T@"UILongPressGestureRecognizer",&,N,V_longPressGestureRecognizer) longPressGestureRecognizer;
@property (T@"<PKPaletteColorPickerController>",&,N,V_colorPickerController) colorPickerController;
@property (T@"UIColor",&,N,V_analyticsInitialColor) analyticsInitialColor;
@property (Tq,N,V_analyticsColorChangeCount) analyticsColorChangeCount;
@property (Td,N,V_selectedColorAlpha) selectedColorAlpha;
@property (T@"<PKPalettePopoverPresenting><PKPaletteColorPickerViewDelegate>",W,N,V_delegate) delegate;
@property (Tq,N,V_colorAppearance) colorAppearance;
@property (T@"UIColor",&,N) selectedColor;
@property (TB,N,V_supportsAlpha) supportsAlpha;
@property (Tq,N,V_colorPickerMode) colorPickerMode;
@property (Td,N,V_colorMaximumLinearExposure) colorMaximumLinearExposure;
@property (TB,R,N,G_isExtendedColorPickerVisible) extendedColorPickerVisible;
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
+[PKPaletteColorPickerView collectionViewFlowLayoutWithItemSize:minimumLineSpacing:minimumInterItemSpacing:];
```

## Instance methods

```
-[PKPaletteColorPickerView adaptivePresentationStyleForPresentationController:traitCollection:];
-[PKPaletteColorPickerView collectionView:didHighlightItemAtIndexPath:];
-[PKPaletteColorPickerView collectionView:didUnhighlightItemAtIndexPath:];
-[PKPaletteColorPickerView intrinsicContentSize];
-[PKPaletteColorPickerView longPressGestureRecognizer];
-[PKPaletteColorPickerView collectionView:numberOfItemsInSection:];
-[PKPaletteColorPickerView scalingFactor];
-[PKPaletteColorPickerView collectionView:didSelectItemAtIndexPath:];
-[PKPaletteColorPickerView collectionView:cellForItemAtIndexPath:];
-[PKPaletteColorPickerView dealloc];
-[PKPaletteColorPickerView collectionView];
-[PKPaletteColorPickerView setCollectionView:];
-[PKPaletteColorPickerView setDelegate:];
-[PKPaletteColorPickerView gestureRecognizer:shouldRecognizeSimultaneouslyWithGestureRecognizer:];
-[PKPaletteColorPickerView delegate];
-[PKPaletteColorPickerView setScalingFactor:];
-[PKPaletteColorPickerView traitCollectionDidChange:];
-[PKPaletteColorPickerView didChangePreferredContentSize:];
-[PKPaletteColorPickerView setLongPressGestureRecognizer:];
-[PKPaletteColorPickerView _updateUI];
-[PKPaletteColorPickerView initWithFrame:];
-[PKPaletteColorPickerView selectedColor];
-[PKPaletteColorPickerView setSelectedColor:];
-[PKPaletteColorPickerView setSupportsAlpha:];
-[PKPaletteColorPickerView supportsAlpha];
-[PKPaletteColorPickerView dismissPalettePopoverWithCompletion:];
-[PKPaletteColorPickerView colorPickerController];
-[PKPaletteColorPickerView setColorPickerController:];
-[PKPaletteColorPickerView _selectedSwatch];
-[PKPaletteColorPickerView colorPickerMode];
-[PKPaletteColorPickerView colorAppearance];
-[PKPaletteColorPickerView updatePopoverUI];
-[PKPaletteColorPickerView _colorPickerAllowsColorSelection];
-[PKPaletteColorPickerView _enableOrDisableLongPressGesture];
-[PKPaletteColorPickerView _isExtendedColorPickerVisible];
-[PKPaletteColorPickerView _multicolorSwatchIndexForEdge:];
-[PKPaletteColorPickerView _popoverPresentingSourceRect];
-[PKPaletteColorPickerView _popoverPresentingSourceView];
-[PKPaletteColorPickerView _rebuildSwatches];
-[PKPaletteColorPickerView _reloadSwatchColorsForTraitCollection:];
-[PKPaletteColorPickerView _setMulticolorSwatchColor:];
-[PKPaletteColorPickerView _shouldDisplayExtendedColorPickerPopoverFromColorSwatch:];
-[PKPaletteColorPickerView _showExtendedColorPicker];
-[PKPaletteColorPickerView _swatchColorsForTraitCollection:];
-[PKPaletteColorPickerView _swatchLongPressHandler:];
-[PKPaletteColorPickerView analyticsColorChangeCount];
-[PKPaletteColorPickerView analyticsInitialColor];
-[PKPaletteColorPickerView colorAtPoint:];
-[PKPaletteColorPickerView colorMaximumLinearExposure];
-[PKPaletteColorPickerView colorPickerControllerDidChangeSelectedColor:isContinuousColorSelection:];
-[PKPaletteColorPickerView cornerLocation];
-[PKPaletteColorPickerView dismissEyeDropper];
-[PKPaletteColorPickerView edgeLocation];
-[PKPaletteColorPickerView multicolorSwatch];
-[PKPaletteColorPickerView reloadColorsForCurrentColorPickerMode];
-[PKPaletteColorPickerView selectedColorAlpha];
-[PKPaletteColorPickerView setAnalyticsColorChangeCount:];
-[PKPaletteColorPickerView setAnalyticsInitialColor:];
-[PKPaletteColorPickerView setColorAppearance:];
-[PKPaletteColorPickerView setColorMaximumLinearExposure:];
-[PKPaletteColorPickerView setColorPickerMode:];
-[PKPaletteColorPickerView setCornerLocation:];
-[PKPaletteColorPickerView setEdgeLocation:];
-[PKPaletteColorPickerView setMulticolorSwatch:];
-[PKPaletteColorPickerView setSelectedColorAlpha:];
-[PKPaletteColorPickerView setSwatchColors:];
-[PKPaletteColorPickerView setSwatches:];
-[PKPaletteColorPickerView swatchColors];
-[PKPaletteColorPickerView swatchSize];
-[PKPaletteColorPickerView swatchWithColor:];
-[PKPaletteColorPickerView swatchWithIdentifier:];
-[PKPaletteColorPickerView swatches];
-[PKPaletteColorPickerView toggleColorSelectionPopover];
-[PKPaletteColorPickerView traitCollectionWithCurrentInterfaceStyle];
```
