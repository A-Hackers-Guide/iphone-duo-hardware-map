# `ManagedNetworkSettings`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 1 properties, 6 instance methods, 1 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _queue;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",&,V_queue) queue;
```

## Class methods

```
+[ManagedNetworkSettings sharedMNS];
```

## Instance methods

```
-[ManagedNetworkSettings handleEvent:];
-[ManagedNetworkSettings init];
-[ManagedNetworkSettings queue];
-[ManagedNetworkSettings setQueue:];
-[ManagedNetworkSettings reloadMNS];
-[ManagedNetworkSettings reloadNetworkdSettings];
```
