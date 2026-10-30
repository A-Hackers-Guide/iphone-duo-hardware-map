# `NetServiceDirectory`

- Image: [`/System/Library/Frameworks/CoreAudioKit.framework/CoreAudioKit`](../userland/System__Library__Frameworks__CoreAudioKit.framework__CoreAudioKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSNetServiceBrowserDelegate`, `NSNetServiceDelegate`
- 4 instance variables, 4 properties, 11 instance methods, 0 class methods

## Instance variables

```
@ mClient;
@"NSMutableArray" mNetServiceBrowsers;
@"NSMutableArray" mNetServices;
@"NSMutableArray" mResolvingServices;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[NetServiceDirectory services];
-[NetServiceDirectory netService:didNotResolve:];
-[NetServiceDirectory netService:didUpdateTXTRecordData:];
-[NetServiceDirectory netServiceBrowser:didFindService:moreComing:];
-[NetServiceDirectory netServiceBrowser:didRemoveService:moreComing:];
-[NetServiceDirectory netServiceDidResolveAddress:];
-[NetServiceDirectory serviceAtIndex:];
-[NetServiceDirectory indexOfService:];
-[NetServiceDirectory initWithClient:forService:inDomain:];
-[NetServiceDirectory initWithClient:forServices:inDomain:];
-[NetServiceDirectory serviceCount];
```
