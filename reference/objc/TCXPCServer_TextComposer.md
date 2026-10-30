# `TCXPCServer`

- Image: [`/System/Library/PrivateFrameworks/TextComposer.framework/TextComposer`](../userland/System__Library__PrivateFrameworks__TextComposer.framework__TextComposer.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSXPCListenerDelegate`
- 3 instance variables, 4 properties, 4 instance methods, 1 class methods

## Instance variables

```
@"TCTextServer" _server;
@"NSXPCListener" _listener;
@"NSObject<OS_dispatch_queue>" _queue;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[TCXPCServer xpcInterface];
```

## Instance methods

```
-[TCXPCServer listener:shouldAcceptNewConnection:];
-[TCXPCServer invalidate];
-[TCXPCServer run];
-[TCXPCServer initWithTextServer:];
```
