# `SBSystemNotesPresentationRequestServer`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSServiceConnectionListenerDelegate`
- 4 instance variables, 5 properties, 6 instance methods, 0 class methods

## Instance variables

```
@"<SBSystemNotesPresentationRequestServerDelegate>" _delegate;
@"FBServiceClientAuthenticator" _clientAuthenticator;
@"BSServiceConnectionListener" _connectionListener;
@"NSObject<OS_dispatch_queue>" _queue;
```

## Properties

```
@property (T@"<SBSystemNotesPresentationRequestServerDelegate>",W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBSystemNotesPresentationRequestServer listener:didReceiveConnection:withContext:];
-[SBSystemNotesPresentationRequestServer init];
-[SBSystemNotesPresentationRequestServer invalidate];
-[SBSystemNotesPresentationRequestServer setDelegate:];
-[SBSystemNotesPresentationRequestServer activate];
-[SBSystemNotesPresentationRequestServer delegate];
```
