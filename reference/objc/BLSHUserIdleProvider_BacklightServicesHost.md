# `BLSHUserIdleProvider`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BLSHUserIdleProviding`
- 7 instance variables, 11 properties, 25 instance methods, 0 class methods

## Instance variables

```
B _shouldNotifyOfUnidle;
B _shouldNotifyOfUnidleChanged;
@"<BLSHUserIdleProvidingDelegate>" _delegate;
d _idleTimeout;
@"AWAttentionAwarenessClient" _attentionAwarenessClient;
@"AWAttentionAwarenessConfiguration" _attentionAwarenessConfiguration;
@"NSMutableDictionary" _attentionLostTimeoutDictionary;
```

## Properties

```
@property (T@"AWAttentionAwarenessClient",&,N,V_attentionAwarenessClient) attentionAwarenessClient;
@property (T@"AWAttentionAwarenessConfiguration",&,N,V_attentionAwarenessConfiguration) attentionAwarenessConfiguration;
@property (T@"NSMutableDictionary",&,N,V_attentionLostTimeoutDictionary) attentionLostTimeoutDictionary;
@property (TB,N,V_shouldNotifyOfUnidleChanged) shouldNotifyOfUnidleChanged;
@property (T@"<BLSHUserIdleProvidingDelegate>",W,N,V_delegate) delegate;
@property (Td,R,N,V_idleTimeout) idleTimeout;
@property (TB,N,V_shouldNotifyOfUnidle) shouldNotifyOfUnidle;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[BLSHUserIdleProvider pause];
-[BLSHUserIdleProvider _reset];
-[BLSHUserIdleProvider idleTimeout];
-[BLSHUserIdleProvider init];
-[BLSHUserIdleProvider _invalidate];
-[BLSHUserIdleProvider reset];
-[BLSHUserIdleProvider _pause];
-[BLSHUserIdleProvider invalidate];
-[BLSHUserIdleProvider setDelegate:];
-[BLSHUserIdleProvider delegate];
-[BLSHUserIdleProvider setAttentionLostTimeoutDictionary:];
-[BLSHUserIdleProvider _resume];
-[BLSHUserIdleProvider attentionLostTimeoutDictionary];
-[BLSHUserIdleProvider resume];
-[BLSHUserIdleProvider setShouldNotifyOfUnidleChanged:];
-[BLSHUserIdleProvider attentionAwarenessConfiguration];
-[BLSHUserIdleProvider _setIdleTimeout:shouldReset:];
-[BLSHUserIdleProvider _setShouldNotifyOfUnidle:];
-[BLSHUserIdleProvider attentionAwarenessClient];
-[BLSHUserIdleProvider setAttentionAwarenessClient:];
-[BLSHUserIdleProvider setAttentionAwarenessConfiguration:];
-[BLSHUserIdleProvider setIdleTimeout:shouldReset:];
-[BLSHUserIdleProvider setShouldNotifyOfUnidle:];
-[BLSHUserIdleProvider shouldNotifyOfUnidle];
-[BLSHUserIdleProvider shouldNotifyOfUnidleChanged];
```
