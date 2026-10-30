# `AVPlayerVideoOutputConfiguration`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"AVPlayerItem" _sourcePlayerItem;
@"NSArray" _dataChannelDescriptions;
{?="value"q"timescale"i"flags"I"epoch"q} _activationTime;
{CGAffineTransform="a"d"b"d"c"d"d"d"tx"d"ty"d} _preferredTransform;
```

## Properties

```
@property (T@"AVPlayerItem",W,N,V_sourcePlayerItem) sourcePlayerItem;
@property (T@"NSArray",C,N,V_dataChannelDescriptions) dataChannelDescriptions;
@property (T{?=qiIq},N,V_activationTime) activationTime;
@property (T{CGAffineTransform=dddddd},R,N,V_preferredTransform) preferredTransform;
```

## Instance methods

```
-[AVPlayerVideoOutputConfiguration preferredTransform];
-[AVPlayerVideoOutputConfiguration copy];
-[AVPlayerVideoOutputConfiguration dealloc];
-[AVPlayerVideoOutputConfiguration setActivationTime:];
-[AVPlayerVideoOutputConfiguration activationTime];
-[AVPlayerVideoOutputConfiguration dataChannelDescriptions];
-[AVPlayerVideoOutputConfiguration initWithSourcePlayerItem:dataChannelDescriptions:transform:activationTime:];
-[AVPlayerVideoOutputConfiguration setDataChannelDescriptions:];
-[AVPlayerVideoOutputConfiguration setSourcePlayerItem:];
-[AVPlayerVideoOutputConfiguration sourcePlayerItem];
```
