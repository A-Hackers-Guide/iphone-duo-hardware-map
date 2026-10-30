# `_UIBasicCellContentViewConfiguration`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIContentViewConfiguration`, `NSSecureCoding`
- 8 instance variables, 10 properties, 20 instance methods, 8 class methods

## Instance variables

```
{?="hasCustomizedAxesPreservingSuperviewLayoutMargins"b1"hasCustomizedDirectionalLayoutMargins"b1"hasCustomizedImageToTextPadding"b1} _configurationFlags;
Q _axesPreservingSuperviewLayoutMargins;
d _imageToTextPadding;
@"_UIContentViewEditingConfiguration" _textLabelEditingConfiguration;
q _defaultStyle;
@"_UIContentViewImageViewConfiguration" _imageView;
@"_UIContentViewLabelConfiguration" _textLabel;
{NSDirectionalEdgeInsets="top"d"leading"d"bottom"d"trailing"d} _directionalLayoutMargins;
```

## Properties

```
@property (T@"_UIContentViewImageViewConfiguration",R,N,V_imageView) imageView;
@property (T@"_UIContentViewLabelConfiguration",R,N,V_textLabel) textLabel;
@property (TQ,N) axesPreservingSuperviewLayoutMargins;
@property (T{NSDirectionalEdgeInsets=dddd},N) directionalLayoutMargins;
@property (Td,N) imageToTextPadding;
@property (T@"_UIContentViewEditingConfiguration",C,N,V_textLabelEditingConfiguration) _textLabelEditingConfiguration;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UIBasicCellContentViewConfiguration supportsSecureCoding];
+[_UIBasicCellContentViewConfiguration listCellConfiguration];
+[_UIBasicCellContentViewConfiguration defaultConfiguration];
+[_UIBasicCellContentViewConfiguration defaultListCellConfigurationForState:];
+[_UIBasicCellContentViewConfiguration defaultOutlineCellConfigurationForState:];
+[_UIBasicCellContentViewConfiguration defaultOutlineParentCellConfigurationForState:];
+[_UIBasicCellContentViewConfiguration outlineCellConfiguration];
+[_UIBasicCellContentViewConfiguration outlineRootParentCellConfiguration];
```

## Instance methods

```
-[_UIBasicCellContentViewConfiguration directionalLayoutMargins];
-[_UIBasicCellContentViewConfiguration setDirectionalLayoutMargins:];
-[_UIBasicCellContentViewConfiguration textLabel];
-[_UIBasicCellContentViewConfiguration updatedConfigurationForState:];
-[_UIBasicCellContentViewConfiguration encodeWithCoder:];
-[_UIBasicCellContentViewConfiguration imageToTextPadding];
-[_UIBasicCellContentViewConfiguration hash];
-[_UIBasicCellContentViewConfiguration description];
-[_UIBasicCellContentViewConfiguration setAxesPreservingSuperviewLayoutMargins:];
-[_UIBasicCellContentViewConfiguration initWithCoder:];
-[_UIBasicCellContentViewConfiguration setImageToTextPadding:];
-[_UIBasicCellContentViewConfiguration copyWithZone:];
-[_UIBasicCellContentViewConfiguration axesPreservingSuperviewLayoutMargins];
-[_UIBasicCellContentViewConfiguration imageView];
-[_UIBasicCellContentViewConfiguration isEqual:];
-[_UIBasicCellContentViewConfiguration _textLabelEditingConfiguration];
-[_UIBasicCellContentViewConfiguration applyToContentView:];
-[_UIBasicCellContentViewConfiguration createContentView];
-[_UIBasicCellContentViewConfiguration set_textLabelEditingConfiguration:];
-[_UIBasicCellContentViewConfiguration updatedConfigurationForState:traitCollection:];
```
