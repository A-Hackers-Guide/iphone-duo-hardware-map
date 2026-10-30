# `AVMetricHLSPlaylistRequestEvent`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVMetricEvent`
- 4 instance variables, 4 properties, 9 instance methods, 1 class methods

## Instance variables

```
@"NSURL" _url;
B _isMultivariantPlaylist;
@"NSString" _mediaType;
@"AVMetricMediaResourceRequestEvent" _mediaResourceRequestEvent;
```

## Properties

```
@property (T@"NSURL",R) url;
@property (TB,R) isMultivariantPlaylist;
@property (T@"NSString",R) mediaType;
@property (T@"AVMetricMediaResourceRequestEvent",R) mediaResourceRequestEvent;
```

## Class methods

```
+[AVMetricHLSPlaylistRequestEvent supportsSecureCoding];
```

## Instance methods

```
-[AVMetricHLSPlaylistRequestEvent debugDescription];
-[AVMetricHLSPlaylistRequestEvent dealloc];
-[AVMetricHLSPlaylistRequestEvent encodeWithCoder:];
-[AVMetricHLSPlaylistRequestEvent initWithCoder:];
-[AVMetricHLSPlaylistRequestEvent mediaType];
-[AVMetricHLSPlaylistRequestEvent url];
-[AVMetricHLSPlaylistRequestEvent initWithDate:mediaTime:sessionID:figMetricEvent:url:isMultivariantPlaylist:mediaType:mediaResourceRequestEvent:];
-[AVMetricHLSPlaylistRequestEvent isMultivariantPlaylist];
-[AVMetricHLSPlaylistRequestEvent mediaResourceRequestEvent];
```
