# `AVAudioSessionXPCServer`

- Image: [`/System/Library/PrivateFrameworks/AudioSessionServer.framework/AudioSessionServer`](../userland/System__Library__PrivateFrameworks__AudioSessionServer.framework__AudioSessionServer.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSXPCListenerDelegate`
- 8 instance variables, 5 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"NSMutableArray" _connections;
@"NSXPCInterface" _exportedInterface;
@"NSXPCInterface" _callbackInterface;
{unique_ptr<std::promise<void>, std::default_delete<std::promise<void>>>=""{?="__ptr_"^v}} _deallocPromise;
B _needsDefaultWorldInit;
{shared_ptr<avas::WorkloopPool>="__ptr_"^{WorkloopPool}"__cntrl_"^{__shared_weak_count}} _workloopPool;
@"<AVAudioSessionServerDelegate>" _serverDelegate;
@"NSXPCListener" _listener;
```

## Properties

```
@property (T@"NSXPCListener",R,N,V_listener) listener;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[AVAudioSessionXPCServer initWithDelegate:];
-[AVAudioSessionXPCServer listener:shouldAcceptNewConnection:];
-[AVAudioSessionXPCServer init];
-[AVAudioSessionXPCServer dealloc];
-[AVAudioSessionXPCServer start];
-[AVAudioSessionXPCServer listener];
-[AVAudioSessionXPCServer removeConnection:];
-[AVAudioSessionXPCServer init2];
```
