# `UIButtonConfiguration`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIButtonConfigurationShim`, `NSCopying`, `NSSecureCoding`
- 31 instance variables, 60 properties, 121 instance methods, 23 class methods

## Instance variables

```
@"_UIButtonConfigurationStyleBehaviors" _behaviors;
@"NSAttributedString" _resolvedTitle;
@"NSAttributedString" _resolvedSubtitle;
@"UIColor" _resolvedImageColor;
@"UIImageSymbolConfiguration" _resolvedSymbolConfig;
@"UIColor" _resolvedIndicatorColor;
@"UIImageSymbolConfiguration" _resolvedIndicatorSymbolConfig;
@"UIColor" _resolvedActivityIndicatorColor;
q _resolvedIdiom;
d _resolvedActivityIndicatorSize;
d _resolvedImageReservation;
{?="macIdiomStyle"b4"buttonSize"b2"showsActivityIndicator"b1"useCustomContentInsets"b1"contentInsetsExpansion"b3"titleLineBreakMode"b3"subtitleLineBreakMode"b3"automaticallyUpdateForSelection"b1"indicator"b2"resolvedTitleIsOversized"b1"resolvedSubtitleIsOversized"b1"resolvedIndicator"b2"titleAlignment"b2"alwaysApplyTitleAlignment"b1"resolvedMonochromaticTreatmentUnspecified"b1"resolvedMonochromaticTreatment"b2"disableGlassAdaptivitiy"b1"resolvedColorMaterialRenderingModeAutomatic"b1"resolvedColorMaterialRenderingMode"b2} _flags;
@"UIBackgroundConfiguration" _background;
q _cornerStyle;
@"UIColor" _baseForegroundColor;
@"UIColor" _baseBackgroundColor;
@"UIImage" _image;
@? _imageColorTransformer;
@"UIImageSymbolConfiguration" _preferredSymbolConfigurationForImage;
@"UISymbolContentTransition" _symbolContentTransition;
@? _activityIndicatorColorTransformer;
@"NSAttributedString" _attributedTitle;
@? _titleTextAttributesTransformer;
@"NSAttributedString" _attributedSubtitle;
@? _subtitleTextAttributesTransformer;
@? _indicatorColorTransformer;
Q _imagePlacement;
d _imagePadding;
d _titlePadding;
d _imageReservation;
{NSDirectionalEdgeInsets="top"d"leading"d"bottom"d"trailing"d} _contentInsets;
```

## Properties

```
@property (T@"UIBackgroundConfiguration",R,N) background;
@property (Tq,R,N) cornerStyle;
@property (Tq,R,N) buttonSize;
@property (Tq,R,N) macIdiomStyle;
@property (T@"UIImage",&,N) image;
@property (T@"UIImageSymbolConfiguration",C,N) preferredSymbolConfigurationForImage;
@property (TB,R,N) showsActivityIndicator;
@property (T@"NSString",C,N) title;
@property (T@"NSAttributedString",C,N) attributedTitle;
@property (T@"NSString",R,C,N) subtitle;
@property (T@"NSAttributedString",R,C,N) attributedSubtitle;
@property (T{NSDirectionalEdgeInsets=dddd},R,N) contentInsets;
@property (TQ,R,N) imagePlacement;
@property (Td,R,N) imagePadding;
@property (Td,R,N) titlePadding;
@property (Tq,R,N) titleAlignment;
@property (Tq,R,N) titleLineBreakMode;
@property (Tq,R,N) subtitleLineBreakMode;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TB,N,S_setAlwaysApplyTitleAlignment:) _alwaysApplyTitleAlignment;
@property (Tq,N,S_setImageColorTransformerIdentifier:) _imageColorTransformerIdentifier;
@property (Tq,N,S_setActivityIndicatorColorTransformerIdentifier:) _activityIndicatorColorTransformerIdentifier;
@property (Tq,N,S_setIndicatorColorTransformerIdentifier:) _indicatorColorTransformerIdentifier;
@property (Td,N,V_imageReservation) imageReservation;
@property (Tq,N,S_dci_setIndicator:) _dci_indicator;
@property (T@?,C,N,S_dci_setIndicatorColorTransformer:) _dci_indicatorColorTransformer;
@property (T@"NSSymbolContentTransition",&,N,S_setSymbolContentTransition:) _symbolContentTransition;
@property (T@"NSSymbolEffectOptions",&,N,S_setSymbolContentTransitionOptions:) _symbolContentTransitionOptions;
@property (TB,N,S_setAllowGlassAdaptivity:) _allowGlassAdaptivity;
@property (T@"UIBackgroundConfiguration",&,N,V_background) background;
@property (Tq,N,V_cornerStyle) cornerStyle;
@property (Tq,N) buttonSize;
@property (Tq,N) macIdiomStyle;
@property (T@"UIColor",&,N,V_baseForegroundColor) baseForegroundColor;
@property (T@"UIColor",&,N,V_baseBackgroundColor) baseBackgroundColor;
@property (T@"UIImage",&,N,V_image) image;
@property (T@?,C,N,V_imageColorTransformer) imageColorTransformer;
@property (T@"UIImageSymbolConfiguration",C,N,V_preferredSymbolConfigurationForImage) preferredSymbolConfigurationForImage;
@property (T@"UISymbolContentTransition",&,N,V_symbolContentTransition) symbolContentTransition;
@property (TB,N) showsActivityIndicator;
@property (T@?,C,N,V_activityIndicatorColorTransformer) activityIndicatorColorTransformer;
@property (T@"NSString",C,N) title;
@property (T@"NSAttributedString",C,N,V_attributedTitle) attributedTitle;
@property (T@?,C,N,V_titleTextAttributesTransformer) titleTextAttributesTransformer;
@property (Tq,N) titleLineBreakMode;
@property (T@"NSString",C,N) subtitle;
@property (T@"NSAttributedString",C,N,V_attributedSubtitle) attributedSubtitle;
@property (T@?,C,N,V_subtitleTextAttributesTransformer) subtitleTextAttributesTransformer;
@property (Tq,N) subtitleLineBreakMode;
@property (Tq,N) indicator;
@property (T@?,C,N,V_indicatorColorTransformer) indicatorColorTransformer;
@property (T{NSDirectionalEdgeInsets=dddd},N,V_contentInsets) contentInsets;
@property (TQ,N,V_imagePlacement) imagePlacement;
@property (Td,N,V_imagePadding) imagePadding;
@property (Td,N,V_titlePadding) titlePadding;
@property (Tq,N) titleAlignment;
@property (TB,N) automaticallyUpdateForSelection;
```

## Class methods

```
+[UIButtonConfiguration supportsSecureCoding];
+[UIButtonConfiguration _tintedGlassButtonConfiguration];
+[UIButtonConfiguration _avPlayerGlassButtonConfiguration];
+[UIButtonConfiguration _clearGlassButtonConfiguration];
+[UIButtonConfiguration _controlCenterGlassButtonConfiguration];
+[UIButtonConfiguration _emptyButtonConfiguration];
+[UIButtonConfiguration _glassButtonConfiguration];
+[UIButtonConfiguration _homescreenCloseGlassButtonConfiguration];
+[UIButtonConfiguration _posterSwitcherGlassButtonConfiguration];
+[UIButtonConfiguration _sidebarGlassButtonConfiguration];
+[UIButtonConfiguration borderedButtonConfiguration];
+[UIButtonConfiguration borderedProminentButtonConfiguration];
+[UIButtonConfiguration borderedTintedButtonConfiguration];
+[UIButtonConfiguration borderlessButtonConfiguration];
+[UIButtonConfiguration clearGlassButtonConfiguration];
+[UIButtonConfiguration filledButtonConfiguration];
+[UIButtonConfiguration glassButtonConfiguration];
+[UIButtonConfiguration grayButtonConfiguration];
+[UIButtonConfiguration plainButtonConfiguration];
+[UIButtonConfiguration prominentClearGlassButtonConfiguration];
+[UIButtonConfiguration prominentGlassButtonConfiguration];
+[UIButtonConfiguration tintedButtonConfiguration];
+[UIButtonConfiguration tintedGlassButtonConfiguration];
```

## Instance methods

```
-[UIButtonConfiguration setTitleAlignment:];
-[UIButtonConfiguration imagePadding];
-[UIButtonConfiguration attributedSubtitle];
-[UIButtonConfiguration cornerStyle];
-[UIButtonConfiguration titleAlignment];
-[UIButtonConfiguration subtitle];
-[UIButtonConfiguration setBackground:];
-[UIButtonConfiguration setContentInsets:];
-[UIButtonConfiguration setCornerStyle:];
-[UIButtonConfiguration setAttributedTitle:];
-[UIButtonConfiguration indicator];
-[UIButtonConfiguration setSubtitle:];
-[UIButtonConfiguration background];
-[UIButtonConfiguration _resolvedIndicatorColor];
-[UIButtonConfiguration setImagePadding:];
-[UIButtonConfiguration _hasTitle];
-[UIButtonConfiguration title];
-[UIButtonConfiguration attributedTitle];
-[UIButtonConfiguration encodeWithCoder:];
-[UIButtonConfiguration contentInsets];
-[UIButtonConfiguration setAttributedSubtitle:];
-[UIButtonConfiguration hash];
-[UIButtonConfiguration buttonSize];
-[UIButtonConfiguration description];
-[UIButtonConfiguration initWithCoder:];
-[UIButtonConfiguration setTitle:];
-[UIButtonConfiguration image];
-[UIButtonConfiguration copyWithZone:];
-[UIButtonConfiguration _resolvedImage];
-[UIButtonConfiguration isEqual:];
-[UIButtonConfiguration setImage:];
-[UIButtonConfiguration _hasSymbolImage];
-[UIButtonConfiguration _resolvedMonochromaticTreatment];
-[UIButtonConfiguration automaticallyUpdateForSelection];
-[UIButtonConfiguration _resolvedActivityIndicatorColor];
-[UIButtonConfiguration _symbolContentTransitionOptions];
-[UIButtonConfiguration _activityIndicatorColorTransformerIdentifier];
-[UIButtonConfiguration _allowGlassAdaptivity];
-[UIButtonConfiguration _alwaysApplyTitleAlignment];
-[UIButtonConfiguration _apiValue];
-[UIButtonConfiguration _copyValuesFromConfiguration:];
-[UIButtonConfiguration _dci_indicator];
-[UIButtonConfiguration _dci_indicatorColorTransformer];
-[UIButtonConfiguration _dci_setIndicator:];
-[UIButtonConfiguration _dci_setIndicatorColorTransformer:];
-[UIButtonConfiguration _hasImage];
-[UIButtonConfiguration _hasMultilineSubtitle];
-[UIButtonConfiguration _hasMultilineTitle];
-[UIButtonConfiguration _hasObscuringBackground];
-[UIButtonConfiguration _hasOversizedSubtitle];
-[UIButtonConfiguration _hasOversizedTitle];
-[UIButtonConfiguration _hasSubtitle];
-[UIButtonConfiguration _honorsTintInMacIdiom];
-[UIButtonConfiguration _imageColorTransformerIdentifier];
-[UIButtonConfiguration _indicatorColorTransformerIdentifier];
-[UIButtonConfiguration _initWithBehaviors:];
-[UIButtonConfiguration _isRoundButton];
-[UIButtonConfiguration _isTintedGlass];
-[UIButtonConfiguration _resolveValuesWithButton:];
-[UIButtonConfiguration _resolvedActivityIndicatorSize];
-[UIButtonConfiguration _resolvedColorMaterialRenderingMode];
-[UIButtonConfiguration _resolvedImageColor];
-[UIButtonConfiguration _resolvedImageReservation];
-[UIButtonConfiguration _resolvedIndicator];
-[UIButtonConfiguration _resolvedIndicatorPadding];
-[UIButtonConfiguration _resolvedIndicatorSymbolConfiguration];
-[UIButtonConfiguration _resolvedMacIdiomStyle];
-[UIButtonConfiguration _resolvedSubtitle];
-[UIButtonConfiguration _resolvedSymbolConfiguration];
-[UIButtonConfiguration _resolvedSymbolContentTransition];
-[UIButtonConfiguration _resolvedTitle];
-[UIButtonConfiguration _resolvedTitleAlignment];
-[UIButtonConfiguration _setActivityIndicatorColorTransformerIdentifier:];
-[UIButtonConfiguration _setAllowGlassAdaptivity:];
-[UIButtonConfiguration _setAlwaysApplyTitleAlignment:];
-[UIButtonConfiguration _setImageColorTransformerIdentifier:];
-[UIButtonConfiguration _setIndicatorColorTransformerIdentifier:];
-[UIButtonConfiguration _setSwiftBridgingBackground:];
-[UIButtonConfiguration _setSymbolContentTransition:];
-[UIButtonConfiguration _setSymbolContentTransitionOptions:];
-[UIButtonConfiguration _spiValue];
-[UIButtonConfiguration _symbolContentTransition];
-[UIButtonConfiguration _updateFromButton:];
-[UIButtonConfiguration activityIndicatorColorTransformer];
-[UIButtonConfiguration baseBackgroundColor];
-[UIButtonConfiguration baseForegroundColor];
-[UIButtonConfiguration imageColorTransformer];
-[UIButtonConfiguration imagePlacement];
-[UIButtonConfiguration imageReservation];
-[UIButtonConfiguration indicatorColorTransformer];
-[UIButtonConfiguration macIdiomStyle];
-[UIButtonConfiguration preferredSymbolConfigurationForImage];
-[UIButtonConfiguration setActivityIndicatorColorTransformer:];
-[UIButtonConfiguration setAutomaticallyUpdateForSelection:];
-[UIButtonConfiguration setBaseBackgroundColor:];
-[UIButtonConfiguration setBaseForegroundColor:];
-[UIButtonConfiguration setButtonSize:];
-[UIButtonConfiguration setDefaultContentInsets];
-[UIButtonConfiguration setImageColorTransformer:];
-[UIButtonConfiguration setImagePlacement:];
-[UIButtonConfiguration setImageReservation:];
-[UIButtonConfiguration setIndicator:];
-[UIButtonConfiguration setIndicatorColorTransformer:];
-[UIButtonConfiguration setMacIdiomStyle:];
-[UIButtonConfiguration setPreferredSymbolConfigurationForImage:];
-[UIButtonConfiguration setShowsActivityIndicator:];
-[UIButtonConfiguration setSubtitleLineBreakMode:];
-[UIButtonConfiguration setSubtitleTextAttributesTransformer:];
-[UIButtonConfiguration setSymbolContentTransition:];
-[UIButtonConfiguration setTitleLineBreakMode:];
-[UIButtonConfiguration setTitlePadding:];
-[UIButtonConfiguration setTitleTextAttributesTransformer:];
-[UIButtonConfiguration showsActivityIndicator];
-[UIButtonConfiguration subtitleLineBreakMode];
-[UIButtonConfiguration subtitleTextAttributesTransformer];
-[UIButtonConfiguration symbolContentTransition];
-[UIButtonConfiguration symbolStyleForSize:hasText:];
-[UIButtonConfiguration titleLineBreakMode];
-[UIButtonConfiguration titlePadding];
-[UIButtonConfiguration titleTextAttributesTransformer];
-[UIButtonConfiguration updatedConfigurationForButton:];
```
