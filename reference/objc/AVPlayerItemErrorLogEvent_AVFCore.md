# `AVPlayerItemErrorLogEvent`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 1 instance variables, 8 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"AVPlayerItemErrorLogEventInternal" _playerItemErrorLogEvent;
```

## Properties

```
@property (T@"NSDate",R,N) date;
@property (T@"NSString",R,N) URI;
@property (T@"NSString",R,N) serverAddress;
@property (T@"NSString",R,N) playbackSessionID;
@property (Tq,R,N) errorStatusCode;
@property (T@"NSString",R,N) errorDomain;
@property (T@"NSString",R,N) errorComment;
@property (T@"NSDictionary",R,N) allHTTPResponseHeaderFields;
```

## Instance methods

```
-[AVPlayerItemErrorLogEvent initWithDictionary:];
-[AVPlayerItemErrorLogEvent init];
-[AVPlayerItemErrorLogEvent dealloc];
-[AVPlayerItemErrorLogEvent date];
-[AVPlayerItemErrorLogEvent serverAddress];
-[AVPlayerItemErrorLogEvent errorDomain];
-[AVPlayerItemErrorLogEvent URI];
-[AVPlayerItemErrorLogEvent copyWithZone:];
-[AVPlayerItemErrorLogEvent errorStatusCode];
-[AVPlayerItemErrorLogEvent _common_init];
-[AVPlayerItemErrorLogEvent allHTTPResponseHeaderFields];
-[AVPlayerItemErrorLogEvent errorComment];
-[AVPlayerItemErrorLogEvent playbackSessionID];
```
