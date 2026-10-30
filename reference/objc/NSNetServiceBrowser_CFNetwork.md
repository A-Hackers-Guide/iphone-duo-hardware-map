# `NSNetServiceBrowser`

- Image: [`/System/Library/Frameworks/CFNetwork.framework/CFNetwork`](../userland/System__Library__Frameworks__CFNetwork.framework__CFNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 2 properties, 16 instance methods, 0 class methods

## Instance variables

```
@ _netServiceBrowser;
@ _delegate;
^v _reserved;
B _includesPeerToPeer;
```

## Properties

```
@property (T@"<NSNetServiceBrowserDelegate>") delegate;
@property (TB,V_includesPeerToPeer) includesPeerToPeer;
```

## Instance methods

```
-[NSNetServiceBrowser init];
-[NSNetServiceBrowser stop];
-[NSNetServiceBrowser dealloc];
-[NSNetServiceBrowser removeFromRunLoop:forMode:];
-[NSNetServiceBrowser setDelegate:];
-[NSNetServiceBrowser delegate];
-[NSNetServiceBrowser scheduleInRunLoop:forMode:];
-[NSNetServiceBrowser _dispatchCallBack:flags:error:];
-[NSNetServiceBrowser _internalNetServiceBrowser];
-[NSNetServiceBrowser _setIncludesAWDL:];
-[NSNetServiceBrowser includesPeerToPeer];
-[NSNetServiceBrowser searchForAllDomains];
-[NSNetServiceBrowser searchForBrowsableDomains];
-[NSNetServiceBrowser searchForRegistrationDomains];
-[NSNetServiceBrowser searchForServicesOfType:inDomain:];
-[NSNetServiceBrowser setIncludesPeerToPeer:];
```
