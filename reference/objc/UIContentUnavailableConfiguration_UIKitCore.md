# `UIContentUnavailableConfiguration`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIContentConfiguration`, `NSSecureCoding`
- 16 instance variables, 24 properties, 48 instance methods, 6 class methods

## Instance variables

```
{?="hasCustomizedPrefersSideBySideButtonAndSecondaryButton"b1"hasCustomizedPrefersButtonsJustified"b1"hasCustomizedAxesPreservingSuperviewLayoutMargins"b1"hasCustomizedDirectionalLayoutMargins"b1"hasCustomizedImageToTextPadding"b1"hasCustomizedTextToSecondaryTextPadding"b1"hasCustomizedTextToButtonPadding"b1"hasCustomizedButtonToSecondaryButtonPadding"b1} _configurationFlags;
B _prefersSideBySideButtonAndSecondaryButton;
B _prefersButtonsJustified;
Q _axesPreservingSuperviewLayoutMargins;
d _imageToTextPadding;
d _textToSecondaryTextPadding;
d _textToButtonPadding;
d _buttonToSecondaryButtonPadding;
q _defaultStyle;
@"UIContentUnavailableImageProperties" _imageProperties;
@"UIContentUnavailableTextProperties" _textProperties;
@"UIContentUnavailableTextProperties" _secondaryTextProperties;
@"UIContentUnavailableButtonProperties" _buttonProperties;
@"UIContentUnavailableButtonProperties" _secondaryButtonProperties;
@"UIBackgroundConfiguration" _background;
{NSDirectionalEdgeInsets="top"d"leading"d"bottom"d"trailing"d} _directionalLayoutMargins;
```

## Properties

```
@property (T@"UIImage",&,N) image;
@property (T@"UIContentUnavailableImageProperties",R,N,V_imageProperties) imageProperties;
@property (T@"NSString",C,N) text;
@property (T@"NSAttributedString",C,N) attributedText;
@property (T@"UIContentUnavailableTextProperties",R,N,V_textProperties) textProperties;
@property (T@"NSString",C,N) secondaryText;
@property (T@"NSAttributedString",C,N) secondaryAttributedText;
@property (T@"UIContentUnavailableTextProperties",R,N,V_secondaryTextProperties) secondaryTextProperties;
@property (T@"UIButtonConfiguration",&,N) button;
@property (T@"UIContentUnavailableButtonProperties",R,N,V_buttonProperties) buttonProperties;
@property (T@"UIButtonConfiguration",&,N) secondaryButton;
@property (T@"UIContentUnavailableButtonProperties",R,N,V_secondaryButtonProperties) secondaryButtonProperties;
@property (Tq,N) alignment;
@property (TQ,N) axesPreservingSuperviewLayoutMargins;
@property (T{NSDirectionalEdgeInsets=dddd},N) directionalLayoutMargins;
@property (Td,N) imageToTextPadding;
@property (Td,N) textToSecondaryTextPadding;
@property (Td,N) textToButtonPadding;
@property (Td,N) buttonToSecondaryButtonPadding;
@property (T@"UIBackgroundConfiguration",&,N,V_background) background;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UIContentUnavailableConfiguration supportsSecureCoding];
+[UIContentUnavailableConfiguration emptyConfiguration];
+[UIContentUnavailableConfiguration emptyExtraProminentConfiguration];
+[UIContentUnavailableConfiguration emptyProminentConfiguration];
+[UIContentUnavailableConfiguration loadingConfiguration];
+[UIContentUnavailableConfiguration searchConfiguration];
```

## Instance methods

```
-[UIContentUnavailableConfiguration imageProperties];
-[UIContentUnavailableConfiguration directionalLayoutMargins];
-[UIContentUnavailableConfiguration setDirectionalLayoutMargins:];
-[UIContentUnavailableConfiguration text];
-[UIContentUnavailableConfiguration setBackground:];
-[UIContentUnavailableConfiguration setButton:];
-[UIContentUnavailableConfiguration setAttributedText:];
-[UIContentUnavailableConfiguration secondaryText];
-[UIContentUnavailableConfiguration button];
-[UIContentUnavailableConfiguration _setSwiftBridgingImageProperties:];
-[UIContentUnavailableConfiguration setAlignment:];
-[UIContentUnavailableConfiguration _setSwiftBridgingSecondaryButtonProperties:];
-[UIContentUnavailableConfiguration makeContentView];
-[UIContentUnavailableConfiguration background];
-[UIContentUnavailableConfiguration setSecondaryButton:];
-[UIContentUnavailableConfiguration alignment];
-[UIContentUnavailableConfiguration setSecondaryText:];
-[UIContentUnavailableConfiguration updatedConfigurationForState:];
-[UIContentUnavailableConfiguration _setSwiftBridgingSecondaryTextProperties:];
-[UIContentUnavailableConfiguration _setSwiftBridgingTextProperties:];
-[UIContentUnavailableConfiguration buttonProperties];
-[UIContentUnavailableConfiguration buttonToSecondaryButtonPadding];
-[UIContentUnavailableConfiguration attributedText];
-[UIContentUnavailableConfiguration encodeWithCoder:];
-[UIContentUnavailableConfiguration imageToTextPadding];
-[UIContentUnavailableConfiguration secondaryButtonProperties];
-[UIContentUnavailableConfiguration secondaryTextProperties];
-[UIContentUnavailableConfiguration hash];
-[UIContentUnavailableConfiguration secondaryButton];
-[UIContentUnavailableConfiguration description];
-[UIContentUnavailableConfiguration setAxesPreservingSuperviewLayoutMargins:];
-[UIContentUnavailableConfiguration initWithCoder:];
-[UIContentUnavailableConfiguration setButtonToSecondaryButtonPadding:];
-[UIContentUnavailableConfiguration setText:];
-[UIContentUnavailableConfiguration setImageToTextPadding:];
-[UIContentUnavailableConfiguration _setSwiftBridgingButtonProperties:];
-[UIContentUnavailableConfiguration image];
-[UIContentUnavailableConfiguration copyWithZone:];
-[UIContentUnavailableConfiguration axesPreservingSuperviewLayoutMargins];
-[UIContentUnavailableConfiguration setSecondaryAttributedText:];
-[UIContentUnavailableConfiguration isEqual:];
-[UIContentUnavailableConfiguration secondaryAttributedText];
-[UIContentUnavailableConfiguration setTextToButtonPadding:];
-[UIContentUnavailableConfiguration setTextToSecondaryTextPadding:];
-[UIContentUnavailableConfiguration textProperties];
-[UIContentUnavailableConfiguration textToButtonPadding];
-[UIContentUnavailableConfiguration textToSecondaryTextPadding];
-[UIContentUnavailableConfiguration setImage:];
```
