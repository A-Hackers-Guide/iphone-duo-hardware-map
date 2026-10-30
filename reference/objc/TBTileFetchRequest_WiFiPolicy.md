# `TBTileFetchRequest`

- Image: [`/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`](../userland/System__Library__PrivateFrameworks__WiFiPolicy.framework__WiFiPolicy.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `TBFetchRequest`, `NSCopying`
- 6 instance variables, 10 properties, 17 instance methods, 1 class methods

## Instance variables

```
B _cacheable;
Q _sourcePolicy;
@"NSDictionary" userInfo;
@? resultsHandler;
@? preferLocalHandler;
@"TBTileFetchRequestDescriptor" _descriptor;
```

## Properties

```
@property (T@"TBTileFetchRequestDescriptor",&,N,V_descriptor) descriptor;
@property (TB,N,V_cacheable) cacheable;
@property (TQ,N,V_sourcePolicy) sourcePolicy;
@property (T@?,C,N,VresultsHandler) resultsHandler;
@property (T@?,C,N,VpreferLocalHandler) preferLocalHandler;
@property (T@"NSDictionary",?,&,N,VuserInfo) userInfo;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[TBTileFetchRequest fetchRequestWithDescriptor:sourcePolicy:cacheable:];
```

## Instance methods

```
-[TBTileFetchRequest cacheable];
-[TBTileFetchRequest setDescriptor:];
-[TBTileFetchRequest doesLocalResultsSatisfyRequest:];
-[TBTileFetchRequest initWithDescriptor:sourcePolicy:cacheable:];
-[TBTileFetchRequest descriptor];
-[TBTileFetchRequest userInfo];
-[TBTileFetchRequest setResultsHandler:];
-[TBTileFetchRequest setUserInfo:];
-[TBTileFetchRequest setCacheable:];
-[TBTileFetchRequest sourcePolicy];
-[TBTileFetchRequest handleResponse:];
-[TBTileFetchRequest handlePreferLocalResponse:];
-[TBTileFetchRequest resultsHandler];
-[TBTileFetchRequest setPreferLocalHandler:];
-[TBTileFetchRequest preferLocalHandler];
-[TBTileFetchRequest copyWithZone:];
-[TBTileFetchRequest setSourcePolicy:];
```
