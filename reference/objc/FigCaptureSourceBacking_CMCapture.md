# `FigCaptureSourceBacking`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 7 properties, 9 instance methods, 0 class methods

## Instance variables

```
I _mediaType;
@"FigCaptureSourceExtendedAttributes" _attributes;
@"NSMutableDictionary" _cachedProperties;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _cachedPropertiesLock;
@"NSArray" _formats;
@"NSArray" _missingFormatNames;
@"NSArray" _synchronizedStreamUniqueIDs;
@"NSArray" _unsynchronizedStreamUniqueIDs;
```

## Properties

```
@property (TI,R,N,V_mediaType) mediaType;
@property (T@"FigCaptureSourceExtendedAttributes",R,N,V_attributes) attributes;
@property (T@"NSDictionary",R,N,V_cachedProperties) cachedProperties;
@property (T@"NSArray",R,N,V_formats) formats;
@property (T@"NSArray",R,N,V_missingFormatNames) missingFormatNames;
@property (T@"NSArray",R,N,V_synchronizedStreamUniqueIDs) synchronizedStreamUniqueIDs;
@property (T@"NSArray",R,N,V_unsynchronizedStreamUniqueIDs) unsynchronizedStreamUniqueIDs;
```

## Instance methods

```
-[FigCaptureSourceBacking dealloc];
-[FigCaptureSourceBacking formats];
-[FigCaptureSourceBacking attributes];
-[FigCaptureSourceBacking mediaType];
-[FigCaptureSourceBacking cachedProperties];
-[FigCaptureSourceBacking initWithMediaType:attributes:cachedProperties:formats:missingFormatNames:synchronizedStreamUniqueIDs:unsynchronizedStreamUniqueIDs:];
-[FigCaptureSourceBacking missingFormatNames];
-[FigCaptureSourceBacking synchronizedStreamUniqueIDs];
-[FigCaptureSourceBacking unsynchronizedStreamUniqueIDs];
```
