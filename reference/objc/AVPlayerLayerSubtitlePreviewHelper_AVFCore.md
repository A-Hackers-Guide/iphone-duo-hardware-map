# `AVPlayerLayerSubtitlePreviewHelper`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 10 instance variables, 3 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _serialQueue;
@"NSString" _subtitlePreviewText;
@"NSString" _subtitlePreviewProfile;
@"NSString" _extendedLanguageTag;
^{OpaqueFigSubtitleRenderer=} _subtitlePreviewRenderer;
@"NSString" _lastPreviewText;
@"NSString" _lastPreviewProfile;
@"NSString" _lastExtendedLanguageTag;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _lastBounds;
^{CGImage=} _lastGeneratedImage;
```

## Properties

```
@property (T@"NSString",C,N) subtitlePreviewText;
@property (T@"NSString",C,N) subtitlePreviewProfile;
@property (T@"NSString",C,N) extendedLanguageTag;
```

## Instance methods

```
-[AVPlayerLayerSubtitlePreviewHelper setExtendedLanguageTag:];
-[AVPlayerLayerSubtitlePreviewHelper clear];
-[AVPlayerLayerSubtitlePreviewHelper init];
-[AVPlayerLayerSubtitlePreviewHelper dealloc];
-[AVPlayerLayerSubtitlePreviewHelper extendedLanguageTag];
-[AVPlayerLayerSubtitlePreviewHelper _createSubtitlePreviewImageWithBounds:text:languageTag:];
-[AVPlayerLayerSubtitlePreviewHelper clearWithSerialQueue];
-[AVPlayerLayerSubtitlePreviewHelper maybeCreateSubtitlePreviewImageWithBounds:];
-[AVPlayerLayerSubtitlePreviewHelper setSubtitlePreviewProfile:];
-[AVPlayerLayerSubtitlePreviewHelper setSubtitlePreviewText:];
-[AVPlayerLayerSubtitlePreviewHelper subtitlePreviewProfile];
-[AVPlayerLayerSubtitlePreviewHelper subtitlePreviewText];
```
