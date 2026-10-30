# `AVAssetVariant`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 4 instance variables, 5 properties, 11 instance methods, 1 class methods

## Instance variables

```
@"FigAlternateObjC" _figAlternateObjC;
@"AVAssetVariantVideoAttributes" _videoAttributes;
@"AVAssetVariantAudioAttributes" _audioAttributes;
^{OpaqueFigSimpleMutex=} _mutex;
```

## Properties

```
@property (Td,R,N) peakBitRate;
@property (Td,R,N) averageBitRate;
@property (T@"AVAssetVariantVideoAttributes",R,N) videoAttributes;
@property (T@"AVAssetVariantAudioAttributes",R,N) audioAttributes;
@property (T@"NSURL",R,N) URL;
```

## Class methods

```
+[AVAssetVariant supportsSecureCoding];
```

## Instance methods

```
-[AVAssetVariant dealloc];
-[AVAssetVariant encodeWithCoder:];
-[AVAssetVariant description];
-[AVAssetVariant initWithCoder:];
-[AVAssetVariant URL];
-[AVAssetVariant audioAttributes];
-[AVAssetVariant videoAttributes];
-[AVAssetVariant _figAlternate];
-[AVAssetVariant averageBitRate];
-[AVAssetVariant initWithFigAlternate:];
-[AVAssetVariant peakBitRate];
```
