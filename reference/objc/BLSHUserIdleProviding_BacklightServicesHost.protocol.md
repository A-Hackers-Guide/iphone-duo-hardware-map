# `BLSHUserIdleProviding` (protocol)

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `BSInvalidatable`
- 0 instance variables, 3 properties, 9 instance methods, 0 class methods

## Properties

```
@property (T@"<BLSHUserIdleProvidingDelegate>",W,N) delegate;
@property (Td,R,N) idleTimeout;
@property (TB,N) shouldNotifyOfUnidle;
```

## Instance methods

```
-[BLSHUserIdleProviding pause];
-[BLSHUserIdleProviding idleTimeout];
-[BLSHUserIdleProviding reset];
-[BLSHUserIdleProviding setDelegate:];
-[BLSHUserIdleProviding delegate];
-[BLSHUserIdleProviding resume];
-[BLSHUserIdleProviding setIdleTimeout:shouldReset:];
-[BLSHUserIdleProviding setShouldNotifyOfUnidle:];
-[BLSHUserIdleProviding shouldNotifyOfUnidle];
```
