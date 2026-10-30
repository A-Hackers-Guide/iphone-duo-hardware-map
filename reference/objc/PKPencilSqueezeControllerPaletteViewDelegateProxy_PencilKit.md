# `PKPencilSqueezeControllerPaletteViewDelegateProxy`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `PKPaletteMoreOptionsViewControllerDelegate`, `PKPaletteColorPickerControllerDelegate`, `_UIStickerPickerViewControllerDelegate`, `PKSqueezePaletteViewDelegate`
- 9 instance variables, 4 properties, 25 instance methods, 0 class methods

## Instance variables

```
@"PKPencilSqueezeController" _controller;
@"PKSqueezePaletteView" _paletteView;
B _moreOptionsViewControllerVisible;
@"PKPaletteMoreOptionsViewController" _moreOptionsViewController;
@"PKStatisticsManager" _statisticsManager;
@"PKHoverSettings" _hoverSettings;
@"UIViewController" _lastPresentedSignaturesViewController;
@"<PKPaletteColorPickerController>" _colorPickerController;
@"_UIStickerPickerViewController" _stickerPickerViewController;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[PKPencilSqueezeControllerPaletteViewDelegateProxy insertStickerFromItemProvider:completionHandler:];
-[PKPencilSqueezeControllerPaletteViewDelegateProxy stickerPickerViewControllerDidDismiss];
-[PKPencilSqueezeControllerPaletteViewDelegateProxy colorPickerControllerDidChangeSelectedColor:isContinuousColorSelection:];
-[PKPencilSqueezeControllerPaletteViewDelegateProxy moreOptionsViewControllerDidSelectOpenPencilSettings:];
-[PKPencilSqueezeControllerPaletteViewDelegateProxy moreOptionsViewControllerDidSelectTapToRadar:];
-[PKPencilSqueezeControllerPaletteViewDelegateProxy moreOptionsViewControllerDidToggleAutoHide:];
-[PKPencilSqueezeControllerPaletteViewDelegateProxy moreOptionsViewControllerDidToggleAutoRefine:];
-[PKPencilSqueezeControllerPaletteViewDelegateProxy moreOptionsViewControllerDidToggleFingerDraws:];
-[PKPencilSqueezeControllerPaletteViewDelegateProxy moreOptionsViewControllerDidToggleProofreading:];
-[PKPencilSqueezeControllerPaletteViewDelegateProxy paletteView:canSelectTool:atIndex:];
-[PKPencilSqueezeControllerPaletteViewDelegateProxy paletteView:didSelectColor:isFromExtendedColorPicker:isContinuousColorSelection:];
-[PKPencilSqueezeControllerPaletteViewDelegateProxy paletteView:didSelectTool:atIndex:];
-[PKPencilSqueezeControllerPaletteViewDelegateProxy paletteViewCanRedo:];
-[PKPencilSqueezeControllerPaletteViewDelegateProxy paletteViewCanUndo:];
-[PKPencilSqueezeControllerPaletteViewDelegateProxy paletteViewDidInvokeAddShape:sourceView:];
-[PKPencilSqueezeControllerPaletteViewDelegateProxy paletteViewDidInvokeAddSticker:sourceView:];
-[PKPencilSqueezeControllerPaletteViewDelegateProxy paletteViewDidInvokeAddTextBox:sourceView:];
-[PKPencilSqueezeControllerPaletteViewDelegateProxy paletteViewDidInvokeExtendedColorPicker:currentSelectedColor:sourceView:];
-[PKPencilSqueezeControllerPaletteViewDelegateProxy paletteViewDidInvokeMoreOptions:sourceView:];
-[PKPencilSqueezeControllerPaletteViewDelegateProxy paletteViewDidInvokeRedo:];
-[PKPencilSqueezeControllerPaletteViewDelegateProxy paletteViewDidInvokeSignature:sourceView:];
-[PKPencilSqueezeControllerPaletteViewDelegateProxy paletteViewDidInvokeUndo:];
-[PKPencilSqueezeControllerPaletteViewDelegateProxy paletteViewDidTapRuler:];
-[PKPencilSqueezeControllerPaletteViewDelegateProxy paletteViewRedoCount:];
-[PKPencilSqueezeControllerPaletteViewDelegateProxy paletteViewUndoCount:];
```
