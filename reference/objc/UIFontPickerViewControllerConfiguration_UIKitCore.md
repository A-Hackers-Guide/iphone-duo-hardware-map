# `UIFontPickerViewControllerConfiguration`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `BSXPCSecureCoding`, `BSDescriptionProviding`, `NSCopying`
- 14 instance variables, 18 properties, 44 instance methods, 3 class methods

## Instance variables

```
B _includeFaces;
B _displayUsingSystemFont;
B __hideSearchBar;
B __includeDefaultFont;
B __showsSectionIndexBar;
I _filteredTraits;
@"NSPredicate" _filteredLanguagesPredicate;
@"NSArray" __allowedLanguages;
@ __swiftPredicate;
@"UIColor" __tintColor;
@"NSString" __filterFamilyName;
@"NSSet" __filterFontNames;
@"NSXPCListenerEndpoint" __clientFontContextEndpoint;
@"NSArray" __clientRecentFonts;
```

## Properties

```
@property (T@"NSArray",C,N,V__allowedLanguages) _allowedLanguages;
@property (T@,C,N,V__swiftPredicate) _swiftPredicate;
@property (TB,N,S_setHideSearchBar:,V__hideSearchBar) _hideSearchBar;
@property (T@"UIColor",&,N,S_setTintColor:,V__tintColor) _tintColor;
@property (TB,N,V__includeDefaultFont) _includeDefaultFont;
@property (T@"NSString",C,N,V__filterFamilyName) _filterFamilyName;
@property (T@"NSSet",C,N,V__filterFontNames) _filterFontNames;
@property (TB,N,V__showsSectionIndexBar) _showsSectionIndexBar;
@property (T@"NSXPCListenerEndpoint",&,N,V__clientFontContextEndpoint) _clientFontContextEndpoint;
@property (T@"NSArray",C,N,S_setClientRecentFonts:,V__clientRecentFonts) _clientRecentFonts;
@property (TB,N,V_includeFaces) includeFaces;
@property (TB,N,V_displayUsingSystemFont) displayUsingSystemFont;
@property (TI,N,V_filteredTraits) filteredTraits;
@property (T@"NSPredicate",C,N,V_filteredLanguagesPredicate) filteredLanguagesPredicate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UIFontPickerViewControllerConfiguration supportsBSXPCSecureCoding];
+[UIFontPickerViewControllerConfiguration supportsSecureCoding];
+[UIFontPickerViewControllerConfiguration filterPredicateForFilteredLanguages:];
```

## Instance methods

```
-[UIFontPickerViewControllerConfiguration _tintColor];
-[UIFontPickerViewControllerConfiguration _setTintColor:];
-[UIFontPickerViewControllerConfiguration debugDescription];
-[UIFontPickerViewControllerConfiguration succinctDescriptionBuilder];
-[UIFontPickerViewControllerConfiguration descriptionWithMultilinePrefix:];
-[UIFontPickerViewControllerConfiguration succinctDescription];
-[UIFontPickerViewControllerConfiguration debugDescriptionWithMultilinePrefix:];
-[UIFontPickerViewControllerConfiguration encodeWithCoder:];
-[UIFontPickerViewControllerConfiguration description];
-[UIFontPickerViewControllerConfiguration initWithCoder:];
-[UIFontPickerViewControllerConfiguration set_includeDefaultFont:];
-[UIFontPickerViewControllerConfiguration encodeWithBSXPCCoder:];
-[UIFontPickerViewControllerConfiguration _includeDefaultFont];
-[UIFontPickerViewControllerConfiguration initWithBSXPCCoder:];
-[UIFontPickerViewControllerConfiguration copyWithZone:];
-[UIFontPickerViewControllerConfiguration isEqual:];
-[UIFontPickerViewControllerConfiguration descriptionBuilderWithMultilinePrefix:];
-[UIFontPickerViewControllerConfiguration _swiftPredicate];
-[UIFontPickerViewControllerConfiguration _allowedLanguages];
-[UIFontPickerViewControllerConfiguration _clientFontContextEndpoint];
-[UIFontPickerViewControllerConfiguration _clientRecentFonts];
-[UIFontPickerViewControllerConfiguration _filterFamilyName];
-[UIFontPickerViewControllerConfiguration _filterFontNames];
-[UIFontPickerViewControllerConfiguration _hideSearchBar];
-[UIFontPickerViewControllerConfiguration _matchesLanguageList:];
-[UIFontPickerViewControllerConfiguration _serializedPredicate];
-[UIFontPickerViewControllerConfiguration _setClientRecentFonts:];
-[UIFontPickerViewControllerConfiguration _setHideSearchBar:];
-[UIFontPickerViewControllerConfiguration _setPredicateFromData:];
-[UIFontPickerViewControllerConfiguration _showsSectionIndexBar];
-[UIFontPickerViewControllerConfiguration displayUsingSystemFont];
-[UIFontPickerViewControllerConfiguration filteredLanguagesPredicate];
-[UIFontPickerViewControllerConfiguration filteredTraits];
-[UIFontPickerViewControllerConfiguration includeFaces];
-[UIFontPickerViewControllerConfiguration setDisplayUsingSystemFont:];
-[UIFontPickerViewControllerConfiguration setFilteredLanguagesPredicate:];
-[UIFontPickerViewControllerConfiguration setFilteredTraits:];
-[UIFontPickerViewControllerConfiguration setIncludeFaces:];
-[UIFontPickerViewControllerConfiguration set_allowedLanguages:];
-[UIFontPickerViewControllerConfiguration set_clientFontContextEndpoint:];
-[UIFontPickerViewControllerConfiguration set_filterFamilyName:];
-[UIFontPickerViewControllerConfiguration set_filterFontNames:];
-[UIFontPickerViewControllerConfiguration set_showsSectionIndexBar:];
-[UIFontPickerViewControllerConfiguration set_swiftPredicate:];
```
