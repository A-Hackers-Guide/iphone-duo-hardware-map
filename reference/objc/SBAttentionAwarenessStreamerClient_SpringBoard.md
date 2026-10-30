# `SBAttentionAwarenessStreamerClient`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSInvalidatable`
- 6 instance variables, 6 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"AWAttentionAwarenessConfiguration" _queue_configuration;
@"SBScreenLongevitySettings" _settings;
@"<SBAttentionAwarenessStreamerClientDelegate>" _delegate;
@"AWAttentionAwarenessClient" _attentionAwarenessClient;
@"NSObject<OS_dispatch_queue>" _queue;
@"NSString" _identifier;
```

## Properties

```
@property (T@"<SBAttentionAwarenessStreamerClientDelegate>",W,N,V_delegate) delegate;
@property (T@"AWAttentionAwarenessConfiguration",&,N) configuration;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBAttentionAwarenessStreamerClient init];
-[SBAttentionAwarenessStreamerClient setConfiguration:];
-[SBAttentionAwarenessStreamerClient setConfiguration:shouldReset:];
-[SBAttentionAwarenessStreamerClient invalidate];
-[SBAttentionAwarenessStreamerClient setDelegate:];
-[SBAttentionAwarenessStreamerClient configuration];
-[SBAttentionAwarenessStreamerClient delegate];
-[SBAttentionAwarenessStreamerClient resume];
-[SBAttentionAwarenessStreamerClient _handleAttentionAwarenessEvent:];
```
