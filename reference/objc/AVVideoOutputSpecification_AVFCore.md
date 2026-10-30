# `AVVideoOutputSpecification`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 3 instance variables, 3 properties, 16 instance methods, 0 class methods

## Instance variables

```
@"NSArray" _tagCollections;
@"AVVideoOutputSettings<AVDecodedVideoSettingsForFig>" _defaultOutputSettings;
@"NSMutableDictionary" _tagCollectionToOutputSettingsMapping;
```

## Properties

```
@property (T@"NSArray",R,C,N) preferredTagCollections;
@property (T@"NSDictionary",C,N) defaultPixelBufferAttributes;
@property (T@"NSDictionary",C,N) defaultOutputSettings;
```

## Instance methods

```
-[AVVideoOutputSpecification init];
-[AVVideoOutputSpecification dealloc];
-[AVVideoOutputSpecification copyWithZone:];
-[AVVideoOutputSpecification _allowWideColorForTagCollection:];
-[AVVideoOutputSpecification _outputSettingsForTagCollection:];
-[AVVideoOutputSpecification _pixelBufferAttributesForTagCollection:];
-[AVVideoOutputSpecification _videoColorPropertiesForTagCollection:];
-[AVVideoOutputSpecification _videoOutputSettingsFromDictionaryRepresentation:exceptionReason:];
-[AVVideoOutputSpecification defaultOutputSettings];
-[AVVideoOutputSpecification defaultPixelBufferAttributes];
-[AVVideoOutputSpecification initWithTagCollections:];
-[AVVideoOutputSpecification preferredTagCollections];
-[AVVideoOutputSpecification setDefaultOutputSettings:];
-[AVVideoOutputSpecification setDefaultPixelBufferAttributes:];
-[AVVideoOutputSpecification setOutputPixelBufferAttributes:forTagCollection:];
-[AVVideoOutputSpecification setOutputSettings:forTagCollection:];
```
