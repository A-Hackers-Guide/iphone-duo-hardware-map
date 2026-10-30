# `_UISearchAtomView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `_UIVisualStyleStylable`, `_UIAtomTextViewAtomLayout`
- 14 instance variables, 22 properties, 42 instance methods, 4 class methods

## Instance variables

```
{?="enabled"b1} _flags;
@"UIColor" _customAtomForegroundColor;
@"UIColor" _atomBackgroundColor;
@"_UISearchAtomBackgroundView" _backgroundView;
@"_UISearchAtomViewVisualStyle" _visualStyle;
@"NSArray" _defaultConstraints;
@"NSLayoutConstraint" _maximumAtomWidthConstraint;
@"NSLayoutConstraint" _imageBaselineConstraint;
@"NSLayoutConstraint" _imageCenterYConstraint;
@"NSArray" _withImageConstraints;
@"NSArray" _withoutImageConstraints;
@"UILabel" _textLabel;
@"UIImageView" _leadingImage;
d _tokenSpacing;
```

## Properties

```
@property (T@"_UISearchAtomBackgroundView",&,N,V_backgroundView) backgroundView;
@property (T@"_UISearchAtomViewVisualStyle",R,N,V_visualStyle) visualStyle;
@property (T@"NSArray",C,N,V_defaultConstraints) defaultConstraints;
@property (T@"NSLayoutConstraint",&,N,V_maximumAtomWidthConstraint) maximumAtomWidthConstraint;
@property (T@"NSLayoutConstraint",&,N,V_imageBaselineConstraint) imageBaselineConstraint;
@property (T@"NSLayoutConstraint",&,N,V_imageCenterYConstraint) imageCenterYConstraint;
@property (T@"NSArray",C,N,V_withImageConstraints) withImageConstraints;
@property (T@"NSArray",C,N,V_withoutImageConstraints) withoutImageConstraints;
@property (T@"UILabel",&,V_textLabel) textLabel;
@property (T@"UIImageView",&,V_leadingImage) leadingImage;
@property (T@"UIColor",&,N,V_atomBackgroundColor) atomBackgroundColor;
@property (T@"UIFont",&,N) atomFont;
@property (Td,N) viewportWidth;
@property (Td,N,V_tokenSpacing) tokenSpacing;
@property (T@"UIColor",&,N,S_setAtomForegroundColor:) _atomForegroundColor;
@property (TB,N,GisEnabled) enabled;
@property (Tq,N) selectionStyle;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) selectionBounds;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UISearchAtomView requiresConstraintBasedLayout];
+[_UISearchAtomView visualStyleRegistryIdentity];
+[_UISearchAtomView _defaultAtomForegroundColorForTraitCollection:];
+[_UISearchAtomView defaultAtomBackgroundColorForTraitCollection:];
```

## Instance methods

```
-[_UISearchAtomView setEnabled:animated:];
-[_UISearchAtomView setTextLabel:];
-[_UISearchAtomView leadingImage];
-[_UISearchAtomView _dynamicUserInterfaceTraitDidChange];
-[_UISearchAtomView visualStyle];
-[_UISearchAtomView _updateColors];
-[_UISearchAtomView setSelectionStyle:];
-[_UISearchAtomView textLabel];
-[_UISearchAtomView viewForLastBaselineLayout];
-[_UISearchAtomView selectionStyle];
-[_UISearchAtomView isEnabled];
-[_UISearchAtomView tintColorDidChange];
-[_UISearchAtomView setLeadingImage:];
-[_UISearchAtomView setEnabled:];
-[_UISearchAtomView backgroundView];
-[_UISearchAtomView updateConstraints];
-[_UISearchAtomView initWithFrame:];
-[_UISearchAtomView setBackgroundView:];
-[_UISearchAtomView selectionBounds];
-[_UISearchAtomView _atomForegroundColor];
-[_UISearchAtomView _setAtomForegroundColor:];
-[_UISearchAtomView atomBackgroundColor];
-[_UISearchAtomView atomFont];
-[_UISearchAtomView defaultConstraints];
-[_UISearchAtomView imageBaselineConstraint];
-[_UISearchAtomView imageCenterYConstraint];
-[_UISearchAtomView maximumAtomWidthConstraint];
-[_UISearchAtomView setAtomBackgroundColor:];
-[_UISearchAtomView setAtomFont:];
-[_UISearchAtomView setDefaultConstraints:];
-[_UISearchAtomView setImageBaselineConstraint:];
-[_UISearchAtomView setImageCenterYConstraint:];
-[_UISearchAtomView setMaximumAtomWidthConstraint:];
-[_UISearchAtomView setSelectionStyle:animated:];
-[_UISearchAtomView setTokenSpacing:];
-[_UISearchAtomView setViewportWidth:];
-[_UISearchAtomView setWithImageConstraints:];
-[_UISearchAtomView setWithoutImageConstraints:];
-[_UISearchAtomView tokenSpacing];
-[_UISearchAtomView viewportWidth];
-[_UISearchAtomView withImageConstraints];
-[_UISearchAtomView withoutImageConstraints];
```
