# `AVMediaSelectionKeyValueOption`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVMediaSelectionOption`
- 6 instance variables, 0 properties, 14 instance methods, 0 class methods

## Instance variables

```
@ _groupID;
@ _groupMediaType;
@"NSString" _optionMediaType;
@"NSDictionary" _dictionary;
@"NSDictionary" _localizedMediaSelectionOptionDisplayNames;
@"AVWeakReference" _weakReferenceToGroup;
```

## Instance methods

```
-[AVMediaSelectionKeyValueOption isPlayable];
-[AVMediaSelectionKeyValueOption commonMetadata];
-[AVMediaSelectionKeyValueOption _groupID];
-[AVMediaSelectionKeyValueOption metadataForFormat:];
-[AVMediaSelectionKeyValueOption dealloc];
-[AVMediaSelectionKeyValueOption group];
-[AVMediaSelectionKeyValueOption dictionary];
-[AVMediaSelectionKeyValueOption availableMetadataFormats];
-[AVMediaSelectionKeyValueOption locale];
-[AVMediaSelectionKeyValueOption initWithAsset:group:dictionary:];
-[AVMediaSelectionKeyValueOption hash];
-[AVMediaSelectionKeyValueOption _groupMediaType];
-[AVMediaSelectionKeyValueOption mediaType];
-[AVMediaSelectionKeyValueOption isEqual:];
```
