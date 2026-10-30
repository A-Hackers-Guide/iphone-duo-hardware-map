# `TBNetworkFetchRequest`

- Image: [`/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`](../userland/System__Library__PrivateFrameworks__WiFiPolicy.framework__WiFiPolicy.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `TBFetchRequest`, `NSCopying`
- 6 instance variables, 10 properties, 16 instance methods, 2 class methods

## Instance variables

```
B _cacheable;
Q _sourcePolicy;
@"NSDictionary" userInfo;
@? resultsHandler;
@? preferLocalHandler;
@"TBNetworkFetchRequestDescriptor" _descriptor;
```

## Properties

```
@property (T@"TBNetworkFetchRequestDescriptor",&,N,V_descriptor) descriptor;
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
+[TBNetworkFetchRequest fetchRequestWithDescriptor:sourcePolicy:];
+[TBNetworkFetchRequest fetchRequestWithDescriptor:sourcePolicy:cacheable:];
```

## Instance methods

```
-[TBNetworkFetchRequest cacheable];
-[TBNetworkFetchRequest setDescriptor:];
-[TBNetworkFetchRequest doesLocalResultsSatisfyRequest:];
-[TBNetworkFetchRequest initWithDescriptor:sourcePolicy:cacheable:];
-[TBNetworkFetchRequest descriptor];
-[TBNetworkFetchRequest userInfo];
-[TBNetworkFetchRequest setResultsHandler:];
-[TBNetworkFetchRequest setUserInfo:];
-[TBNetworkFetchRequest setCacheable:];
-[TBNetworkFetchRequest sourcePolicy];
-[TBNetworkFetchRequest handleResponse:];
-[TBNetworkFetchRequest resultsHandler];
-[TBNetworkFetchRequest setPreferLocalHandler:];
-[TBNetworkFetchRequest preferLocalHandler];
-[TBNetworkFetchRequest copyWithZone:];
-[TBNetworkFetchRequest setSourcePolicy:];
```
