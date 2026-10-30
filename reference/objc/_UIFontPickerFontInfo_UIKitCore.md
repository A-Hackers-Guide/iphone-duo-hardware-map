# `_UIFontPickerFontInfo`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 21 instance variables, 19 properties, 45 instance methods, 4 class methods

## Instance variables

```
@"NSString" _familyName;
@"NSString" _styleName;
@"NSString" _fontName;
@"NSString" _localizedFamilyName;
@"NSString" _localizedStyleName;
@"NSString" _localizedFullName;
d _lineHeight;
@"UIFontDescriptor" _fontDescriptor;
@"NSAttributedString" _attributedString;
@"NSString" _attributedStringContentSize;
@"NSString" _preferredShortPreviewString;
@"NSNumber" _previewStringContainsArabic;
@"UIImage" _previewImage;
@"NSString" _previewImageContentSize;
d _previewImageDisplayScale;
B _previewImageUsesSingleCharacter;
Q _hasMultipleFaces;
@"NSArray" _subInfos;
B _isSystemFont;
@"NSNumber" _canRenderName;
B _previewImagePrefersSingleCharacter;
```

## Properties

```
@property (T@"NSString",R,V_familyName) familyName;
@property (T@"NSString",R) postscriptName;
@property (T@"NSString",R,V_styleName) styleName;
@property (T@"NSString",R,V_fontName) fontName;
@property (Td,R) lineHeight;
@property (T@"NSAttributedString",R) attributedString;
@property (T@"NSString",R) localizedName;
@property (T@"NSString",R) localizedFullName;
@property (T@"NSString",R) localizedFamilyName;
@property (TB,R) fontCanRenderLocalizedName;
@property (T@"NSString",R) preferredShortPreviewString;
@property (T@"UIImage",R) previewImage;
@property (TB,N,V_previewImagePrefersSingleCharacter) previewImagePrefersSingleCharacter;
@property (T@"UIFontDescriptor",R) fontDescriptor;
@property (TB,R,GisFontFamilyAvailable) fontFamilyAvailable;
@property (TB,R) hasMultipleFaces;
@property (T@"NSArray",R) faces;
@property (T@"_UIFontPickerFontInfo",R) familyInfo;
@property (TB,R) isSystemFont;
```

## Class methods

```
+[_UIFontPickerFontInfo infoWithFamilyName:];
+[_UIFontPickerFontInfo infoWithFontDescriptor:];
+[_UIFontPickerFontInfo infoWithName:];
+[_UIFontPickerFontInfo initWithSystemDefaultFont];
```

## Instance methods

```
-[_UIFontPickerFontInfo fontName];
-[_UIFontPickerFontInfo localizedFullName];
-[_UIFontPickerFontInfo attributedString];
-[_UIFontPickerFontInfo faces];
-[_UIFontPickerFontInfo localizedName];
-[_UIFontPickerFontInfo previewImage];
-[_UIFontPickerFontInfo familyName];
-[_UIFontPickerFontInfo fontDescriptor];
-[_UIFontPickerFontInfo hash];
-[_UIFontPickerFontInfo description];
-[_UIFontPickerFontInfo matchesConfiguration:];
-[_UIFontPickerFontInfo isEqual:];
-[_UIFontPickerFontInfo _updateAttributedStringIfNeeded];
-[_UIFontPickerFontInfo matchesFamilyForFontDescriptor:];
-[_UIFontPickerFontInfo _createPreviewImage:];
-[_UIFontPickerFontInfo _fontStringForTraitCollection:];
-[_UIFontPickerFontInfo _hasMultipleFacesForFamily];
-[_UIFontPickerFontInfo _populateLocalizedNamesIfNecessary];
-[_UIFontPickerFontInfo _sortedFacesByWeight];
-[_UIFontPickerFontInfo _updatePreviewImageIfNeeded];
-[_UIFontPickerFontInfo faceMatchingDescriptor:];
-[_UIFontPickerFontInfo familyInfo];
-[_UIFontPickerFontInfo fontCanRenderLocalizedName];
-[_UIFontPickerFontInfo hasMultipleFaces];
-[_UIFontPickerFontInfo initWithFamilyName:];
-[_UIFontPickerFontInfo initWithFontDescriptor:];
-[_UIFontPickerFontInfo initWithFontDescriptor:isSystemFont:];
-[_UIFontPickerFontInfo initWithSystemDefaultFont];
-[_UIFontPickerFontInfo isFontFamilyAvailable];
-[_UIFontPickerFontInfo isSystemFont];
-[_UIFontPickerFontInfo lineHeight];
-[_UIFontPickerFontInfo localizedFamilyName];
-[_UIFontPickerFontInfo matchesClientFontContext:];
-[_UIFontPickerFontInfo matchesFamilyName:];
-[_UIFontPickerFontInfo matchesFontDescriptor:];
-[_UIFontPickerFontInfo matchesFontNames:];
-[_UIFontPickerFontInfo matchesSearchString:];
-[_UIFontPickerFontInfo matchesTraits:];
-[_UIFontPickerFontInfo passesLanguageFilter:];
-[_UIFontPickerFontInfo postscriptName];
-[_UIFontPickerFontInfo preferredShortPreviewString];
-[_UIFontPickerFontInfo previewImagePrefersSingleCharacter];
-[_UIFontPickerFontInfo setHasMultipleFaces:];
-[_UIFontPickerFontInfo setPreviewImagePrefersSingleCharacter:];
-[_UIFontPickerFontInfo styleName];
```
