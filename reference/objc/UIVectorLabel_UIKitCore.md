# `UIVectorLabel`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 9 instance variables, 7 properties, 44 instance methods, 3 class methods

## Instance variables

```
@"_UILabelContent" _content;
@"NSMutableDictionary" _defaultAttributes;
@"UIColor" _textColor;
@"_UIVectorTextLayout" _sizingLayout;
@"_UIVectorTextLayout" _visualLayout;
{?="usesExplicitPreferredMaxLayoutWidth"b1} _labelFlags;
d _multilineContextWidth;
Q _numberOfLines;
d _preferredMaxLayoutWidth;
```

## Properties

```
@property (T@"_UILabelContent",&,N,G_content,S_setContent:) _content;
@property (T@"NSString",C,N) text;
@property (T@"UIColor",&,N) textColor;
@property (T@"UIFont",&,N) font;
@property (TQ,N,V_numberOfLines) numberOfLines;
@property (Td,N,V_preferredMaxLayoutWidth) preferredMaxLayoutWidth;
@property (T@"NSAttributedString",C,N,S_setAttributedText:) _attributedText;
```

## Class methods

```
+[UIVectorLabel layerClass];
+[UIVectorLabel _defaultAttributes];
+[UIVectorLabel _defaultFont];
```

## Instance methods

```
-[UIVectorLabel _setTextColor:];
-[UIVectorLabel _preferredMaxLayoutWidth];
-[UIVectorLabel intrinsicContentSize];
-[UIVectorLabel _multilineContextWidth];
-[UIVectorLabel text];
-[UIVectorLabel _generateDeferredAnimations:];
-[UIVectorLabel _intrinsicSizeWithinSize:];
-[UIVectorLabel textColor];
-[UIVectorLabel numberOfLines];
-[UIVectorLabel setTextColor:];
-[UIVectorLabel _prepareForSecondIntrinsicContentSizeCalculationWithLayoutEngineBounds:];
-[UIVectorLabel layoutSubviews];
-[UIVectorLabel setBounds:];
-[UIVectorLabel _setMultilineContextWidth:];
-[UIVectorLabel _prepareForFirstIntrinsicContentSizeCalculation];
-[UIVectorLabel sizeThatFits:];
-[UIVectorLabel _needsDoubleUpdateConstraintsPass];
-[UIVectorLabel textRectForBounds:limitedToNumberOfLines:];
-[UIVectorLabel setNumberOfLines:];
-[UIVectorLabel setFrame:];
-[UIVectorLabel setText:];
-[UIVectorLabel font];
-[UIVectorLabel _defaultAttributes];
-[UIVectorLabel _shouldAnimatePropertyWithKey:];
-[UIVectorLabel setPreferredMaxLayoutWidth:];
-[UIVectorLabel initWithFrame:];
-[UIVectorLabel _baselineOffsetFromBottom];
-[UIVectorLabel preferredMaxLayoutWidth];
-[UIVectorLabel setFont:];
-[UIVectorLabel _attributedText];
-[UIVectorLabel _attributedTextCompatibleForSizing];
-[UIVectorLabel _content];
-[UIVectorLabel _ensureSizingLayout];
-[UIVectorLabel _ensureVisualLayout];
-[UIVectorLabel _firstBaselineOffsetFromTop];
-[UIVectorLabel _firstLineBaseline];
-[UIVectorLabel _labelLayer];
-[UIVectorLabel _lastLineBaseline];
-[UIVectorLabel _layoutParametersWithinSize:forSizing:];
-[UIVectorLabel _materializedAttributedText];
-[UIVectorLabel _mergeDefaultAttributesForDowngradingContent:];
-[UIVectorLabel _setAttributedText:];
-[UIVectorLabel _setContent:];
-[UIVectorLabel _setNeedsUpdateLayerIfNeeded];
```
