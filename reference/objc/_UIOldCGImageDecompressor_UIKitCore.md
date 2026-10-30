# `_UIOldCGImageDecompressor`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UICGImageDecompressor`
- 8 instance variables, 0 properties, 4 instance methods, 0 class methods

## Instance variables

```
@"NSData" _imageData;
{CGSize="width"d"height"d} _maxSize;
^{CGImage=} _imageRef;
Q _renderingIntent;
Q _jpegDecodeRequestID;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _metadataLock;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _decompressionLock;
{?="metadataFinished"b1"imageOrientation"b3"decompressionFinished"b1"cache"b1} _decompressorFlags;
```

## Instance methods

```
-[_UIOldCGImageDecompressor dealloc];
-[_UIOldCGImageDecompressor hash];
-[_UIOldCGImageDecompressor isEqual:];
-[_UIOldCGImageDecompressor waitForImageRef];
```
