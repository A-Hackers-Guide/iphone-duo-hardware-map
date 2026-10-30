# `CoreLocationDelegate`

- Image: [`/System/Library/PrivateFrameworks/IPTelephony.framework/Support/libIPTelephony.dylib`](../userland/System__Library__PrivateFrameworks__IPTelephony.framework__Support__libIPTelephony.dylib.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CLLocationManagerDelegate`
- 3 instance variables, 4 properties, 3 instance methods, 0 class methods

## Instance variables

```
@"CLLocationManager" _locationManager;
{atomic<CLAuthorizationStatus>="__a_"{__cxx_atomic_impl<CLAuthorizationStatus, std::__cxx_atomic_base_impl<CLAuthorizationStatus>>="__a_value"Ai}} _authStatus;
@"NSObject<OS_dispatch_queue>" _queue;
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
-[CoreLocationDelegate initWithQueue:];
-[CoreLocationDelegate locationManagerDidChangeAuthorization:];
-[CoreLocationDelegate isLocationAuthorized];
```
