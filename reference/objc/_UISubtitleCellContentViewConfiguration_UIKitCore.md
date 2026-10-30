# `_UISubtitleCellContentViewConfiguration`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIContentViewConfiguration`, `NSSecureCoding`
- 10 instance variables, 12 properties, 23 instance methods, 6 class methods

## Instance variables

```
{?="hasCustomizedAxesPreservingSuperviewLayoutMargins"b1"hasCustomizedDirectionalLayoutMargins"b1"hasCustomizedImageToTextPadding"b1"hasCustomizedTextToSubtitlePadding"b1} _configurationFlags;
Q _axesPreservingSuperviewLayoutMargins;
d _imageToTextPadding;
d _textToSubtitlePadding;
@"_UIContentViewEditingConfiguration" _textLabelEditingConfiguration;
q _defaultStyle;
@"_UIContentViewImageViewConfiguration" _imageView;
@"_UIContentViewLabelConfiguration" _textLabel;
@"_UIContentViewLabelConfiguration" _subtitleLabel;
{NSDirectionalEdgeInsets="top"d"leading"d"bottom"d"trailing"d} _directionalLayoutMargins;
```

## Properties

```
@property (T@"_UIContentViewImageViewConfiguration",R,N,V_imageView) imageView;
@property (T@"_UIContentViewLabelConfiguration",R,N,V_textLabel) textLabel;
@property (T@"_UIContentViewLabelConfiguration",R,N,V_subtitleLabel) subtitleLabel;
@property (TQ,N) axesPreservingSuperviewLayoutMargins;
@property (T{NSDirectionalEdgeInsets=dddd},N) directionalLayoutMargins;
@property (Td,N) imageToTextPadding;
@property (Td,N) textToSubtitlePadding;
@property (T@"_UIContentViewEditingConfiguration",C,N,V_textLabelEditingConfiguration) _textLabelEditingConfiguration;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UISubtitleCellContentViewConfiguration supportsSecureCoding];
+[_UISubtitleCellContentViewConfiguration listCellConfiguration];
+[_UISubtitleCellContentViewConfiguration defaultConfiguration];
+[_UISubtitleCellContentViewConfiguration defaultListCellConfigurationForState:];
+[_UISubtitleCellContentViewConfiguration defaultOutlineCellConfigurationForState:];
+[_UISubtitleCellContentViewConfiguration outlineCellConfiguration];
```

## Instance methods

```
-[_UISubtitleCellContentViewConfiguration subtitleLabel];
-[_UISubtitleCellContentViewConfiguration directionalLayoutMargins];
-[_UISubtitleCellContentViewConfiguration setDirectionalLayoutMargins:];
-[_UISubtitleCellContentViewConfiguration textLabel];
-[_UISubtitleCellContentViewConfiguration updatedConfigurationForState:];
-[_UISubtitleCellContentViewConfiguration encodeWithCoder:];
-[_UISubtitleCellContentViewConfiguration imageToTextPadding];
-[_UISubtitleCellContentViewConfiguration hash];
-[_UISubtitleCellContentViewConfiguration description];
-[_UISubtitleCellContentViewConfiguration setAxesPreservingSuperviewLayoutMargins:];
-[_UISubtitleCellContentViewConfiguration initWithCoder:];
-[_UISubtitleCellContentViewConfiguration setImageToTextPadding:];
-[_UISubtitleCellContentViewConfiguration copyWithZone:];
-[_UISubtitleCellContentViewConfiguration axesPreservingSuperviewLayoutMargins];
-[_UISubtitleCellContentViewConfiguration imageView];
-[_UISubtitleCellContentViewConfiguration isEqual:];
-[_UISubtitleCellContentViewConfiguration _textLabelEditingConfiguration];
-[_UISubtitleCellContentViewConfiguration applyToContentView:];
-[_UISubtitleCellContentViewConfiguration createContentView];
-[_UISubtitleCellContentViewConfiguration setTextToSubtitlePadding:];
-[_UISubtitleCellContentViewConfiguration set_textLabelEditingConfiguration:];
-[_UISubtitleCellContentViewConfiguration textToSubtitlePadding];
-[_UISubtitleCellContentViewConfiguration updatedConfigurationForState:traitCollection:];
```
