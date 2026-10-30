# `CUIThemeFacet`

- Image: [`/System/Library/PrivateFrameworks/CoreUI.framework/CoreUI`](../userland/System__Library__PrivateFrameworks__CoreUI.framework__CoreUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CUIThemeImageSource`, `NSCopying`, `NSCoding`
- 7 instance variables, 4 properties, 91 instance methods, 15 class methods

## Instance variables

```
^{_renditionkeytoken=SS} _renditionKeyList;
Q _themeIndex;
q _renditionType;
{CGSize="width"d"height"d} _thumbnailSize;
{CGPoint="x"d"y"d} _hotSpot;
i _isTintable;
{?="hasCheckedButtonGlyph"b1"isButtonGlyph"b1"reserved"b14} _fFlags;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[CUIThemeFacet themeWithContentsOfURL:error:];
+[CUIThemeFacet initialize];
+[CUIThemeFacet _invalidateArtworkCaches];
+[CUIThemeFacet themeUnregisterThemeRef:];
+[CUIThemeFacet themeForBundleIdentifier:error:];
+[CUIThemeFacet _facetWithKeyList:andRenditionKeyClass:orRenditionKey:fromTheme:];
+[CUIThemeFacet facetWithElement:part:dimension1:dimension2:fromTheme:];
+[CUIThemeFacet themeNamed:forBundleIdentifier:error:];
+[CUIThemeFacet themeWithBytes:length:error:];
+[CUIThemeFacet _themeStoreForThemeIndex:];
+[CUIThemeFacet _bundleIdentifierForThemeRef:];
+[CUIThemeFacet assetExistsForRenditionKey:fromTheme:];
+[CUIThemeFacet facetWithElement:part:fromTheme:];
+[CUIThemeFacet facetWithRenditionKey:fromTheme:];
+[CUIThemeFacet cursorFacetWithName:fromTheme:];
```

## Instance methods

```
-[CUIThemeFacet imageSize];
-[CUIThemeFacet properties];
-[CUIThemeFacet thumbnailSize];
-[CUIThemeFacet init];
-[CUIThemeFacet displayName];
-[CUIThemeFacet renditionType];
-[CUIThemeFacet dealloc];
-[CUIThemeFacet imageForSliceIndex:];
-[CUIThemeFacet encodeWithCoder:];
-[CUIThemeFacet themeIndex];
-[CUIThemeFacet imageForState:];
-[CUIThemeFacet description];
-[CUIThemeFacet thumbnail];
-[CUIThemeFacet initWithCoder:];
-[CUIThemeFacet alpha];
-[CUIThemeFacet image];
-[CUIThemeFacet renditionKey];
-[CUIThemeFacet copyWithZone:];
-[CUIThemeFacet blendMode];
-[CUIThemeFacet _setThemeIndex:];
-[CUIThemeFacet initWithRenditionKey:fromTheme:];
-[CUIThemeFacet maskForSlice:withKeyAdjustment:];
-[CUIThemeFacet renditionForSpecificKeyWrapper:];
-[CUIThemeFacet _applyFixedAttributesToKey:];
-[CUIThemeFacet _canGetRenditionForKey:withDrawingLayer:];
-[CUIThemeFacet _drawSlice:inFrame:withKeyAdjustment:context:];
-[CUIThemeFacet _hotSpot];
-[CUIThemeFacet _isButtonGlyph];
-[CUIThemeFacet _rendition];
-[CUIThemeFacet _renditionForSpecificKey:];
-[CUIThemeFacet _setHasCheckedButtonGlyph:];
-[CUIThemeFacet _setIsButtonGlyph:];
-[CUIThemeFacet _sliceIndexForSlice:ofRendition:];
-[CUIThemeFacet _themeStore];
-[CUIThemeFacet _thumbnailSizeForRendition:];
-[CUIThemeFacet _updateSpecificRenditionKey:isFocused:owner:userInfo:];
-[CUIThemeFacet alphaWithKeyAdjustment:];
-[CUIThemeFacet blendModeAsCAFilterString];
-[CUIThemeFacet blendModeAsCAFilterStringWithKeyAjustment:];
-[CUIThemeFacet blendModeWithKeyAdjustment:];
-[CUIThemeFacet copyLayerImageContentsAndCenter:];
-[CUIThemeFacet copyLayerImageContentsAndCenter:renditionKey:];
-[CUIThemeFacet drawAbsoluteAnimationFrame:destinationFrame:isFocused:focusRingColor:context:];
-[CUIThemeFacet drawAnimationFrameMappedFrom0_1RangedValue:destinationFrame:isFocused:focusRingColor:context:];
-[CUIThemeFacet drawAnimationFrameMappedFrom0_1RangedValue:destinationFrame:isFocused:focusRingColor:context:effects:];
-[CUIThemeFacet drawAsOnePartWithSlice:inFrame:isFocused:focusRingColor:context:effects:];
-[CUIThemeFacet drawGradientInFrame:angle:alpha:operation:isFocused:focusRingColor:keyAdjustment:context:effects:];
-[CUIThemeFacet drawHighlightInFrame:alpha:keyAdjustment:context:];
-[CUIThemeFacet drawHighlightInFrame:alpha:operation:keyAdjustment:context:];
-[CUIThemeFacet drawHighlightInFrame:alpha:operation:owner:userInfo:context:];
-[CUIThemeFacet drawHighlightInFrame:alpha:owner:userInfo:context:];
-[CUIThemeFacet drawHighlightInFrame:owner:userInfo:context:];
-[CUIThemeFacet drawInFrame:alpha:isFocused:focusRingColor:context:];
-[CUIThemeFacet drawInFrame:alpha:isFocused:focusRingColor:context:effects:];
-[CUIThemeFacet drawInFrame:alpha:isFocused:focusRingColor:keyAdjustment:context:];
-[CUIThemeFacet drawInFrame:alpha:operation:isFocused:focusRingColor:context:effects:];
-[CUIThemeFacet drawInFrame:alpha:operation:isFocused:focusRingColor:keyAdjustment:context:];
-[CUIThemeFacet drawInFrame:alpha:operation:owner:userInfo:context:];
-[CUIThemeFacet drawInFrame:alpha:owner:userInfo:context:];
-[CUIThemeFacet drawInFrame:isFocused:context:];
-[CUIThemeFacet drawInFrame:isFocused:focusRingColor:context:];
-[CUIThemeFacet drawInFrame:isFocused:focusRingColor:context:effects:];
-[CUIThemeFacet drawInFrame:owner:userInfo:context:];
-[CUIThemeFacet drawMaskInFrame:alpha:isFocused:focusRingColor:keyAdjustment:context:];
-[CUIThemeFacet drawMaskInFrame:alpha:operation:isFocused:focusRingColor:keyAdjustment:context:];
-[CUIThemeFacet drawMaskInFrame:alpha:owner:userInfo:context:];
-[CUIThemeFacet drawMaskInFrame:owner:userInfo:context:];
-[CUIThemeFacet drawPulseInFrame:pulseValue:isFocused:focusRingColor:keyAdjustment:context:];
-[CUIThemeFacet drawPulseInFrame:pulseValue:owner:userInfo:context:];
-[CUIThemeFacet drawSegmentInFrame:isFocused:focusRingColor:segmentType:context:effects:];
-[CUIThemeFacet gradientWithKeyAdjustment:angle:style:];
-[CUIThemeFacet hasValueSlices];
-[CUIThemeFacet highlightWithSize:keyAdjustment:];
-[CUIThemeFacet hitTestAtPoint:inFrame:owner:userInfo:];
-[CUIThemeFacet imageForSlice:withKeyAdjustment:];
-[CUIThemeFacet imageForState:value:];
-[CUIThemeFacet imageForState:value:size:];
-[CUIThemeFacet imageForState:withValue:];
-[CUIThemeFacet imageWithSize:keyAdjustment:];
-[CUIThemeFacet isTintable];
-[CUIThemeFacet isValidButtonImageSource];
-[CUIThemeFacet makeLayer];
-[CUIThemeFacet maskWithSize:keyAdjustment:];
-[CUIThemeFacet renditionMetricsWithKeyAdjustment:];
-[CUIThemeFacet renditionSliceInformationForRect:keyAdjustment:];
-[CUIThemeFacet sizeForSegmentOfType:];
-[CUIThemeFacet themeRendition];
-[CUIThemeFacet topLeftCapSize];
-[CUIThemeFacet updateLayer:];
-[CUIThemeFacet updateLayer:effects:];
-[CUIThemeFacet updateSegmentBezelLeadingCapLayer:bezelFillLayer:trailingBezelCapLayer:forSegmentType:segmentBounds:leadingSeparatorWidth:trailingSeparatorWidth:renditionKey:effects:];
```
