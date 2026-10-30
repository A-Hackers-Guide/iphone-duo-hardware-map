# `UISwitch`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIControl`
- Protocols: `UISwitchControl`, `UISwitchVisualElementProvider`, `NSCoding`
- 12 instance variables, 17 properties, 62 instance methods, 5 class methods

## Instance variables

```
B _on;
B _alwaysShowOnOffLabel;
@"NSString" _title;
@"UIColor" _onTintColor;
@"UIColor" _thumbTintColor;
@"UIImage" _onImage;
@"UIImage" _offImage;
q _style;
q _preferredStyle;
@"UIColor" _tintColor;
@"UISwitchVisualElement" _visualElement;
q _switchStyle;
```

## Properties

```
@property (T@"UIColor",&,N,V_tintColor) tintColor;
@property (T@"UISwitchVisualElement",&,N,V_visualElement) visualElement;
@property (TB,N,G_alwaysShowOnOffLabel,S_setAlwaysShowsOnOffLabel:,V_alwaysShowOnOffLabel) alwaysShowOnOffLabel;
@property (T@"UIImpactFeedbackGenerator",&,N,G_impactFeedbackGenerator,S_setImpactFeedbackGenerator:) impactFeedbackGenerator;
@property (Tq,N,V_switchStyle) switchStyle;
@property (T@"UIColor",&,N,V_onTintColor) onTintColor;
@property (T@"UIColor",&,N,V_thumbTintColor) thumbTintColor;
@property (T@"UIImage",&,N,V_onImage) onImage;
@property (T@"UIImage",&,N,V_offImage) offImage;
@property (T@"NSString",C,N,V_title) title;
@property (Tq,R,N,V_style) style;
@property (Tq,N,V_preferredStyle) preferredStyle;
@property (TB,N,GisOn,V_on) on;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UISwitch visualElementForTraitCollection:style:];
+[UISwitch setVisualElementProvider:];
+[UISwitch _setAllowsUnsupportedMacIdiomBehavior:];
+[UISwitch visualElementForTraitCollection:];
+[UISwitch _allowsUnsupportedMacIdiomBehavior];
```

## Instance methods

```
-[UISwitch _controlEventsForActionTriggered];
-[UISwitch setOnTintColor:];
-[UISwitch _intrinsicContentSizeInvalidatedForChildView:];
-[UISwitch setOnImage:];
-[UISwitch pointerInteraction:styleForRegion:];
-[UISwitch _intrinsicSizeWithinSize:];
-[UISwitch init];
-[UISwitch alignmentRectInsets];
-[UISwitch pointerInteraction:willEnterRegion:animator:];
-[UISwitch pointerInteraction:willExitRegion:animator:];
-[UISwitch offImage];
-[UISwitch dealloc];
-[UISwitch setOn:animated:];
-[UISwitch style];
-[UISwitch setSemanticContentAttribute:];
-[UISwitch preferredStyle];
-[UISwitch sizeThatFits:];
-[UISwitch _contentHuggingDefault_isUsuallyFixedHeight];
-[UISwitch tintColorDidChange];
-[UISwitch thumbTintColor];
-[UISwitch _setStyle:];
-[UISwitch setTintColor:];
-[UISwitch title];
-[UISwitch setEnabled:];
-[UISwitch encodeWithCoder:];
-[UISwitch setOffImage:];
-[UISwitch pointerInteraction:regionForRequest:defaultRegion:];
-[UISwitch setOn:];
-[UISwitch setFrame:];
-[UISwitch isElementAccessibilityExposedToInterfaceBuilder];
-[UISwitch tintColor];
-[UISwitch initWithCoder:];
-[UISwitch setTitle:];
-[UISwitch isOn];
-[UISwitch _populateArchivedSubviews:];
-[UISwitch setThumbTintColor:];
-[UISwitch accessibilityActivationPoint];
-[UISwitch onImage];
-[UISwitch initWithFrame:];
-[UISwitch _layoutSizeThatFits:fixedAxes:];
-[UISwitch _contentHuggingDefault_isUsuallyFixedWidth];
-[UISwitch isAccessibilityElementByDefault];
-[UISwitch setSwitchStyle:];
-[UISwitch visualElement:transitionedToOn:];
-[UISwitch _alwaysShowOnOffLabel];
-[UISwitch _impactFeedbackGenerator];
-[UISwitch _isFixedSize];
-[UISwitch _refreshVisualElement];
-[UISwitch _refreshVisualElementForTraitCollection:populatingAPIProperties:];
-[UISwitch _setAlwaysShowsOnOffLabel:];
-[UISwitch _setImpactFeedbackGenerator:];
-[UISwitch _shouldShowOnOffLabels];
-[UISwitch _showingOnOffLabelChanged];
-[UISwitch defaultAccessibilityTraits];
-[UISwitch onTintColor];
-[UISwitch pointMostlyInside:];
-[UISwitch setOn:animated:notifyingVisualElement:];
-[UISwitch setPreferredStyle:];
-[UISwitch setVisualElement:];
-[UISwitch switchStyle];
-[UISwitch visualElement];
-[UISwitch visualElementHadTouchUpInside:];
```
