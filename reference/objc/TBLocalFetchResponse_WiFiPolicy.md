# `TBLocalFetchResponse`

- Image: [`/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`](../userland/System__Library__PrivateFrameworks__WiFiPolicy.framework__WiFiPolicy.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `TBFetchResponse`
- 4 instance variables, 8 properties, 8 instance methods, 2 class methods

## Instance variables

```
@"NSError" error;
@"NSSet" _tiles;
@"NSArray" _results;
@"NSDictionary" _resultsByBSSID;
```

## Properties

```
@property (T@"NSArray",&,N,V_results) results;
@property (T@"NSDictionary",&,N,V_resultsByBSSID) resultsByBSSID;
@property (T@"NSError",R,C,N,Verror) error;
@property (T@"NSSet",R,N,V_tiles) tiles;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[TBLocalFetchResponse responseWithResults:entityDescription:];
+[TBLocalFetchResponse responseWithResultsByBSSID:];
```

## Instance methods

```
-[TBLocalFetchResponse tiles];
-[TBLocalFetchResponse error];
-[TBLocalFetchResponse results];
-[TBLocalFetchResponse setResults:];
-[TBLocalFetchResponse initWithResults:entityDescription:];
-[TBLocalFetchResponse initWithResultsByBSSID:];
-[TBLocalFetchResponse resultsByBSSID];
-[TBLocalFetchResponse setResultsByBSSID:];
```
