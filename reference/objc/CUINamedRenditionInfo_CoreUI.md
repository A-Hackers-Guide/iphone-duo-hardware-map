# `CUINamedRenditionInfo`

- Image: [`/System/Library/PrivateFrameworks/CoreUI.framework/CoreUI`](../userland/System__Library__PrivateFrameworks__CoreUI.framework__CoreUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 3 instance variables, 0 properties, 24 instance methods, 2 class methods

## Instance variables

```
^v _bitmap;
r^{_renditionkeyfmt=III[0I]} _keyFormat;
q _platform;
```

## Class methods

```
+[CUINamedRenditionInfo subtypeFromIndexWithPlatform:andIndex:];
+[CUINamedRenditionInfo subtypeToIndexWithPlatform:andInput:];
```

## Instance methods

```
-[CUINamedRenditionInfo debugDescription];
-[CUINamedRenditionInfo decrementValue:forAttribute:];
-[CUINamedRenditionInfo contentPresentForAttribute:];
-[CUINamedRenditionInfo dealloc];
-[CUINamedRenditionInfo getClosestValueOfAttribute:withValue:];
-[CUINamedRenditionInfo bitwiseOrWith:forAttribute:];
-[CUINamedRenditionInfo setAttributePresent:withValue:];
-[CUINamedRenditionInfo archivedData];
-[CUINamedRenditionInfo initWithData:keyFormat:andPlatform:];
-[CUINamedRenditionInfo containsVectorGlyphWithWeight:size:];
-[CUINamedRenditionInfo incrementIndex:inValues:forAttribute:];
-[CUINamedRenditionInfo description];
-[CUINamedRenditionInfo clearAttributePresent:withValue:];
-[CUINamedRenditionInfo attributePresent:withValue:];
-[CUINamedRenditionInfo isEqualToNamedRenditionInfo:];
-[CUINamedRenditionInfo containsVectorGlyphInterpolationSources];
-[CUINamedRenditionInfo diverseContentPresentForAttribute:];
-[CUINamedRenditionInfo copyWithZone:];
-[CUINamedRenditionInfo getValueOfAttribute:];
-[CUINamedRenditionInfo numberOfBitsSet];
-[CUINamedRenditionInfo isEqual:];
-[CUINamedRenditionInfo contentEqualForAttribute:withRenditionInfo:];
-[CUINamedRenditionInfo bitwiseAndWith:];
-[CUINamedRenditionInfo initWithKeyFormat:andPlatform:];
```
