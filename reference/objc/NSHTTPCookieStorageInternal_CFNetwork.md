# `NSHTTPCookieStorageInternal`

- Image: [`/System/Library/Frameworks/CFNetwork.framework/CFNetwork`](../userland/System__Library__Frameworks__CFNetwork.framework__CFNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 0 properties, 3 instance methods, 0 class methods

## Instance variables

```
^{OpaqueCFHTTPCookieStorage=} storage;
^{OpaqueCFHTTPCookieStorage=} privateStorage;
@"NSRecursiveLock" dataLock;
B privateBrowsing;
B _storage_didRegister;
B _privateStorage_didRegister;
```

## Instance methods

```
-[NSHTTPCookieStorageInternal dealloc];
-[NSHTTPCookieStorageInternal _syncCookies];
-[NSHTTPCookieStorageInternal registerForPostingNotificationsWithContext:];
```
