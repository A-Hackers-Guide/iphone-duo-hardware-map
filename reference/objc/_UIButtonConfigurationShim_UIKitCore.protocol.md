# `_UIButtonConfigurationShim` (protocol)

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`, `NSCopying`, `NSSecureCoding`
- 0 instance variables, 18 properties, 51 instance methods, 0 class methods

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
```

## Instance methods

```
-[_UIButtonConfigurationShim imagePadding];
-[_UIButtonConfigurationShim attributedSubtitle];
-[_UIButtonConfigurationShim cornerStyle];
-[_UIButtonConfigurationShim titleAlignment];
-[_UIButtonConfigurationShim subtitle];
-[_UIButtonConfigurationShim copy];
-[_UIButtonConfigurationShim setAttributedTitle:];
-[_UIButtonConfigurationShim background];
-[_UIButtonConfigurationShim _resolvedIndicatorColor];
-[_UIButtonConfigurationShim title];
-[_UIButtonConfigurationShim attributedTitle];
-[_UIButtonConfigurationShim contentInsets];
-[_UIButtonConfigurationShim buttonSize];
-[_UIButtonConfigurationShim setTitle:];
-[_UIButtonConfigurationShim image];
-[_UIButtonConfigurationShim _resolvedImage];
-[_UIButtonConfigurationShim setImage:];
-[_UIButtonConfigurationShim _hasSymbolImage];
-[_UIButtonConfigurationShim _resolvedMonochromaticTreatment];
-[_UIButtonConfigurationShim _resolvedActivityIndicatorColor];
-[_UIButtonConfigurationShim _apiValue];
-[_UIButtonConfigurationShim _hasMultilineSubtitle];
-[_UIButtonConfigurationShim _hasMultilineTitle];
-[_UIButtonConfigurationShim _hasObscuringBackground];
-[_UIButtonConfigurationShim _hasOversizedSubtitle];
-[_UIButtonConfigurationShim _hasOversizedTitle];
-[_UIButtonConfigurationShim _isRoundButton];
-[_UIButtonConfigurationShim _resolvedActivityIndicatorSize];
-[_UIButtonConfigurationShim _resolvedColorMaterialRenderingMode];
-[_UIButtonConfigurationShim _resolvedIdiom];
-[_UIButtonConfigurationShim _resolvedImageColor];
-[_UIButtonConfigurationShim _resolvedImageReservation];
-[_UIButtonConfigurationShim _resolvedIndicator];
-[_UIButtonConfigurationShim _resolvedIndicatorPadding];
-[_UIButtonConfigurationShim _resolvedIndicatorSymbolConfiguration];
-[_UIButtonConfigurationShim _resolvedMacIdiomStyle];
-[_UIButtonConfigurationShim _resolvedSubtitle];
-[_UIButtonConfigurationShim _resolvedSymbolConfiguration];
-[_UIButtonConfigurationShim _resolvedSymbolContentTransition];
-[_UIButtonConfigurationShim _resolvedTitle];
-[_UIButtonConfigurationShim _resolvedTitleAlignment];
-[_UIButtonConfigurationShim _spiValue];
-[_UIButtonConfigurationShim _updateFromButton:];
-[_UIButtonConfigurationShim imagePlacement];
-[_UIButtonConfigurationShim macIdiomStyle];
-[_UIButtonConfigurationShim preferredSymbolConfigurationForImage];
-[_UIButtonConfigurationShim setPreferredSymbolConfigurationForImage:];
-[_UIButtonConfigurationShim showsActivityIndicator];
-[_UIButtonConfigurationShim subtitleLineBreakMode];
-[_UIButtonConfigurationShim titleLineBreakMode];
-[_UIButtonConfigurationShim titlePadding];
```
