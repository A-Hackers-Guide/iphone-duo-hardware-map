# `UIImageReaderConfiguration`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 3 instance variables, 5 properties, 14 instance methods, 0 class methods

## Instance variables

```
{?="prefersHighDynamicRange"b1"preparesImagesForDisplay"b1"generatesThumbnails"b1"skipImageStats"b1} _flags;
d _pixelsPerInch;
{CGSize="width"d"height"d} _preferredThumbnailSize;
```

## Properties

```
@property (TB,N,S_setSkipImageStats:) _skipImageStats;
@property (TB,N) prefersHighDynamicRange;
@property (TB,N) preparesImagesForDisplay;
@property (T{CGSize=dd},N,V_preferredThumbnailSize) preferredThumbnailSize;
@property (Td,N,V_pixelsPerInch) pixelsPerInch;
```

## Instance methods

```
-[UIImageReaderConfiguration init];
-[UIImageReaderConfiguration pixelsPerInch];
-[UIImageReaderConfiguration preferredThumbnailSize];
-[UIImageReaderConfiguration hash];
-[UIImageReaderConfiguration copyWithZone:];
-[UIImageReaderConfiguration isEqual:];
-[UIImageReaderConfiguration _skipImageStats];
-[UIImageReaderConfiguration _setSkipImageStats:];
-[UIImageReaderConfiguration prefersHighDynamicRange];
-[UIImageReaderConfiguration preparesImagesForDisplay];
-[UIImageReaderConfiguration setPixelsPerInch:];
-[UIImageReaderConfiguration setPreferredThumbnailSize:];
-[UIImageReaderConfiguration setPrefersHighDynamicRange:];
-[UIImageReaderConfiguration setPreparesImagesForDisplay:];
```
