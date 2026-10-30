# `_UIButtonConfiguration`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIButtonConfigurationShim`, `NSCopying`, `NSSecureCoding`
- 21 instance variables, 41 properties, 82 instance methods, 6 class methods

## Instance variables

```
@? _baseAttributesTransformer;
@"UITraitCollection" _traitCollection;
q _role;
B _hasCustomizedImageTintColorTransformer;
B _showsBusyIndicator;
@"UIBackgroundConfiguration" _background;
@"UIImage" _image;
@"UIColor" _imageTintColor;
@? _imageTintColorTransformer;
@"UIImageSymbolConfiguration" _preferredSymbolConfigurationForImage;
Q _imageEdge;
q _buttonSize;
@"NSAttributedString" _attributedTitle;
@? _titleTextAttributesTransformer;
@"NSAttributedString" _attributedSubtitle;
@? _subtitleTextAttributesTransformer;
d _imageToTitlePadding;
q _imageTintColorTransformerIdentifier;
q _style;
q _macIdiomStyle;
{NSDirectionalEdgeInsets="top"d"leading"d"bottom"d"trailing"d} _backgroundToContentInsets;
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
@property (Tq,N,S_setImageTintColorTransformerIdentifier:,V_imageTintColorTransformerIdentifier) imageTintColorTransformerIdentifier;
@property (Tq,R,N,V_style) style;
@property (Tq,N,V_macIdiomStyle) macIdiomStyle;
@property (T@"UIBackgroundConfiguration",R,N,V_background) background;
@property (T@"UIImage",&,N,V_image) image;
@property (T@"UIColor",&,N,V_imageTintColor) imageTintColor;
@property (T@?,C,N,V_imageTintColorTransformer) imageTintColorTransformer;
@property (T@"UIImageSymbolConfiguration",&,N,V_preferredSymbolConfigurationForImage) preferredSymbolConfigurationForImage;
@property (TQ,N,V_imageEdge) imageEdge;
@property (Tq,N,V_buttonSize) buttonSize;
@property (T@"NSString",C,N) title;
@property (T@"NSAttributedString",C,N,V_attributedTitle) attributedTitle;
@property (T@?,C,N,V_titleTextAttributesTransformer) titleTextAttributesTransformer;
@property (T@"NSString",C,N) subtitle;
@property (T@"NSAttributedString",C,N,V_attributedSubtitle) attributedSubtitle;
@property (T@?,C,N,V_subtitleTextAttributesTransformer) subtitleTextAttributesTransformer;
@property (TB,N,V_showsBusyIndicator) showsBusyIndicator;
@property (T{NSDirectionalEdgeInsets=dddd},N,V_backgroundToContentInsets) backgroundToContentInsets;
@property (Td,N,V_imageToTitlePadding) imageToTitlePadding;
```

## Class methods

```
+[_UIButtonConfiguration supportsSecureCoding];
+[_UIButtonConfiguration configurationWithStyle:];
+[_UIButtonConfiguration filledButtonConfiguration];
+[_UIButtonConfiguration grayButtonConfiguration];
+[_UIButtonConfiguration plainButtonConfiguration];
+[_UIButtonConfiguration tintedButtonConfiguration];
```

## Instance methods

```
-[_UIButtonConfiguration imagePadding];
-[_UIButtonConfiguration attributedSubtitle];
-[_UIButtonConfiguration cornerStyle];
-[_UIButtonConfiguration titleAlignment];
-[_UIButtonConfiguration subtitle];
-[_UIButtonConfiguration setAttributedTitle:];
-[_UIButtonConfiguration setSubtitle:];
-[_UIButtonConfiguration style];
-[_UIButtonConfiguration imageTintColor];
-[_UIButtonConfiguration background];
-[_UIButtonConfiguration _resolvedIndicatorColor];
-[_UIButtonConfiguration updatedConfigurationForState:];
-[_UIButtonConfiguration showsBusyIndicator];
-[_UIButtonConfiguration setImageTintColor:];
-[_UIButtonConfiguration title];
-[_UIButtonConfiguration attributedTitle];
-[_UIButtonConfiguration encodeWithCoder:];
-[_UIButtonConfiguration contentInsets];
-[_UIButtonConfiguration setAttributedSubtitle:];
-[_UIButtonConfiguration hash];
-[_UIButtonConfiguration buttonSize];
-[_UIButtonConfiguration _traitCollection];
-[_UIButtonConfiguration description];
-[_UIButtonConfiguration initWithCoder:];
-[_UIButtonConfiguration setTitle:];
-[_UIButtonConfiguration image];
-[_UIButtonConfiguration copyWithZone:];
-[_UIButtonConfiguration _resolvedImage];
-[_UIButtonConfiguration isEqual:];
-[_UIButtonConfiguration setImage:];
-[_UIButtonConfiguration _hasSymbolImage];
-[_UIButtonConfiguration _resolvedMonochromaticTreatment];
-[_UIButtonConfiguration _resolvedActivityIndicatorColor];
-[_UIButtonConfiguration _apiValue];
-[_UIButtonConfiguration _hasMultilineSubtitle];
-[_UIButtonConfiguration _hasMultilineTitle];
-[_UIButtonConfiguration _hasObscuringBackground];
-[_UIButtonConfiguration _hasOversizedSubtitle];
-[_UIButtonConfiguration _hasOversizedTitle];
-[_UIButtonConfiguration _isRoundButton];
-[_UIButtonConfiguration _resolvedActivityIndicatorSize];
-[_UIButtonConfiguration _resolvedColorMaterialRenderingMode];
-[_UIButtonConfiguration _resolvedIdiom];
-[_UIButtonConfiguration _resolvedImageColor];
-[_UIButtonConfiguration _resolvedImageReservation];
-[_UIButtonConfiguration _resolvedIndicator];
-[_UIButtonConfiguration _resolvedIndicatorPadding];
-[_UIButtonConfiguration _resolvedIndicatorSymbolConfiguration];
-[_UIButtonConfiguration _resolvedMacIdiomStyle];
-[_UIButtonConfiguration _resolvedSubtitle];
-[_UIButtonConfiguration _resolvedSymbolConfiguration];
-[_UIButtonConfiguration _resolvedSymbolContentTransition];
-[_UIButtonConfiguration _resolvedTitle];
-[_UIButtonConfiguration _resolvedTitleAlignment];
-[_UIButtonConfiguration _setImageTintColorTransformerIdentifier:];
-[_UIButtonConfiguration _spiValue];
-[_UIButtonConfiguration _updateFromButton:];
-[_UIButtonConfiguration _updateMetadataFromButton:];
-[_UIButtonConfiguration backgroundToContentInsets];
-[_UIButtonConfiguration imageEdge];
-[_UIButtonConfiguration imagePlacement];
-[_UIButtonConfiguration imageTintColorTransformer];
-[_UIButtonConfiguration imageTintColorTransformerIdentifier];
-[_UIButtonConfiguration imageToTitlePadding];
-[_UIButtonConfiguration macIdiomStyle];
-[_UIButtonConfiguration preferredSymbolConfigurationForImage];
-[_UIButtonConfiguration setBackgroundToContentInsets:];
-[_UIButtonConfiguration setButtonSize:];
-[_UIButtonConfiguration setImageEdge:];
-[_UIButtonConfiguration setImageTintColorTransformer:];
-[_UIButtonConfiguration setImageToTitlePadding:];
-[_UIButtonConfiguration setMacIdiomStyle:];
-[_UIButtonConfiguration setPreferredSymbolConfigurationForImage:];
-[_UIButtonConfiguration setShowsBusyIndicator:];
-[_UIButtonConfiguration setSubtitleTextAttributesTransformer:];
-[_UIButtonConfiguration setTitleTextAttributesTransformer:];
-[_UIButtonConfiguration showsActivityIndicator];
-[_UIButtonConfiguration subtitleLineBreakMode];
-[_UIButtonConfiguration subtitleTextAttributesTransformer];
-[_UIButtonConfiguration titleLineBreakMode];
-[_UIButtonConfiguration titlePadding];
-[_UIButtonConfiguration titleTextAttributesTransformer];
```
