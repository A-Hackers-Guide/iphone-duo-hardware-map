# `_UIValueCellContentViewConfiguration`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIContentViewConfiguration`, `NSSecureCoding`
- 9 instance variables, 11 properties, 21 instance methods, 6 class methods

## Instance variables

```
{?="hasCustomizedAxesPreservingSuperviewLayoutMargins"b1"hasCustomizedDirectionalLayoutMargins"b1"hasCustomizedImageToTextPadding"b1"hasCustomizedTextToValuePadding"b1} _configurationFlags;
Q _axesPreservingSuperviewLayoutMargins;
d _imageToTextPadding;
q _defaultStyle;
@"_UIContentViewImageViewConfiguration" _imageView;
@"_UIContentViewLabelConfiguration" _textLabel;
@"_UIContentViewLabelConfiguration" _valueLabel;
{UIOffset="horizontal"d"vertical"d} _textToValuePadding;
{NSDirectionalEdgeInsets="top"d"leading"d"bottom"d"trailing"d} _directionalLayoutMargins;
```

## Properties

```
@property (T@"_UIContentViewImageViewConfiguration",R,N,V_imageView) imageView;
@property (T@"_UIContentViewLabelConfiguration",R,N,V_textLabel) textLabel;
@property (T@"_UIContentViewLabelConfiguration",R,N,V_valueLabel) valueLabel;
@property (TQ,N) axesPreservingSuperviewLayoutMargins;
@property (T{NSDirectionalEdgeInsets=dddd},N) directionalLayoutMargins;
@property (Td,N) imageToTextPadding;
@property (T{UIOffset=dd},N) textToValuePadding;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UIValueCellContentViewConfiguration supportsSecureCoding];
+[_UIValueCellContentViewConfiguration listCellConfiguration];
+[_UIValueCellContentViewConfiguration defaultConfiguration];
+[_UIValueCellContentViewConfiguration defaultListCellConfigurationForState:];
+[_UIValueCellContentViewConfiguration defaultOutlineCellConfigurationForState:];
+[_UIValueCellContentViewConfiguration outlineCellConfiguration];
```

## Instance methods

```
-[_UIValueCellContentViewConfiguration valueLabel];
-[_UIValueCellContentViewConfiguration directionalLayoutMargins];
-[_UIValueCellContentViewConfiguration setDirectionalLayoutMargins:];
-[_UIValueCellContentViewConfiguration textLabel];
-[_UIValueCellContentViewConfiguration updatedConfigurationForState:];
-[_UIValueCellContentViewConfiguration encodeWithCoder:];
-[_UIValueCellContentViewConfiguration imageToTextPadding];
-[_UIValueCellContentViewConfiguration hash];
-[_UIValueCellContentViewConfiguration description];
-[_UIValueCellContentViewConfiguration setAxesPreservingSuperviewLayoutMargins:];
-[_UIValueCellContentViewConfiguration initWithCoder:];
-[_UIValueCellContentViewConfiguration setImageToTextPadding:];
-[_UIValueCellContentViewConfiguration copyWithZone:];
-[_UIValueCellContentViewConfiguration axesPreservingSuperviewLayoutMargins];
-[_UIValueCellContentViewConfiguration imageView];
-[_UIValueCellContentViewConfiguration isEqual:];
-[_UIValueCellContentViewConfiguration applyToContentView:];
-[_UIValueCellContentViewConfiguration createContentView];
-[_UIValueCellContentViewConfiguration setTextToValuePadding:];
-[_UIValueCellContentViewConfiguration textToValuePadding];
-[_UIValueCellContentViewConfiguration updatedConfigurationForState:traitCollection:];
```
