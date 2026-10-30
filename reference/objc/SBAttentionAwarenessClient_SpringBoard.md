# `SBAttentionAwarenessClient`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSInvalidatable`
- 6 instance variables, 7 properties, 15 instance methods, 0 class methods

## Instance variables

```
@"AWAttentionAwarenessConfiguration" _queue_configuration;
B _enabled;
@"<SBAttentionAwarenessClientDelegate>" _delegate;
@"AWAttentionAwarenessClient" _attentionAwarenessClient;
@"NSObject<OS_dispatch_queue>" _queue;
@"NSString" _identifier;
```

## Properties

```
@property (T@"<SBAttentionAwarenessClientDelegate>",W,N,V_delegate) delegate;
@property (T@"AWAttentionAwarenessConfiguration",&,N) configuration;
@property (TB,N,GisEnabled,V_enabled) enabled;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBAttentionAwarenessClient _suspend];
-[SBAttentionAwarenessClient init];
-[SBAttentionAwarenessClient setConfiguration:];
-[SBAttentionAwarenessClient isEnabled];
-[SBAttentionAwarenessClient setConfiguration:shouldReset:];
-[SBAttentionAwarenessClient invalidate];
-[SBAttentionAwarenessClient setDelegate:];
-[SBAttentionAwarenessClient configuration];
-[SBAttentionAwarenessClient setEnabled:];
-[SBAttentionAwarenessClient getEventMaskDescription:];
-[SBAttentionAwarenessClient delegate];
-[SBAttentionAwarenessClient _resume];
-[SBAttentionAwarenessClient _handleAttentionAwarenessEvent:];
-[SBAttentionAwarenessClient _resetAttentionLostTimeout];
-[SBAttentionAwarenessClient resetAttentionLostTimeout];
```
