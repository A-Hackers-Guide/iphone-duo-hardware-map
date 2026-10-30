# `_NSHSTSStorage`

- Image: [`/System/Library/Frameworks/CFNetwork.framework/CFNetwork`](../userland/System__Library__Frameworks__CFNetwork.framework__CFNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 2 properties, 11 instance methods, 1 class methods

## Instance variables

```
^{_CFHSTSPolicy=} _policy;
```

## Properties

```
@property (T^{_CFHSTSPolicy=},R) _policyRef;
@property (T@"NSURL",R,N) path;
```

## Class methods

```
+[_NSHSTSStorage sharedPersistentStore];
```

## Instance methods

```
-[_NSHSTSStorage shouldPromoteHostToHTTPS:];
-[_NSHSTSStorage dealloc];
-[_NSHSTSStorage shouldPromoteHostToHTTPS:isPreload:];
-[_NSHSTSStorage _policyRef];
-[_NSHSTSStorage handleSTSHeader:forURL:];
-[_NSHSTSStorage initPersistentStoreWithURL:];
-[_NSHSTSStorage nonPreloadedHosts];
-[_NSHSTSStorage resetHSTSHostsSinceDate:];
-[_NSHSTSStorage resetHSTSForHost:];
-[_NSHSTSStorage initInMemoryStore];
-[_NSHSTSStorage path];
```
