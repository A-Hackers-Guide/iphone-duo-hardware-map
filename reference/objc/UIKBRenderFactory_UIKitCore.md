# `UIKBRenderFactory`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 16 instance variables, 24 properties, 140 instance methods, 13 class methods

## Instance variables

```
@"UIKBRenderingContext" _renderingContext;
@"NSMutableArray" _segmentTraits;
B _suppressSegmentTraits;
d _rivenSizeFactor;
B _lightweightFactory;
d _scale;
{CGSize="width"d"height"d} _stretchFactor;
B _boldTextEnabled;
B _increasedContrastEnabled;
B _reduceHighlightingEffectsEnabled;
B _allowsPaddles;
B _preferStringKeycapOverImage;
B _drawsOneHandedAffordance;
B _dynamicFactory;
d _currentHeight;
d _wideKeyboardMiddlePadding;
```

## Properties

```
@property (T@"NSArray",R,N,V_segmentTraits) segmentTraits;
@property (Td,N,V_rivenSizeFactor) rivenSizeFactor;
@property (TB,N,V_lightweightFactory) lightweightFactory;
@property (TB,N,V_increasedContrastEnabled) increasedContrastEnabled;
@property (TB,N,V_reduceHighlightingEffectsEnabled) reduceHighlightingEffectsEnabled;
@property (T@"NSString",R,N) shortClassNameForCaching;
@property (Td,N,V_scale) scale;
@property (T{CGSize=dd},N,V_stretchFactor) stretchFactor;
@property (T@"UIKBRenderingContext",&,N,V_renderingContext) renderingContext;
@property (T@"UIKBRenderConfig",R,GrenderConfig) renderConfig;
@property (TB,N,V_allowsPaddles) allowsPaddles;
@property (TB,N,V_preferStringKeycapOverImage) preferStringKeycapOverImage;
@property (TB,R,N,V_boldTextEnabled) boldTextEnabled;
@property (TB,N,V_drawsOneHandedAffordance) drawsOneHandedAffordance;
@property (Tq,R,N) assetIdiom;
@property (TB,N,V_dynamicFactory) dynamicFactory;
@property (TB,N) isKeyboardMinorEdgeWidth;
@property (Tq,N) keyboardVerticalSizeClass;
@property (Tq,N) keyboardHorizontalSizeClass;
@property (Tq,N) currentHandBias;
@property (Td,N,V_currentHeight) currentHeight;
@property (T{UIEdgeInsets=dddd},R,N) dynamicInsets;
@property (Td,R,N,V_wideKeyboardMiddlePadding) wideKeyboardMiddlePadding;
@property (Td,R,N) dynamicBottomRowMultiplier;
```

## Class methods

```
+[UIKBRenderFactory _graphicsQuality];
+[UIKBRenderFactory _characterSetForGlyphSelectors];
+[UIKBRenderFactory _enabled];
+[UIKBRenderFactory cacheKeyForString:withRenderFlags:renderConfig:];
+[UIKBRenderFactory couldUseGlyphSelectorForDisplayString:];
+[UIKBRenderFactory displayStringContainsOnlyLowercaseLetters:];
+[UIKBRenderFactory factoryClassForLayoutClass:visualStyling:renderingContext:];
+[UIKBRenderFactory factoryClassForVisualStyle:renderingContext:];
+[UIKBRenderFactory factoryForLayoutClass:visualStyle:renderingContext:skipLayoutSegments:];
+[UIKBRenderFactory factoryForVisualStyle:renderingContext:];
+[UIKBRenderFactory factoryForVisualStyle:renderingContext:skipLayoutSegments:];
+[UIKBRenderFactory lightweightFactoryForVisualStyle:renderingContext:];
+[UIKBRenderFactory segmentedControlColor:];
```

## Instance methods

```
-[UIKBRenderFactory currentHandBias];
-[UIKBRenderFactory assetIdiom];
-[UIKBRenderFactory renderingContext];
-[UIKBRenderFactory reduceHighlightingEffectsEnabled];
-[UIKBRenderFactory setRenderingContext:];
-[UIKBRenderFactory renderConfig];
-[UIKBRenderFactory stretchFactor];
-[UIKBRenderFactory currentHeight];
-[UIKBRenderFactory muttitapReverseKeyImageName];
-[UIKBRenderFactory setIncreasedContrastEnabled:];
-[UIKBRenderFactory dynamicBottomRowMultiplier];
-[UIKBRenderFactory supportsPaddles];
-[UIKBRenderFactory setAllowsPaddles:];
-[UIKBRenderFactory dynamicInsets];
-[UIKBRenderFactory increasedContrastEnabled];
-[UIKBRenderFactory keyCornerRadius];
-[UIKBRenderFactory setScale:];
-[UIKBRenderFactory thinKeycapsFontNameForKey:];
-[UIKBRenderFactory skinnyKeyThreshold];
-[UIKBRenderFactory setReduceHighlightingEffectsEnabled:];
-[UIKBRenderFactory lightKeycapsFontNameForKey:];
-[UIKBRenderFactory _traitsForKey:onKeyplane:];
-[UIKBRenderFactory traitsHashStringForKey:withGeometry:withSymbolStyle:controlOpacities:blendForm:blurBlending:renderConfig:];
-[UIKBRenderFactory scale];
-[UIKBRenderFactory shouldClearBaseDisplayStringForVariants:];
-[UIKBRenderFactory allowsPaddles];
-[UIKBRenderFactory setStretchFactor:];
-[UIKBRenderFactory emojiPopupDividerKeyOffset];
-[UIKBRenderFactory setCurrentHandBias:];
-[UIKBRenderFactory lightKeycapsFontFallbackName];
-[UIKBRenderFactory isKeyboardMinorEdgeWidth];
-[UIKBRenderFactory _customizeTraits:forPopupForKey:withRenderingContext:keycapsFontName:fallbackFontName:];
-[UIKBRenderFactory messagesWriteboardKeyImageName];
-[UIKBRenderFactory multitapCompleteKeyImageName];
-[UIKBRenderFactory dynamicInsetsForNumberOfRows:];
-[UIKBRenderFactory RivenFactor:];
-[UIKBRenderFactory cutKeyImageName];
-[UIKBRenderFactory setKeyboardHorizontalSizeClass:];
-[UIKBRenderFactory RivenPointFactor:];
-[UIKBRenderFactory biuKeyImageName];
-[UIKBRenderFactory boldTextEnabled];
-[UIKBRenderFactory lightPadKeycapsFontFallbackName];
-[UIKBRenderFactory passcodeShiftedControlKeyTraits];
-[UIKBRenderFactory rivenSizeFactor];
-[UIKBRenderFactory setPreferStringKeycapOverImage:];
-[UIKBRenderFactory spaceKeyGrabberHandlesImageName];
-[UIKBRenderFactory ZWNJKeyImageName];
-[UIKBRenderFactory _controlKeyBackgroundColorName];
-[UIKBRenderFactory _customizeTraits:forPopupForKey:withRenderingContext:keycapsFontName:];
-[UIKBRenderFactory _defaultControlKeyBackgroundColorName];
-[UIKBRenderFactory addLayoutSegment:];
-[UIKBRenderFactory additionalDynamicDrawingInsets];
-[UIKBRenderFactory allowsPaddleForKey:];
-[UIKBRenderFactory applyBoldTextForContent:withKey:];
-[UIKBRenderFactory backgroundTraitsForKeyplane:];
-[UIKBRenderFactory blackKeycapColor];
-[UIKBRenderFactory boldKeyImageName];
-[UIKBRenderFactory compactFontCanRenderKeyGlyph:];
-[UIKBRenderFactory contentViewClassNameForPopupKey:];
-[UIKBRenderFactory controlKeyBackgroundColorName];
-[UIKBRenderFactory controlKeyForegroundColorName];
-[UIKBRenderFactory controlKeyShadowColorName];
-[UIKBRenderFactory copyKeyImageName];
-[UIKBRenderFactory customizeLanguageIndicatorTraitsForTraits:];
-[UIKBRenderFactory customizeMicOnTraitsForTraits:lightKeyboard:keyState:];
-[UIKBRenderFactory defaultKeyBackgroundColorName];
-[UIKBRenderFactory defaultKeyShadowColorName];
-[UIKBRenderFactory deleteKeyImageName];
-[UIKBRenderFactory deleteOnKeyImageName];
-[UIKBRenderFactory dictationKeyImageName];
-[UIKBRenderFactory dismissKeyImageName];
-[UIKBRenderFactory displayContentsForKey:];
-[UIKBRenderFactory drawsOneHandedAffordance];
-[UIKBRenderFactory dualStringKeyBottomTextOffset:keyplane:];
-[UIKBRenderFactory dualStringKeyTopTextOffset:keyplane:];
-[UIKBRenderFactory dynamicFactory];
-[UIKBRenderFactory enabledBlendForm];
-[UIKBRenderFactory extraPasscodePaddleTraits];
-[UIKBRenderFactory globalEmojiKeyImageName];
-[UIKBRenderFactory globalKeyImageName];
-[UIKBRenderFactory globalWithBackChevronKeyImageName];
-[UIKBRenderFactory glyphSelectorForDisplayString:];
-[UIKBRenderFactory handwritingMoreKeyImageName];
-[UIKBRenderFactory hashStringElement];
-[UIKBRenderFactory imageNameForReturnKey:];
-[UIKBRenderFactory initWithRenderingContext:skipLayoutSegments:];
-[UIKBRenderFactory keyImageNameWithSkinnyVariation:];
-[UIKBRenderFactory keyIsRightToLeftSensitive:];
-[UIKBRenderFactory keyboardHorizontalSizeClass];
-[UIKBRenderFactory keyboardVerticalSizeClass];
-[UIKBRenderFactory leftArrowKeyImageName];
-[UIKBRenderFactory lightHighQualityEnabledBlendForm];
-[UIKBRenderFactory lightPadKeycapsFontNameForKey:];
-[UIKBRenderFactory lightTextFontFallbackName];
-[UIKBRenderFactory lightTextFontNameForKey:];
-[UIKBRenderFactory lightweightFactory];
-[UIKBRenderFactory lowQualityLayeredBackgroundColorName];
-[UIKBRenderFactory lowQualityTraits:];
-[UIKBRenderFactory modifyKeyTraitsForPasscode:forKey:onKeyplane:];
-[UIKBRenderFactory modifyTraitsForDetachedInputSwitcher:withKey:];
-[UIKBRenderFactory modifyTraitsForDividerVariant:withKey:];
-[UIKBRenderFactory passcodeActiveControlKeyTraits];
-[UIKBRenderFactory passcodeBackgroundTraitsForKeyplane:];
-[UIKBRenderFactory passcodeControlKeyTraits];
-[UIKBRenderFactory passcodeEdgeWeight];
-[UIKBRenderFactory passcodeKeyEdgeColorName];
-[UIKBRenderFactory pasteKeyImageName];
-[UIKBRenderFactory popupKeyUsesCustomKeyContentView:];
-[UIKBRenderFactory preferStringKeycapOverImage];
-[UIKBRenderFactory redoKeyImageName];
-[UIKBRenderFactory rightArrowKeyImageName];
-[UIKBRenderFactory scaleTraits:];
-[UIKBRenderFactory segmentTraits];
-[UIKBRenderFactory setCurrentHeight:];
-[UIKBRenderFactory setDrawsOneHandedAffordance:];
-[UIKBRenderFactory setDynamicFactory:];
-[UIKBRenderFactory setIsKeyboardMinorEdgeWidth:];
-[UIKBRenderFactory setKeyboardVerticalSizeClass:];
-[UIKBRenderFactory setLightweightFactory:];
-[UIKBRenderFactory setRivenSizeFactor:];
-[UIKBRenderFactory setupLayoutSegments];
-[UIKBRenderFactory shiftKeyImageName];
-[UIKBRenderFactory shiftLockImageName];
-[UIKBRenderFactory shiftOnKeyImageName];
-[UIKBRenderFactory shortClassNameForCaching];
-[UIKBRenderFactory shouldKeepBackgroundInEmojiInputModeForKey:];
-[UIKBRenderFactory shouldOverlayAlternateTagKey:onKeyplane:];
-[UIKBRenderFactory shouldOverlayDictationKey:onKeyplane:];
-[UIKBRenderFactory shouldOverlayTraitsForKey:onKeyplane:];
-[UIKBRenderFactory shouldUpdateFocusSizeForContentSizeCategory];
-[UIKBRenderFactory supportsInputTraits:forKeyplane:];
-[UIKBRenderFactory suppressLayoutSegments];
-[UIKBRenderFactory thinKeycapsFontFallbackName];
-[UIKBRenderFactory thinTextFontFallbackName];
-[UIKBRenderFactory thinTextFontNameForKey:];
-[UIKBRenderFactory traitsForKey:onKeyplane:];
-[UIKBRenderFactory translucentGapWidth];
-[UIKBRenderFactory undoKeyImageName];
-[UIKBRenderFactory useBlueThemingForKey:];
-[UIKBRenderFactory wideKeyboardMiddlePadding];
```
