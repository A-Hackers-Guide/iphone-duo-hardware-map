# `TBFetchRequest` (protocol)

- Image: [`/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`](../userland/System__Library__PrivateFrameworks__WiFiPolicy.framework__WiFiPolicy.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`, `NSCopying`
- 0 instance variables, 6 properties, 12 instance methods, 0 class methods

## Properties

```
@property (T@"<TBFetchRequestDescriptor>",R,N) descriptor;
@property (TQ,N) sourcePolicy;
@property (T@?,C,N) resultsHandler;
@property (T@?,C,N) preferLocalHandler;
@property (TB,R,N) cacheable;
@property (T@"NSDictionary",?,&,N) userInfo;
```

## Instance methods

```
-[TBFetchRequest cacheable];
-[TBFetchRequest descriptor];
-[TBFetchRequest setResultsHandler:];
-[TBFetchRequest sourcePolicy];
-[TBFetchRequest handleResponse:];
-[TBFetchRequest resultsHandler];
-[TBFetchRequest setPreferLocalHandler:];
-[TBFetchRequest preferLocalHandler];
-[TBFetchRequest setSourcePolicy:];
-[TBFetchRequest userInfo];
-[TBFetchRequest setUserInfo:];
-[TBFetchRequest handlePreferLocalResponse:];
```
