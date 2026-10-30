# `AVMovie`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVAsset`
- Protocols: `NSCopying`, `NSMutableCopying`
- 1 instance variables, 6 properties, 39 instance methods, 5 class methods

## Instance variables

```
@"AVMovieInternal" _movie;
```

## Properties

```
@property (T@"NSURL",R,N) URL;
@property (T@"NSData",R,N) data;
@property (T@"AVMediaDataStorage",R,N) defaultMediaDataStorage;
@property (T@"NSArray",R,N) tracks;
@property (TB,R,N) canContainMovieFragments;
@property (TB,R,N) containsMovieFragments;
```

## Class methods

```
+[AVMovie initialize];
+[AVMovie expectsPropertyRevisedNotifications];
+[AVMovie movieTypes];
+[AVMovie movieWithData:options:];
+[AVMovie movieWithURL:options:];
```

## Instance methods

```
-[AVMovie trackReferences];
-[AVMovie tracksWithMediaCharacteristic:];
-[AVMovie tracksWithMediaType:];
-[AVMovie mutableCopyWithZone:];
-[AVMovie hasProtectedContent];
-[AVMovie init];
-[AVMovie initWithURL:options:];
-[AVMovie data];
-[AVMovie dealloc];
-[AVMovie _classForTrackInspectors];
-[AVMovie isDefunct];
-[AVMovie trackWithTrackID:];
-[AVMovie description];
-[AVMovie initWithData:options:];
-[AVMovie copyWithZone:];
-[AVMovie tracks];
-[AVMovie _copyFormatReader];
-[AVMovie URL];
-[AVMovie _assetInspector];
-[AVMovie _absoluteURL];
-[AVMovie _assetInspectorLoader];
-[AVMovie _classForMovieTracks];
-[AVMovie _figMutableMovie];
-[AVMovie _figMutableMovieFromFormatReader:];
-[AVMovie _initWithFigAsset:];
-[AVMovie _initWithFigError:userInfo:];
-[AVMovie _initWithFormatReader:URL:data:options:];
-[AVMovie _initializationOptions];
-[AVMovie _mutableMovieForFileType:];
-[AVMovie _startListeningToLoaderNotifications];
-[AVMovie _stopListeningToLoaderNotifications];
-[AVMovie canContainMovieFragments];
-[AVMovie containsMovieFragments];
-[AVMovie defaultMediaDataStorage];
-[AVMovie initWithData:contentType:options:];
-[AVMovie isCompatibleWithFileType:];
-[AVMovie movieHeaderWithFileType:error:];
-[AVMovie referenceRestrictions];
-[AVMovie writeMovieHeaderToURL:fileType:options:error:];
```
