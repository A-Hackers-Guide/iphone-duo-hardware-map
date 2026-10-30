# `TBErrorFetchResponse`

- Image: [`/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`](../userland/System__Library__PrivateFrameworks__WiFiPolicy.framework__WiFiPolicy.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `TBFetchResponse`
- 3 instance variables, 8 properties, 5 instance methods, 2 class methods

## Instance variables

```
@"NSArray" results;
@"NSSet" tiles;
@"NSError" _error;
```

## Properties

```
@property (T@"NSError",C,N,V_error) error;
@property (T@"NSArray",R,N,Vresults) results;
@property (T@"NSSet",R,N,Vtiles) tiles;
@property (T@"NSDictionary",?,R,N) resultsByBSSID;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[TBErrorFetchResponse responseWithError:];
+[TBErrorFetchResponse remoteResponseWithError:];
```

## Instance methods

```
-[TBErrorFetchResponse setError:];
-[TBErrorFetchResponse initWithError:];
-[TBErrorFetchResponse tiles];
-[TBErrorFetchResponse error];
-[TBErrorFetchResponse results];
```
