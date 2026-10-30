# `UIKBDynamicRenderFactory`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIKBRenderFactoryiPhone`
- 6 instance variables, 1 properties, 140 instance methods, 1 class methods

## Instance variables

```
B _isKeyboardMinorEdgeWidth;
q _keyboardVerticalSizeClass;
q _keyboardHorizontalSizeClass;
q _currentHandBias;
d _currentHeight;
d _emojiWideEdgeControlKeyCapsuleHeight;
```

## Properties

```
@property (Td,N,V_emojiWideEdgeControlKeyCapsuleHeight) emojiWideEdgeControlKeyCapsuleHeight;
```

## Class methods

```
+[UIKBDynamicRenderFactory _textOffsetHints];
```

## Instance methods

```
-[UIKBDynamicRenderFactory isSplit];
-[UIKBDynamicRenderFactory currentHandBias];
-[UIKBDynamicRenderFactory assetIdiom];
-[UIKBDynamicRenderFactory isFloating];
-[UIKBDynamicRenderFactory currentHeight];
-[UIKBDynamicRenderFactory muttitapReverseKeyImageName];
-[UIKBDynamicRenderFactory dynamicBottomRowMultiplier];
-[UIKBDynamicRenderFactory supportsPaddles];
-[UIKBDynamicRenderFactory dynamicInsets];
-[UIKBDynamicRenderFactory keyCornerRadius];
-[UIKBDynamicRenderFactory variantSymbolTextOffset];
-[UIKBDynamicRenderFactory isCarPlay];
-[UIKBDynamicRenderFactory thinKeycapsFontNameForKey:];
-[UIKBDynamicRenderFactory skinnyKeyThreshold];
-[UIKBDynamicRenderFactory lightKeycapsFontNameForKey:];
-[UIKBDynamicRenderFactory _traitsForKey:onKeyplane:];
-[UIKBDynamicRenderFactory _row4ControlSegmentWidthRight];
-[UIKBDynamicRenderFactory wideShadowPaddleInsets];
-[UIKBDynamicRenderFactory variantSymbolFrameInsets];
-[UIKBDynamicRenderFactory symbolImageControlKeyFontSize];
-[UIKBDynamicRenderFactory wideShadowPopupMenuInsets];
-[UIKBDynamicRenderFactory setCurrentHandBias:];
-[UIKBDynamicRenderFactory lightKeycapsFontFallbackName];
-[UIKBDynamicRenderFactory popupFontSize];
-[UIKBDynamicRenderFactory isTallPopup];
-[UIKBDynamicRenderFactory popupSymbolTextOffset];
-[UIKBDynamicRenderFactory layoutClass];
-[UIKBDynamicRenderFactory isKeyboardMinorEdgeWidth];
-[UIKBDynamicRenderFactory _row4ControlSegmentWidthLeft];
-[UIKBDynamicRenderFactory isNumberPad];
-[UIKBDynamicRenderFactory currentLayoutClassIsRegularWidth];
-[UIKBDynamicRenderFactory messagesWriteboardKeyImageName];
-[UIKBDynamicRenderFactory multitapCompleteKeyImageName];
-[UIKBDynamicRenderFactory variantPaddedFrameInsets];
-[UIKBDynamicRenderFactory dynamicInsetsForNumberOfRows:];
-[UIKBDynamicRenderFactory variantDisplayFrameInsets];
-[UIKBDynamicRenderFactory cutKeyImageName];
-[UIKBDynamicRenderFactory fontNameForKey:];
-[UIKBDynamicRenderFactory setKeyboardHorizontalSizeClass:];
-[UIKBDynamicRenderFactory spaceKeySecondarySymbolFontName];
-[UIKBDynamicRenderFactory usesSymbolImageForKey:contents:];
-[UIKBDynamicRenderFactory _isFullHeightKeyFor:onKeyplane:];
-[UIKBDynamicRenderFactory biuKeyImageName];
-[UIKBDynamicRenderFactory fontSizeForKey:];
-[UIKBDynamicRenderFactory lightPadKeycapsFontFallbackName];
-[UIKBDynamicRenderFactory spaceKeyGrabberHandlesImageName];
-[UIKBDynamicRenderFactory tabKeyImageName];
-[UIKBDynamicRenderFactory ZWNJKeyImageName];
-[UIKBDynamicRenderFactory _customizePopupTraits:forKey:onKeyplane:];
-[UIKBDynamicRenderFactory _customizeSymbolStyle:forKey:contents:isPrimary:onKeyplane:];
-[UIKBDynamicRenderFactory _customizeSymbolStyle:forKey:contents:onKeyplane:];
-[UIKBDynamicRenderFactory _customizeTraits:forMultiscriptKey:style:];
-[UIKBDynamicRenderFactory _customizeTraits:forThaiMultiKey:];
-[UIKBDynamicRenderFactory _customizeTraits:forZhuyinGridDualStringKey:];
-[UIKBDynamicRenderFactory _flickTraitsForKey:onKeyplane:withTraits:];
-[UIKBDynamicRenderFactory _isActiveKeyplaneSwitchKey:];
-[UIKBDynamicRenderFactory _isEmojiWideEdgeControlKey:];
-[UIKBDynamicRenderFactory _isThaiMultiKey:];
-[UIKBDynamicRenderFactory _multiscriptStyleForKey:isPopup:];
-[UIKBDynamicRenderFactory _shouldConfigureSecondarySymbolStyleForSpaceKey:];
-[UIKBDynamicRenderFactory _textStyleForSpaceKey];
-[UIKBDynamicRenderFactory _typographyScaleForKey:];
-[UIKBDynamicRenderFactory boldKeyImageName];
-[UIKBDynamicRenderFactory capslockKeyImageName];
-[UIKBDynamicRenderFactory controlKeyBackgroundColorName];
-[UIKBDynamicRenderFactory controlKeyDividerColorName];
-[UIKBDynamicRenderFactory controlKeyForegroundColorName];
-[UIKBDynamicRenderFactory controlKeyTraits];
-[UIKBDynamicRenderFactory copyKeyImageName];
-[UIKBDynamicRenderFactory currentSoftwareLayout];
-[UIKBDynamicRenderFactory defaultKeyDividerColorName];
-[UIKBDynamicRenderFactory deleteKeyImageName];
-[UIKBDynamicRenderFactory deleteOnKeyImageName];
-[UIKBDynamicRenderFactory dictationKeyImageName];
-[UIKBDynamicRenderFactory dismissKeyImageName];
-[UIKBDynamicRenderFactory displayContentsForKey:];
-[UIKBDynamicRenderFactory dualStringBottomAdditionalOffsetForDisplayContents:];
-[UIKBDynamicRenderFactory dualStringKeyBottomFontSize:];
-[UIKBDynamicRenderFactory dualStringKeyBottomTextOffset:];
-[UIKBDynamicRenderFactory dualStringKeyTopFontSize:];
-[UIKBDynamicRenderFactory dualStringKeyTopTextOffset:];
-[UIKBDynamicRenderFactory emojiWideEdgeControlKeyCapsuleHeight];
-[UIKBDynamicRenderFactory fontGradeForKey:];
-[UIKBDynamicRenderFactory fontSizeForBilingualMultiscriptKey:isPrimary:];
-[UIKBDynamicRenderFactory fontSizeForKey:isPrimary:];
-[UIKBDynamicRenderFactory fontSizeForMultiscriptKey:isPrimary:];
-[UIKBDynamicRenderFactory fontSizeForThaiKey:isPrimary:];
-[UIKBDynamicRenderFactory fontSizeForZhuyinGridKey:isPrimary:];
-[UIKBDynamicRenderFactory globalEmojiKeyImageName];
-[UIKBDynamicRenderFactory globalKeyImageName];
-[UIKBDynamicRenderFactory handwritingGradientStartLocation];
-[UIKBDynamicRenderFactory handwritingMoreKeyImageName];
-[UIKBDynamicRenderFactory imageNameForReturnKey:];
-[UIKBDynamicRenderFactory isCustomizedKeyStyle];
-[UIKBDynamicRenderFactory isGrid];
-[UIKBDynamicRenderFactory kerningForKey:];
-[UIKBDynamicRenderFactory keyIsRightToLeftSensitive:];
-[UIKBDynamicRenderFactory keyboardHorizontalSizeClass];
-[UIKBDynamicRenderFactory keyboardVerticalSizeClass];
-[UIKBDynamicRenderFactory keycapsFallbackForKey:];
-[UIKBDynamicRenderFactory leftArrowKeyImageName];
-[UIKBDynamicRenderFactory lightHighQualityEnabledBlendForm];
-[UIKBDynamicRenderFactory lightPadKeycapsFontNameForKey:];
-[UIKBDynamicRenderFactory lightTextFontFallbackName];
-[UIKBDynamicRenderFactory lightTextFontNameForKey:];
-[UIKBDynamicRenderFactory needsFontCaseForKey:];
-[UIKBDynamicRenderFactory needsSmallerFontSizeForKey:];
-[UIKBDynamicRenderFactory pasteKeyImageName];
-[UIKBDynamicRenderFactory populateFlickGuide:forKey:from:scale:];
-[UIKBDynamicRenderFactory redoKeyImageName];
-[UIKBDynamicRenderFactory rightArrowKeyImageName];
-[UIKBDynamicRenderFactory setCurrentHeight:];
-[UIKBDynamicRenderFactory setEmojiWideEdgeControlKeyCapsuleHeight:];
-[UIKBDynamicRenderFactory setIsKeyboardMinorEdgeWidth:];
-[UIKBDynamicRenderFactory setKeyboardVerticalSizeClass:];
-[UIKBDynamicRenderFactory setupLayoutSegments];
-[UIKBDynamicRenderFactory shiftKeyImageName];
-[UIKBDynamicRenderFactory shiftLockImageName];
-[UIKBDynamicRenderFactory shiftOnKeyImageName];
-[UIKBDynamicRenderFactory shouldKeepBackgroundInEmojiInputModeForKey:];
-[UIKBDynamicRenderFactory shouldOverlayTraitsForKey:onKeyplane:];
-[UIKBDynamicRenderFactory smallSymbolImageFontSize];
-[UIKBDynamicRenderFactory stringKeyFontSize:];
-[UIKBDynamicRenderFactory stringKeyOffset:];
-[UIKBDynamicRenderFactory textOpacityForKey:];
-[UIKBDynamicRenderFactory textOpacityForKey:isPrimary:];
-[UIKBDynamicRenderFactory thinKeycapsFontFallbackName];
-[UIKBDynamicRenderFactory thinTextFontFallbackName];
-[UIKBDynamicRenderFactory thinTextFontNameForKey:];
-[UIKBDynamicRenderFactory topEdgeAdjustmentInsets];
-[UIKBDynamicRenderFactory typesettingOffsetForArabicMultiscriptKey:isPrimary:];
-[UIKBDynamicRenderFactory typesettingOffsetForKey:];
-[UIKBDynamicRenderFactory typesettingOffsetForKey:isPrimary:secondaryIndex:];
-[UIKBDynamicRenderFactory typesettingOffsetForKoreanMultiscriptKey:isPrimary:secondaryIndex:];
-[UIKBDynamicRenderFactory typesettingOffsetForMultiscriptKey:isPrimary:];
-[UIKBDynamicRenderFactory typesettingOffsetForThaiKey:isPrimary:secondaryIndex:];
-[UIKBDynamicRenderFactory typesettingOffsetForZhuyinGridKey:isPrimary:];
-[UIKBDynamicRenderFactory undoKeyImageName];
-[UIKBDynamicRenderFactory variantAnnotationTextFontSize];
-[UIKBDynamicRenderFactory variantAnnotationTextOffsetForKey:];
```
