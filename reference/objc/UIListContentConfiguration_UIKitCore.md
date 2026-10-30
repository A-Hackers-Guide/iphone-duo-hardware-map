# `UIListContentConfiguration`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIContentConfiguration`, `NSSecureCoding`
- 15 instance variables, 21 properties, 44 instance methods, 22 class methods

## Instance variables

```
{?="hasCustomizedAxesPreservingSuperviewLayoutMargins"b1"hasCustomizedDirectionalLayoutMargins"b1"hasCustomizedPrefersSideBySideTextAndSecondaryText"b1"hasCustomizedImageToTextPadding"b1"hasCustomizedTextToSecondaryTextHorizontalPadding"b1"hasCustomizedTextToSecondaryTextVerticalPadding"b1"hasCustomizedEnforcesMinimumHeight"b1"hasCustomizedAlpha"b1"isSidebarStyle"b1} _configurationFlags;
B _prefersSideBySideTextAndSecondaryText;
B _enforcesMinimumHeight;
B __disableAutomaticDefaultStyleUpdates;
Q _axesPreservingSuperviewLayoutMargins;
d _imageToTextPadding;
d _textToSecondaryTextHorizontalPadding;
d _textToSecondaryTextVerticalPadding;
d _alpha;
@"_UIContentViewEditingConfiguration" _textEditingConfiguration;
q _defaultStyle;
@"UIListContentImageProperties" _imageProperties;
@"UIListContentTextProperties" _textProperties;
@"UIListContentTextProperties" _secondaryTextProperties;
{NSDirectionalEdgeInsets="top"d"leading"d"bottom"d"trailing"d} _directionalLayoutMargins;
```

## Properties

```
@property (TB,N,S_setEnforcesMinimumHeight:) _enforcesMinimumHeight;
@property (T@"_UIContentViewEditingConfiguration",C,N,S_setTextEditingConfiguration:,V_textEditingConfiguration) _textEditingConfiguration;
@property (T@"UIImage",&,N) image;
@property (T@"UIListContentImageProperties",R,N,V_imageProperties) imageProperties;
@property (T@"NSString",C,N) text;
@property (T@"NSAttributedString",C,N) attributedText;
@property (T@"UIListContentTextProperties",R,N,V_textProperties) textProperties;
@property (T@"NSString",C,N) secondaryText;
@property (T@"NSAttributedString",C,N) secondaryAttributedText;
@property (T@"UIListContentTextProperties",R,N,V_secondaryTextProperties) secondaryTextProperties;
@property (TQ,N) axesPreservingSuperviewLayoutMargins;
@property (T{NSDirectionalEdgeInsets=dddd},N) directionalLayoutMargins;
@property (TB,N) prefersSideBySideTextAndSecondaryText;
@property (Td,N) imageToTextPadding;
@property (Td,N) textToSecondaryTextHorizontalPadding;
@property (Td,N) textToSecondaryTextVerticalPadding;
@property (Td,N) alpha;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UIListContentConfiguration supportsSecureCoding];
+[UIListContentConfiguration valueCellConfiguration];
+[UIListContentConfiguration _prominentInsetGroupedHeaderConfiguration];
+[UIListContentConfiguration prominentInsetGroupedHeaderConfiguration];
+[UIListContentConfiguration footerConfiguration];
+[UIListContentConfiguration plainHeaderConfiguration];
+[UIListContentConfiguration plainFooterConfiguration];
+[UIListContentConfiguration _interactiveInsetGroupedHeaderConfiguration];
+[UIListContentConfiguration groupedHeaderConfiguration];
+[UIListContentConfiguration headerConfiguration];
+[UIListContentConfiguration _headerConfiguration];
+[UIListContentConfiguration accompaniedSidebarCellConfiguration];
+[UIListContentConfiguration cellConfiguration];
+[UIListContentConfiguration sidebarCellConfiguration];
+[UIListContentConfiguration _defaultInsetGroupedCellConfiguration];
+[UIListContentConfiguration groupedFooterConfiguration];
+[UIListContentConfiguration sidebarHeaderConfiguration];
+[UIListContentConfiguration _footerConfiguration];
+[UIListContentConfiguration subtitleCellConfiguration];
+[UIListContentConfiguration extraProminentInsetGroupedHeaderConfiguration];
+[UIListContentConfiguration accompaniedSidebarSubtitleCellConfiguration];
+[UIListContentConfiguration sidebarSubtitleCellConfiguration];
```

## Instance methods

```
-[UIListContentConfiguration imageProperties];
-[UIListContentConfiguration directionalLayoutMargins];
-[UIListContentConfiguration setDirectionalLayoutMargins:];
-[UIListContentConfiguration debugDescription];
-[UIListContentConfiguration text];
-[UIListContentConfiguration setAttributedText:];
-[UIListContentConfiguration secondaryText];
-[UIListContentConfiguration _setSwiftBridgingImageProperties:];
-[UIListContentConfiguration makeContentView];
-[UIListContentConfiguration setSecondaryText:];
-[UIListContentConfiguration updatedConfigurationForState:];
-[UIListContentConfiguration _setSwiftBridgingSecondaryTextProperties:];
-[UIListContentConfiguration _setSwiftBridgingTextProperties:];
-[UIListContentConfiguration setAlpha:];
-[UIListContentConfiguration attributedText];
-[UIListContentConfiguration encodeWithCoder:];
-[UIListContentConfiguration imageToTextPadding];
-[UIListContentConfiguration secondaryTextProperties];
-[UIListContentConfiguration hash];
-[UIListContentConfiguration description];
-[UIListContentConfiguration setAxesPreservingSuperviewLayoutMargins:];
-[UIListContentConfiguration initWithCoder:];
-[UIListContentConfiguration setText:];
-[UIListContentConfiguration alpha];
-[UIListContentConfiguration setImageToTextPadding:];
-[UIListContentConfiguration image];
-[UIListContentConfiguration copyWithZone:];
-[UIListContentConfiguration axesPreservingSuperviewLayoutMargins];
-[UIListContentConfiguration setSecondaryAttributedText:];
-[UIListContentConfiguration isEqual:];
-[UIListContentConfiguration secondaryAttributedText];
-[UIListContentConfiguration textProperties];
-[UIListContentConfiguration setImage:];
-[UIListContentConfiguration _enforcesMinimumHeight];
-[UIListContentConfiguration _minimumHeightForTraitCollection:];
-[UIListContentConfiguration _setEnforcesMinimumHeight:];
-[UIListContentConfiguration _setTextEditingConfiguration:];
-[UIListContentConfiguration _textEditingConfiguration];
-[UIListContentConfiguration prefersSideBySideTextAndSecondaryText];
-[UIListContentConfiguration setPrefersSideBySideTextAndSecondaryText:];
-[UIListContentConfiguration setTextToSecondaryTextHorizontalPadding:];
-[UIListContentConfiguration setTextToSecondaryTextVerticalPadding:];
-[UIListContentConfiguration textToSecondaryTextHorizontalPadding];
-[UIListContentConfiguration textToSecondaryTextVerticalPadding];
```
