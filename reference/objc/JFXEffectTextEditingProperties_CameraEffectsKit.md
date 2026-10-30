# `JFXEffectTextEditingProperties`

- Image: [`/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit`](../userland/System__Library__PrivateFrameworks__CameraEffectsKit.framework__CameraEffectsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 21 instance variables, 26 properties, 55 instance methods, 1 class methods

## Instance variables

```
B _useFullTransform;
B _isAllCaps;
B _isEmoji;
B _isTextFlipped;
B _outlineDisabled;
B _moveBeforeScalingToAvoidKeyboard;
B _isSpecialCaseForGameOverPoster;
@"JFXTextEffectFrame" _effectFrame;
@"NSAttributedString" _attributedText;
@"NSDictionary" _defaultTypingAttributes;
q _textAlignment;
Q _numberOfLines;
d _baselineYOffset;
@"UIColor" _defaultTextColor;
@"UIColor" _customTextColor;
@"UIColor" _customTextEditTintColor;
@"NSValue" _cachedScale;
@"NSNumber" _cachedRotation;
@"PVMatrix44Double" _cachedPartialTransformNoScaleNoTranslation;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _cachedFrame;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _cachedBounds;
```

## Properties

```
@property (T@"JFXTextEffectFrame",&,N,V_effectFrame) effectFrame;
@property (T@"NSAttributedString",C,N,V_attributedText) attributedText;
@property (T@"NSDictionary",C,N,V_defaultTypingAttributes) defaultTypingAttributes;
@property (TB,N,V_useFullTransform) useFullTransform;
@property (TB,N,V_isAllCaps) isAllCaps;
@property (TB,N,V_isEmoji) isEmoji;
@property (TB,N,V_isTextFlipped) isTextFlipped;
@property (TB,N,GisOutlineDisabled,V_outlineDisabled) outlineDisabled;
@property (TB,N,V_moveBeforeScalingToAvoidKeyboard) moveBeforeScalingToAvoidKeyboard;
@property (T@"UIColor",C,N,V_defaultTextColor) defaultTextColor;
@property (T@"UIColor",C,N,V_customTextColor) customTextColor;
@property (T@"UIColor",C,N,V_customTextEditTintColor) customTextEditTintColor;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_cachedFrame) cachedFrame;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_cachedBounds) cachedBounds;
@property (T@"NSValue",&,N,V_cachedScale) cachedScale;
@property (T@"NSNumber",&,N,V_cachedRotation) cachedRotation;
@property (T@"PVMatrix44Double",&,N,V_cachedPartialTransformNoScaleNoTranslation) cachedPartialTransformNoScaleNoTranslation;
@property (Tq,N,V_textAlignment) textAlignment;
@property (TQ,N,V_numberOfLines) numberOfLines;
@property (Td,N,V_baselineYOffset) baselineYOffset;
@property (TB,N,V_isSpecialCaseForGameOverPoster) isSpecialCaseForGameOverPoster;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) frame;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) bounds;
@property (T{CGPoint=dd},R,N) scale;
@property (Td,R,N) rotation;
@property (T{CGAffineTransform=dddddd},R,N) partialTransformNoScaleNoTranslation;
```

## Class methods

```
+[JFXEffectTextEditingProperties textEditingPropertiesWithTextEffect:withText:relativeTo:atTime:index:moveBeforeScalingToAvoidKeyboard:];
```

## Instance methods

```
-[JFXEffectTextEditingProperties setTextAlignment:];
-[JFXEffectTextEditingProperties setCachedBounds:];
-[JFXEffectTextEditingProperties rotation];
-[JFXEffectTextEditingProperties textAlignment];
-[JFXEffectTextEditingProperties cachedFrame];
-[JFXEffectTextEditingProperties numberOfLines];
-[JFXEffectTextEditingProperties setAttributedText:];
-[JFXEffectTextEditingProperties setCustomTextColor:];
-[JFXEffectTextEditingProperties defaultTextColor];
-[JFXEffectTextEditingProperties setCachedFrame:];
-[JFXEffectTextEditingProperties scale];
-[JFXEffectTextEditingProperties cachedBounds];
-[JFXEffectTextEditingProperties attributedText];
-[JFXEffectTextEditingProperties setNumberOfLines:];
-[JFXEffectTextEditingProperties bounds];
-[JFXEffectTextEditingProperties description];
-[JFXEffectTextEditingProperties customTextColor];
-[JFXEffectTextEditingProperties frame];
-[JFXEffectTextEditingProperties setDefaultTextColor:];
-[JFXEffectTextEditingProperties baselineYOffset];
-[JFXEffectTextEditingProperties JFX_configureWithAttributedString:text:];
-[JFXEffectTextEditingProperties JFX_configureWithEffect:];
-[JFXEffectTextEditingProperties JFX_modifyEntireAttributedString:forTargetSize:fontColor:];
-[JFXEffectTextEditingProperties JFX_configureWithDefaultTypingAttributes:];
-[JFXEffectTextEditingProperties JFX_modifyAttributedString:];
-[JFXEffectTextEditingProperties JFX_modifyRangesOfAttributedString:isOutlineDisabled:];
-[JFXEffectTextEditingProperties isEmoji];
-[JFXEffectTextEditingProperties setCachedScale:];
-[JFXEffectTextEditingProperties setEffectFrame:];
-[JFXEffectTextEditingProperties cachedPartialTransformNoScaleNoTranslation];
-[JFXEffectTextEditingProperties cachedRotation];
-[JFXEffectTextEditingProperties cachedScale];
-[JFXEffectTextEditingProperties customTextEditTintColor];
-[JFXEffectTextEditingProperties defaultTypingAttributes];
-[JFXEffectTextEditingProperties effectFrame];
-[JFXEffectTextEditingProperties initWithTextEffect:withText:relativeTo:atTime:index:moveBeforeScalingToAvoidKeyboard:];
-[JFXEffectTextEditingProperties isAllCaps];
-[JFXEffectTextEditingProperties isOutlineDisabled];
-[JFXEffectTextEditingProperties isSpecialCaseForGameOverPoster];
-[JFXEffectTextEditingProperties isTextFlipped];
-[JFXEffectTextEditingProperties moveBeforeScalingToAvoidKeyboard];
-[JFXEffectTextEditingProperties partialTransformNoScaleNoTranslation];
-[JFXEffectTextEditingProperties setBaselineYOffset:];
-[JFXEffectTextEditingProperties setCachedPartialTransformNoScaleNoTranslation:];
-[JFXEffectTextEditingProperties setCachedRotation:];
-[JFXEffectTextEditingProperties setCustomTextEditTintColor:];
-[JFXEffectTextEditingProperties setDefaultTypingAttributes:];
-[JFXEffectTextEditingProperties setIsAllCaps:];
-[JFXEffectTextEditingProperties setIsEmoji:];
-[JFXEffectTextEditingProperties setIsSpecialCaseForGameOverPoster:];
-[JFXEffectTextEditingProperties setIsTextFlipped:];
-[JFXEffectTextEditingProperties setMoveBeforeScalingToAvoidKeyboard:];
-[JFXEffectTextEditingProperties setOutlineDisabled:];
-[JFXEffectTextEditingProperties setUseFullTransform:];
-[JFXEffectTextEditingProperties useFullTransform];
```
