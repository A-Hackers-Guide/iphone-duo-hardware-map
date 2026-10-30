# `PKPaletteReturnKeyButton`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PKPaletteButton`
- 5 instance variables, 4 properties, 31 instance methods, 0 class methods

## Instance variables

```
d _scalingFactor;
q _returnKeyType;
q _axis;
@"PKPaletteReturnKeyButtonContentView" _contentView;
@"PKTextInputLanguageSelectionToken" _observerToken;
```

## Properties

```
@property (T@"PKPaletteReturnKeyButtonContentView",&,N,V_contentView) contentView;
@property (T@"PKTextInputLanguageSelectionToken",&,N,V_observerToken) observerToken;
@property (Tq,N,V_returnKeyType) returnKeyType;
@property (Tq,N,V_axis) axis;
```

## Instance methods

```
-[PKPaletteReturnKeyButton _updateImageView];
-[PKPaletteReturnKeyButton _updateLabelText];
-[PKPaletteReturnKeyButton setReturnKeyType:];
-[PKPaletteReturnKeyButton axis];
-[PKPaletteReturnKeyButton setContentView:];
-[PKPaletteReturnKeyButton setObserverToken:];
-[PKPaletteReturnKeyButton intrinsicContentSize];
-[PKPaletteReturnKeyButton setAxis:];
-[PKPaletteReturnKeyButton _backgroundColor];
-[PKPaletteReturnKeyButton _textColor];
-[PKPaletteReturnKeyButton scalingFactor];
-[PKPaletteReturnKeyButton dealloc];
-[PKPaletteReturnKeyButton observerToken];
-[PKPaletteReturnKeyButton layoutSubviews];
-[PKPaletteReturnKeyButton setHighlighted:];
-[PKPaletteReturnKeyButton setEnabled:];
-[PKPaletteReturnKeyButton contentView];
-[PKPaletteReturnKeyButton setScalingFactor:];
-[PKPaletteReturnKeyButton traitCollectionDidChange:];
-[PKPaletteReturnKeyButton _updateUI];
-[PKPaletteReturnKeyButton initWithFrame:];
-[PKPaletteReturnKeyButton returnKeyType];
-[PKPaletteReturnKeyButton _returnKeyImage];
-[PKPaletteReturnKeyButton _contentViewSize];
-[PKPaletteReturnKeyButton _regularLayoutBackgroundColor];
-[PKPaletteReturnKeyButton _returnKeyImageSymbolConfiguration];
-[PKPaletteReturnKeyButton _returnKeyLabelText];
-[PKPaletteReturnKeyButton _returnKeyTintColor];
-[PKPaletteReturnKeyButton _shouldUseBlueReturnKeyColor];
-[PKPaletteReturnKeyButton _updateContentViewOrientation];
-[PKPaletteReturnKeyButton _useCompactLayout];
```
