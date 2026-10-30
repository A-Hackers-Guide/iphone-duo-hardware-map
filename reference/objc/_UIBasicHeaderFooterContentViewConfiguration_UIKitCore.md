# `_UIBasicHeaderFooterContentViewConfiguration`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIContentViewConfiguration`, `NSSecureCoding`
- 5 instance variables, 8 properties, 17 instance methods, 5 class methods

## Instance variables

```
{?="hasCustomizedAxesPreservingSuperviewLayoutMargins"b1"hasCustomizedDirectionalLayoutMargins"b1} _configurationFlags;
Q _axesPreservingSuperviewLayoutMargins;
q _defaultStyle;
@"_UIContentViewLabelConfiguration" _textLabel;
{NSDirectionalEdgeInsets="top"d"leading"d"bottom"d"trailing"d} _directionalLayoutMargins;
```

## Properties

```
@property (T@"_UIContentViewLabelConfiguration",R,N,V_textLabel) textLabel;
@property (TQ,N) axesPreservingSuperviewLayoutMargins;
@property (T{NSDirectionalEdgeInsets=dddd},N) directionalLayoutMargins;
@property (TB,N) resetsVerticalLayoutMargins;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UIBasicHeaderFooterContentViewConfiguration supportsSecureCoding];
+[_UIBasicHeaderFooterContentViewConfiguration defaultFooterConfiguration];
+[_UIBasicHeaderFooterContentViewConfiguration defaultGroupedFooterConfiguration];
+[_UIBasicHeaderFooterContentViewConfiguration defaultGroupedHeaderConfiguration];
+[_UIBasicHeaderFooterContentViewConfiguration defaultHeaderConfiguration];
```

## Instance methods

```
-[_UIBasicHeaderFooterContentViewConfiguration directionalLayoutMargins];
-[_UIBasicHeaderFooterContentViewConfiguration setDirectionalLayoutMargins:];
-[_UIBasicHeaderFooterContentViewConfiguration textLabel];
-[_UIBasicHeaderFooterContentViewConfiguration updatedConfigurationForState:];
-[_UIBasicHeaderFooterContentViewConfiguration encodeWithCoder:];
-[_UIBasicHeaderFooterContentViewConfiguration hash];
-[_UIBasicHeaderFooterContentViewConfiguration description];
-[_UIBasicHeaderFooterContentViewConfiguration setAxesPreservingSuperviewLayoutMargins:];
-[_UIBasicHeaderFooterContentViewConfiguration initWithCoder:];
-[_UIBasicHeaderFooterContentViewConfiguration copyWithZone:];
-[_UIBasicHeaderFooterContentViewConfiguration axesPreservingSuperviewLayoutMargins];
-[_UIBasicHeaderFooterContentViewConfiguration isEqual:];
-[_UIBasicHeaderFooterContentViewConfiguration setResetsVerticalLayoutMargins:];
-[_UIBasicHeaderFooterContentViewConfiguration applyToContentView:];
-[_UIBasicHeaderFooterContentViewConfiguration createContentView];
-[_UIBasicHeaderFooterContentViewConfiguration resetsVerticalLayoutMargins];
-[_UIBasicHeaderFooterContentViewConfiguration updatedConfigurationForState:traitCollection:];
```
