# `TBRemoteFetchResponse`

- Image: [`/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`](../userland/System__Library__PrivateFrameworks__WiFiPolicy.framework__WiFiPolicy.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `TBFetchResponse`
- 3 instance variables, 8 properties, 6 instance methods, 1 class methods

## Instance variables

```
@"NSSet" _tiles;
@"NSArray" _results;
@"NSError" _error;
```

## Properties

```
@property (T@"NSArray",&,N,V_results) results;
@property (T@"NSError",C,N,V_error) error;
@property (T@"NSSet",R,N,V_tiles) tiles;
@property (T@"NSDictionary",?,R,N) resultsByBSSID;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[TBRemoteFetchResponse responseWithResults:tiles:error:];
```

## Instance methods

```
-[TBRemoteFetchResponse setError:];
-[TBRemoteFetchResponse tiles];
-[TBRemoteFetchResponse error];
-[TBRemoteFetchResponse results];
-[TBRemoteFetchResponse setResults:];
-[TBRemoteFetchResponse initWithResults:tiles:error:];
```
