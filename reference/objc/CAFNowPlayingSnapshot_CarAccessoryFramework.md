# `CAFNowPlayingSnapshot`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 10 instance variables, 11 properties, 19 instance methods, 1 class methods

## Instance variables

```
C _mediaSourceType;
C _playbackState;
@"NSData" _artworkData;
@"NSArray" _titles;
@"NSString" _currentMediaSourceIdentifier;
q _lastArtworkToken;
q _lastMediaItemImageToken;
q _artworkType;
Q _multicast;
@"NSString" _mediaItemIdentifier;
```

## Properties

```
@property (T@"NSData",R,N,V_artworkData) artworkData;
@property (T@"NSArray",R,N,V_titles) titles;
@property (TC,R,N,V_mediaSourceType) mediaSourceType;
@property (T@"NSString",R,C,N,V_currentMediaSourceIdentifier) currentMediaSourceIdentifier;
@property (Tq,R,N,V_lastArtworkToken) lastArtworkToken;
@property (Tq,R,N,V_lastMediaItemImageToken) lastMediaItemImageToken;
@property (Tq,R,N,V_artworkType) artworkType;
@property (TQ,R,N,V_multicast) multicast;
@property (TC,R,N,V_playbackState) playbackState;
@property (TB,R,N,GisValid) valid;
@property (T@"NSString",R,N,V_mediaItemIdentifier) mediaItemIdentifier;
```

## Class methods

```
+[CAFNowPlayingSnapshot supportsSecureCoding];
```

## Instance methods

```
-[CAFNowPlayingSnapshot playbackState];
-[CAFNowPlayingSnapshot artworkData];
-[CAFNowPlayingSnapshot artworkType];
-[CAFNowPlayingSnapshot encodeWithCoder:];
-[CAFNowPlayingSnapshot isValid];
-[CAFNowPlayingSnapshot hash];
-[CAFNowPlayingSnapshot description];
-[CAFNowPlayingSnapshot initWithCoder:];
-[CAFNowPlayingSnapshot copyWithZone:];
-[CAFNowPlayingSnapshot isEqual:];
-[CAFNowPlayingSnapshot multicast];
-[CAFNowPlayingSnapshot titles];
-[CAFNowPlayingSnapshot mediaItemIdentifier];
-[CAFNowPlayingSnapshot isEqualToSnapshot:];
-[CAFNowPlayingSnapshot currentMediaSourceIdentifier];
-[CAFNowPlayingSnapshot mediaSourceType];
-[CAFNowPlayingSnapshot initWithTitles:artworkData:mediaSourceType:mediaSourceIdentifier:artworkToken:mediaItemImageToken:artworkType:multicast:playbackState:mediaItemIdentifier:];
-[CAFNowPlayingSnapshot lastArtworkToken];
-[CAFNowPlayingSnapshot lastMediaItemImageToken];
```
