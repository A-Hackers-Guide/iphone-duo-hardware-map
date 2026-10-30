# `_UISticker`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 12 instance variables, 14 properties, 29 instance methods, 1 class methods

## Instance variables

```
@"NSString" _identifier;
@"NSArray" _representations;
@"_UIStickerRepresentation" _bakedInRep;
q _effectType;
@"NSString" _name;
@"NSString" _externalURI;
@"NSString" _searchText;
@"NSString" _sanitizedPrompt;
@"NSString" _accessibilityName;
@"NSString" _accessibilityLabel;
@"NSData" _metadata;
@"NSDictionary" _attributionInfo;
```

## Properties

```
@property (T@"NSString",&,N,V_identifier) identifier;
@property (T@"NSArray",&,N,V_representations) representations;
@property (T@"_UIStickerRepresentation",&,N,V_bakedInRep) bakedInRep;
@property (Tq,N,V_effectType) effectType;
@property (T@"NSString",&,N,V_name) name;
@property (T@"NSString",&,N,V_externalURI) externalURI;
@property (T@"NSString",&,N,V_searchText) searchText;
@property (T@"NSString",&,N,V_sanitizedPrompt) sanitizedPrompt;
@property (T@"NSString",&,N,V_accessibilityName) accessibilityName;
@property (T@"NSString",&,N,V_accessibilityLabel) accessibilityLabel;
@property (T@"NSData",&,N,V_metadata) metadata;
@property (T@"NSDictionary",&,N,V_attributionInfo) attributionInfo;
@property (TB,R,N) isAnimated;
@property (TB,R,N) hasLiveEffect;
```

## Class methods

```
+[_UISticker supportsSecureCoding];
```

## Instance methods

```
-[_UISticker attributionInfo];
-[_UISticker setExternalURI:];
-[_UISticker setAttributionInfo:];
-[_UISticker identifier];
-[_UISticker init];
-[_UISticker isAnimated];
-[_UISticker searchText];
-[_UISticker representations];
-[_UISticker metadata];
-[_UISticker externalURI];
-[_UISticker setIdentifier:];
-[_UISticker setEffectType:];
-[_UISticker setSearchText:];
-[_UISticker accessibilityLabel];
-[_UISticker encodeWithCoder:];
-[_UISticker setMetadata:];
-[_UISticker setName:];
-[_UISticker effectType];
-[_UISticker initWithCoder:];
-[_UISticker setAccessibilityLabel:];
-[_UISticker name];
-[_UISticker sanitizedPrompt];
-[_UISticker accessibilityName];
-[_UISticker bakedInRep];
-[_UISticker hasLiveEffect];
-[_UISticker setAccessibilityName:];
-[_UISticker setBakedInRep:];
-[_UISticker setRepresentations:];
-[_UISticker setSanitizedPrompt:];
```
