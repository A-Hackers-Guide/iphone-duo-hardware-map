# `_UIViewServiceDeputyManager`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 1 properties, 16 instance methods, 2 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _queue;
@"_UIAsyncInvocation" _invalidationInvocation;
@"NSMutableDictionary" _connectionHandlers;
@"NSLock" _connectionHandlersLock;
@"NSMutableSet" _deputies;
@ _delegate;
```

## Properties

```
@property (T@,V_delegate) delegate;
```

## Class methods

```
+[_UIViewServiceDeputyManager initialize];
+[_UIViewServiceDeputyManager exportedInterfaceSupportingDeputyInterfaces:];
```

## Instance methods

```
-[_UIViewServiceDeputyManager _objc_initiateDealloc];
-[_UIViewServiceDeputyManager init];
-[_UIViewServiceDeputyManager dealloc];
-[_UIViewServiceDeputyManager invalidate];
-[_UIViewServiceDeputyManager setDelegate:];
-[_UIViewServiceDeputyManager delegate];
-[_UIViewServiceDeputyManager methodSignatureForSelector:];
-[_UIViewServiceDeputyManager forwardInvocation:];
-[_UIViewServiceDeputyManager __requestConnectionToDeputyOfClass:fromHostObject:replyHandler:];
-[_UIViewServiceDeputyManager _invalidateUnconditionallyThen:];
-[_UIViewServiceDeputyManager __prototype_requestConnectionToDeputyFromHostObject:replyHandler:];
-[_UIViewServiceDeputyManager _deputyClassForConnectionSelector:];
-[_UIViewServiceDeputyManager checkDeputyForRotation:];
-[_UIViewServiceDeputyManager registerDeputyClass:withConnectionHandler:];
-[_UIViewServiceDeputyManager unregisterDeputyClass:];
-[_UIViewServiceDeputyManager viewControllerOperator:didCreateServiceViewControllerOfClass:];
```
